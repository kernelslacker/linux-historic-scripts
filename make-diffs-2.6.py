#!/usr/bin/env python3
"""Generate diffs/linux-VERSION.diff for 2.6.x. New script (no shell reference existed).

2.6.0-test1's base (2.5.75) comes from the 2.5 series, so unpack/linux-
2.5.75 must already exist (run untar-2.5.py first).
"""

import argparse

from linux_hist_common import DIFFS, make_diff
from linux_hist_2_6 import VERSIONS


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force", action="store_true", help="regenerate diffs that already exist"
    )
    args: argparse.Namespace = parser.parse_args()

    DIFFS.mkdir(exist_ok=True)
    for v in VERSIONS:
        make_diff(
            v.name, v.base, args.force, "(run untar-2.5.py first if this is 2.5.75)"
        )


if __name__ == "__main__":
    main()
