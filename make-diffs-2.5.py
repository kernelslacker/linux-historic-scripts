#!/usr/bin/env python3
"""Generate diffs/linux-VERSION.diff for 2.5.x. New script (no shell reference existed).

2.5.1's base (2.4.15) comes from the 2.4 series, so unpack/linux-2.4.15
must already exist (run untar-2.4.py first).
"""

from linux_hist_common import make_diff, parse_force
from linux_hist_2_5 import VERSIONS


def main() -> None:
    args = parse_force(__doc__)

    for v in VERSIONS:
        make_diff(
            v.name, v.base, args.force, "(run untar-2.4.py first if this is 2.4.15)"
        )


if __name__ == "__main__":
    main()
