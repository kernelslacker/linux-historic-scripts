#!/usr/bin/env python3
"""Continue the git history through 1.0/1.1/1.2/1.3/pre2.0.

Reuses the repo built by import-0.x.py (must already exist at
unpack/linux-git, checked out on master at the 1.0alpha tag) and continues
committing into it -- it does not create a fresh repo. 1.0 splits off onto
branch "1.0" at 1.0.6 while "master" continues into 1.1; 1.2 splits off onto
branch "1.2" at 1.2.10 while "master" continues into 1.3.
"""

import argparse
from pathlib import Path

from linux_hist_common import (
    DIFFS,
    UNPACK,
    apply_diff,
    author_env,
    commit_version,
    log,
    remove_empty_files,
    run,
)
from linux_hist_1x import LINUS, VERSIONS, changelog_path


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    repo: Path = UNPACK / "linux-git"
    if not (repo / ".git").exists():
        raise FileNotFoundError(f"{repo} doesn't exist -- run import-0.x.py first")
    env: dict[str, str] = author_env(LINUS)
    run(["git", "checkout", "master"], cwd=repo, env=env)

    for v in VERSIONS:
        if v.branch_create:
            run(["git", "branch", v.branch_create], cwd=repo, env=env)
        if v.branch_checkout:
            run(["git", "checkout", v.branch_checkout], cwd=repo, env=env)

        log(f"importing {v.name}")
        diff_file: Path = DIFFS / f"linux-{v.name}.diff"
        if not diff_file.exists():
            raise FileNotFoundError(diff_file)
        apply_diff(repo, diff_file.read_bytes(), v.name)
        run(["git", "add", "--all"], cwd=repo, env=env)
        remove_empty_files(repo, env)
        commit_version(repo, v.name, v.date, env, changelog_path(v))
        run(["git", "tag", v.name], cwd=repo, env=env)


if __name__ == "__main__":
    main()
