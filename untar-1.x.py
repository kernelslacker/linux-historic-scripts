#!/usr/bin/env python3
"""Unpack the 1.0/1.1/1.2/1.3/pre2.0 tarballs and apply prepatches. Python
port of untar-1.x.sh."""

import argparse
from collections.abc import Callable
from pathlib import Path

from linux_hist_common import UNPACK, apply_patch, extract_tarball, tree_dir
from linux_hist_1x import BINARIES, VERSIONS, Version, series_dir


def chmod_writable(v: Version) -> Callable[[Path], None]:
    def prepare(tmp: Path) -> None:
        for rel in v.chmod_writable:
            p: Path = tmp / rel
            p.chmod(p.stat().st_mode | 0o200)

    return prepare


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
            archive: Path = (
                BINARIES / series_dir(v.name) / f"linux-{v.name}.tar.gz"
            )
            extract_tarball(v.name, tree_dir(v.name), archive, args.force)
        else:
            if v.compression == "none":
                cat_cmd: str | None = None
            elif v.compression == "bz2":
                cat_cmd = "bzcat"
            else:
                cat_cmd = "zcat"
            apply_patch(
                v.name,
                tree_dir(v.name),
                tree_dir(v.base),
                BINARIES / series_dir(v.name) / v.patch,
                cat_cmd,
                args.force,
                args.strict,
                prepare=chmod_writable(v),
            )


if __name__ == "__main__":
    main()
