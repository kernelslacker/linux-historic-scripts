#!/usr/bin/env python3
"""Structural integrity checks for the per-branch VERSIONS tables.

Pure-data checks over the linux_hist_*.py tables -- no binaries, no built
repo, milliseconds to run, so they're cheap enough for CI and for a
pre-flight before a multi-hour build. They catch the data-entry slips a
hand-maintained 1600-row table is prone to:

  * a `base` / `patch_base` / `alias_of` that names a version that doesn't
    exist (typo, or a rename that missed a reference);
  * a version listed as its own base;
  * a duplicate version name (these become git tags, which must be unique);
  * a `date` string git's parser wouldn't accept.

Deliberately NOT checked: date monotonicity. The real history is genuinely
non-monotonic in valid ways -- development forks (1.0.9 -> 1.1.0), prereleases
dated just before the stable they follow in the list, and the documented
2.0.40pre3 / 2.2.18pre1 oddities -- so a monotonicity rule is false-positive
noise. Artifact-level fidelity (does a tag's tree match its tarball) is
verify.py's job, not this one's.
"""

import argparse
import importlib
from datetime import datetime
from types import ModuleType

from linux_hist_common import log

# branch id -> module holding its VERSIONS table, in dependency order
BRANCH_MODULES: dict[str, str] = {
    "0.x": "linux_hist_0x",
    "1.x": "linux_hist_1x",
    "2.0": "linux_hist_2_0",
    "2.1": "linux_hist_2_1",
    "2.2": "linux_hist_2_2",
    "2.3": "linux_hist_2_3",
    "2.4": "linux_hist_2_4",
    "2.5": "linux_hist_2_5",
    "2.6": "linux_hist_2_6",
}

# git accepts this for both --date and GIT_COMMITTER_DATE
DATE_FMT: str = "%a %b %d %H:%M:%S %Y %z"


def load_versions() -> list[tuple[str, str, object]]:
    """Return (branch, module, version) triples for every table row."""
    rows: list[tuple[str, str, object]] = []
    for branch, mod_name in BRANCH_MODULES.items():
        module: ModuleType = importlib.import_module(mod_name)
        for v in module.VERSIONS:
            rows.append((branch, mod_name, v))
    return rows


def check_unique_names(rows: list[tuple[str, str, object]]) -> list[str]:
    problems: list[str] = []
    seen: dict[str, str] = {}
    for branch, _, v in rows:
        name: str = v.name  # type: ignore[attr-defined]
        if name in seen:
            problems.append(
                f"duplicate version name {name!r} (in {seen[name]} and {branch})"
            )
        seen[name] = branch
    return problems


def check_references(rows: list[tuple[str, str, object]]) -> list[str]:
    problems: list[str] = []
    known: set[str] = {v.name for _, _, v in rows}  # type: ignore[attr-defined]
    for branch, _, v in rows:
        name: str = v.name  # type: ignore[attr-defined]
        for field in ("base", "patch_base", "alias_of"):
            ref = getattr(v, field, None)
            if ref is None:
                continue
            if ref == name:
                problems.append(f"{branch}: {name} lists itself as {field}")
            elif ref not in known:
                problems.append(
                    f"{branch}: {name} {field}={ref!r} names an unknown version"
                )
    return problems


def check_dates(rows: list[tuple[str, str, object]]) -> list[str]:
    problems: list[str] = []
    for branch, _, v in rows:
        date = getattr(v, "date", None)
        if date is None:
            continue  # alias entries legitimately carry no date
        try:
            datetime.strptime(date, DATE_FMT)
        except ValueError:
            name: str = v.name  # type: ignore[attr-defined]
            problems.append(f"{branch}: {name} has an unparseable date {date!r}")
    return problems


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.parse_args()

    rows: list[tuple[str, str, object]] = load_versions()
    problems: list[str] = (
        check_unique_names(rows) + check_references(rows) + check_dates(rows)
    )

    for problem in problems:
        log(f"FAIL {problem}")
    log(
        f"checked {len(rows)} versions across {len(BRANCH_MODULES)} branches: "
        f"{len(problems)} problem(s)"
    )
    raise SystemExit(1 if problems else 0)


if __name__ == "__main__":
    main()
