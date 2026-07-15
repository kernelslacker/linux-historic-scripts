#!/usr/bin/env python3
"""Generate diffs/linux-VERSION.diff for 2.5.x. New script (no shell reference existed).

2.5.1's base (2.4.15) comes from the 2.4 series, so unpack/linux-2.4.15
must already exist (run untar-2.4.py first).
"""

import argparse

from linux_hist_common import DIFFS, make_diff
from linux_hist_2_5 import VERSIONS


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force", action="store_true", help="regenerate diffs that already exist"
    )
    args: argparse.Namespace = parser.parse_args()

    DIFFS.mkdir(exist_ok=True)
    for v in VERSIONS:
        make_diff(
            v.name, v.base, args.force, "(run untar-2.4.py first if this is 2.4.15)"
        )


if __name__ == "__main__":
    main()
