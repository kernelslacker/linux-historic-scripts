#!/usr/bin/env python3
"""Generate diffs/linux-VERSION.diff for the 0.x series."""

import argparse

from linux_hist_common import DIFFS, make_diff
from linux_hist_0x import VERSIONS


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force", action="store_true", help="regenerate diffs that already exist"
    )
    args: argparse.Namespace = parser.parse_args()

    DIFFS.mkdir(exist_ok=True)
    for v in VERSIONS:
        if v.base is None:
            continue
        make_diff(v.name, v.base, args.force, "(run untar-0.x.py first)")


if __name__ == "__main__":
    main()
