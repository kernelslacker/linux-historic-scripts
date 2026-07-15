#!/usr/bin/env python3
"""Unpack the 2.1.x tarballs and apply prepatches. Python port of
untar-2.1.sh."""

from collections.abc import Callable
from pathlib import Path

from linux_hist_common import (
    UNPACK,
    apply_patch,
    extract_tarball,
    parse_force_strict,
    tree_dir,
)
from linux_hist_2_1 import BINARIES, VERSIONS, Version


def apply_fixup(v: Version) -> Callable[[Path], None]:
    def prepare(tmp: Path) -> None:
        if v.fixup:
            for rel, content in v.fixup.items():
                (tmp / rel).write_text(content)

    return prepare


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
                prepare=apply_fixup(v),
            )


if __name__ == "__main__":
    main()
