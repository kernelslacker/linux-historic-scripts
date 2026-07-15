#!/usr/bin/env python3
"""Unpack the 2.5.x tarballs. New script (no shell reference existed) -- pure
tarball chain, no prepatches archived.

2.5.1's base (2.4.15) comes from the 2.4 series, so unpack/linux-2.4.15
must already exist (run untar-2.4.py first).
"""

import argparse
from pathlib import Path

from linux_hist_common import UNPACK, extract_to, log, tree_dir
from linux_hist_2_5 import BINARIES, VERSIONS, Version


def extract_tarball(v: Version, force: bool) -> None:
    dest: Path = tree_dir(v.name)
    if dest.exists() and not force:
        log(f"skip {v.name} (already unpacked)")
        return
    archive: Path = BINARIES / f"linux-{v.name}.tar.gz"
    if not archive.exists():
        raise FileNotFoundError(archive)
    log(f"unpacking {v.name}")
    extract_to(archive, dest)


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--force", action="store_true", help="rebuild trees that already exist"
    )
    args: argparse.Namespace = parser.parse_args()

    UNPACK.mkdir(exist_ok=True)
    for v in VERSIONS:
        extract_tarball(v, args.force)


if __name__ == "__main__":
    main()
