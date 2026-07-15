#!/usr/bin/env python3
"""Continue the git history through 2.4.x. New script (no shell reference existed).

Reuses the repo built by import-2.3.py (must already exist at
unpack/linux-git, on branch "master" at the 2.4.0-prerelease tag). At
2.4.16, branches off onto "2.4" (2.5.1 forked from 2.4.15 in real history,
and Linus' own tree moved on from there -- matches the 1.0/1.1, 2.0/2.1,
2.2/2.3 pattern). Always Linus Torvalds; no aliases in this segment.
"""

from linux_hist_common import import_version, log, open_repo, parse_no_flags
from linux_hist_2_4 import LINUS, VERSIONS, changelog_path


def main() -> None:
    parse_no_flags(__doc__)

    repo = open_repo("import-2.3.py", LINUS)

    for v in VERSIONS:
        if v.branch_create and not repo.branch_exists(v.branch_create):
            repo.branch(v.branch_create)
        if v.branch_checkout:
            repo.checkout(v.branch_checkout)

        if repo.tag_exists(v.name):
            log(f"skip {v.name} (already imported)")
            continue

        import_version(repo, v.name, v.date, changelog_path(v))


if __name__ == "__main__":
    main()
