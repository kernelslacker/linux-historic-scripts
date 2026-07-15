"""Shared version table and helpers for untar-2.0.py / make-diffs-2.0.py / import-2.0.py.

Continues from 1.x's pre2.0.14 (on branch "master"). At 2.0.21, development
moves to 2.1 on master while Alan Cox takes over long-term 2.0.x maintenance
on a new branch "2.0" (this script never checks back out to master -- 2.1's
import picks up master from 2.0.21). Authorship changes again to David
Weinehall at 2.0.39pre1, still on branch "2.0".

2.0.34, 2.0.36, and 2.0.38 are tag-only aliases: the named prepatch and the
"final" release are byte-identical, so the original script just adds an
extra git tag on the existing commit instead of importing a no-op diff.

Prepatches from 2.0.31 onward are cut against the last STABLE release
(cp -rl always from e.g. "2.0.31", not from the previous prepatch) even
though the git history/diffs are incremental prepatch-to-prepatch -- hence
`base` (diff/import predecessor) and `patch_base` (cp -rl source during
untar) are tracked separately here, unlike 0.x/1.x where they were always
the same version.

20 dates have no source in the original import-2.0.sh (it silently fell
back to wall-clock time at the moment the script was run). Real dates were
recovered: "2.0"'s from the tarball's own newest internal file mtime
(matches the well-known public 2.0.0 release date), the rest from the
latest embedded diff-header timestamp in each prepatch file (same
technique as the 0.10 RCS-file dig, applied directly to the diffs this
time). See conversation history for the extraction commands.
"""

import dataclasses

from linux_hist_common import LINUS, ROOT, Author  # noqa: F401 (re-exported)

BINARIES = ROOT / "binaries" / "2.0"


@dataclasses.dataclass
class Version:
    # fmt: off
    name: str
    base: str | None            # diff/import predecessor; None for alias entries
    date: str | None            # git --date value; None for alias entries (inherits target's commit)
    patch: str | None = None    # filename under BINARIES; None means "extract the tarball"
    compression: str = "gz"     # "gz" -> zcat (only meaningful when patch is set)
    patch_base: str | None = None   # cp -rl source during untar, if different from `base`
    branch_create: str | None = None
    branch_checkout: str | None = None
    author: Author | None = None    # (name, email); sticky until changed again
    changelog: str | None = None    # override changelog basename (without .txt) if it doesn't match `name`
    alias_of: str | None = None     # if set: not a real commit, just `git tag name` on alias_of's commit
    # fmt: on


