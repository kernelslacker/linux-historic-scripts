#!/usr/bin/env python3
"""Generate diffs/linux-VERSION.diff for the 0.x series. Python port of
make-diffs-0.x.sh."""

from linux_hist_common import DIFFS, make_diff, parse_force
from linux_hist_0x import VERSIONS


def main() -> None:
    args = parse_force(__doc__)

    DIFFS.mkdir(exist_ok=True)
    for v in VERSIONS:
        if v.base is None:
            continue
        make_diff(v.name, v.base, args.force, "(run untar-0.x.py first)")


if __name__ == "__main__":
    main()
