#!/usr/bin/env python3
"""Generate diffs/linux-VERSION.diff for the 0.x series."""

import argparse
from pathlib import Path

from linux_hist_common import DIFFS, log, write_diff
from linux_hist_0x import VERSIONS, Version


def make_diff(v: Version, force: bool) -> None:
    out: Path = DIFFS / f"linux-{v.name}.diff"
    if out.exists() and not force:
        log(f"skip diff for {v.name} (already exists)")
        return
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
        if v.base is None:
            continue
        make_diff(v, args.force)


if __name__ == "__main__":
    main()
