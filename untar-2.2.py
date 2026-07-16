#!/usr/bin/env python3
"""Unpack the 2.2.x tarballs and apply prepatches. Python port of
untar-2.2.sh.

2.2.0's base (2.2.0pre9) comes from the 2.1 series, so
unpack/2.2/linux-2.2.0pre9 must already exist (run untar-2.1.py first).
Alias versions
(2.2.18pre27, 2.2.18) still get real trees built here -- only import.py
treats them specially.
"""

from pathlib import Path

from linux_hist_common import (
    UNPACK,
    apply_patch,
    extract_tarball,
    parse_force_strict,
    tree_dir,
)
from linux_hist_2_2 import BINARIES, VERSIONS


def main() -> None:
    args = parse_force_strict(__doc__)

    UNPACK.mkdir(exist_ok=True)
    for v in VERSIONS:
        if v.patch is None:
            archive: Path = BINARIES / f"linux-{v.name}.tar.gz"
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
                missing_base_hint=("(run untar-2.1.py first if this is 2.2.0pre9)"),
            )


if __name__ == "__main__":
    main()
