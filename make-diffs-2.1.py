#!/usr/bin/env python3
"""Generate diffs/linux-VERSION.diff for 2.1.x + 2.2.0pre1-9. Python port
of make-diffs-2.1.sh."""

from linux_hist_common import make_diff, parse_force
from linux_hist_2_1 import VERSIONS


def main() -> None:
    args = parse_force(__doc__)

    for v in VERSIONS:
        make_diff(v.name, v.base, args.force)


if __name__ == "__main__":
    main()
