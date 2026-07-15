#!/usr/bin/env python3
"""Continue the git history through 2.5.x. New script (no shell reference existed).

Reuses the repo built by import-2.4.py (must already exist at
unpack/linux-git). Checks out "master" (which import-2.4.py left parked at
2.4.15 -- 2.4.16 onward moved onto branch "2.4") and continues from there,
always Linus Torvalds. Real per-release changelogs come from
binaries/2.5/ChangeLog-N (not the usual changelogs/ dir).
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
from linux_hist_2_5 import LINUS, VERSIONS, changelog_path


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    repo: Path = UNPACK / "linux-git"
    if not (repo / ".git").exists():
        raise FileNotFoundError(f"{repo} doesn't exist -- run import-2.4.py first")
    env: dict[str, str] = author_env(LINUS)
    run(["git", "checkout", "master"], cwd=repo, env=env)

    for v in VERSIONS:
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
