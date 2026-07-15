#!/usr/bin/env python3
"""Unpack the 2.4.x tarballs and apply prepatches. Python port/extension of untar-2.4.sh
(the original only went to 2.4.15; this covers the full range -- see linux_hist_2_4.py).

2.4.0's base (2.4.0-prerelease) comes from the 2.3 series, so unpack/linux-
2.4.0-prerelease must already exist (run untar-2.3.py first).
"""

from pathlib import Path

from linux_hist_common import (
    UNPACK,
    apply_patch,
    extract_tarball,
    parse_force_strict,
    tree_dir,
)
from linux_hist_2_4 import BINARIES, VERSIONS


def main() -> None:
    args = parse_force_strict(__doc__)

    UNPACK.mkdir(exist_ok=True)
    for v in VERSIONS:
        if v.patch is None:
            archive: Path = BINARIES / (v.archive or f"linux-{v.name}.tar.gz")
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
                missing_base_hint=(
                    "(run untar-2.3.py first if this is 2.4.0-prerelease)"
                ),
            )


if __name__ == "__main__":
    main()
