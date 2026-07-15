#!/usr/bin/env python3
"""Unpack the 0.x kernel tarballs and apply prepatches. Python port of untar-0.x.sh."""

import argparse
import os
import shutil
import subprocess
from pathlib import Path

from linux_hist_common import (
    UNPACK,
    extract_to,
    hardlink_tree,
    log,
    patch_tree,
    tree_dir,
)
from linux_hist_0x import BINARIES, VERSIONS, Version


def extract_tarball(v: Version, force: bool) -> None:
    dest: Path = tree_dir(v.name)
    if dest.exists() and not force:
        log(f"skip {v.name} (already unpacked)")
        return
    archive: Path = BINARIES / f"linux-{v.name}.tar.bz2"
    if not archive.exists():
        raise FileNotFoundError(archive)
    log(f"unpacking {v.name}")
    extract_to(archive, dest)


def apply_patch(v: Version, force: bool, strict: bool) -> None:
    dest: Path = tree_dir(v.name)
    if dest.exists() and not force:
        log(f"skip {v.name} (already patched)")
        return
    base: Path = tree_dir(v.base)
    if not base.exists():
        raise FileNotFoundError(f"base tree missing for {v.name}: {base}")
    patchfile: Path = BINARIES / v.patch
    if not patchfile.exists():
        raise FileNotFoundError(patchfile)
    log(f"patching to {v.name}")
    if dest.exists():
        shutil.rmtree(dest)
    hardlink_tree(base, dest)
    cat_cmd: str = "bzcat" if v.compression == "bz2" else "zcat"
    patch_bytes: bytes = subprocess.run(
        [cat_cmd, str(patchfile)], capture_output=True, check=True
    ).stdout
    patch_tree(dest, patch_bytes, v.name, strict)


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
            extract_tarball(v, args.force)
        else:
            apply_patch(v, args.force, args.strict)
        if v.fix_perms:
            fix_permissions(v)


if __name__ == "__main__":
    main()
