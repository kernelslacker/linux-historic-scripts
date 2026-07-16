#!/usr/bin/env python3
"""Generate diffs/linux-VERSION.diff for 2.4.x. New script (no shell reference existed).

2.4.0's base (2.4.0-prerelease) comes from the 2.3 series, so unpack/linux-
2.4.0-prerelease must already exist (run untar-2.3.py first).
"""

from linux_hist_common import make_diff, parse_force
from linux_hist_2_4 import VERSIONS


def main() -> None:
    args = parse_force(__doc__)

    for v in VERSIONS:
        make_diff(
            v.name,
            v.base,
            args.force,
            "(run untar-2.3.py first if this is 2.4.0-prerelease)",
        )


if __name__ == "__main__":
    main()
