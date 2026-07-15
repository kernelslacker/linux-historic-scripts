#!/usr/bin/env python3
"""Continue the git history through 2.2.x. Python port of import-2.2.sh.

Reuses the repo built by import-2.1.py (must already exist at
unpack/linux-git, on branch "master" at the 2.2.0pre9 tag). At 2.2.8,
branches off onto "2.2" (mirroring 2.0/2.1's split) and never checks back
out to master -- 2.3's import continues master from 2.2.8. Author changes
to Alan Cox at 2.2.11pre1, still on branch "2.2".

2.2.18pre27 and 2.2.18 are tag-only aliases of 2.2.18pre26's commit (see
linux_hist_2_2.py) -- their diffs exist on disk but are deliberately not
applied here, matching the original script.
"""

from linux_hist_common import (
    author_env,
    import_version,
    log,
    open_repo,
    parse_no_flags,
)
from linux_hist_2_2 import LINUS, VERSIONS, changelog_path


def main() -> None:
    parse_no_flags(__doc__)

    repo = open_repo("import-2.1.py", LINUS)

    for v in VERSIONS:
        if v.author:
            repo.env = author_env(v.author)

        if v.branch_create and not repo.branch_exists(v.branch_create):
            repo.branch(v.branch_create)
        if v.branch_checkout:
            repo.checkout(v.branch_checkout)

        if v.alias_of:
            if repo.tag_exists(v.name):
                log(f"skip {v.name} (already tagged)")
                continue
            log(f"tagging {v.name} -> {v.alias_of}")
            repo.tag(v.name)
            continue

        if repo.tag_exists(v.name):
            log(f"skip {v.name} (already imported)")
            continue

        import_version(repo, v.name, v.date, changelog_path(v))


if __name__ == "__main__":
    main()
