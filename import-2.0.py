#!/usr/bin/env python3
"""Continue the git history through 2.0.x.

Reuses the repo built by import-1.x.py (must already exist at
unpack/linux-git, on branch "master" at the pre2.0.14 tag). At 2.0.22,
branches off onto "2.0" (Alan Cox takes over) and never checks back out to
master -- 2.1's import continues master from 2.0.21. Author changes again
to David Weinehall at 2.0.39pre1, still on branch "2.0".
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
from linux_hist_2_0 import LINUS, VERSIONS, changelog_path


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    repo: Path = UNPACK / "linux-git"
    if not (repo / ".git").exists():
        raise FileNotFoundError(f"{repo} doesn't exist -- run import-1.x.py first")
    env: dict[str, str] = author_env(LINUS)
    run(["git", "checkout", "master"], cwd=repo, env=env)

    for v in VERSIONS:
        if v.author:
            env = author_env(v.author)

        if v.branch_create and not branch_exists(repo, v.branch_create):
            run(["git", "branch", v.branch_create], cwd=repo, env=env)
        if v.branch_checkout:
            run(["git", "checkout", v.branch_checkout], cwd=repo, env=env)

        if v.alias_of:
            if tag_exists(repo, v.name):
                log(f"skip {v.name} (already tagged)")
                continue
            log(f"tagging {v.name} -> {v.alias_of}")
            run(["git", "tag", v.name], cwd=repo, env=env)
            continue

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
