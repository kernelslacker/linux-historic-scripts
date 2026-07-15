#!/usr/bin/env python3
"""Unpack the 2.2.x tarballs and apply prepatches. Python port of
untar-2.2.sh.

2.2.0's base (2.2.0pre9) comes from the 2.1 series, so unpack/linux-
2.2.0pre9 must already exist (run untar-2.1.py first). Alias versions
(2.2.18pre27, 2.2.18) still get real trees built here -- only import.py
treats them specially.
"""

import argparse
from pathlib import Path

from linux_hist_common import (
    UNPACK,
    apply_prepatch,
    build_patched_tree,
    extract_tarball,
    log,
    tree_dir,
)
from linux_hist_2_2 import BINARIES, VERSIONS, Version


def apply_patch(v: Version, force: bool, strict: bool) -> None:
    dest: Path = tree_dir(v.name)
    if dest.exists() and not force:
        log(f"skip {v.name} (already patched)")
        return
    base: Path = tree_dir(v.patch_base or v.base)
    if not base.exists():
        raise FileNotFoundError(
            f"base tree missing for {v.name}: {base} "
            "(run untar-2.1.py first if this is 2.2.0pre9)"
        )
    patchfile: Path = BINARIES / v.patch
    if not patchfile.exists():
        raise FileNotFoundError(patchfile)
    log(f"patching to {v.name}")
    build_patched_tree(
        base,
        dest,
        lambda tmp: apply_prepatch(tmp, patchfile, "zcat", v.name, strict),
    )


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
            archive: Path = BINARIES / f"linux-{v.name}.tar.gz"
            extract_tarball(v.name, tree_dir(v.name), archive, args.force)
        else:
            apply_patch(v, args.force, args.strict)


if __name__ == "__main__":
    main()
