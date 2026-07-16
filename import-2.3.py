#!/usr/bin/env python3
"""Continue the git history through 2.3.x + 2.4.0-testN. Python port of
import-2.3.sh.

Reuses the repo built by import-2.2.py (must already exist at
linux-git, on branch "master" at the 2.2.8 tag -- 2.2's own stable
maintenance continues separately on branch "2.2"). Stays on master
throughout, always Linus Torvalds.

2.3.8 and 2.4.0-test3 are tag-only aliases (of 2.3.8pre3 and
2.4.0-test3pre9 respectively) -- their diffs exist on disk but are
deliberately not applied here, matching the original script.
"""

from linux_hist_common import import_version, log, open_repo, parse_no_flags
from linux_hist_2_3 import LINUS, VERSIONS, changelog_path


def main() -> None:
    parse_no_flags(__doc__)

    repo = open_repo("import-2.2.py", LINUS)

    for v in VERSIONS:
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
