#!/usr/bin/env python3
"""Generate diffs/linux-VERSION.diff for 1.0/1.1/1.2/1.3/pre2.0. Python
port of make-diffs-1.x.sh.

1.0's base (1.0alpha) comes from the 0.x series, so unpack/linux-1.0alpha
must already exist (run untar-0.x.py first).
"""

from linux_hist_common import make_diff, parse_force
from linux_hist_1x import VERSIONS


def main() -> None:
    args = parse_force(__doc__)

    for v in VERSIONS:
        make_diff(
            v.name,
            v.base,
            args.force,
            "(run untar-0.x.py first if this is 1.0alpha)",
        )


if __name__ == "__main__":
    main()
