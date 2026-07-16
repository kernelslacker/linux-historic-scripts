#!/usr/bin/env python3
"""Unpack the 2.6.x tarballs. New script (no shell reference existed) -- pure
tarball chain, no prepatches archived.

2.6.0-test1's base (2.5.75) comes from the 2.5 series, so
unpack/2.5/linux-2.5.75 must already exist (run untar-2.5.py first).
"""

from pathlib import Path

from linux_hist_common import UNPACK, extract_tarball, parse_force, tree_dir
from linux_hist_2_6 import BINARIES, VERSIONS


def main() -> None:
    args = parse_force(__doc__, "rebuild trees that already exist")

    UNPACK.mkdir(exist_ok=True)
    for v in VERSIONS:
        archive: Path = BINARIES / f"linux-{v.name}.tar.gz"
        extract_tarball(v.name, tree_dir(v.name), archive, args.force)


if __name__ == "__main__":
    main()
