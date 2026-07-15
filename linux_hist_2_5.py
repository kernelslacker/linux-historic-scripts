"""Shared version table and helpers for untar-2.5.py / make-diffs-2.5.py / import-2.5.py.

No shell reference exists for this branch at all. It's the simplest one in
the whole project: 75 plain tarball releases (2.5.1-2.5.75), no prepatches
archived, no branching, always Linus Torvalds. 2.5.1 forked from 2.4.15 in
real history (confirmed: Linus' own tree moved on there while 2.4.x stable
maintenance continued on its own branch -- see linux_hist_2_4.py), so
unpack/linux-2.4.15 must already exist (run untar-2.4.py first).

Real per-release changelogs exist as ChangeLog-2.5.N files under
binaries/2.5/ (not the usual changelogs/ dir) -- these are cumulative
summaries covering everything since the previous release, including
prepatches that were never separately archived as tarballs. Used directly
as commit messages.

Dates recovered via tarball-internal-mtime digging (same technique as
0.10/2.0/2.2/2.3/2.4); all land in the expected Dec 2001 - Jul 2003 range.
"""

import dataclasses

from linux_hist_common import LINUS, ROOT  # noqa: F401 (re-exported for import-2.5.py)

BINARIES = ROOT / "binaries" / "2.5"


@dataclasses.dataclass
class Version:
    name: str
    base: str
    date: str


