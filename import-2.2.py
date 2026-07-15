#!/usr/bin/env python3
"""Continue the git history through 2.2.x.

Reuses the repo built by import-2.1.py (must already exist at
unpack/linux-git, on branch "master" at the 2.2.0pre9 tag). At 2.2.8,
branches off onto "2.2" (mirroring 2.0/2.1's split) and never checks back
out to master -- 2.3's import continues master from 2.2.8. Author changes
to Alan Cox at 2.2.11pre1, still on branch "2.2".

2.2.18pre27 and 2.2.18 are tag-only aliases of 2.2.18pre26's commit (see
linux_hist_2_2.py) -- their diffs exist on disk but are deliberately not
applied here, matching the original script.
"""

import argparse
from pathlib import Path

from linux_hist_common import (
    DIFFS,
    UNPACK,
    apply_diff,
    author_env,
    branch_exists,
    commit_version,
    log,
    remove_empty_files,
    run,
    tag_exists,
)
from linux_hist_2_2 import LINUS, VERSIONS, changelog_path


def main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()

    repo: Path = UNPACK / "linux-git"
    if not (repo / ".git").exists():
        raise FileNotFoundError(f"{repo} doesn't exist -- run import-2.1.py first")
    env: dict[str, str] = author_env(LINUS)
    run(["git", "checkout", "master"], cwd=repo, env=env)

    for v in VERSIONS:
        if v.author:
            env = author_env(v.author)

        if v.branch_create and not branch_exists(repo, v.branch_create):
            run(["git", "branch", v.branch_create], cwd=repo, env=env)
        if v.branch_checkout:
            run(["git", "checkout", v.branch_checkout], cwd=repo, env=env)

        if v.alias_of:
            if tag_exists(repo, v.name):
                log(f"skip {v.name} (already tagged)")
                continue
            log(f"tagging {v.name} -> {v.alias_of}")
            run(["git", "tag", v.name], cwd=repo, env=env)
            continue

        if tag_exists(repo, v.name):
            log(f"skip {v.name} (already imported)")
            continue

        log(f"importing {v.name}")
        diff_file: Path = DIFFS / f"linux-{v.name}.diff"
        if not diff_file.exists():
            raise FileNotFoundError(diff_file)
        apply_diff(repo, diff_file, v.name)
        run(["git", "add", "--all"], cwd=repo, env=env)
        remove_empty_files(repo, env)
        commit_version(repo, v.name, v.date, env, changelog_path(v))
        run(["git", "tag", v.name], cwd=repo, env=env)


if __name__ == "__main__":
    main()
