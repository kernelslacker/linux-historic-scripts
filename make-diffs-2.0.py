#!/usr/bin/env python3
"""Generate diffs/linux-VERSION.diff for 2.0.x.

"2.0"'s base (pre2.0.14) comes from the 1.x series, so unpack/linux-
pre2.0.14 must already exist (run untar-1.x.py first). Alias versions
(2.0.34, 2.0.36, 2.0.38) have no diff of their own -- skipped.
"""

import argparse

from linux_hist_common import DIFFS, make_diff
from linux_hist_2_0 import VERSIONS


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force", action="store_true", help="regenerate diffs that already exist"
    )
    args: argparse.Namespace = parser.parse_args()

    DIFFS.mkdir(exist_ok=True)
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
