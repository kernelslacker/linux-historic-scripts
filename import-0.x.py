#!/usr/bin/env python3
"""Build the 0.x git history from the generated diffs. Python port of
import-0.x.sh."""

import argparse
import shutil
from pathlib import Path

from linux_hist_common import (
    UNPACK,
    author_env,
    commit_version,
    hardlink_tree,
    import_version,
    log,
    run,
    tree_dir,
)
from linux_hist_0x import LINUS, VERSIONS, Version, changelog_path


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
    commit_version(repo, first.name, first.date, env, changelog_path(first))
    # No tag for the seed commit -- matches the original import.sh, which
    # never tags 0.01 either.

    for v in rest:
        import_version(repo, v.name, v.date, env, changelog_path(v))


if __name__ == "__main__":
    main()
