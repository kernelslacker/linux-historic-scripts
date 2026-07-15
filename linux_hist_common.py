"""Shared helpers for the untar-*/make-diffs-*/import-* script trios.

Each per-branch ``linux_hist_*.py`` imports the path constants (and, where the
generic form fits, ``tree_dir``) and the ``LINUS`` author tuple from here, and
supplies its own ``BINARIES`` path, ``Version`` dataclass and ``VERSIONS``
table. The trio scripts import their mechanical helpers from here so the
per-branch loop bodies stay small and identical branch-to-branch.
"""

import os
import shutil
import subprocess
import sys
from collections.abc import Callable
from pathlib import Path

ROOT: Path = Path(__file__).resolve().parent
UNPACK: Path = ROOT / "unpack"
DIFFS: Path = ROOT / "diffs"
CHANGELOGS: Path = ROOT / "changelogs"

Author = tuple[str, str]  # (name, email)
LINUS: Author = ("Linus Torvalds", "torvalds@linuxfoundation.org")


def log(msg: str) -> None:
    print(f"-- {msg}", file=sys.stderr)


def run(
    cmd: list[str], cwd: Path | None = None, env: dict[str, str] | None = None
) -> subprocess.CompletedProcess[str]:
    result: subprocess.CompletedProcess[str] = subprocess.run(
        cmd, cwd=cwd, env=env, capture_output=True, text=True
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"command failed ({result.returncode}): {' '.join(map(str, cmd))}\n"
            f"{result.stdout}\n{result.stderr}"
        )
    return result


def tree_dir(name: str) -> Path:
    return UNPACK / f"linux-{name}"


# --- git import helpers (used by import-*.py) ---


def author_env(author: Author) -> dict[str, str]:
    name, email = author
    env: dict[str, str] = os.environ.copy()
    env.update(
        {
            "GIT_AUTHOR_NAME": name,
            "GIT_AUTHOR_EMAIL": email,
            "GIT_COMMITTER_NAME": name,
            "GIT_COMMITTER_EMAIL": email,
        }
    )
    return env


def commit_version(
    repo: Path, name: str, date: str, env: dict[str, str], changelog: Path
) -> None:
    if changelog.exists():
        run(
            ["git", "commit", "-F", str(changelog), f"--date={date}"], cwd=repo, env=env
        )
    else:
        run(
            ["git", "commit", "-m", f"Import {name}", f"--date={date}"],
            cwd=repo,
            env=env,
        )


def remove_empty_files(repo: Path, env: dict[str, str]) -> None:
    empties: list[str] = [
        str(f.relative_to(repo))
        for f in repo.rglob("*")
        if ".git" not in f.parts and f.is_file() and f.stat().st_size == 0
    ]
    if empties:
        run(["git", "rm", "-f", "--quiet", *empties], cwd=repo, env=env)


def apply_diff(repo: Path, diff_bytes: bytes, name: str) -> None:
    """Apply a unified diff to `repo` with `patch -p1` (import side).

    Uses `patch` rather than `git apply`: on the larger 2.6 diffs `git apply`
    was seen to exit 0 while silently dropping hunks (see import-2.6.py).
    """
    result: subprocess.CompletedProcess[bytes] = subprocess.run(
        ["patch", "-p1", "-s"], cwd=repo, input=diff_bytes, capture_output=True
    )
    if result.returncode != 0:
        sys.stderr.buffer.write(result.stdout)
        sys.stderr.buffer.write(result.stderr)
        raise RuntimeError(f"patch failed for {name}")


# --- tarball helpers (used by untar-*.py) ---


def extract_to(archive: Path, dest: Path) -> None:
    """Extract a kernel tarball and normalise its top dir to `dest`.

    Some tarballs unpack to 'linux/', others straight to 'linux-VERSION/' --
    mirrors the "if [ -d linux ]" guard in the original shell scripts.
    """
    staging: Path = UNPACK / "linux"
    if staging.exists():
        shutil.rmtree(staging)
    if dest.exists():
        shutil.rmtree(dest)
    run(["tar", "xf", str(archive)], cwd=UNPACK)
    if staging.exists():
        staging.rename(dest)
    elif not dest.exists():
        raise RuntimeError(f"{archive} did not extract to 'linux/' or '{dest.name}/'")


def hardlink_tree(src: Path, dest: Path) -> None:
    """Copy a tree via hardlinks, like `cp -rl src dest`."""
    shutil.copytree(src, dest, copy_function=os.link)


def build_patched_tree(
    base: Path, dest: Path, apply_fn: Callable[[Path], None]
) -> None:
    """Hardlink-copy `base` under a temp name, run `apply_fn(tmp)`, then
    rename into `dest` only once it succeeds.

    A run interrupted between the hardlink copy and the patch completing
    (Ctrl-C, a missing `patch` binary) leaves the temp dir behind, not
    `dest` -- so a later run's `dest.exists()` skip check won't mistake a
    half-patched tree for a finished one.
    """
    tmp: Path = dest.with_name(dest.name + ".tmp")
    if tmp.exists():
        shutil.rmtree(tmp)
    hardlink_tree(base, tmp)
    try:
        apply_fn(tmp)
    except BaseException:
        shutil.rmtree(tmp, ignore_errors=True)
        raise
    if dest.exists():
        shutil.rmtree(dest)
    tmp.rename(dest)


def patch_tree(dest: Path, patch_bytes: bytes, name: str, strict: bool) -> None:
    """Apply a prepatch to an unpacked tree with `patch -p1` (untar side).

    Non-strict mode logs a warning and continues on failure (matching the
    original scripts, which tolerated a few historically-broken prepatches).
    """
    result: subprocess.CompletedProcess[bytes] = subprocess.run(
        ["patch", "-p1"], cwd=dest, input=patch_bytes, capture_output=True
    )
    if result.stdout:
        sys.stderr.buffer.write(result.stdout)
    if result.stderr:
        sys.stderr.buffer.write(result.stderr)
    if result.returncode != 0:
        msg: str = f"patch exited {result.returncode} for {name}"
        if strict:
            raise RuntimeError(msg)
        log(f"WARNING: {msg} (tree may be broken, continuing)")


# --- diff helpers (used by make-diffs-*.py) ---


def write_diff(base_label: str, name_label: str, out: Path) -> None:
    """Write `diff -urN linux-BASE linux-NAME` to `out` (run inside UNPACK).

    Relative "linux-VERSION" names keep the diff headers at
    "linux-BASE/foo" / "linux-VERSION/foo" so `patch -p1` strips exactly one
    leading component. diff exits 1 when it finds differences (the expected
    case); only >= 2 is a real failure.

    Writes under a temp name and renames into place only on success, so a
    Ctrl-C or missing `diff` binary mid-run can't leave a truncated file at
    `out` for a later run's skip-if-exists check to mistake for a cached diff.
    """
    tmp: Path = out.with_name(out.name + ".tmp")
    try:
        with tmp.open("wb") as f:
            result: subprocess.CompletedProcess[bytes] = subprocess.run(
                ["diff", "-urN", f"linux-{base_label}", f"linux-{name_label}"],
                stdout=f,
                cwd=UNPACK,
            )
        if result.returncode not in (0, 1):
            raise RuntimeError(f"diff failed ({result.returncode}) for {name_label}")
    except BaseException:
        tmp.unlink(missing_ok=True)
        raise
    tmp.rename(out)
