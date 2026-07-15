#!/usr/bin/env python3
"""Generate diffs/linux-VERSION.diff for 2.0.x.

"2.0"'s base (pre2.0.14) comes from the 1.x series, so unpack/linux-
pre2.0.14 must already exist (run untar-1.x.py first). Alias versions
(2.0.34, 2.0.36, 2.0.38) have no diff of their own -- skipped.
"""

import argparse
from pathlib import Path

from linux_hist_common import DIFFS, log, tree_dir, write_diff
from linux_hist_2_0 import VERSIONS, Version


def make_diff(v: Version, force: bool) -> None:
    out: Path = DIFFS / f"linux-{v.name}.diff"
    if out.exists() and not force:
        log(f"skip diff for {v.name} (already exists)")
        return
    base_dir: Path = tree_dir(v.base)
    if not base_dir.exists():
        raise FileNotFoundError(
            f"base tree missing for {v.name}: {base_dir} "
            "(run untar-1.x.py first if this is pre2.0.14)"
        )
    log(f"diffing {v.name}")
    write_diff(v.base, v.name, out)


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
        make_diff(v, args.force)


if __name__ == "__main__":
    main()
