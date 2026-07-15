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


def ref_exists(repo: Path, ref: str) -> bool:
    return (
        subprocess.run(
            ["git", "rev-parse", "-q", "--verify", ref],
            cwd=repo,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ).returncode
        == 0
    )


def tag_exists(repo: Path, name: str) -> bool:
    return ref_exists(repo, f"refs/tags/{name}")


def branch_exists(repo: Path, name: str) -> bool:
    return ref_exists(repo, f"refs/heads/{name}")


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
    # `git rm` doesn't consult author/committer identity, so `env` is unused
    # here in practice -- kept for the uniform (cwd=repo, env=env) call style
    # every other `run()` site in the import scripts follows.
    empties: list[str] = []
    for dirpath, dirnames, filenames in os.walk(repo):
        if ".git" in dirnames:
            dirnames.remove(".git")
        for filename in filenames:
            f: Path = Path(dirpath, filename)
            if f.stat().st_size == 0:
                empties.append(str(f.relative_to(repo)))
    if empties:
        run(["git", "rm", "-f", "--quiet", *empties], cwd=repo, env=env)


def apply_diff(repo: Path, diff_file: Path, name: str) -> None:
    """Apply a unified diff to `repo` with `patch -p1` (import side).

    Uses `patch` rather than `git apply`: on the larger 2.6 diffs `git apply`
    was seen to exit 0 while silently dropping hunks (see import-2.6.py).

    Streams the diff in from disk (up to ~30MB for the largest ones) instead
    of reading it into memory first.
    """
    with diff_file.open("rb") as f:
        result: subprocess.CompletedProcess[bytes] = subprocess.run(
            ["patch", "-p1", "-s"], cwd=repo, stdin=f, capture_output=True
        )
    if result.returncode != 0:
        sys.stderr.buffer.write(result.stdout)
        sys.stderr.buffer.write(result.stderr)
        raise RuntimeError(f"patch failed for {name}")


class GitRepo:
    """A repo path + author env pair, wrapping the `cwd=repo, env=env` pattern
    every import-*.py git call follows.

    `env` is a plain attribute (not read-only) since several scripts swap it
    mid-loop on an author change (e.g. `repo.env = author_env(v.author)`).
    """

    def __init__(self, path: Path, env: dict[str, str]) -> None:
        self.path = path
        self.env = env

    def git(self, *args: str) -> subprocess.CompletedProcess[str]:
        return run(["git", *args], cwd=self.path, env=self.env)

    def checkout(self, ref: str) -> None:
        self.git("checkout", ref)

    def branch(self, name: str) -> None:
        self.git("branch", name)

    def tag(self, name: str) -> None:
        self.git("tag", name)

    def tag_exists(self, name: str) -> bool:
        return tag_exists(self.path, name)

    def branch_exists(self, name: str) -> bool:
        return branch_exists(self.path, name)

    def commit(self, name: str, date: str, changelog: Path) -> None:
        commit_version(self.path, name, date, self.env, changelog)


def open_repo(prev_script: str, author: Author) -> GitRepo:
    """Open the shared unpack/linux-git repo left by an earlier import-*.py
    and check out "master".

    Common preamble shared by every non-seed import-*.py -- only the
    "run X first" hint (naming the previous script in the chain) varies.
    """
    path: Path = UNPACK / "linux-git"
    if not (path / ".git").exists():
        raise FileNotFoundError(f"{path} doesn't exist -- run {prev_script} first")
    repo = GitRepo(path, author_env(author))
    repo.checkout("master")
    return repo


def import_version(
    repo: GitRepo, name: str, date: str, changelog: Path
) -> None:
    """Apply `diffs/linux-NAME.diff`, commit, and tag it -- the seven-step
    block (log, diff-file check, apply_diff, git add, remove_empty_files,
    commit_version, git tag) shared verbatim by every import-*.py loop.
    """
    log(f"importing {name}")
    diff_file: Path = DIFFS / f"linux-{name}.diff"
    if not diff_file.exists():
        raise FileNotFoundError(diff_file)
    apply_diff(repo.path, diff_file, name)
    repo.git("add", "--all")
    remove_empty_files(repo.path, repo.env)
    repo.commit(name, date, changelog)
    repo.tag(name)


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


