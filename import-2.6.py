#!/usr/bin/env python3
"""Continue the git history through 2.6.x. New script (no shell reference existed).

Reuses the repo built by import-2.5.py (must already exist at
unpack/linux-git). Checks out "master" and continues from 2.5.75, always
Linus Torvalds. Real per-release changelogs come from
binaries/2.6/ChangeLog-N (not the usual changelogs/ dir).

Stops at 2.6.11.12 -- the official upstream git tree begins at Linux
2.6.12-rc2, so this project's job is done from there on (see
linux_hist_2_6.py for why there's no 2.6.12-rc1 entry to stop closer to).

Diffs are applied with `patch -p1` (via apply_diff): on this branch's larger
diffs, `git apply --whitespace=nowarn` was observed to exit 0 while silently
failing to apply some hunks (e.g. drivers/net/tg3.c in the 2.6.1 diff) --
caught by comparing the imported tree against the independently unpacked
source, not by any error message. `patch` applied the exact same diffs
correctly. See linux_hist_common.apply_diff.
"""

import argparse
from pathlib import Path

from linux_hist_common import (
    DIFFS,
    UNPACK,
    apply_diff,
    author_env,
    commit_version,
    log,
    remove_empty_files,
    run,
)
from linux_hist_2_6 import LINUS, VERSIONS, changelog_path


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    repo: Path = UNPACK / "linux-git"
    if not (repo / ".git").exists():
        raise FileNotFoundError(f"{repo} doesn't exist -- run import-2.5.py first")
    env: dict[str, str] = author_env(LINUS)
    run(["git", "checkout", "master"], cwd=repo, env=env)

    for v in VERSIONS:
        log(f"importing {v.name}")
        diff_file: Path = DIFFS / f"linux-{v.name}.diff"
        if not diff_file.exists():
            raise FileNotFoundError(diff_file)
        apply_diff(repo, diff_file.read_bytes(), v.name)
        run(["git", "add", "--all"], cwd=repo, env=env)
        remove_empty_files(repo, env)
        commit_version(repo, v.name, v.date, env, changelog_path(v))
        run(["git", "tag", v.name], cwd=repo, env=env)


if __name__ == "__main__":
    main()
