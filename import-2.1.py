#!/usr/bin/env python3
"""Continue the git history through 2.1.x + 2.2.0pre1-9. Python port of
import-2.1.sh.

Reuses the repo built by import-2.0.py (must already exist at
unpack/linux-git). Checks out "master" (which import-2.0.py left parked at
2.0.21) and continues from there, all as Linus Torvalds -- no branching or
author changes in this segment.
"""

import argparse

from linux_hist_common import import_version, log, open_repo, tag_exists
from linux_hist_2_1 import LINUS, VERSIONS, changelog_path


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    repo, env = open_repo("import-2.0.py", LINUS)

    for v in VERSIONS:
        if tag_exists(repo, v.name):
            log(f"skip {v.name} (already imported)")
            continue

        import_version(repo, v.name, v.date, env, changelog_path(v))


if __name__ == "__main__":
    main()
