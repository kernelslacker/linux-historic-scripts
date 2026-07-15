#!/usr/bin/env python3
"""Continue the git history through 1.0/1.1/1.2/1.3/pre2.0. Python port of
import-1.x.sh.

Reuses the repo built by import-0.x.py (must already exist at
unpack/linux-git, checked out on master at the 1.0alpha tag) and continues
committing into it -- it does not create a fresh repo. 1.0 splits off onto
branch "1.0" at 1.0.6 while "master" continues into 1.1; 1.2 splits off onto
branch "1.2" at 1.2.10 while "master" continues into 1.3.
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
from linux_hist_1x import LINUS, VERSIONS, changelog_path


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    repo, env = open_repo("import-0.x.py", LINUS)

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
