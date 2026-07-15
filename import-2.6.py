#!/usr/bin/env python3
"""Continue the git history through 2.6.x. New script (no shell reference existed).

Reuses the repo built by import-2.5.py (must already exist at
unpack/linux-git). Checks out "master" and continues from 2.5.75, always
Linus Torvalds. Real per-release changelogs come from
binaries/2.6/ChangeLog-N (not the usual changelogs/ dir).

Stops at 2.6.11.12 -- the official upstream git tree begins at Linux
2.6.12-rc2, so this project's job is done from there on (see
linux_hist_2_6.py for why there's no 2.6.12-rc1 entry to stop closer to).

Diffs are applied with `patch -p1` (via apply_diff): on this branch's larger
diffs, `git apply --whitespace=nowarn` was observed to exit 0 while silently
failing to apply some hunks (e.g. drivers/net/tg3.c in the 2.6.1 diff) --
caught by comparing the imported tree against the independently unpacked
source, not by any error message. `patch` applied the exact same diffs
correctly. See linux_hist_common.apply_diff.
"""

from linux_hist_common import import_version, log, open_repo, parse_no_flags
from linux_hist_2_6 import LINUS, VERSIONS, changelog_path


def main() -> None:
    parse_no_flags(__doc__)

    repo = open_repo("import-2.5.py", LINUS)

    for v in VERSIONS:
        if repo.tag_exists(v.name):
            log(f"skip {v.name} (already imported)")
            continue

        import_version(repo, v.name, v.date, changelog_path(v))


if __name__ == "__main__":
    main()
