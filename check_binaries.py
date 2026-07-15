#!/usr/bin/env python3
"""Check the downloaded binaries against a pinned SHA-256 manifest.

The tarballs and patches under binaries/ aren't in the repo -- everyone
downloads their own ~11 GB from kernel.org (see the README). A wrong,
truncated, or tampered file is the most likely cause of a build that
diverges from the canonical history, and it won't surface until deep into a
multi-hour run. This pins every file's SHA-256 so a mismatch is caught up
front.

    ./check_binaries.py            # verify binaries/ against binaries.sha256
    ./check_binaries.py --update   # (re)generate the manifest from disk

The manifest is plain `sha256sum` format (`<hash>  <path>` relative to the
repo root), so `sha256sum -c binaries.sha256` works too.
"""

import argparse
import hashlib
from pathlib import Path

from linux_hist_common import ROOT, log

BINARIES: Path = ROOT / "binaries"
MANIFEST: Path = ROOT / "binaries.sha256"


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def disk_files() -> list[Path]:
    """Every regular file under binaries/, as repo-root-relative paths."""
    return sorted(p.relative_to(ROOT) for p in BINARIES.rglob("*") if p.is_file())


def read_manifest() -> dict[str, str]:
    entries: dict[str, str] = {}
    for line in MANIFEST.read_text().splitlines():
        if not line.strip():
            continue
        digest, _, path = line.partition("  ")
        entries[path] = digest
    return entries


def update() -> None:
    lines: list[str] = [f"{sha256(ROOT / rel)}  {rel}" for rel in disk_files()]
    MANIFEST.write_text("\n".join(lines) + "\n")
    log(f"wrote {MANIFEST.name} ({len(lines)} files)")


def verify() -> int:
    if not MANIFEST.exists():
        raise SystemExit(f"{MANIFEST.name} missing -- run --update first")
    expected: dict[str, str] = read_manifest()
    on_disk: set[str] = {str(rel) for rel in disk_files()}

    problems: int = 0
    for path, digest in expected.items():
        full: Path = ROOT / path
        if not full.exists():
            log(f"FAIL {path}: missing")
            problems += 1
        elif sha256(full) != digest:
            log(f"FAIL {path}: sha256 mismatch")
            problems += 1
    for path in sorted(on_disk - set(expected)):
        log(f"WARN {path}: on disk but not in manifest")

    log(f"checked {len(expected)} files: {problems} problem(s)")
    return problems


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--update",
        action="store_true",
        help="regenerate the manifest from what's on disk instead of verifying",
    )
    args: argparse.Namespace = parser.parse_args()

    if not BINARIES.exists():
        raise SystemExit(f"{BINARIES} not found -- download the binaries first")
    if args.update:
        update()
    else:
        raise SystemExit(1 if verify() else 0)


if __name__ == "__main__":
    main()
