#!/usr/bin/env python3
"""Build the 0.x git history from the generated diffs. Python port of
import-0.x.sh."""

import shutil

from linux_hist_common import (
    BUILD_REPO,
    GitRepo,
    author_env,
    hardlink_tree,
    import_version,
    log,
    parse_no_flags,
    tree_dir,
)
from linux_hist_0x import LINUS, VERSIONS, Version, changelog_path


def main() -> None:
    parse_no_flags(__doc__)

    repo: GitRepo = GitRepo(BUILD_REPO, author_env(LINUS))
    first: Version = VERSIONS[0]
    rest: list[Version] = VERSIONS[1:]

    if repo.path.exists():
        shutil.rmtree(repo.path)
    log(f"seeding repo from {first.name}")
    hardlink_tree(tree_dir(first.name), repo.path)
    # Pin the initial branch name explicitly -- don't rely on the operator's
    # init.defaultBranch, since import-1.x.py hardcodes "master" for the
    # branch/checkout points inherited from the original shell scripts.
    repo.git("init", "-q", "-b", "master")
    repo.git("add", "--all")
    repo.commit(first.name, first.date, changelog_path(first))
    # No tag for the seed commit -- matches the original import.sh, which
    # never tags 0.01 either.

    for v in rest:
        import_version(repo, v.name, v.date, changelog_path(v))


if __name__ == "__main__":
    main()
