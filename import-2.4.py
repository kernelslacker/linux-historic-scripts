#!/usr/bin/env python3
"""Continue the git history through 2.4.x. New script (no shell reference existed).

Reuses the repo built by import-2.3.py (must already exist at
unpack/linux-git, on branch "master" at the 2.4.0-prerelease tag). At
2.4.16, branches off onto "2.4" (2.5.1 forked from 2.4.15 in real history,
and Linus' own tree moved on from there -- matches the 1.0/1.1, 2.0/2.1,
2.2/2.3 pattern). Always Linus Torvalds; no aliases in this segment.
"""

import argparse

from linux_hist_common import (
    branch_exists,
    import_version,
    log,
    open_repo,
    run,
    tag_exists,
)
from linux_hist_2_4 import LINUS, VERSIONS, changelog_path


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    repo, env = open_repo("import-2.3.py", LINUS)

    for v in VERSIONS:
        if v.branch_create and not branch_exists(repo, v.branch_create):
            run(["git", "branch", v.branch_create], cwd=repo, env=env)
        if v.branch_checkout:
            run(["git", "checkout", v.branch_checkout], cwd=repo, env=env)

        if tag_exists(repo, v.name):
            log(f"skip {v.name} (already imported)")
            continue

        import_version(repo, v.name, v.date, env, changelog_path(v))


if __name__ == "__main__":
    main()
