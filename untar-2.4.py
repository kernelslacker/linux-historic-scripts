#!/usr/bin/env python3
"""Unpack the 2.4.x tarballs and apply prepatches. Python port/extension of untar-2.4.sh
(the original only went to 2.4.15; this covers the full range -- see linux_hist_2_4.py).

2.4.0's base (2.4.0-prerelease) comes from the 2.3 series, so unpack/linux-
2.4.0-prerelease must already exist (run untar-2.3.py first).
"""

import argparse
import shutil
import subprocess
from pathlib import Path

from linux_hist_common import UNPACK, extract_to, log, patch_tree, run, tree_dir
from linux_hist_2_4 import BINARIES, VERSIONS, Version


def extract_tarball(v: Version, force: bool) -> None:
    dest: Path = tree_dir(v.name)
    if dest.exists() and not force:
        log(f"skip {v.name} (already unpacked)")
        return
    archive: Path = BINARIES / (v.archive or f"linux-{v.name}.tar.gz")
    if not archive.exists():
        raise FileNotFoundError(archive)
    log(f"unpacking {v.name}")
    extract_to(archive, dest)


def apply_patch(v: Version, force: bool, strict: bool) -> None:
    dest: Path = tree_dir(v.name)
    if dest.exists() and not force:
        log(f"skip {v.name} (already patched)")
        return
    base: Path = tree_dir(v.patch_base or v.base)
    if not base.exists():
        raise FileNotFoundError(
            f"base tree missing for {v.name}: {base} "
            "(run untar-2.3.py first if this is 2.4.0-prerelease)"
        )
    patchfile: Path = BINARIES / v.patch
    if not patchfile.exists():
        raise FileNotFoundError(patchfile)
    log(f"patching to {v.name}")
    if dest.exists():
        shutil.rmtree(dest)
    run(["cp", "-rl", str(base), str(dest)])
    patch_bytes: bytes = subprocess.run(
        ["zcat", str(patchfile)], capture_output=True, check=True
    ).stdout
    patch_tree(dest, patch_bytes, v.name, strict)


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
