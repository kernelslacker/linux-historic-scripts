#!/usr/bin/env python3
"""Unpack the 1.0/1.1/1.2/1.3/pre2.0 tarballs and apply prepatches."""

import argparse
import subprocess
from pathlib import Path

from linux_hist_common import (
    UNPACK,
    build_patched_tree,
    extract_to,
    log,
    patch_tree,
    tree_dir,
)
from linux_hist_1x import BINARIES, VERSIONS, Version, series_dir


def extract_tarball(v: Version, force: bool) -> None:
    dest: Path = tree_dir(v.name)
    if dest.exists() and not force:
        log(f"skip {v.name} (already unpacked)")
        return
    archive: Path = BINARIES / series_dir(v.name) / f"linux-{v.name}.tar.gz"
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
    patchfile: Path = BINARIES / series_dir(v.name) / v.patch
    if not patchfile.exists():
        raise FileNotFoundError(patchfile)
    log(f"patching to {v.name}")
    if v.compression == "none":
        patch_bytes: bytes = patchfile.read_bytes()
    else:
        cat_cmd: str = "bzcat" if v.compression == "bz2" else "zcat"
        patch_bytes = subprocess.run(
            [cat_cmd, str(patchfile)], capture_output=True, check=True
        ).stdout

    def prepare(tmp: Path) -> None:
        for rel in v.chmod_writable:
            p: Path = tmp / rel
            p.chmod(p.stat().st_mode | 0o200)
        patch_tree(tmp, patch_bytes, v.name, strict)

    build_patched_tree(base, dest, prepare)


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


if __name__ == "__main__":
    main()
