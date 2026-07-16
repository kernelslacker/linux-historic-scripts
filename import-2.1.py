#!/usr/bin/env python3
"""Continue the git history through 2.1.x + 2.2.0pre1-9. Python port of
import-2.1.sh.

Reuses the repo built by import-2.0.py (must already exist at
linux-git). Checks out "master" (which import-2.0.py left parked at
2.0.21) and continues from there, all as Linus Torvalds -- no branching or
author changes in this segment.
"""

from linux_hist_common import import_version, log, open_repo, parse_no_flags
from linux_hist_2_1 import LINUS, VERSIONS, changelog_path


def main() -> None:
    parse_no_flags(__doc__)

    repo = open_repo("import-2.0.py", LINUS)

    for v in VERSIONS:
        if repo.tag_exists(v.name):
            log(f"skip {v.name} (already imported)")
            continue

        import_version(repo, v.name, v.date, changelog_path(v))


if __name__ == "__main__":
    main()
