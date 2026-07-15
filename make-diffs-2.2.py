#!/usr/bin/env python3
"""Generate diffs/linux-VERSION.diff for 2.2.x.

Alias versions (2.2.18pre27, 2.2.18) still get a real diff generated here,
matching the original script exactly -- only import.py skips applying them.
"""

import argparse

from linux_hist_common import DIFFS, make_diff
from linux_hist_2_2 import VERSIONS


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
            "(run untar-2.1.py first if this is 2.2.0pre9)",
        )


if __name__ == "__main__":
    main()
