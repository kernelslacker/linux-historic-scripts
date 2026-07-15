#!/usr/bin/env python3
"""Build the 0.x git history from the generated diffs."""

import argparse
import shutil
from pathlib import Path

from linux_hist_common import (
    CHANGELOGS,
    DIFFS,
    UNPACK,
    apply_diff,
    author_env,
    commit_version,
    hardlink_tree,
    log,
    remove_empty_files,
    run,
    tree_dir,
)
from linux_hist_0x import LINUS, VERSIONS, Version


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    repo: Path = UNPACK / "linux-git"
    env: dict[str, str] = author_env(LINUS)
    first: Version = VERSIONS[0]
    rest: list[Version] = VERSIONS[1:]

    if repo.exists():
        shutil.rmtree(repo)
    log(f"seeding repo from {first.name}")
    hardlink_tree(tree_dir(first.name), repo)
    # Pin the initial branch name explicitly -- don't rely on the operator's
    # init.defaultBranch, since import-1.x.py hardcodes "master" for the
    # branch/checkout points inherited from the original shell scripts.
    run(["git", "init", "-q", "-b", "master"], cwd=repo, env=env)
    run(["git", "add", "--all"], cwd=repo, env=env)
    commit_version(repo, first.name, first.date, env, CHANGELOGS / f"{first.name}.txt")
    # No tag for the seed commit -- matches the original import.sh, which
    # never tags 0.01 either.

    for v in rest:
        log(f"importing {v.name}")
        diff_file: Path = DIFFS / f"linux-{v.name}.diff"
        if not diff_file.exists():
            raise FileNotFoundError(diff_file)
        apply_diff(repo, diff_file.read_bytes(), v.name)
        run(["git", "add", "--all"], cwd=repo, env=env)
        remove_empty_files(repo, env)
        commit_version(repo, v.name, v.date, env, CHANGELOGS / f"{v.name}.txt")
        run(["git", "tag", v.name], cwd=repo, env=env)


if __name__ == "__main__":
    main()
