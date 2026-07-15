#!/usr/bin/env python3
"""Continue the git history through 2.4.x. New script (no shell reference existed).

Reuses the repo built by import-2.3.py (must already exist at
unpack/linux-git, on branch "master" at the 2.4.0-prerelease tag). At
2.4.16, branches off onto "2.4" (2.5.1 forked from 2.4.15 in real history,
and Linus' own tree moved on from there -- matches the 1.0/1.1, 2.0/2.1,
2.2/2.3 pattern). Always Linus Torvalds; no aliases in this segment.
"""

import argparse
from pathlib import Path

from linux_hist_common import (
    DIFFS,
    UNPACK,
    apply_diff,
    author_env,
    branch_exists,
    commit_version,
    log,
    remove_empty_files,
    run,
    tag_exists,
)
from linux_hist_2_4 import LINUS, VERSIONS, changelog_path


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    repo: Path = UNPACK / "linux-git"
    if not (repo / ".git").exists():
        raise FileNotFoundError(f"{repo} doesn't exist -- run import-2.3.py first")
    env: dict[str, str] = author_env(LINUS)
    run(["git", "checkout", "master"], cwd=repo, env=env)

    for v in VERSIONS:
        if v.branch_create and not branch_exists(repo, v.branch_create):
            run(["git", "branch", v.branch_create], cwd=repo, env=env)
        if v.branch_checkout:
            run(["git", "checkout", v.branch_checkout], cwd=repo, env=env)

        if tag_exists(repo, v.name):
            log(f"skip {v.name} (already imported)")
            continue

        log(f"importing {v.name}")
        diff_file: Path = DIFFS / f"linux-{v.name}.diff"
        if not diff_file.exists():
            raise FileNotFoundError(diff_file)
        apply_diff(repo, diff_file, v.name)
        run(["git", "add", "--all"], cwd=repo, env=env)
        remove_empty_files(repo, env)
        commit_version(repo, v.name, v.date, env, changelog_path(v))
        run(["git", "tag", v.name], cwd=repo, env=env)


if __name__ == "__main__":
    main()
