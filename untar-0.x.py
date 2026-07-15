#!/usr/bin/env python3
"""Unpack the 0.x kernel tarballs and apply prepatches. Python port of untar-0.x.sh."""

import argparse
import os
from pathlib import Path

from linux_hist_common import UNPACK, apply_patch, extract_tarball, tree_dir
from linux_hist_0x import BINARIES, VERSIONS, Compression, Version


def fix_permissions(v: Version) -> None:
    # 0.97's upstream tarball has mode 644 on every directory (no +x), so
    # nothing under it can even be listed/stat'd until this runs. Fix
    # top-down so each directory is walkable before we descend into it.
    dest: Path = tree_dir(v.name)
    dest.chmod(dest.stat().st_mode | 0o111)
    for dirpath, dirnames, _ in os.walk(dest):
        for name in dirnames:
            p: Path = Path(dirpath, name)
            p.chmod(p.stat().st_mode | 0o111)


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
            extract_tarball(
                v.name,
                tree_dir(v.name),
                BINARIES / f"linux-{v.name}.tar.bz2",
                args.force,
            )
        else:
            cat_cmd: str = "bzcat" if v.compression == Compression.BZ2 else "zcat"
            apply_patch(
                v.name,
                tree_dir(v.name),
                tree_dir(v.base),
                BINARIES / v.patch,
                cat_cmd,
                args.force,
                args.strict,
            )
        if v.fix_perms:
            fix_permissions(v)


if __name__ == "__main__":
    main()
