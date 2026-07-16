"""Shared version table and helpers for untar-2.2.py / make-diffs-2.2.py / import-2.2.py.

Continues from 2.1's "2.2.0pre9" (all on master, still Linus). At 2.2.8,
branches off onto "2.2" (mirroring the 2.0/2.1 and 1.0/1.1 splits: master
moves on to 2.3, the "2.2" branch continues stable maintenance). Alan Cox
takes over authorship on that branch at 2.2.11pre1.

Like 2.0/2.1, prepatches are generally cut against the last stable release
(`base` vs `patch_base` diverge), except 2.2.11pre3-7 and 2.2.15pre20 which
are genuine interdiffs (chained, patch_base==base, so just omitted).
2.2.18pre1-3 are cut against "2.2.17pre20" specifically ("Alan horked the
beginning of this patchset" per the original script's comment) while
pre4-27 are cut against the final "2.2.17".

2.2.18pre27 and 2.2.18 are both tag-only aliases of 2.2.18pre26 (the
original script's comment: "pre27 was pre26 with some binary files
removed... pre27 == final") -- unlike 0.2's aliases, these DO get real
trees/diffs built (matching the original untar/make-diffs scripts exactly);
only the import step treats them as a no-op tag rather than a new commit.

No date in import-2.2.sh is real -- literally every `import` call in the
original is missing its date argument, so the whole branch relied on
nondeterministic wall-clock time. All 233 dates here were recovered from
tarball mtimes / embedded diff-header timestamps (same technique as the
0.10 and 2.0 digs). Only one entry (2.2.18pre1) comes out earlier than its
predecessor, and that's explained by the same "based on 2.2.17pre20" note
above -- it was genuinely cut before 2.2.17's final release.
"""

import dataclasses
from pathlib import Path

from linux_hist_common import (  # noqa: F401 (re-exported)
    CHANGELOGS,
    LINUS,
    ROOT,
    Author,
    version_subdir,
)

BINARIES = ROOT / "binaries" / "2.2"


@dataclasses.dataclass
class Version:
    # fmt: off
    name: str
    base: str
    date: str
    patch: str | None = None        # filename under BINARIES; None means "extract the tarball"
    patch_base: str | None = None   # cp -rl source during untar, if different from `base`
    branch_create: str | None = None
    branch_checkout: str | None = None
    author: Author | None = None    # (name, email); sticky until changed again
    alias_of: str | None = None     # if set: import step tags this name onto alias_of's commit instead of committing
    # fmt: on


