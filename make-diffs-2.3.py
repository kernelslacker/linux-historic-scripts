#!/usr/bin/env python3
"""Generate diffs/linux-VERSION.diff for 2.3.x + 2.4.0-testN.

2.3.0's base (2.2.8) comes from the 2.2 series, so unpack/linux-2.2.8 must
already exist (run untar-2.2.py first). Alias versions (2.3.8, 2.4.0-test3)
still get a real diff generated here, matching the original script exactly
-- only import.py skips applying them. dir_name is used for the actual
`diff` arguments (matching what's really on disk for the 2.3.99 family);
the output file is always named after the canonical version name.
"""

import argparse
from pathlib import Path

from linux_hist_common import DIFFS, log, write_diff
from linux_hist_2_3 import VERSIONS, Version, tree_dir

BY_NAME: dict[str, Version] = {v.name: v for v in VERSIONS}


def dirname_of(name: str) -> str:
    v: Version | None = BY_NAME.get(name)
    return v.dir_name if v and v.dir_name else name


def make_diff(v: Version, force: bool) -> None:
    out: Path = DIFFS / f"linux-{v.name}.diff"
    if out.exists() and not force:
        log(f"skip diff for {v.name} (already exists)")
        return
    base_dir: Path = tree_dir(v.base)
    if not base_dir.exists():
        raise FileNotFoundError(
            f"base tree missing for {v.name}: {base_dir} "
            "(run untar-2.2.py first if this is 2.2.8)"
        )
    log(f"diffing {v.name}")
    write_diff(dirname_of(v.base), dirname_of(v.name), out)


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