def extract_tarball(name: str, dest: Path, archive: Path, force: bool) -> None:
    """Unpack `archive` to `dest`, skipping if it already exists.

    Common orchestration shared by every untar-*.py's own extract_tarball --
    only the archive path construction (and, for untar-2.3.py, `dest` itself
    via its dir_name-aware tree_dir override) varies script to script.
    """
    if dest.exists() and not force:
        log(f"skip {name} (already unpacked)")
        return
    if not archive.exists():
        raise FileNotFoundError(archive)
    log(f"unpacking {name}")
    extract_to(archive, dest)


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


def apply_prepatch(
    dest: Path,
    patchfile: Path,
    cat_cmd: str | None,
    name: str,
    strict: bool,
) -> None:
    """Decompress `patchfile` (if `cat_cmd` is given) and apply it to `dest`
    with `patch -p1` (untar side).

    Streams `cat_cmd | patch` as a real pipe (rather than buffering the
    whole decompressed patch in memory first) and lets `patch`'s own
    output go straight to our stderr instead of capturing it just to dump
    it there afterwards.

    Non-strict mode logs a warning and continues on failure (matching the
    original scripts, which tolerated a few historically-broken prepatches).
    """
    cat_proc: subprocess.Popen[bytes] | None = None
    if cat_cmd is None:
        patch_stdin = patchfile.open("rb")
    else:
        cat_proc = subprocess.Popen([cat_cmd, str(patchfile)], stdout=subprocess.PIPE)
        assert cat_proc.stdout is not None
        patch_stdin = cat_proc.stdout
    try:
        result: subprocess.CompletedProcess[bytes] = subprocess.run(
            ["patch", "-p1"],
            cwd=dest,
            stdin=patch_stdin,
            stdout=sys.stderr,
            stderr=sys.stderr,
        )
    finally:
        patch_stdin.close()
        if cat_proc is not None:
            cat_proc.wait()
    if cat_proc is not None and cat_proc.returncode != 0:
        raise RuntimeError(f"{cat_cmd} exited {cat_proc.returncode} for {name}")
    if result.returncode != 0:
        msg: str = f"patch exited {result.returncode} for {name}"
        if strict:
            raise RuntimeError(msg)
        log(f"WARNING: {msg} (tree may be broken, continuing)")


def apply_patch(
    name: str,
    dest: Path,
    base: Path,
    patchfile: Path,
    cat_cmd: str | None,
    force: bool,
    strict: bool,
    prepare: Callable[[Path], None] | None = None,
    missing_base_hint: str = "",
) -> None:
    """Build `dest` by hardlink-copying `base` and applying `patchfile`,
    skipping if `dest` already exists.

    Common orchestration shared by every untar-*.py's own apply_patch --
    only the base/patchfile path construction, `cat_cmd` selection, and an
    optional `prepare(tmp)` hook (untar-1.x.py's chmod_writable,
    untar-2.1.py's fixup) vary script to script.
    """
    if dest.exists() and not force:
        log(f"skip {name} (already patched)")
        return
    if not base.exists():
        hint: str = f" {missing_base_hint}" if missing_base_hint else ""
        raise FileNotFoundError(f"base tree missing for {name}: {base}{hint}")
    if not patchfile.exists():
        raise FileNotFoundError(patchfile)
    log(f"patching to {name}")

    def do_apply(tmp: Path) -> None:
        if prepare:
            prepare(tmp)
        apply_prepatch(tmp, patchfile, cat_cmd, name, strict)

    build_patched_tree(base, dest, do_apply)


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


def make_diff(
    name: str,
    base: str,
    force: bool,
    missing_base_hint: str = "",
    dirname_of: Callable[[str], str] = lambda n: n,
) -> None:
    """Generate diffs/linux-NAME.diff via `write_diff`, skipping if it
    already exists and raising early if the base tree isn't unpacked yet.

    `dirname_of` maps a version name to its on-disk directory name where
    they differ (only the 2.3 family's 2.3.99pre* range needs this); the
    output file is always named after the canonical version name.
    """
    out: Path = DIFFS / f"linux-{name}.diff"
    if out.exists() and not force:
        log(f"skip diff for {name} (already exists)")
        return
    base_dir: Path = tree_dir(dirname_of(base))
    if not base_dir.exists():
        hint: str = f" {missing_base_hint}" if missing_base_hint else ""
        raise FileNotFoundError(f"base tree missing for {name}: {base_dir}{hint}")
    log(f"diffing {name}")
    write_diff(dirname_of(base), dirname_of(name), out)
