#!/usr/bin/env python3
"""Unpack the 2.5.x tarballs. New script (no shell reference existed) -- pure
tarball chain, no prepatches archived.

2.5.1's base (2.4.15) comes from the 2.4 series, so unpack/linux-2.4.15
must already exist (run untar-2.4.py first).
"""

from pathlib import Path

from linux_hist_common import UNPACK, extract_tarball, parse_force, tree_dir
from linux_hist_2_5 import BINARIES, VERSIONS


def main() -> None:
    args = parse_force(__doc__, "rebuild trees that already exist")

    UNPACK.mkdir(exist_ok=True)
    for v in VERSIONS:
        archive: Path = BINARIES / f"linux-{v.name}.tar.gz"
        extract_tarball(v.name, tree_dir(v.name), archive, args.force)


if __name__ == "__main__":
    main()
