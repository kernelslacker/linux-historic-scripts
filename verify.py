#!/usr/bin/env python3
"""Verify the reconstructed git history against the unpacked source trees.

For every tagged version, extract that tag's tree out of unpack/linux-git and
compare it file-by-file against the independently-unpacked tarball tree the
diff was generated from (unpack/linux-<name>). This is the automated form of
the manual spot-check the import-2.6.py docstring describes -- the thing that
once caught `git apply` silently dropping hunks.

Two differences are expected and are NOT treated as failures:

  * Empty files. import.py runs `git rm` on every zero-byte file, so the git
    tree legitimately lacks empties that exist in the tarball.
  * Binary files. The pipeline reconstructs trees from textual `diff -urN`,
    which can't carry binary content, so a binary file added or changed in a
    release (e.g. Documentation/logo.gif) won't match. These are reported as
    warnings, not failures -- it's a known, pre-existing limitation.

Anything else -- a text file whose content differs, a non-empty text file
missing from git, or a file present in git but absent from the tarball -- is
a real fidelity failure and makes verify.py exit non-zero.
"""

import argparse
import filecmp
import importlib
import subprocess
import sys
import tempfile
from pathlib import Path
from types import ModuleType

from linux_hist_common import UNPACK, log, tag_exists, tree_dir

REPO: Path = UNPACK / "linux-git"

# branch id -> module holding its VERSIONS table, in dependency order
BRANCH_MODULES: dict[str, str] = {
    "0.x": "linux_hist_0x",
    "1.x": "linux_hist_1x",
    "2.0": "linux_hist_2_0",
    "2.1": "linux_hist_2_1",
    "2.2": "linux_hist_2_2",
    "2.3": "linux_hist_2_3",
    "2.4": "linux_hist_2_4",
    "2.5": "linux_hist_2_5",
    "2.6": "linux_hist_2_6",
}


class Mismatch:
    """One file that differs between the git tree and the tarball tree."""

    def __init__(self, path: str, kind: str, binary: bool) -> None:
        self.path = path
        self.kind = kind  # "differs", "missing-from-git", "extra-in-git"
        self.binary = binary


def is_binary(path: Path) -> bool:
    """Treat a file as binary if its first 8 KiB contains a NUL byte."""
    try:
        return b"\0" in path.read_bytes()[:8192]
    except OSError:
        return False


def source_tree(module: ModuleType, name: str) -> Path:
    """On-disk unpacked tree for a version. Only 2.3 renames its dirs (the
    2.3.99-preN family), and its module carries the dir_name-aware tree_dir."""
    branch_tree_dir = getattr(module, "tree_dir", tree_dir)
    return branch_tree_dir(name)


def compare_version(tag: str, src: Path) -> list[Mismatch]:
    """Diff the extracted tag tree against the unpacked tarball tree `src`."""
    mismatches: list[Mismatch] = []
    with tempfile.TemporaryDirectory() as tmpdir:
        git = subprocess.Popen(
            ["git", "-C", str(REPO), "archive", tag], stdout=subprocess.PIPE
        )
        tar = subprocess.Popen(["tar", "-x", "-C", tmpdir], stdin=git.stdout)
        if git.stdout is not None:
            git.stdout.close()
        tar.wait()
        if git.wait() != 0 or tar.returncode != 0:
            raise RuntimeError(f"failed to extract tag {tag}")
        _walk_compare(Path(tmpdir), src, mismatches)
    return mismatches


def _walk_compare(gitdir: Path, src: Path, out: list[Mismatch]) -> None:
    git_files: set[str] = _relfiles(gitdir)
    src_files: set[str] = _relfiles(src)
    for rel in sorted(src_files - git_files):
        srcfile: Path = src / rel
        if srcfile.stat().st_size == 0:
            continue  # zero-byte file dropped by `git rm`; expected
        out.append(Mismatch(rel, "missing-from-git", is_binary(srcfile)))
    for rel in sorted(git_files - src_files):
        out.append(Mismatch(rel, "extra-in-git", is_binary(gitdir / rel)))
    for rel in sorted(git_files & src_files):
        if not filecmp.cmp(gitdir / rel, src / rel, shallow=False):
            out.append(Mismatch(rel, "differs", is_binary(src / rel)))


def _relfiles(root: Path) -> set[str]:
    return {str(p.relative_to(root)) for p in root.rglob("*") if p.is_file()}


def versions_to_check(branches: list[str]) -> list[tuple[str, Path]]:
    checks: list[tuple[str, Path]] = []
    for branch in branches:
        module: ModuleType = importlib.import_module(BRANCH_MODULES[branch])
        for v in module.VERSIONS:
            if not tag_exists(REPO, v.name):
                log(f"skip {v.name} (untagged -- e.g. the 0.x seed)")
                continue
            checks.append((v.name, source_tree(module, v.name)))
    return checks


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--branch",
        action="append",
        choices=list(BRANCH_MODULES),
        help="limit to this branch (repeatable; default: all)",
    )
    parser.add_argument(
        "--stop-on-fail",
        action="store_true",
        help="stop at the first version with a real (text) mismatch",
    )
    args: argparse.Namespace = parser.parse_args()

    if not (REPO / ".git").exists():
        raise SystemExit(f"{REPO} not built yet -- run build.py first")

    branches: list[str] = args.branch or list(BRANCH_MODULES)
    checks: list[tuple[str, Path]] = versions_to_check(branches)

    real_failures: int = 0
    binary_warnings: int = 0
    for tag, src in checks:
        if not src.exists():
            log(f"FAIL {tag}: source tree {src} missing")
            real_failures += 1
            if args.stop_on_fail:
                break
            continue
        mismatches: list[Mismatch] = compare_version(tag, src)
        real: list[Mismatch] = [m for m in mismatches if not m.binary]
        binary: list[Mismatch] = [m for m in mismatches if m.binary]
        binary_warnings += len(binary)
        if real:
            real_failures += len(real)
            for m in real:
                log(f"FAIL {tag}: {m.kind} {m.path}")
            if args.stop_on_fail:
                break
        elif binary:
            log(f"ok   {tag} ({len(binary)} binary file(s) differ -- expected)")
        else:
            log(f"ok   {tag}")

    log(
        f"checked {len(checks)} versions: "
        f"{real_failures} real failure(s), "
        f"{binary_warnings} binary difference(s) (known limitation)"
    )
    sys.exit(1 if real_failures else 0)


if __name__ == "__main__":
    main()
