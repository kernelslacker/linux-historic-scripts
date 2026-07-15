#!/usr/bin/env python3
"""Generate diffs/linux-VERSION.diff for 1.0/1.1/1.2/1.3/pre2.0.

1.0's base (1.0alpha) comes from the 0.x series, so unpack/linux-1.0alpha
must already exist (run untar-0.x.py first).
"""

import argparse
from pathlib import Path

from linux_hist_common import DIFFS, log, tree_dir, write_diff
from linux_hist_1x import VERSIONS, Version


def make_diff(v: Version, force: bool) -> None:
    out: Path = DIFFS / f"linux-{v.name}.diff"
    if out.exists() and not force:
        log(f"skip diff for {v.name} (already exists)")
        return
    base_dir: Path = tree_dir(v.base)
    if not base_dir.exists():
        raise FileNotFoundError(
            f"base tree missing for {v.name}: {base_dir} "
            "(run untar-0.x.py first if this is 1.0alpha)"
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
