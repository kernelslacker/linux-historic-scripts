"""Shared version table and helpers for untar-2.6.py / make-diffs-2.6.py / import-2.6.py.

No shell reference exists for this branch either. Like 2.5, it's a plain
tarball chain -- 2.6.0-test1 through test11, then 2.6.0 itself, then
2.6.1-2.6.11.12 -- no prepatches archived, no branching, always Linus
Torvalds. 2.6.0-test1 forked from 2.5.75 (confirmed directly by its own
ChangeLog: "Summary of changes from v2.5.75 to v2.6.0-test1"), so
unpack/linux-2.5.75 must already exist (run untar-2.5.py first).

linux-2.6.0.tar.gz was missing from the original binaries collection
(kernel.org mirrors don't keep every historic release forever) and was
freshly downloaded for this port; its own file mtime lands on 2003-12-17,
matching the real public release date exactly.

Stops at 2.6.11.12, NOT 2.6.12 or later: the official upstream git tree
begins at Linux 2.6.12-rc2, so anything from there on is already covered
by real git history and doesn't need reconstructing. No 2.6.12-rc1 tarball
is archived here to build a closer stopping point against, so 2.6.11.12
is the last version this branch covers.

Real per-release changelogs exist as ChangeLog-2.6.N files under
binaries/2.6/ (not the usual changelogs/ dir), same as 2.5 -- used
directly as commit messages.

Dates recovered via tarball-internal-mtime digging; all land in the
expected Jul 2003 - Jun 2005 range.
"""

import dataclasses
from pathlib import Path

from linux_hist_common import LINUS, ROOT  # noqa: F401 (re-exported for import-2.6.py)

BINARIES = ROOT / "binaries" / "2.6"


@dataclasses.dataclass
class Version:
    name: str
    base: str
    date: str


# fmt: off
VERSIONS: list[Version] = [
    Version("2.6.0-test1", "2.5.75", "Mon Jul 14 03:39:47 2003 +0000"),
    Version("2.6.0-test2", "2.6.0-test1", "Sun Jul 27 17:12:53 2003 +0000"),
    Version("2.6.0-test3", "2.6.0-test2", "Sat Aug  9 04:42:58 2003 +0000"),
    Version("2.6.0-test4", "2.6.0-test3", "Sat Aug 23 00:03:28 2003 +0000"),
    Version("2.6.0-test5", "2.6.0-test4", "Mon Sep  8 19:51:01 2003 +0000"),
    Version("2.6.0-test6", "2.6.0-test5", "Sun Sep 28 00:51:29 2003 +0000"),
    Version("2.6.0-test7", "2.6.0-test6", "Wed Oct  8 19:24:53 2003 +0000"),
    Version("2.6.0-test8", "2.6.0-test7", "Fri Oct 17 21:43:48 2003 +0000"),
    Version("2.6.0-test9", "2.6.0-test8", "Sat Oct 25 18:45:07 2003 +0000"),
    Version("2.6.0-test10", "2.6.0-test9", "Mon Nov 24 01:33:32 2003 +0000"),
    Version("2.6.0-test11", "2.6.0-test10", "Wed Nov 26 20:46:13 2003 +0000"),
    Version("2.6.0", "2.6.0-test11", "Thu Dec 18 03:00:03 2003 +0000"),
    Version("2.6.1", "2.6.0", "Fri Jan  9 07:00:14 2004 +0000"),
    Version("2.6.2", "2.6.1", "Wed Feb  4 03:45:13 2004 +0000"),
    Version("2.6.3", "2.6.2", "Wed Feb 18 04:00:01 2004 +0000"),
    Version("2.6.4", "2.6.3", "Thu Mar 11 02:56:03 2004 +0000"),
    Version("2.6.5", "2.6.4", "Sun Apr  4 03:38:28 2004 +0000"),
    Version("2.6.6", "2.6.5", "Mon May 10 02:33:22 2004 +0000"),
    Version("2.6.7", "2.6.6", "Wed Jun 16 05:20:27 2004 +0000"),
    Version("2.6.8", "2.6.7", "Sat Aug 14 05:38:11 2004 +0000"),
    Version("2.6.8.1", "2.6.8", "Sat Aug 14 10:56:26 2004 +0000"),
    Version("2.6.9", "2.6.8.1", "Mon Oct 18 21:55:43 2004 +0000"),
    Version("2.6.10", "2.6.9", "Fri Dec 24 21:36:05 2004 +0000"),
    Version("2.6.11", "2.6.10", "Wed Mar  2 07:38:38 2005 +0000"),
    Version("2.6.11.1", "2.6.11", "Fri Mar  4 17:27:12 2005 +0000"),
    Version("2.6.11.2", "2.6.11.1", "Wed Mar  9 08:13:23 2005 +0000"),
    Version("2.6.11.3", "2.6.11.2", "Sun Mar 13 06:44:55 2005 +0000"),
    Version("2.6.11.4", "2.6.11.3", "Wed Mar 16 00:09:53 2005 +0000"),
    Version("2.6.11.5", "2.6.11.4", "Sat Mar 19 06:35:07 2005 +0000"),
    Version("2.6.11.6", "2.6.11.5", "Sat Mar 26 03:28:51 2005 +0000"),
    Version("2.6.11.7", "2.6.11.6", "Thu Apr  7 18:58:54 2005 +0000"),
    Version("2.6.11.8", "2.6.11.7", "Sat Apr 30 01:34:09 2005 +0000"),
    Version("2.6.11.9", "2.6.11.8", "Wed May 11 22:43:48 2005 +0000"),
    Version("2.6.11.10", "2.6.11.9", "Mon May 16 17:52:18 2005 +0000"),
    Version("2.6.11.11", "2.6.11.10", "Fri May 27 05:06:46 2005 +0000"),
    Version("2.6.11.12", "2.6.11.11", "Sun Jun 12 02:45:37 2005 +0000"),
]
# fmt: on


def changelog_path(v: Version) -> Path:
    return BINARIES / f"ChangeLog-{v.name}"
