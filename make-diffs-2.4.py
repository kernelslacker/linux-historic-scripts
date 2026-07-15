#!/usr/bin/env python3
"""Generate diffs/linux-VERSION.diff for 2.4.x. New script (no shell reference existed).

2.4.0's base (2.4.0-prerelease) comes from the 2.3 series, so unpack/linux-
2.4.0-prerelease must already exist (run untar-2.3.py first).
"""

import argparse

from linux_hist_common import DIFFS, make_diff
from linux_hist_2_4 import VERSIONS


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force", action="store_true", help="regenerate diffs that already exist"
    )
    args: argparse.Namespace = parser.parse_args()

    DIFFS.mkdir(exist_ok=True)
    for v in VERSIONS:
        make_diff(
            v.name,
            v.base,
            args.force,
            "(run untar-2.3.py first if this is 2.4.0-prerelease)",
        )


if __name__ == "__main__":
    main()