# fmt: off
VERSIONS: list[Version] = [
    Version("2.2.0", "2.2.0pre9", "Tue Jan 26 01:21:20 1999 +0000"),
    Version("2.2.1", "2.2.0", "Thu Jan 28 20:50:30 1999 +0000"),
    Version("2.2.2pre1", "2.2.1", "Mon Feb  1 17:25:53 1999 +0000", "patch-2.2.2-pre1.gz"),
    Version("2.2.2pre2", "2.2.2pre1", "Fri Feb  5 10:00:04 1999 +0000", "patch-2.2.2-pre2.gz", patch_base="2.2.1"),
    Version("2.2.2pre4", "2.2.2pre2", "Mon Feb 15 10:48:10 1999 +0000", "patch-2.2.2-pre4.gz", patch_base="2.2.1"),
    Version("2.2.2pre5", "2.2.2pre4", "Thu Feb 18 11:59:28 1999 +0000", "patch-2.2.2-pre5.gz", patch_base="2.2.1"),
    Version("2.2.2", "2.2.2pre5", "Tue Feb 23 00:24:07 1999 +0000"),
    Version("2.2.3pre1", "2.2.2", "Thu Mar  4 18:27:27 1999 +0000", "patch-2.2.3-pre1.gz"),
    Version("2.2.3pre2", "2.2.3pre1", "Sat Mar  6 14:44:56 1999 +0000", "patch-2.2.3-pre2.gz", patch_base="2.2.2"),
    Version("2.2.3pre3", "2.2.3pre2", "Sun Mar  7 20:38:44 1999 +0000", "patch-2.2.3-pre3.gz", patch_base="2.2.2"),
    Version("2.2.3", "2.2.3pre3", "Tue Mar  9 00:03:48 1999 +0000"),
    Version("2.2.4pre4", "2.2.3", "Sat Mar 20 12:42:40 1999 +0000", "patch-2.2.4-pre4.gz"),
    Version("2.2.4pre6", "2.2.4pre4", "Sun Mar 21 18:37:56 1999 +0000", "patch-2.2.4-pre6.gz", patch_base="2.2.3"),
    Version("2.2.4", "2.2.4pre6", "Tue Mar 23 22:08:13 1999 +0000"),
    Version("2.2.5pre1", "2.2.4", "Wed Mar 24 16:07:59 1999 +0000", "patch-2.2.5-pre1.gz"),
    Version("2.2.5pre2", "2.2.5pre1", "Fri Mar 26 14:52:34 1999 +0000", "patch-2.2.5-pre2.gz", patch_base="2.2.4"),
    Version("2.2.5", "2.2.5pre2", "Mon Mar 29 06:36:32 1999 +0000"),
    Version("2.2.6pre1", "2.2.5", "Mon Apr 12 13:12:57 1999 +0000", "patch-2.2.6-pre1.gz"),
    Version("2.2.6pre2", "2.2.6pre1", "Mon Apr 12 21:46:19 1999 +0000", "patch-2.2.6-pre2.gz", patch_base="2.2.5"),
    Version("2.2.6pre3", "2.2.6pre2", "Thu Apr 15 16:30:17 1999 +0000", "patch-2.2.6-pre3.gz", patch_base="2.2.5"),
    Version("2.2.6", "2.2.6pre3", "Fri Apr 16 21:39:36 1999 +0000"),
    Version("2.2.7pre1", "2.2.6", "Wed Apr 21 13:06:18 1999 +0000", "patch-2.2.7-pre1.gz"),
    Version("2.2.7pre2", "2.2.7pre1", "Fri Apr 23 08:42:03 1999 +0000", "patch-2.2.7-pre2.gz", patch_base="2.2.6"),
    Version("2.2.7pre3", "2.2.7pre2", "Fri Apr 23 18:39:47 1999 +0000", "patch-2.2.7-pre3.gz", patch_base="2.2.6"),
    Version("2.2.7pre4", "2.2.7pre3", "Mon Apr 26 15:05:57 1999 +0000", "patch-2.2.7-pre4.gz", patch_base="2.2.6"),
    Version("2.2.7", "2.2.7pre4", "Wed Apr 28 18:14:03 1999 +0000"),
    Version("2.2.8pre1", "2.2.7", "Thu May  6 15:13:05 1999 +0000", "patch-2.2.8-pre1.gz"),
    Version("2.2.8pre2", "2.2.8pre1", "Thu May  6 16:22:42 1999 +0000", "patch-2.2.8-pre2.gz", patch_base="2.2.7"),
    Version("2.2.8pre3", "2.2.8pre2", "Thu May  6 16:48:51 1999 +0000", "patch-2.2.8-pre3.gz", patch_base="2.2.7"),
    Version("2.2.8pre4", "2.2.8pre3", "Fri May  7 15:17:59 1999 +0000", "patch-2.2.8-pre4.gz", patch_base="2.2.7"),
    Version("2.2.8pre5", "2.2.8pre4", "Sat May  8 20:52:26 1999 +0000", "patch-2.2.8-pre5.gz", patch_base="2.2.7"),
    Version("2.2.8pre6", "2.2.8pre5", "Mon May 10 11:16:51 1999 +0000", "patch-2.2.8-pre6.gz", patch_base="2.2.7"),
    Version("2.2.8pre7", "2.2.8pre6", "Mon May 10 13:01:21 1999 +0000", "patch-2.2.8-pre7.gz", patch_base="2.2.7"),
    Version("2.2.8", "2.2.8pre7", "Tue May 11 19:45:54 1999 +0000"),
    Version("2.2.9", "2.2.8", "Thu May 13 23:41:00 1999 +0000", branch_create="2.2", branch_checkout="2.2"),
    Version("2.2.10pre1", "2.2.9", "Fri May 28 18:10:19 1999 +0000", "patch-2.2.10-pre1.gz"),
    Version("2.2.10pre2", "2.2.10pre1", "Tue Jun  1 16:44:20 1999 +0000", "patch-2.2.10-pre2.gz", patch_base="2.2.9"),
    Version("2.2.10pre3", "2.2.10pre2", "Mon Jun  7 11:06:06 1999 +0000", "patch-2.2.10-pre3.gz", patch_base="2.2.9"),
    Version("2.2.10pre4", "2.2.10pre3", "Sat Jun 12 11:52:52 1999 +0000", "patch-2.2.10-pre4.gz", patch_base="2.2.9"),
    Version("2.2.10pre5", "2.2.10pre4", "Sun Jun 13 10:50:04 1999 +0000", "patch-2.2.10-pre5.gz", patch_base="2.2.9"),
    Version("2.2.10", "2.2.10pre5", "Mon Jun 14 02:54:15 1999 +0000"),
    Version("2.2.11pre1", "2.2.10", "Mon Jun 28 08:11:58 1999 +0000", "patch-2.2.11-pre1.gz", author=("Alan Cox", "alan@lxorguk.ukuu.org.uk")),
    Version("2.2.11pre2", "2.2.11pre1", "Tue Jul 20 02:02:45 1999 +0000", "patch-2.2.11-pre2.gz", patch_base="2.2.10"),
    Version("2.2.11pre3", "2.2.11pre2", "Fri Jul 30 20:19:06 1999 +0000", "patch-2.2.11pre2-pre3.gz"),
    Version("2.2.11pre4", "2.2.11pre3", "Sat Jul 31 16:47:42 1999 +0000", "patch-2.2.11pre3-pre4.gz"),
    Version("2.2.11pre5", "2.2.11pre4", "Fri Aug  6 20:44:14 1999 +0000", "patch-2.2.11pre4-pre5.gz"),
    Version("2.2.11pre6", "2.2.11pre5", "Sun Aug  8 02:01:01 1999 +0000", "patch-2.2.11pre5-pre6.gz"),
    Version("2.2.11pre7", "2.2.11pre6", "Mon Aug  9 00:48:23 1999 +0000", "patch-2.2.11pre6-pre7.gz"),
    Version("2.2.11", "2.2.11pre7", "Mon Aug  9 19:13:09 1999 +0000"),
    Version("2.2.12pre1", "2.2.11", "Fri Aug 13 00:51:38 1999 +0000", "patch-2.2.12-pre1.gz"),
    Version("2.2.12pre3", "2.2.12pre1", "Fri Aug 13 14:18:15 1999 +0000", "patch-2.2.12-pre3.gz", patch_base="2.2.11"),
    Version("2.2.12pre4", "2.2.12pre3", "Sat Aug 14 01:33:39 1999 +0000", "patch-2.2.12-pre4.gz", patch_base="2.2.11"),
    Version("2.2.12pre5", "2.2.12pre4", "Sun Aug 15 22:47:30 1999 +0000", "patch-2.2.12-pre5.gz", patch_base="2.2.11"),
    Version("2.2.12pre6", "2.2.12pre5", "Mon Aug 16 19:31:05 1999 +0000", "patch-2.2.12-pre6.gz", patch_base="2.2.11"),
    Version("2.2.12pre7", "2.2.12pre6", "Mon Aug 16 22:40:02 1999 +0000", "patch-2.2.12-pre7.gz", patch_base="2.2.11"),
    Version("2.2.12pre8", "2.2.12pre7", "Tue Aug 17 15:20:49 1999 +0000", "patch-2.2.12-pre8.gz", patch_base="2.2.11"),
    Version("2.2.12", "2.2.12pre8", "Thu Aug 26 00:30:00 1999 +0000"),
    Version("2.2.13pre1", "2.2.12", "Sun Aug 29 01:56:50 1999 +0000", "patch-2.2.13-pre1.gz"),
    Version("2.2.13pre2", "2.2.13pre1", "Tue Aug 31 18:35:37 1999 +0000", "patch-2.2.13-pre2.gz", patch_base="2.2.12"),
    Version("2.2.13pre3", "2.2.13pre2", "Wed Sep  1 17:36:08 1999 +0000", "patch-2.2.13-pre3.gz", patch_base="2.2.12"),
    Version("2.2.13pre4", "2.2.13pre3", "Fri Sep  3 15:22:38 1999 +0000", "patch-2.2.13-pre4.gz", patch_base="2.2.12"),
    Version("2.2.13pre5", "2.2.13pre4", "Thu Sep  9 14:55:46 1999 +0000", "patch-2.2.13-pre5.gz", patch_base="2.2.12"),
    Version("2.2.13pre6", "2.2.13pre5", "Fri Sep 10 16:55:35 1999 +0000", "patch-2.2.13-pre6.gz", patch_base="2.2.12"),
    Version("2.2.13pre7", "2.2.13pre6", "Sun Sep 12 23:37:25 1999 +0000", "patch-2.2.13-pre7.gz", patch_base="2.2.12"),
    Version("2.2.13pre8", "2.2.13pre7", "Tue Sep 14 21:22:24 1999 +0000", "patch-2.2.13-pre8.gz", patch_base="2.2.12"),
    Version("2.2.13pre9", "2.2.13pre8", "Fri Sep 17 00:11:20 1999 +0000", "patch-2.2.13-pre9.gz", patch_base="2.2.12"),
    Version("2.2.13pre10", "2.2.13pre9", "Sat Sep 18 22:27:17 1999 +0000", "patch-2.2.13-pre10.gz", patch_base="2.2.12"),
    Version("2.2.13pre11", "2.2.13pre10", "Tue Sep 21 23:28:15 1999 +0000", "patch-2.2.13-pre11.gz", patch_base="2.2.12"),
    Version("2.2.13pre12", "2.2.13pre11", "Thu Sep 23 13:21:21 1999 +0000", "patch-2.2.13-pre12.gz", patch_base="2.2.12"),
    Version("2.2.13pre13", "2.2.13pre12", "Mon Sep 27 00:16:35 1999 +0000", "patch-2.2.13-pre13.gz", patch_base="2.2.12"),
    Version("2.2.13pre14", "2.2.13pre13", "Mon Sep 27 15:55:26 1999 +0000", "patch-2.2.13-pre14.gz", patch_base="2.2.12"),
    Version("2.2.13pre15", "2.2.13pre14", "Mon Oct  4 22:51:11 1999 +0000", "patch-2.2.13-pre15.gz", patch_base="2.2.12"),
    Version("2.2.13pre16", "2.2.13pre15", "Mon Oct 11 13:12:34 1999 +0000", "patch-2.2.13-pre16.gz", patch_base="2.2.12"),
    Version("2.2.13pre17", "2.2.13pre16", "Tue Oct 12 19:15:53 1999 +0000", "patch-2.2.13-pre17.gz", patch_base="2.2.12"),
    Version("2.2.13pre18", "2.2.13pre17", "Sun Oct 17 22:36:37 1999 +0000", "patch-2.2.13-pre18.gz", patch_base="2.2.12"),
    Version("2.2.13", "2.2.13pre18", "Wed Oct 20 00:21:25 1999 +0000"),
    Version("2.2.14pre1", "2.2.13", "Fri Oct 22 23:39:41 1999 +0000", "pre-patch-2.2.14-1.gz"),
    Version("2.2.14pre2", "2.2.14pre1", "Wed Oct 27 20:23:29 1999 +0000", "pre-patch-2.2.14-2.gz", patch_base="2.2.13"),
    Version("2.2.14pre3", "2.2.14pre2", "Sat Oct 30 00:39:41 1999 +0000", "pre-patch-2.2.14-3.gz", patch_base="2.2.13"),
    Version("2.2.14pre4", "2.2.14pre3", "Thu Nov  4 23:55:15 1999 +0000", "pre-patch-2.2.14-4.gz", patch_base="2.2.13"),
    Version("2.2.14pre5", "2.2.14pre4", "Sat Nov 13 18:15:22 1999 +0000", "pre-patch-2.2.14-5.gz", patch_base="2.2.13"),
    Version("2.2.14pre6", "2.2.14pre5", "Tue Nov 16 17:28:20 1999 +0000", "pre-patch-2.2.14-6.gz", patch_base="2.2.13"),
    Version("2.2.14pre7", "2.2.14pre6", "Thu Nov 18 20:39:49 1999 +0000", "pre-patch-2.2.14-7.gz", patch_base="2.2.13"),
    Version("2.2.14pre8", "2.2.14pre7", "Mon Nov 22 22:45:49 1999 +0000", "pre-patch-2.2.14-8.gz", patch_base="2.2.13"),
    Version("2.2.14pre9", "2.2.14pre8", "Thu Nov 25 17:49:03 1999 +0000", "pre-patch-2.2.14-9.gz", patch_base="2.2.13"),
    Version("2.2.14pre10", "2.2.14pre9", "Thu Dec  2 15:41:17 1999 +0000", "pre-patch-2.2.14-10.gz", patch_base="2.2.13"),
    Version("2.2.14pre11", "2.2.14pre10", "Sat Dec  4 00:56:28 1999 +0000", "pre-patch-2.2.14-11.gz", patch_base="2.2.13"),
    Version("2.2.14pre12", "2.2.14pre11", "Tue Dec  7 17:41:54 1999 +0000", "pre-patch-2.2.14-12.gz", patch_base="2.2.13"),
    Version("2.2.14pre13", "2.2.14pre12", "Mon Dec 13 21:51:21 1999 +0000", "pre-patch-2.2.14-13.gz", patch_base="2.2.13"),
    Version("2.2.14pre14", "2.2.14pre13", "Wed Dec 15 23:34:37 1999 +0000", "pre-patch-2.2.14-14.gz", patch_base="2.2.13"),
    Version("2.2.14pre15", "2.2.14pre14", "Sat Dec 18 01:27:10 1999 +0000", "pre-patch-2.2.14-15.gz", patch_base="2.2.13"),
    Version("2.2.14pre16", "2.2.14pre15", "Tue Dec 21 01:28:10 1999 +0000", "pre-patch-2.2.14-16.gz", patch_base="2.2.13"),
    Version("2.2.14pre17", "2.2.14pre16", "Tue Dec 28 19:40:51 1999 +0000", "pre-patch-2.2.14-17.gz", patch_base="2.2.13"),
    Version("2.2.14pre18", "2.2.14pre17", "Sat Jan  1 20:22:08 2000 +0000", "pre-patch-2.2.14-18.gz", patch_base="2.2.13"),
    Version("2.2.14", "2.2.14pre18", "Tue Jan  4 18:13:31 2000 +0000"),
    Version("2.2.15pre1", "2.2.14", "Wed Jan 12 18:01:03 2000 +0000", "pre-patch-2.2.15-1.gz"),
    Version("2.2.15pre2", "2.2.15pre1", "Fri Jan 14 16:03:42 2000 +0000", "pre-patch-2.2.15-2.gz", patch_base="2.2.14"),
    Version("2.2.15pre3", "2.2.15pre2", "Tue Jan 18 01:47:46 2000 +0000", "pre-patch-2.2.15-3.gz", patch_base="2.2.14"),
    Version("2.2.15pre4", "2.2.15pre3", "Sat Jan 22 02:24:12 2000 +0000", "pre-patch-2.2.15-4.gz", patch_base="2.2.14"),
    Version("2.2.15pre5", "2.2.15pre4", "Thu Jan 27 15:59:02 2000 +0000", "pre-patch-2.2.15-5.gz", patch_base="2.2.14"),
    Version("2.2.15pre6", "2.2.15pre5", "Mon Feb  7 15:13:46 2000 +0000", "pre-patch-2.2.15-6.gz", patch_base="2.2.14"),
    Version("2.2.15pre7", "2.2.15pre6", "Wed Feb  9 21:57:54 2000 +0000", "pre-patch-2.2.15-7.gz", patch_base="2.2.14"),
    Version("2.2.15pre8", "2.2.15pre7", "Thu Feb 17 14:27:20 2000 +0000", "pre-patch-2.2.15-8.gz", patch_base="2.2.14"),
    Version("2.2.15pre9", "2.2.15pre8", "Thu Feb 17 23:04:25 2000 +0000", "pre-patch-2.2.15-9.gz", patch_base="2.2.14"),
    Version("2.2.15pre10", "2.2.15pre9", "Thu Feb 24 14:26:52 2000 +0000", "pre-patch-2.2.15-10.gz", patch_base="2.2.14"),
    Version("2.2.15pre11", "2.2.15pre10", "Mon Feb 28 23:10:46 2000 +0000", "pre-patch-2.2.15-11.gz", patch_base="2.2.14"),
    Version("2.2.15pre12", "2.2.15pre11", "Wed Mar  1 17:31:16 2000 +0000", "pre-patch-2.2.15-12.gz", patch_base="2.2.14"),
    Version("2.2.15pre13", "2.2.15pre12", "Sat Mar  4 00:55:26 2000 +0000", "pre-patch-2.2.15-13.gz", patch_base="2.2.14"),
    Version("2.2.15pre14", "2.2.15pre13", "Thu Mar  9 23:48:11 2000 +0000", "pre-patch-2.2.15-14.gz", patch_base="2.2.14"),
    Version("2.2.15pre15", "2.2.15pre14", "Fri Mar 17 16:15:25 2000 +0000", "pre-patch-2.2.15-15.gz", patch_base="2.2.14"),
    Version("2.2.15pre16", "2.2.15pre15", "Wed Mar 29 00:41:56 2000 +0000", "pre-patch-2.2.15-16.gz", patch_base="2.2.14"),
    Version("2.2.15pre17", "2.2.15pre16", "Sun Apr  2 00:33:36 2000 +0000", "pre-patch-2.2.15-17.gz", patch_base="2.2.14"),
    Version("2.2.15pre18", "2.2.15pre17", "Sat Apr  8 21:03:21 2000 +0000", "pre-patch-2.2.15-18.gz", patch_base="2.2.14"),
    Version("2.2.15pre19", "2.2.15pre18", "Sun Apr 16 19:06:01 2000 +0000", "pre-patch-2.2.15-19.gz", patch_base="2.2.14"),
    Version("2.2.15pre20", "2.2.15pre19", "Fri Apr 21 23:00:39 2000 +0000", "pre-patch-2.2.15-19to20.gz"),
    Version("2.2.15", "2.2.15pre20", "Thu May  4 00:17:10 2000 +0000"),
    Version("2.2.16pre2", "2.2.15", "Thu May  4 01:21:03 2000 +0000", "pre-patch-2.2.16-2.gz"),
    Version("2.2.16pre3", "2.2.16pre2", "Tue May 16 12:54:16 2000 +0000", "pre-patch-2.2.16-3.gz", patch_base="2.2.15"),
    Version("2.2.16pre4", "2.2.16pre3", "Sun May 21 17:54:50 2000 +0000", "pre-patch-2.2.16-4.gz", patch_base="2.2.15"),
    Version("2.2.16pre5", "2.2.16pre4", "Sat May 27 01:30:02 2000 +0000", "pre-patch-2.2.16-5.gz", patch_base="2.2.15"),
    Version("2.2.16pre6", "2.2.16pre5", "Tue May 30 22:18:15 2000 +0000", "pre-patch-2.2.16-6.gz", patch_base="2.2.15"),
    Version("2.2.16pre7", "2.2.16pre6", "Wed May 31 12:31:09 2000 +0000", "pre-patch-2.2.16-7.gz", patch_base="2.2.15"),
    Version("2.2.16pre8", "2.2.16pre7", "Mon Jun  5 16:26:44 2000 +0000", "pre-patch-2.2.16-8.gz", patch_base="2.2.15"),
    Version("2.2.16", "2.2.16pre8", "Wed Jun  7 21:26:53 2000 +0000"),
    Version("2.2.17pre1", "2.2.16", "Sun Jun 11 22:38:04 2000 +0000", "pre-patch-2.2.17-1.gz"),
    Version("2.2.17pre2", "2.2.17pre1", "Thu Jun 15 17:29:58 2000 +0000", "pre-patch-2.2.17-2.gz", patch_base="2.2.16"),
    Version("2.2.17pre3", "2.2.17pre2", "Fri Jun 16 17:03:07 2000 +0000", "pre-patch-2.2.17-3.gz", patch_base="2.2.16"),
    Version("2.2.17pre4", "2.2.17pre3", "Sat Jun 17 15:49:28 2000 +0000", "pre-patch-2.2.17-4.gz", patch_base="2.2.16"),
    Version("2.2.17pre5", "2.2.17pre4", "Tue Jun 20 23:54:54 2000 +0000", "pre-patch-2.2.17-5.gz", patch_base="2.2.16"),
    Version("2.2.17pre6", "2.2.17pre5", "Fri Jun 23 00:42:23 2000 +0000", "pre-patch-2.2.17-6.gz", patch_base="2.2.16"),
    Version("2.2.17pre7", "2.2.17pre6", "Sun Jun 25 18:18:54 2000 +0000", "pre-patch-2.2.17-7.gz", patch_base="2.2.16"),
    Version("2.2.17pre8", "2.2.17pre7", "Mon Jun 26 16:42:44 2000 +0000", "pre-patch-2.2.17-8.gz", patch_base="2.2.16"),
    Version("2.2.17pre9", "2.2.17pre8", "Tue Jun 27 13:13:44 2000 +0000", "pre-patch-2.2.17-9.gz", patch_base="2.2.16"),
    Version("2.2.17pre10", "2.2.17pre9", "Mon Jul  3 22:31:35 2000 +0000", "pre-patch-2.2.17-10.gz", patch_base="2.2.16"),
    Version("2.2.17pre11", "2.2.17pre10", "Mon Jul 10 16:01:40 2000 +0000", "pre-patch-2.2.17-11.gz", patch_base="2.2.16"),
    Version("2.2.17pre12", "2.2.17pre11", "Fri Jul 14 23:11:56 2000 +0000", "pre-patch-2.2.17-12.gz", patch_base="2.2.16"),
    Version("2.2.17pre13", "2.2.17pre12", "Sun Jul 16 13:37:18 2000 +0000", "pre-patch-2.2.17-13.gz", patch_base="2.2.16"),
    Version("2.2.17pre14", "2.2.17pre13", "Sun Jul 30 18:01:09 2000 +0000", "pre-patch-2.2.17-14.gz", patch_base="2.2.16"),
    Version("2.2.17pre15", "2.2.17pre14", "Tue Aug  1 18:35:55 2000 +0000", "pre-patch-2.2.17-15.gz", patch_base="2.2.16"),
    Version("2.2.17pre16", "2.2.17pre15", "Wed Aug  9 22:52:47 2000 +0000", "pre-patch-2.2.17-16.gz", patch_base="2.2.16"),
    Version("2.2.17pre17", "2.2.17pre16", "Tue Aug 15 12:48:29 2000 +0000", "pre-patch-2.2.17-17.gz", patch_base="2.2.16"),
    Version("2.2.17pre18", "2.2.17pre17", "Thu Aug 17 19:35:54 2000 +0000", "pre-patch-2.2.17-18.gz", patch_base="2.2.16"),
    Version("2.2.17pre19", "2.2.17pre18", "Fri Aug 18 21:38:56 2000 +0000", "pre-patch-2.2.17-19.gz", patch_base="2.2.16"),
    Version("2.2.17pre20", "2.2.17pre19", "Wed Aug 23 11:37:26 2000 +0000", "pre-patch-2.2.17-20.gz", patch_base="2.2.16"),
    Version("2.2.17", "2.2.17pre20", "Mon Sep  4 17:58:37 2000 +0000"),
    # 2.2.18pre1 predates 2.2.17's own tarball date -- it was cut against
    # 2.2.17pre20, not the final release (see module docstring).
    Version("2.2.18pre1", "2.2.17", "Thu Aug 31 22:18:27 2000 +0000", "pre-patch-2.2.18-1.gz", patch_base="2.2.17pre20"),
    Version("2.2.18pre2", "2.2.18pre1", "Fri Sep  1 14:43:02 2000 +0000", "pre-patch-2.2.18-2.gz", patch_base="2.2.17pre20"),
    Version("2.2.18pre3", "2.2.18pre2", "Mon Sep  4 17:21:55 2000 +0000", "pre-patch-2.2.18-3.gz", patch_base="2.2.17pre20"),
    Version("2.2.18pre4", "2.2.18pre3", "Sun Sep 10 15:42:48 2000 +0000", "pre-patch-2.2.18-4.gz", patch_base="2.2.17"),
    Version("2.2.18pre5", "2.2.18pre4", "Mon Sep 11 21:20:33 2000 +0000", "pre-patch-2.2.18-5.gz", patch_base="2.2.17"),
    Version("2.2.18pre6", "2.2.18pre5", "Tue Sep 12 13:55:10 2000 +0000", "pre-patch-2.2.18-6.gz", patch_base="2.2.17"),
    Version("2.2.18pre7", "2.2.18pre6", "Thu Sep 14 15:44:52 2000 +0000", "pre-patch-2.2.18-7.gz", patch_base="2.2.17"),
    Version("2.2.18pre8", "2.2.18pre7", "Fri Sep 15 15:13:39 2000 +0000", "pre-patch-2.2.18-8.gz", patch_base="2.2.17"),
    Version("2.2.18pre9", "2.2.18pre8", "Sat Sep 16 12:10:51 2000 +0000", "pre-patch-2.2.18-9.gz", patch_base="2.2.17"),
    Version("2.2.18pre10", "2.2.18pre9", "Sat Sep 23 14:13:02 2000 +0000", "pre-patch-2.2.18-10.gz", patch_base="2.2.17"),
    Version("2.2.18pre11", "2.2.18pre10", "Wed Sep 27 12:25:18 2000 +0000", "pre-patch-2.2.18-11.gz", patch_base="2.2.17"),
    Version("2.2.18pre12", "2.2.18pre11", "Fri Sep 29 22:46:28 2000 +0000", "pre-patch-2.2.18-12.gz", patch_base="2.2.17"),
    Version("2.2.18pre13", "2.2.18pre12", "Sat Sep 30 18:45:23 2000 +0000", "pre-patch-2.2.18-13.gz", patch_base="2.2.17"),
    Version("2.2.18pre14", "2.2.18pre13", "Sun Oct  1 11:58:48 2000 +0000", "pre-patch-2.2.18-14.gz", patch_base="2.2.17"),
    Version("2.2.18pre15", "2.2.18pre14", "Mon Oct  2 17:00:03 2000 +0000", "pre-patch-2.2.18-15.gz", patch_base="2.2.17"),
    Version("2.2.18pre16", "2.2.18pre15", "Sun Oct 15 23:56:33 2000 +0000", "pre-patch-2.2.18-16.gz", patch_base="2.2.17"),
    Version("2.2.18pre17", "2.2.18pre16", "Thu Oct 19 01:52:31 2000 +0000", "pre-patch-2.2.18-17.gz", patch_base="2.2.17"),
    Version("2.2.18pre18", "2.2.18pre17", "Sat Oct 28 20:13:14 2000 +0000", "pre-patch-2.2.18-18.gz", patch_base="2.2.17"),
    Version("2.2.18pre19", "2.2.18pre18", "Wed Nov  1 17:39:29 2000 +0000", "pre-patch-2.2.18-19.gz", patch_base="2.2.17"),
    Version("2.2.18pre20", "2.2.18pre19", "Tue Nov  7 17:32:05 2000 +0000", "pre-patch-2.2.18-20.gz", patch_base="2.2.17"),
    Version("2.2.18pre21", "2.2.18pre20", "Fri Nov 10 01:59:46 2000 +0000", "pre-patch-2.2.18-21.gz", patch_base="2.2.17"),
    Version("2.2.18pre22", "2.2.18pre21", "Sat Nov 18 20:16:39 2000 +0000", "pre-patch-2.2.18-22.gz", patch_base="2.2.17"),
    Version("2.2.18pre23", "2.2.18pre22", "Wed Nov 22 16:40:16 2000 +0000", "pre-patch-2.2.18-23.gz", patch_base="2.2.17"),
    Version("2.2.18pre24", "2.2.18pre23", "Tue Nov 28 22:29:35 2000 +0000", "pre-patch-2.2.18-24.gz", patch_base="2.2.17"),
    Version("2.2.18pre25", "2.2.18pre24", "Thu Dec  7 15:57:50 2000 +0000", "pre-patch-2.2.18-25.gz", patch_base="2.2.17"),
    Version("2.2.18pre26", "2.2.18pre25", "Sat Dec  9 21:53:12 2000 +0000", "pre-patch-2.2.18-26.gz", patch_base="2.2.17"),
    Version("2.2.18pre27", "2.2.18pre26", "Sat Dec  9 21:53:12 2000 +0000", "pre-patch-2.2.18-27.gz", patch_base="2.2.17", alias_of="2.2.18pre26"),
    Version("2.2.18", "2.2.18pre27", "Mon Dec 11 00:49:45 2000 +0000", alias_of="2.2.18pre26"),
    Version("2.2.19pre1", "2.2.18", "Thu Dec 14 16:55:18 2000 +0000", "pre-patch-2.2.19-1.gz"),
    Version("2.2.19pre2", "2.2.19pre1", "Sat Dec 16 17:45:22 2000 +0000", "pre-patch-2.2.19-2.gz", patch_base="2.2.18"),
    Version("2.2.19pre3", "2.2.19pre2", "Thu Dec 21 23:42:13 2000 +0000", "pre-patch-2.2.19-3.gz", patch_base="2.2.18"),
    Version("2.2.19pre4", "2.2.19pre3", "Sat Dec 30 20:05:19 2000 +0000", "pre-patch-2.2.19-4.gz", patch_base="2.2.18"),
    Version("2.2.19pre5", "2.2.19pre4", "Wed Jan  3 01:27:12 2001 +0000", "pre-patch-2.2.19-5.gz", patch_base="2.2.18"),
    Version("2.2.19pre6", "2.2.19pre5", "Wed Jan  3 14:15:16 2001 +0000", "pre-patch-2.2.19-6.gz", patch_base="2.2.18"),
    Version("2.2.19pre7", "2.2.19pre6", "Tue Jan  9 13:00:40 2001 +0000", "pre-patch-2.2.19-7.gz", patch_base="2.2.18"),
    Version("2.2.19pre8", "2.2.19pre7", "Thu Feb  1 16:02:11 2001 +0000", "pre-patch-2.2.19-8.gz", patch_base="2.2.18"),
    Version("2.2.19pre9", "2.2.19pre8", "Thu Feb  8 12:08:42 2001 +0000", "pre-patch-2.2.19-9.gz", patch_base="2.2.18"),
    Version("2.2.19pre10", "2.2.19pre9", "Mon Feb 12 15:41:06 2001 +0000", "pre-patch-2.2.19-10.gz", patch_base="2.2.18"),
    Version("2.2.19pre11", "2.2.19pre10", "Tue Feb 13 19:11:54 2001 +0000", "pre-patch-2.2.19-11.gz", patch_base="2.2.18"),
    Version("2.2.19pre12", "2.2.19pre11", "Wed Feb 14 14:50:09 2001 +0000", "pre-patch-2.2.19-12.gz", patch_base="2.2.18"),
    Version("2.2.19pre13", "2.2.19pre12", "Thu Feb 15 16:50:28 2001 +0000", "pre-patch-2.2.19-13.gz", patch_base="2.2.18"),
    Version("2.2.19pre14", "2.2.19pre13", "Tue Feb 20 13:45:37 2001 +0000", "pre-patch-2.2.19-14.gz", patch_base="2.2.18"),
    Version("2.2.19pre15", "2.2.19pre14", "Sun Feb 25 23:42:50 2001 +0000", "pre-patch-2.2.19-15.gz", patch_base="2.2.18"),
    Version("2.2.19pre16", "2.2.19pre15", "Tue Feb 27 22:33:38 2001 +0000", "pre-patch-2.2.19-16.gz", patch_base="2.2.18"),
    Version("2.2.19pre17", "2.2.19pre16", "Sun Mar 11 13:49:55 2001 +0000", "pre-patch-2.2.19-17.gz", patch_base="2.2.18"),
    Version("2.2.19pre18", "2.2.19pre17", "Fri Mar 23 00:36:20 2001 +0000", "pre-patch-2.2.19-18.gz", patch_base="2.2.18"),
    Version("2.2.19", "2.2.19pre18", "Sun Mar 25 18:45:46 2001 +0000"),
    Version("2.2.20pre1", "2.2.19", "Sat May  5 00:03:04 2001 +0000", "pre-patch-2.2.20-1.gz"),
    Version("2.2.20pre2", "2.2.20pre1", "Tue May  8 16:20:43 2001 +0000", "pre-patch-2.2.20-2.gz", patch_base="2.2.19"),
    Version("2.2.20pre3", "2.2.20pre2", "Mon Jun 18 09:35:46 2001 +0000", "pre-patch-2.2.20-3.gz", patch_base="2.2.19"),
    Version("2.2.20pre4", "2.2.20pre3", "Tue Jun 19 12:13:14 2001 +0000", "pre-patch-2.2.20-4.gz", patch_base="2.2.19"),
    Version("2.2.20pre5", "2.2.20pre4", "Tue Jun 19 17:40:55 2001 +0000", "pre-patch-2.2.20-5.gz", patch_base="2.2.19"),
    Version("2.2.20pre6", "2.2.20pre5", "Mon Jun 25 15:35:03 2001 +0000", "pre-patch-2.2.20-6.gz", patch_base="2.2.19"),
    Version("2.2.20pre7", "2.2.20pre6", "Wed Jul  4 16:22:43 2001 +0000", "pre-patch-2.2.20-7.gz", patch_base="2.2.19"),
    Version("2.2.20pre8", "2.2.20pre7", "Thu Jul 26 18:26:56 2001 +0000", "pre-patch-2.2.20-8.gz", patch_base="2.2.19"),
    Version("2.2.20pre9", "2.2.20pre8", "Wed Aug  8 23:26:59 2001 +0000", "pre-patch-2.2.20-9.gz", patch_base="2.2.19"),
    Version("2.2.20pre10", "2.2.20pre9", "Mon Sep 10 16:02:39 2001 +0000", "pre-patch-2.2.20-10.gz", patch_base="2.2.19"),
    Version("2.2.20pre11", "2.2.20pre10", "Mon Oct 22 11:00:31 2001 +0000", "pre-patch-2.2.20-11.gz", patch_base="2.2.19"),
    Version("2.2.20pre12", "2.2.20pre11", "Wed Oct 31 14:20:23 2001 +0000", "pre-patch-2.2.20-12.gz", patch_base="2.2.19"),
    Version("2.2.20", "2.2.20pre12", "Fri Nov  2 16:41:06 2001 +0000"),
    Version("2.2.21pre1", "2.2.20", "Sat Dec 29 03:50:08 2001 +0000", "patch-2.2.21-pre1.gz"),
    Version("2.2.21pre2", "2.2.21pre1", "Wed Jan  2 11:01:09 2002 +0000", "patch-2.2.21-pre2.gz", patch_base="2.2.20"),
    Version("2.2.21pre3", "2.2.21pre2", "Mon Feb 25 22:18:56 2002 +0000", "patch-2.2.21-pre3.gz", patch_base="2.2.20"),
    Version("2.2.21pre4", "2.2.21pre3", "Fri Mar  8 21:58:12 2002 +0000", "patch-2.2.21-pre4.gz", patch_base="2.2.20"),
    Version("2.2.21-rc1", "2.2.21pre4", "Tue Mar 12 11:48:50 2002 +0000", "patch-2.2.21-rc1.gz", patch_base="2.2.20"),
    Version("2.2.21-rc2", "2.2.21-rc1", "Thu Mar 14 17:53:28 2002 +0000", "patch-2.2.21-rc2.gz", patch_base="2.2.20"),
    Version("2.2.21-rc3", "2.2.21-rc2", "Mon Apr  1 17:10:26 2002 +0000", "patch-2.2.21-rc3.gz", patch_base="2.2.20"),
    Version("2.2.21-rc4", "2.2.21-rc3", "Wed May 15 17:05:08 2002 +0000", "patch-2.2.21-rc4.gz", patch_base="2.2.20"),
    Version("2.2.21", "2.2.21-rc4", "Mon May 20 23:32:35 2002 +0000"),
    Version("2.2.22-rc1", "2.2.21", "Fri Aug 16 01:03:53 2002 +0000", "patch-2.2.22-rc1.gz"),
    Version("2.2.22-rc2", "2.2.22-rc1", "Fri Aug 30 15:38:26 2002 +0000", "patch-2.2.22-rc2.gz", patch_base="2.2.21"),
    Version("2.2.22-rc3", "2.2.22-rc2", "Fri Sep 13 14:45:04 2002 +0000", "patch-2.2.22-rc3.gz", patch_base="2.2.21"),
    Version("2.2.22", "2.2.22-rc3", "Mon Sep 16 16:26:34 2002 +0000"),
    Version("2.2.23-rc1", "2.2.22", "Wed Nov 20 12:22:28 2002 +0000", "patch-2.2.23-rc1.gz"),
    Version("2.2.23-rc2", "2.2.23-rc1", "Wed Nov 20 15:50:44 2002 +0000", "patch-2.2.23-rc2.gz", patch_base="2.2.22"),
    Version("2.2.23", "2.2.23-rc2", "Fri Nov 29 18:07:37 2002 +0000"),
    Version("2.2.24-rc1", "2.2.23", "Mon Dec 16 19:14:54 2002 +0000", "patch-2.2.24-rc1.gz"),
    Version("2.2.24-rc2", "2.2.24-rc1", "Thu Dec 19 18:52:38 2002 +0000", "patch-2.2.24-rc2.gz", patch_base="2.2.23"),
    Version("2.2.24-rc3", "2.2.24-rc2", "Thu Feb 13 20:19:02 2003 +0000", "patch-2.2.24-rc3.gz", patch_base="2.2.23"),
    Version("2.2.24-rc4", "2.2.24-rc3", "Wed Feb 19 13:33:37 2003 +0000", "patch-2.2.24-rc4.gz", patch_base="2.2.23"),
    Version("2.2.24-rc5", "2.2.24-rc4", "Mon Mar  3 14:59:59 2003 +0000", "patch-2.2.24-rc5.gz", patch_base="2.2.23"),
    Version("2.2.24", "2.2.24-rc5", "Wed Mar  5 14:47:02 2003 +0000"),
    Version("2.2.25", "2.2.24", "Mon Mar 17 14:15:54 2003 +0000"),
    Version("2.2.26", "2.2.25", "Tue Feb 24 18:10:30 2004 +0000"),
    Version("2.2.27pre1", "2.2.26", "Wed Mar 24 20:09:38 2004 +0000", "patch-2.2.27-pre1.gz"),
    Version("2.2.27pre2", "2.2.27pre1", "Tue Apr 20 20:59:55 2004 +0000", "patch-2.2.27-pre2.gz", patch_base="2.2.26"),
    Version("2.2.27-rc1", "2.2.27pre2", "Tue Jan 11 17:22:11 2005 +0000", "patch-2.2.27-rc1.gz", patch_base="2.2.26"),
    Version("2.2.27-rc2", "2.2.27-rc1", "Thu Jan 13 00:52:37 2005 +0000", "patch-2.2.27-rc2.gz", patch_base="2.2.26"),
]
# fmt: on


def changelog_path(v: Version) -> Path:
    return CHANGELOGS / version_subdir(v.name) / f"{v.name}.txt"
