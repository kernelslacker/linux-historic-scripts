#!/usr/bin/env python3
"""Continue the git history through 2.0.x. Python port of import-2.0.sh.

Reuses the repo built by import-1.x.py (must already exist at
unpack/linux-git, on branch "master" at the pre2.0.14 tag). At 2.0.22,
branches off onto "2.0" (Alan Cox takes over) and never checks back out to
master -- 2.1's import continues master from 2.0.21. Author changes again
to David Weinehall at 2.0.39pre1, still on branch "2.0".
"""

import argparse

from linux_hist_common import author_env, import_version, log, open_repo
from linux_hist_2_0 import LINUS, VERSIONS, changelog_path


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    repo = open_repo("import-1.x.py", LINUS)

    for v in VERSIONS:
        if v.author:
            repo.env = author_env(v.author)

        if v.branch_create and not repo.branch_exists(v.branch_create):
            repo.branch(v.branch_create)
        if v.branch_checkout:
            repo.checkout(v.branch_checkout)

        if v.alias_of:
            if repo.tag_exists(v.name):
                log(f"skip {v.name} (already tagged)")
                continue
            log(f"tagging {v.name} -> {v.alias_of}")
            repo.tag(v.name)
            continue

        if repo.tag_exists(v.name):
            log(f"skip {v.name} (already imported)")
            continue

        import_version(repo, v.name, v.date, changelog_path(v))


if __name__ == "__main__":
    main()
