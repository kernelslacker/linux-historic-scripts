#!/usr/bin/env python3
"""Generate diffs/linux-VERSION.diff for 2.0.x. Python port of
make-diffs-2.0.sh.

"2.0"'s base (pre2.0.14) comes from the 1.x series, so
unpack/1.3/linux-pre2.0.14 must already exist (run untar-1.x.py first).
Alias versions
(2.0.34, 2.0.36, 2.0.38) have no diff of their own -- skipped.
"""

from linux_hist_common import make_diff, parse_force
from linux_hist_2_0 import VERSIONS


def main() -> None:
    args = parse_force(__doc__)

    for v in VERSIONS:
        if v.alias_of:
            continue
        make_diff(
            v.name,
            v.base,
            args.force,
            "(run untar-1.x.py first if this is pre2.0.14)",
        )


if __name__ == "__main__":
    main()
