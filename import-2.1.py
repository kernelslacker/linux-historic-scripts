#!/usr/bin/env python3
"""Continue the git history through 2.1.x + 2.2.0pre1-9.

Reuses the repo built by import-2.0.py (must already exist at
unpack/linux-git). Checks out "master" (which import-2.0.py left parked at
2.0.21) and continues from there, all as Linus Torvalds -- no branching or
author changes in this segment.
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
    tag_exists,
)
from linux_hist_2_1 import LINUS, VERSIONS, changelog_path


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    repo: Path = UNPACK / "linux-git"
    if not (repo / ".git").exists():
        raise FileNotFoundError(f"{repo} doesn't exist -- run import-2.0.py first")
    env: dict[str, str] = author_env(LINUS)
    run(["git", "checkout", "master"], cwd=repo, env=env)

    for v in VERSIONS:
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
