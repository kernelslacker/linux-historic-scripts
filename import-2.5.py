#!/usr/bin/env python3
"""Continue the git history through 2.5.x. New script (no shell reference existed).

Reuses the repo built by import-2.4.py (must already exist at
unpack/linux-git). Checks out "master" (which import-2.4.py left parked at
2.4.15 -- 2.4.16 onward moved onto branch "2.4") and continues from there,
always Linus Torvalds. Real per-release changelogs come from
binaries/2.5/ChangeLog-N (not the usual changelogs/ dir).
"""

import argparse

from linux_hist_common import import_version, log, open_repo
from linux_hist_2_5 import LINUS, VERSIONS, changelog_path


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    repo = open_repo("import-2.4.py", LINUS)

    for v in VERSIONS:
        if repo.tag_exists(v.name):
            log(f"skip {v.name} (already imported)")
            continue

        import_version(repo, v.name, v.date, changelog_path(v))


if __name__ == "__main__":
    main()
