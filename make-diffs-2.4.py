#!/usr/bin/env python3
"""Generate diffs/linux-VERSION.diff for 2.4.x. New script (no shell reference existed).

2.4.0's base (2.4.0-prerelease) comes from the 2.3 series, so unpack/linux-
2.4.0-prerelease must already exist (run untar-2.3.py first).
"""

import argparse
from pathlib import Path

from linux_hist_common import DIFFS, log, tree_dir, write_diff
from linux_hist_2_4 import VERSIONS, Version


def make_diff(v: Version, force: bool) -> None:
    out: Path = DIFFS / f"linux-{v.name}.diff"
    if out.exists() and not force:
        log(f"skip diff for {v.name} (already exists)")
        return
    base_dir: Path = tree_dir(v.base)
    if not base_dir.exists():
        raise FileNotFoundError(
            f"base tree missing for {v.name}: {base_dir} "
            "(run untar-2.3.py first if this is 2.4.0-prerelease)"
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
        make_diff(v, args.force)


if __name__ == "__main__":
    main()
