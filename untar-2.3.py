#!/usr/bin/env python3
"""Unpack the 2.3.x / 2.4.0-testN tarballs and apply prepatches. Python
port of untar-2.3.sh.

2.3.0's base (2.2.8) comes from the 2.2 series, so unpack/linux-2.2.8 must
already exist (run untar-2.2.py first). Alias versions (2.3.8, 2.4.0-test3)
still get real trees built here -- only import.py treats them specially.
"""

import argparse
from pathlib import Path

from linux_hist_common import UNPACK, apply_patch, extract_tarball
from linux_hist_2_3 import BINARIES, VERSIONS, tree_dir


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force", action="store_true", help="rebuild trees that already exist"
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="abort on the first patch that doesn't apply cleanly",
    )
    args: argparse.Namespace = parser.parse_args()

    UNPACK.mkdir(exist_ok=True)
    for v in VERSIONS:
        if v.patch is None:
            archive: Path = BINARIES / f"linux-{v.dir_name or v.name}.tar.gz"
            extract_tarball(v.name, tree_dir(v.name), archive, args.force)
        else:
            apply_patch(
                v.name,
                tree_dir(v.name),
                tree_dir(v.patch_base or v.base),
                BINARIES / v.patch,
                "zcat",
                args.force,
                args.strict,
                missing_base_hint="(run untar-2.2.py first if this is 2.2.8)",
            )


if __name__ == "__main__":
    main()