# fmt: off
VERSIONS: list[Version] = [
    Version("2.5.1", "2.4.15", "Sun Dec 16 23:53:11 2001 +0000"),
    Version("2.5.2", "2.5.1", "Tue Jan 15 02:12:55 2002 +0000"),
    Version("2.5.3", "2.5.2", "Wed Jan 30 06:34:46 2002 +0000"),
    Version("2.5.4", "2.5.3", "Mon Feb 11 01:50:18 2002 +0000"),
    Version("2.5.5", "2.5.4", "Wed Feb 20 02:11:50 2002 +0000"),
    Version("2.5.6", "2.5.5", "Fri Mar  8 02:18:59 2002 +0000"),
    Version("2.5.7", "2.5.6", "Mon Mar 18 20:37:19 2002 +0000"),
    Version("2.5.8", "2.5.7", "Sun Apr 14 19:18:56 2002 +0000"),
    Version("2.5.9", "2.5.8", "Mon Apr 22 22:29:55 2002 +0000"),
    Version("2.5.10", "2.5.9", "Wed Apr 24 07:15:23 2002 +0000"),
    Version("2.5.11", "2.5.10", "Mon Apr 29 03:13:30 2002 +0000"),
    Version("2.5.12", "2.5.11", "Wed May  1 00:09:02 2002 +0000"),
    Version("2.5.13", "2.5.12", "Fri May  3 00:22:58 2002 +0000"),
    Version("2.5.14", "2.5.13", "Mon May  6 03:38:06 2002 +0000"),
    Version("2.5.15", "2.5.14", "Thu May  9 22:25:56 2002 +0000"),
    Version("2.5.16", "2.5.15", "Sat May 18 07:46:16 2002 +0000"),
    Version("2.5.17", "2.5.16", "Tue May 21 05:07:43 2002 +0000"),
    Version("2.5.18", "2.5.17", "Sat May 25 01:55:31 2002 +0000"),
    Version("2.5.19", "2.5.18", "Wed May 29 18:42:59 2002 +0000"),
    Version("2.5.20", "2.5.19", "Mon Jun  3 01:44:54 2002 +0000"),
    Version("2.5.21", "2.5.20", "Sun Jun  9 05:31:33 2002 +0000"),
    Version("2.5.22", "2.5.21", "Mon Jun 17 02:31:37 2002 +0000"),
    Version("2.5.23", "2.5.22", "Wed Jun 19 02:11:59 2002 +0000"),
    Version("2.5.24", "2.5.23", "Thu Jun 20 22:53:57 2002 +0000"),
    Version("2.5.25", "2.5.24", "Fri Jul  5 23:42:38 2002 +0000"),
    Version("2.5.26", "2.5.25", "Tue Jul 16 23:49:39 2002 +0000"),
    Version("2.5.27", "2.5.26", "Sat Jul 20 19:12:32 2002 +0000"),
    Version("2.5.28", "2.5.27", "Wed Jul 24 21:03:32 2002 +0000"),
    Version("2.5.29", "2.5.28", "Sat Jul 27 02:58:46 2002 +0000"),
    Version("2.5.30", "2.5.29", "Thu Aug  1 21:17:32 2002 +0000"),
    Version("2.5.31", "2.5.30", "Sun Aug 11 01:42:11 2002 +0000"),
    Version("2.5.32", "2.5.31", "Tue Aug 27 19:27:34 2002 +0000"),
    Version("2.5.33", "2.5.32", "Sat Aug 31 22:05:45 2002 +0000"),
    Version("2.5.34", "2.5.33", "Mon Sep  9 17:35:38 2002 +0000"),
    Version("2.5.35", "2.5.34", "Mon Sep 16 02:19:10 2002 +0000"),
    Version("2.5.36", "2.5.35", "Wed Sep 18 00:59:23 2002 +0000"),
    Version("2.5.37", "2.5.36", "Fri Sep 20 15:20:37 2002 +0000"),
    Version("2.5.38", "2.5.37", "Sun Sep 22 04:25:36 2002 +0000"),
    Version("2.5.39", "2.5.38", "Fri Sep 27 21:51:00 2002 +0000"),
    Version("2.5.40", "2.5.39", "Tue Oct  1 07:07:59 2002 +0000"),
    Version("2.5.41", "2.5.40", "Mon Oct  7 18:25:22 2002 +0000"),
    Version("2.5.42", "2.5.41", "Sat Oct 12 04:22:47 2002 +0000"),
    Version("2.5.43", "2.5.42", "Wed Oct 16 03:29:07 2002 +0000"),
    Version("2.5.44", "2.5.43", "Sat Oct 19 04:03:00 2002 +0000"),
    Version("2.5.45", "2.5.44", "Thu Oct 31 00:44:13 2002 +0000"),
    Version("2.5.46", "2.5.45", "Mon Nov  4 22:30:57 2002 +0000"),
    Version("2.5.47", "2.5.46", "Mon Nov 11 03:28:33 2002 +0000"),
    Version("2.5.48", "2.5.47", "Mon Nov 18 04:29:59 2002 +0000"),
    Version("2.5.49", "2.5.48", "Fri Nov 22 21:41:14 2002 +0000"),
    Version("2.5.50", "2.5.49", "Wed Nov 27 22:36:24 2002 +0000"),
    Version("2.5.51", "2.5.50", "Tue Dec 10 02:46:29 2002 +0000"),
    Version("2.5.52", "2.5.51", "Mon Dec 16 02:08:24 2002 +0000"),
    Version("2.5.53", "2.5.52", "Tue Dec 24 05:21:38 2002 +0000"),
    Version("2.5.54", "2.5.53", "Thu Jan  2 03:23:32 2003 +0000"),
    Version("2.5.55", "2.5.54", "Thu Jan  9 04:04:28 2003 +0000"),
    Version("2.5.56", "2.5.55", "Fri Jan 10 20:12:27 2003 +0000"),
    Version("2.5.57", "2.5.56", "Mon Jan 13 18:18:01 2003 +0000"),
    Version("2.5.58", "2.5.57", "Tue Jan 14 05:59:36 2003 +0000"),
    Version("2.5.59", "2.5.58", "Fri Jan 17 02:23:01 2003 +0000"),
    Version("2.5.60", "2.5.59", "Mon Feb 10 18:39:18 2003 +0000"),
    Version("2.5.61", "2.5.60", "Fri Feb 14 23:53:03 2003 +0000"),
    Version("2.5.62", "2.5.61", "Mon Feb 17 22:57:22 2003 +0000"),
    Version("2.5.63", "2.5.62", "Mon Feb 24 19:06:03 2003 +0000"),
    Version("2.5.64", "2.5.63", "Wed Mar  5 03:29:58 2003 +0000"),
    Version("2.5.65", "2.5.64", "Mon Mar 17 21:44:52 2003 +0000"),
    Version("2.5.66", "2.5.65", "Mon Mar 24 22:01:53 2003 +0000"),
    Version("2.5.67", "2.5.66", "Mon Apr  7 17:33:04 2003 +0000"),
    Version("2.5.68", "2.5.67", "Sun Apr 20 02:51:23 2003 +0000"),
    Version("2.5.69", "2.5.68", "Sun May  4 23:53:57 2003 +0000"),
    Version("2.5.70", "2.5.69", "Tue May 27 01:01:04 2003 +0000"),
    Version("2.5.71", "2.5.70", "Sat Jun 14 19:18:52 2003 +0000"),
    Version("2.5.72", "2.5.71", "Tue Jun 17 04:20:30 2003 +0000"),
    Version("2.5.73", "2.5.72", "Sun Jun 22 18:33:37 2003 +0000"),
    Version("2.5.74", "2.5.73", "Wed Jul  2 20:58:30 2003 +0000"),
    Version("2.5.75", "2.5.74", "Thu Jul 10 20:15:51 2003 +0000"),
]
# fmt: on
