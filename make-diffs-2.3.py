#!/usr/bin/env python3
"""Generate diffs/linux-VERSION.diff for 2.3.x + 2.4.0-testN. Python port
of make-diffs-2.3.sh.

2.3.0's base (2.2.8) comes from the 2.2 series, so unpack/2.2/linux-2.2.8
must already exist (run untar-2.2.py first). Alias versions (2.3.8, 2.4.0-test3)
still get a real diff generated here, matching the original script exactly
-- only import.py skips applying them. dir_name is used for the actual
`diff` arguments (matching what's really on disk for the 2.3.99 family);
the output file is always named after the canonical version name.
"""

from linux_hist_common import make_diff, parse_force
from linux_hist_2_3 import VERSIONS, dirname_of


def main() -> None:
    args = parse_force(__doc__)

    for v in VERSIONS:
        make_diff(
            v.name,
            v.base,
            args.force,
            "(run untar-2.2.py first if this is 2.2.8)",
            dirname_of,
        )


if __name__ == "__main__":
    main()