# fmt: off
VERSIONS: list[Version] = [
    Version("2.0", "pre2.0.14", "Sun Jun  9 05:48:00 1996 +0000"),  # date recovered, not in original import-2.0.sh
    Version("2.0.1", "2.0", "Wed Jul  3 11:12:00 1996 +0000"),
    Version("2.0.2", "2.0.1", "Fri Jul  5 11:59:00 1996 +0000"),
    Version("2.0.3", "2.0.2", "Sat Jul  6 06:38:00 1996 +0000"),
    Version("2.0.4", "2.0.3", "Mon Jul  8 08:39:00 1996 +0000"),
    Version("2.0.5", "2.0.4", "Wed Jul 10 08:11:00 1996 +0000"),
    Version("2.0.6", "2.0.5", "Fri Jul 12 05:30:00 1996 +0000"),
    Version("2.0.7", "2.0.6", "Mon Jul 15 07:23:00 1996 +0000"),
    Version("2.0.8", "2.0.7", "Sat Jul 20 02:29:00 1996 +0000"),
    Version("2.0.9", "2.0.8", "Fri Jul 26 03:55:00 1996 +0000"),
    Version("2.0.10", "2.0.9", "Sat Jul 27 06:31:00 1996 +0000"),
    Version("2.0.11", "2.0.10", "Mon Aug  5 02:26:00 1996 +0000"),
    Version("2.0.12", "2.0.11", "Fri Aug  9 09:43:00 1996 +0000"),
    Version("2.0.13", "2.0.12", "Fri Aug 16 04:40:00 1996 +0000"),
    Version("2.0.14", "2.0.13", "Tue Aug 20 11:20:00 1996 +0000"),
    Version("2.0.15", "2.0.14", "Sun Aug 25 03:04:00 1996 +0000"),
    Version("2.0.16", "2.0.15", "Sat Aug 31 13:53:00 1996 +0000"),
    Version("2.0.17", "2.0.16", "Mon Sep  2 03:56:00 1996 +0000"),
    Version("2.0.18", "2.0.17", "Thu Sep  5 08:45:00 1996 +0000"),
    Version("2.0.19", "2.0.18", "Wed Sep 11 08:21:00 1996 +0000"),
    Version("2.0.20", "2.0.19", "Fri Sep 13 08:46:00 1996 +0000"),
    Version("2.0.21", "2.0.20", "Fri Sep 20 09:26:00 1996 +0000"),
    Version("2.0.22", "2.0.21", "Tue Oct  8 12:51:00 1996 +0000", branch_create="2.0", branch_checkout="2.0", author=("Alan Cox", "alan@lxorguk.ukuu.org.uk")),
    Version("2.0.23", "2.0.22", "Fri Oct 18 08:11:00 1996 +0000"),
    Version("2.0.24", "2.0.23", "Tue Oct 29 22:00:00 1996 +0000"),
    Version("2.0.25", "2.0.24", "Fri Nov  8 01:44:00 1996 +0000"),
    Version("2.0.26", "2.0.25", "Fri Nov 22 05:13:00 1996 +0000"),
    Version("2.0.27", "2.0.26", "Sun Dec  1 13:08:00 1996 +0000"),
    Version("2.0.28", "2.0.27", "Tue Jan 14 07:21:00 1997 +0000"),
    Version("2.0.29", "2.0.28", "Fri Feb  7 07:34:00 1997 +0000"),
    Version("2.0.30", "2.0.29", "Tue Apr  8 12:14:00 1997 +0000"),
    Version("2.0.31pre1", "2.0.30", "Sun Aug  3 15:40:59 1997 +0000", "patch-2.0.31-pre1.gz", "gz"),
    Version("2.0.31pre2", "2.0.31pre1", "Mon Aug  4 15:41:59 1997 +0000", "patch-2.0.31-pre2.gz", "gz", patch_base="2.0.30"),
    Version("2.0.31pre3", "2.0.31pre2", "Mon Aug  4 17:35:57 1997 +0000", "patch-2.0.31-pre3.gz", "gz", patch_base="2.0.30"),
    Version("2.0.31pre4", "2.0.31pre3", "Mon Aug 11 13:42:11 1997 +0000", "patch-2.0.31-pre4.gz", "gz", patch_base="2.0.30"),
    Version("2.0.31pre5", "2.0.31pre4", "Tue Aug 12 14:47:16 1997 +0000", "patch-2.0.31-pre5.gz", "gz", patch_base="2.0.30"),
    Version("2.0.31pre6", "2.0.31pre5", "Thu Aug 14 11:19:48 1997 +0000", "patch-2.0.31-pre6.gz", "gz", patch_base="2.0.30"),
    Version("2.0.31pre7", "2.0.31pre6", "Sun Aug 17 13:35:10 1997 +0000", "patch-2.0.31-pre7.gz", "gz", patch_base="2.0.30"),
    Version("2.0.31pre8", "2.0.31pre7", "Sun Aug 31 08:49:57 1997 +0000", "patch-2.0.31-pre8.gz", "gz", patch_base="2.0.30"),
    Version("2.0.31pre9", "2.0.31pre8", "Fri Sep  5 20:43:59 1997 +0000", "patch-2.0.31-pre9.gz", "gz", patch_base="2.0.30"),
    Version("2.0.31pre10", "2.0.31pre9", "Tue Sep 23 21:04:20 1997 +0000", "patch-2.0.31-pre10.gz", "gz", patch_base="2.0.30"),
    Version("2.0.31", "2.0.31pre10", "Fri Oct 17 17:05:00 1997 +0000"),
    Version("2.0.32pre1", "2.0.31", "Fri Nov  7 10:51:05 1997 +0000", "patch-2.0.32-pre1.gz", "gz"),
    Version("2.0.32pre2", "2.0.32pre1", "Fri Nov  7 16:58:01 1997 +0000", "patch-2.0.32-pre2.gz", "gz", patch_base="2.0.31"),
    Version("2.0.32pre5", "2.0.32pre2", "Fri Nov 14 10:55:32 1997 +0000", "patch-2.0.32-pre5.gz", "gz", patch_base="2.0.31"),
    Version("2.0.32pre6", "2.0.32pre5", "Sun Nov 16 17:17:04 1997 +0000", "patch-2.0.32-pre6.gz", "gz", patch_base="2.0.31"),
    Version("2.0.32", "2.0.32pre6", "Mon Nov 17 21:25:00 1997 +0000"),
    Version("2.0.33pre1", "2.0.32", "Tue Dec  2 14:18:13 1997 +0000", "patch-2.0.33-pre1.gz", "gz"),
    Version("2.0.33pre2", "2.0.33pre1", "Thu Dec  4 13:13:23 1997 +0000", "patch-2.0.33-pre2.gz", "gz", patch_base="2.0.32"),
    Version("2.0.33pre3", "2.0.33pre2", "Wed Dec 10 18:21:47 1997 +0000", "patch-2.0.33-pre3.gz", "gz", patch_base="2.0.32"),
    Version("2.0.33", "2.0.33pre3", "Mon Dec 15 21:37:00 1997 +0000"),
    Version("2.0.34pre2", "2.0.33", "Fri Jan 23 00:42:42 1998 +0000", "patch-2.0.34-pre2.gz", "gz"),
    Version("2.0.34pre3", "2.0.34pre2", "Sat Jan 31 10:00:00 1998 +0000", "patch-2.0.34-pre3.gz", "gz", patch_base="2.0.33"),
    Version("2.0.34pre4", "2.0.34pre3", "Thu Mar 26 10:30:08 1998 +0000", "patch-2.0.34pre4.gz", "gz", patch_base="2.0.33"),
    Version("2.0.34pre5", "2.0.34pre4", "Tue Mar 31 20:01:59 1998 +0000", "patch-2.0.34pre5.gz", "gz", patch_base="2.0.33"),
    Version("2.0.34pre6", "2.0.34pre5", "Sat Apr  4 19:56:20 1998 +0000", "patch-2.0.34pre6.gz", "gz", patch_base="2.0.33"),
    Version("2.0.34pre7", "2.0.34pre6", "Sun Apr  5 18:59:27 1998 +0000", "patch-2.0.34pre7.gz", "gz", patch_base="2.0.33"),
    Version("2.0.34pre8", "2.0.34pre7", "Tue Apr 14 22:42:58 1998 +0000", "patch-2.0.34pre8.gz", "gz", patch_base="2.0.33"),
    Version("2.0.34pre9", "2.0.34pre8", "Sun Apr 19 18:52:55 1998 +0000", "patch-2.0.34pre9.gz", "gz", patch_base="2.0.33"),
    Version("2.0.34pre10", "2.0.34pre9", "Mon Apr 20 09:04:32 1998 +0000", "patch-2.0.34pre10.gz", "gz", patch_base="2.0.33"),
    Version("2.0.34pre11b", "2.0.34pre10", "Wed Apr 22 00:33:18 1998 +0000", "patch-2.0.34pre11b.gz", "gz", patch_base="2.0.33"),
    Version("2.0.34pre15", "2.0.34pre11b", "Sun May 17 18:46:05 1998 +0000", "patch-2.0.34pre15.gz", "gz", patch_base="2.0.33"),
    Version("2.0.34pre16", "2.0.34pre15", "Thu May 21 01:03:34 1998 +0000", "patch-2.0.34pre16.gz", "gz", patch_base="2.0.33"),
    Version("2.0.34", None, None, alias_of="2.0.34pre16"),
    Version("2.0.35pre1", "2.0.34", "Sun Jun 21 19:54:01 1998 +0000", "2.0.35-pre-patch-1.gz", "gz"),
    Version("2.0.35pre2", "2.0.35pre1", "Mon Jun 29 17:46:22 1998 +0000", "2.0.35-pre-patch-2.gz", "gz", patch_base="2.0.34"),
    Version("2.0.35pre3", "2.0.35pre2", "Tue Jun 30 18:03:32 1998 +0000", "2.0.35-pre-patch-3.gz", "gz", patch_base="2.0.34"),
    Version("2.0.35pre4", "2.0.35pre3", "Wed Jul  1 16:24:11 1998 +0000", "2.0.35-pre-patch-4.gz", "gz", patch_base="2.0.34"),
    Version("2.0.35pre5", "2.0.35pre4", "Thu Jul  2 13:08:48 1998 +0000", "2.0.35-pre-patch-5.gz", "gz", patch_base="2.0.34"),
    Version("2.0.35pre6", "2.0.35pre5", "Thu Jul  9 15:26:44 1998 +0000", "2.0.35-pre-patch-6.gz", "gz", patch_base="2.0.34"),
    Version("2.0.35pre7", "2.0.35pre6", "Sat Jul 11 15:09:43 1998 +0000", "2.0.35-pre-patch-7.gz", "gz", patch_base="2.0.34"),
    Version("2.0.35pre8", "2.0.35pre7", "Mon Jul 13 09:51:38 1998 +0000", "2.0.35-pre-patch-8.gz", "gz", patch_base="2.0.34"),
    Version("2.0.35pre9", "2.0.35pre8", "Mon Jul 13 09:51:38 1998 +0000", "2.0.35-pre-patch-9.gz", "gz", patch_base="2.0.34"),
    Version("2.0.35", "2.0.35pre9", "Mon Jul 13 16:59:00 1998 +0000"),
    Version("2.0.36pre1", "2.0.35", "Fri Jul 24 17:29:06 1998 +0000", "2.0.36-pre-patch-1.gz", "gz"),
    Version("2.0.36pre2", "2.0.36pre1", "Tue Aug  4 02:17:33 1998 +0000", "2.0.36-pre-patch-2.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre3", "2.0.36pre2", "Tue Aug 11 18:21:52 1998 +0000", "2.0.36-pre-patch-3.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre4", "2.0.36pre3", "Wed Aug 12 18:35:14 1998 +0000", "2.0.36-pre-patch-4.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre5", "2.0.36pre4", "Wed Aug 12 18:35:14 1998 +0000", "2.0.36-pre-patch-5.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre6", "2.0.36pre5", "Tue Aug 18 14:39:27 1998 +0000", "2.0.36-pre-patch-6.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre7", "2.0.36pre6", "Mon Aug 31 22:51:25 1998 +0000", "2.0.36-pre-patch-7.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre8", "2.0.36pre7", "Mon Sep  7 16:42:06 1998 +0000", "2.0.36-pre-patch-8.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre9", "2.0.36pre8", "Fri Sep 11 05:51:10 1998 +0000", "2.0.36-pre-patch-9.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre10", "2.0.36pre9", "Tue Sep 15 18:39:29 1998 +0000", "2.0.36-pre-patch-10.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre11", "2.0.36pre10", "Wed Sep 23 16:18:57 1998 +0000", "2.0.36-pre-patch-11.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre12", "2.0.36pre11", "Fri Sep 25 01:15:03 1998 +0000", "2.0.36-pre-patch-12.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre13", "2.0.36pre12", "Sun Oct  4 22:34:28 1998 +0000", "2.0.36-pre-patch-13.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre14", "2.0.36pre13", "Thu Oct  8 19:00:04 1998 +0000", "2.0.36-pre-patch-14.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre15", "2.0.36pre14", "Thu Oct 15 00:13:37 1998 +0000", "2.0.36-pre-patch-15.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre16", "2.0.36pre15", "Fri Oct 30 17:38:59 1998 +0000", "2.0.36-pre-patch-16.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre17", "2.0.36pre16", "Thu Nov  5 23:45:27 1998 +0000", "2.0.36-pre-patch-17.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre18", "2.0.36pre17", "Mon Nov  9 15:41:39 1998 +0000", "2.0.36-pre-patch-18.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre19", "2.0.36pre18", "Mon Nov  9 20:15:26 1998 +0000", "2.0.36-pre-patch-19.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre20", "2.0.36pre19", "Tue Nov 10 21:29:41 1998 +0000", "2.0.36-pre-patch-20.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre21", "2.0.36pre20", "Wed Nov 11 15:10:48 1998 +0000", "2.0.36-pre-patch-21.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36pre22", "2.0.36pre21", "Sat Nov 14 02:15:46 1998 +0000", "2.0.36-pre-patch-22.gz", "gz", patch_base="2.0.35"),
    Version("2.0.36", None, None, alias_of="2.0.36pre22"),
    Version("2.0.37pre1", "2.0.36", "Tue Dec  8 03:06:00 1998 +0000", "patch-2.0.37-pre1.gz", "gz"),
    Version("2.0.37pre2", "2.0.37pre1", "Fri Dec 11 23:11:00 1998 +0000", "patch-2.0.37-pre2.gz", "gz", patch_base="2.0.36"),
    Version("2.0.37pre3", "2.0.37pre2", "Tue Dec 15 00:00:00 1998 +0000", "patch-2.0.37-pre3.gz", "gz", patch_base="2.0.36"),
    Version("2.0.37pre4", "2.0.37pre3", "Mon Dec 28 06:43:00 1998 +0000", "patch-2.0.37-pre4.gz", "gz", patch_base="2.0.36"),
    Version("2.0.37pre5", "2.0.37pre4", "Sun Jan 31 20:50:00 1999 +0000", "patch-2.0.37-pre5.gz", "gz", patch_base="2.0.36"),
    Version("2.0.37pre6", "2.0.37pre5", "Thu Feb 11 14:13:00 1999 +0000", "patch-2.0.37-pre6.gz", "gz", patch_base="2.0.36"),
    Version("2.0.37pre7", "2.0.37pre6", "Tue Mar  2 04:06:29 1999 +0000", "patch-2.0.37-pre7.gz", "gz", patch_base="2.0.36"),
    Version("2.0.37pre8", "2.0.37pre7", "Thu Mar  4 03:51:00 1999 +0000", "patch-2.0.37-pre8.gz", "gz", patch_base="2.0.36"),
    Version("2.0.37pre9", "2.0.37pre8", "Fri Mar 26 19:10:59 1999 +0000", "patch-2.0.37-pre9.gz", "gz", patch_base="2.0.36"),
    Version("2.0.37pre10", "2.0.37pre9", "Wed Apr 14 23:25:10 1999 +0000", "patch-2.0.37-pre10.gz", "gz", patch_base="2.0.36"),
    Version("2.0.37pre11", "2.0.37pre10", "Tue Apr 27 14:58:41 1999 +0000", "patch-2.0.37-pre11.gz", "gz", patch_base="2.0.36"),
    Version("2.0.37pre12", "2.0.37pre11", "Thu May 13 14:21:00 1999 +0000", "patch-2.0.37-pre12.gz", "gz", patch_base="2.0.36"),
    Version("2.0.37", "2.0.37pre12", "Sun Jun 13 14:01:00 1999 +0000"),
    Version("2.0.38pre1", "2.0.37", "Fri Aug 13 16:37:00 1999 +0000", "patch-2.0.38-pre1.gz", "gz"),
    Version("2.0.38", None, None, alias_of="2.0.38pre1"),
    Version("2.0.39pre1", "2.0.38", "Thu Dec 16 00:28:46 1999 +0000", "patch-2.0.39-pre1.gz", "gz", author=("David Weinehall", "tao@acc.umu.se")),  # date recovered, not in original import-2.0.sh
    Version("2.0.39pre2", "2.0.39pre1", "Wed Feb  2 09:25:57 2000 +0000", "patch-2.0.39-pre2.gz", "gz", patch_base="2.0.38"),  # date recovered, not in original import-2.0.sh
    Version("2.0.39pre3", "2.0.39pre2", "Tue Feb  8 15:48:52 2000 +0000", "patch-2.0.39-pre3.gz", "gz", patch_base="2.0.38"),  # date recovered, not in original import-2.0.sh
    Version("2.0.39pre4", "2.0.39pre3", "Tue Apr 25 16:34:46 2000 +0000", "patch-2.0.39-pre4.gz", "gz", patch_base="2.0.38"),  # date recovered, not in original import-2.0.sh
    Version("2.0.39pre5", "2.0.39pre4", "Wed Jun 28 15:43:19 2000 +0000", "patch-2.0.39-pre5.gz", "gz", patch_base="2.0.38"),  # date recovered, not in original import-2.0.sh
    Version("2.0.39pre6", "2.0.39pre5", "Mon Jul 17 14:04:57 2000 +0000", "patch-2.0.39-pre6.gz", "gz", patch_base="2.0.38"),  # date recovered, not in original import-2.0.sh
    Version("2.0.39pre7", "2.0.39pre6", "Sun Aug 27 21:54:12 2000 +0000", "patch-2.0.39-pre7.gz", "gz", patch_base="2.0.38"),  # date recovered, not in original import-2.0.sh
    Version("2.0.39pre8", "2.0.39pre7", "Thu Sep  7 03:58:35 2000 +0000", "patch-2.0.39-pre8.gz", "gz", patch_base="2.0.38"),  # date recovered, not in original import-2.0.sh
    Version("2.0.39", "2.0.39pre8", "Tue Jan 9 16:29:00 2001 +0000"),
    Version("2.0.40pre1", "2.0.39", "Wed Sep 12 15:37:34 2001 +0000", "patch-2.0.40-pre1.gz", "gz", changelog="2.0.40-pre1"),  # date recovered, not in original import-2.0.sh
    Version("2.0.40pre2", "2.0.40pre1", "Sun Dec  9 16:04:40 2001 +0000", "patch-2.0.40-pre2.gz", "gz", patch_base="2.0.39", changelog="2.0.40-pre2"),  # date recovered, not in original import-2.0.sh
    Version("2.0.40pre3", "2.0.40pre2", "Mon Nov 26 21:12:45 2001 +0000", "patch-2.0.40-pre3.gz", "gz", patch_base="2.0.39", changelog="2.0.40-pre3"),  # date recovered; out of order vs pre2, but genuinely what's embedded in this patch -- see conversation
    Version("2.0.40-rc1", "2.0.40pre3", "Tue Jan  8 23:21:40 2002 +0000", "patch-2.0.40-rc1.gz", "gz", patch_base="2.0.39"),  # date recovered, not in original import-2.0.sh
    Version("2.0.40-rc2", "2.0.40-rc1", "Wed Jan 23 22:27:01 2002 +0000", "patch-2.0.40-rc2.gz", "gz", patch_base="2.0.39"),  # date recovered, not in original import-2.0.sh
    Version("2.0.40-rc3", "2.0.40-rc2", "Wed Jan 23 22:27:01 2002 +0000", "patch-2.0.40-rc3.gz", "gz", patch_base="2.0.39"),  # date recovered, not in original import-2.0.sh
    Version("2.0.40-rc4", "2.0.40-rc3", "Sun Mar 17 12:54:46 2002 +0000", "patch-2.0.40-rc4.gz", "gz", patch_base="2.0.39"),  # date recovered, not in original import-2.0.sh
    Version("2.0.40-rc5", "2.0.40-rc4", "Sun Jun  2 19:13:36 2002 +0000", "patch-2.0.40-rc5.gz", "gz", patch_base="2.0.39"),  # date recovered, not in original import-2.0.sh
    Version("2.0.40-rc6", "2.0.40-rc5", "Tue Jun 25 16:12:48 2002 +0000", "patch-2.0.40-rc6.gz", "gz", patch_base="2.0.39"),  # date recovered, not in original import-2.0.sh
    Version("2.0.40-rc7", "2.0.40-rc6", "Mon Mar 24 18:12:28 2003 +0000", "patch-2.0.40-rc7.gz", "gz", patch_base="2.0.39"),  # date recovered, not in original import-2.0.sh
    Version("2.0.40-rc8", "2.0.40-rc7", "Sun Jan 25 20:28:37 2004 +0000", "patch-2.0.40-rc8.gz", "gz", patch_base="2.0.39"),  # date recovered, not in original import-2.0.sh
    Version("2.0.40", "2.0.40-rc8", "Sun Feb 8 02:13:00 2004 +0000"),
]
# fmt: on
