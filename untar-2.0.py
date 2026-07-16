#!/usr/bin/env python3
"""Unpack the 2.0.x tarballs and apply prepatches. Python port of
untar-2.0.sh.

pre2.0.14 comes from the 1.x series, so unpack/1.3/linux-pre2.0.14 must
already exist (run untar-1.x.py first).

Alias versions (2.0.34, 2.0.36, 2.0.38) don't get their own tree -- a
relative symlink is created instead, pointing at the real target's tree, so
that later cp -rl / diff steps that reference the alias name resolve
transparently while diff headers still read the alias's own name.
"""

import shutil
from pathlib import Path

from linux_hist_common import (
    UNPACK,
    apply_patch,
    extract_tarball,
    log,
    parse_force_strict,
    tree_dir,
)
from linux_hist_2_0 import BINARIES, VERSIONS, Version


def make_alias(v: Version, force: bool) -> None:
    dest: Path = tree_dir(v.name)
    if dest.exists() or dest.is_symlink():
        if not force:
            log(f"skip {v.name} (already aliased)")
            return
        if dest.is_symlink():
            dest.unlink()
        else:
            shutil.rmtree(dest)
    log(f"aliasing {v.name} -> {v.alias_of}")
    dest.symlink_to(f"linux-{v.alias_of}")


def main() -> None:
    args = parse_force_strict(__doc__)

    UNPACK.mkdir(exist_ok=True)
    for v in VERSIONS:
        if v.alias_of:
            make_alias(v, args.force)
        elif v.patch is None:
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
            )


if __name__ == "__main__":
    main()
