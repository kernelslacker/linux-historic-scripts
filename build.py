#!/usr/bin/env python3
"""Top-level driver: build the whole historic git tree in one command.

Runs the untar -> make-diffs -> import trio for each branch, branches in
dependency order (0.x, 1.x, 2.0 ... 2.6) -- the manual sequence the README
documents. Each stage is just the existing per-branch script run as a
subprocess; they all skip work that's already on disk, so an interrupted
run resumes where it left off.

Examples:
    ./build.py                          # build everything, 0.x through 2.6
    ./build.py --from-branch 2.4        # resume from the 2.4 branch onward
    ./build.py --stage untar            # only unpack, all branches
    ./build.py --to-branch 1.x --force  # rebuild 0.x + 1.x from scratch
    ./build.py --dry-run                # print the plan, run nothing
"""

import argparse
import shutil
import subprocess
import sys

from linux_hist_common import BUILD_REPO, FINAL_REPO, ROOT, log

BRANCHES: list[str] = [
    "0.x",
    "1.x",
    "2.0",
    "2.1",
    "2.2",
    "2.3",
    "2.4",
    "2.5",
    "2.6",
]
STAGES: tuple[str, ...] = ("untar", "make-diffs", "import")

# The 2.5/2.6 untar stages are pure tarball chains with no prepatches, so
# their scripts define --force but not --strict; don't pass --strict there.
NO_STRICT_UNTAR: frozenset[str] = frozenset({"2.5", "2.6"})


def run_stage(
    stage: str, branch: str, force: bool, strict: bool, dry_run: bool
) -> None:
    cmd: list[str] = [sys.executable, str(ROOT / f"{stage}-{branch}.py")]
    if force and stage in ("untar", "make-diffs"):
        cmd.append("--force")
    if strict and stage == "untar" and branch not in NO_STRICT_UNTAR:
        cmd.append("--strict")
    log(f"=== {stage} {branch} ===")
    if dry_run:
        log(f"   (dry-run) {' '.join(cmd)}")
        return
    subprocess.run(cmd, check=True)


def finalize(dry_run: bool) -> None:
    """Lift the finished history out of the throwaway unpack/ dir.

    The import stage builds into BUILD_REPO (unpack/linux-git), buried
    alongside the unpacked tarballs. Once the full chain has run, move it up to
    FINAL_REPO (./linux-git) so the deliverable isn't stranded in the gitignored
    scratch dir. Idempotent: replaces an existing FINAL_REPO from a prior run.
    """
    if not (BUILD_REPO / ".git").exists():
        log(f"finalize: {BUILD_REPO} not found, nothing to move")
        return
    log(f"=== finalize: move {BUILD_REPO} -> {FINAL_REPO} ===")
    if dry_run:
        log(f"   (dry-run) mv {BUILD_REPO} {FINAL_REPO}")
        return
    if FINAL_REPO.exists():
        shutil.rmtree(FINAL_REPO)
    shutil.move(str(BUILD_REPO), str(FINAL_REPO))


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--from-branch", choices=BRANCHES, default=BRANCHES[0])
    parser.add_argument("--to-branch", choices=BRANCHES, default=BRANCHES[-1])
    parser.add_argument(
        "--stage",
        choices=(*STAGES, "all"),
        default="all",
        help="run just one stage across the selected branches (default: all)",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="pass --force to the untar/make-diffs stages (rebuild existing)",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="pass --strict to the patch-applying untar stages",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="print the stages that would run, without running them",
    )
    args: argparse.Namespace = parser.parse_args()

    lo: int = BRANCHES.index(args.from_branch)
    hi: int = BRANCHES.index(args.to_branch)
    if lo > hi:
        parser.error(
            f"--from-branch {args.from_branch} comes after "
            f"--to-branch {args.to_branch}"
        )
    selected: list[str] = BRANCHES[lo : hi + 1]
    stages: tuple[str, ...] = STAGES if args.stage == "all" else (args.stage,)

    for branch in selected:
        for stage in stages:
            try:
                run_stage(stage, branch, args.force, args.strict, args.dry_run)
            except subprocess.CalledProcessError as exc:
                log(f"FAILED: {stage} {branch} (exit {exc.returncode})")
                raise SystemExit(exc.returncode) from exc

    # Only relocate once the import stage has actually run through the final
    # branch -- a partial range leaves an incomplete tree that shouldn't be
    # presented as the finished linux-git.
    if "import" in stages and args.to_branch == BRANCHES[-1]:
        finalize(args.dry_run)


if __name__ == "__main__":
    main()
