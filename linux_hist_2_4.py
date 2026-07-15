"""Shared version table and helpers for untar-2.4.py / make-diffs-2.4.py / import-2.4.py.

Unlike 0.x-2.3, there was no existing make-diffs-2.4.sh or import-2.4.sh to
port -- untar-2.4.sh itself only got as far as 2.4.15. This module extends
that (per user decision) all the way to 2.4.35.3, following the same
conventions established by the earlier branches: prepatches cut against
the last stable release where archived (`base` vs `patch_base` diverge),
plain tarball-to-tarball diffs where no prepatches exist. Continues from
2.3's "2.4.0-prerelease" (all on master, always Linus -- no branching here).

2.4.11 is included as the real (if short-lived) release it was: Linux 2.4.11
was withdrawn within days of release over a serious VFS bug, and the
binaries directory only has it under openly hostile names
("2.4.11-pre-dangerous-dont-use*.gz", "linux-2.4.11-dontuse.tar.gz") -- kept
verbatim, consistent with this project's "include the messy details"
philosophy (NOTES.md) and consistent with 2.2/2.3's "REALLY-DANGEROUS" /
"for-alan-only" patches being included rather than dropped. The four
"-dangerous" prepatches predate the normal pre1-pre6 sequence
chronologically (confirmed via dates/2.4.txt) -- they're the real, if
extremely nervous, lead-up to the recall. dontuse-patch-2.4.1-pre6.gz is
the same situation on a smaller scale: no normally-named alternative
exists for that slot, and its date sits exactly between pre5 and pre7.

Dates for 2.4.0-2.4.31 come from dates/2.4.txt (real FTP publish
timestamps researched previously). Dates for 2.4.32 onward are NOT in that
file usably -- every entry from 2.4.32 on shares the identical bogus
"01-May-2013" timestamp (a bulk re-download date, not a release date), so
those were recovered via tarball-internal-mtime digging instead (same
technique as 2.0/2.2/2.3).
"""

import dataclasses
from pathlib import Path

from linux_hist_common import CHANGELOGS, LINUS, ROOT  # noqa: F401 (re-exported)

BINARIES = ROOT / "binaries" / "2.4"


@dataclasses.dataclass
class Version:
    # fmt: off
    name: str
    base: str
    date: str
    patch: str | None = None        # filename under BINARIES; None means "extract the tarball"
    patch_base: str | None = None   # cp -rl source during untar, if different from `base`
    archive: str | None = None      # tarball filename, if different from f"linux-{name}.tar.gz"
    branch_create: str | None = None
    branch_checkout: str | None = None
    # fmt: on


# fmt: off
VERSIONS: list[Version] = [
    Version("2.4.0", "2.4.0-prerelease", "Thu Jan  4 23:45:00 2001 +0000"),
    Version("2.4.1pre1", "2.4.0", "Tue Jan  9 02:56:00 2001 +0000", "patch-2.4.1-pre1.gz"),
    Version("2.4.1pre2", "2.4.1pre1", "Thu Jan 11 08:26:00 2001 +0000", "patch-2.4.1-pre2.gz", patch_base="2.4.0"),
    Version("2.4.1pre3", "2.4.1pre2", "Fri Jan 12 02:02:00 2001 +0000", "patch-2.4.1-pre3.gz", patch_base="2.4.0"),
    Version("2.4.1pre4", "2.4.1pre3", "Mon Jan 15 20:55:00 2001 +0000", "patch-2.4.1-pre4.gz", patch_base="2.4.0"),
    Version("2.4.1pre5", "2.4.1pre4", "Mon Jan 15 23:50:00 2001 +0000", "patch-2.4.1-pre5.gz", patch_base="2.4.0"),
    Version("2.4.1pre6", "2.4.1pre5", "Tue Jan 16 01:23:00 2001 +0000", "dontuse-patch-2.4.1-pre6.gz", patch_base="2.4.0"),
    Version("2.4.1pre7", "2.4.1pre6", "Tue Jan 16 02:36:00 2001 +0000", "patch-2.4.1-pre7.gz", patch_base="2.4.0"),
    Version("2.4.1pre8", "2.4.1pre7", "Wed Jan 17 01:37:00 2001 +0000", "patch-2.4.1-pre8.gz", patch_base="2.4.0"),
    Version("2.4.1pre9", "2.4.1pre8", "Sat Jan 20 00:35:00 2001 +0000", "patch-2.4.1-pre9.gz", patch_base="2.4.0"),
    Version("2.4.1pre10", "2.4.1pre9", "Tue Jan 23 01:08:00 2001 +0000", "patch-2.4.1-pre10.gz", patch_base="2.4.0"),
    Version("2.4.1pre11", "2.4.1pre10", "Sun Jan 28 18:16:00 2001 +0000", "patch-2.4.1-pre11.gz", patch_base="2.4.0"),
    Version("2.4.1pre12", "2.4.1pre11", "Mon Jan 29 21:48:00 2001 +0000", "patch-2.4.1-pre12.gz", patch_base="2.4.0"),
    Version("2.4.1", "2.4.1pre12", "Tue Jan 30 07:56:00 2001 +0000"),
    Version("2.4.2pre1", "2.4.1", "Sun Feb  4 04:09:00 2001 +0000", "patch-2.4.2-pre1.gz"),
    Version("2.4.2pre2", "2.4.2pre1", "Fri Feb  9 00:49:00 2001 +0000", "patch-2.4.2-pre2.gz", patch_base="2.4.1"),
    Version("2.4.2pre3", "2.4.2pre2", "Fri Feb  9 22:52:00 2001 +0000", "patch-2.4.2-pre3.gz", patch_base="2.4.1"),
    Version("2.4.2pre4", "2.4.2pre3", "Fri Feb 16 19:17:00 2001 +0000", "patch-2.4.2-pre4.gz", patch_base="2.4.1"),
    Version("2.4.2", "2.4.2pre4", "Thu Feb 22 01:00:00 2001 +0000"),
    Version("2.4.3pre1", "2.4.2", "Fri Mar  2 21:01:00 2001 +0000", "patch-2.4.3-pre1.gz"),
    Version("2.4.3pre2", "2.4.3pre1", "Sun Mar  4 22:40:00 2001 +0000", "patch-2.4.3-pre2.gz", patch_base="2.4.2"),
    Version("2.4.3pre3", "2.4.3pre2", "Wed Mar  7 06:50:00 2001 +0000", "patch-2.4.3-pre3.gz", patch_base="2.4.2"),
    Version("2.4.3pre4", "2.4.3pre3", "Tue Mar 13 02:45:00 2001 +0000", "patch-2.4.3-pre4.gz", patch_base="2.4.2"),
    Version("2.4.3pre5", "2.4.3pre4", "Tue Mar 20 02:38:00 2001 +0000", "patch-2.4.3-pre5.gz", patch_base="2.4.2"),
    Version("2.4.3pre6", "2.4.3pre5", "Wed Mar 21 00:35:00 2001 +0000", "patch-2.4.3-pre6.gz", patch_base="2.4.2"),
    Version("2.4.3pre7", "2.4.3pre6", "Sat Mar 24 03:03:00 2001 +0000", "patch-2.4.3-pre7.gz", patch_base="2.4.2"),
    Version("2.4.3pre8", "2.4.3pre7", "Mon Mar 26 04:08:00 2001 +0000", "patch-2.4.3-pre8.gz", patch_base="2.4.2"),
    Version("2.4.3", "2.4.3pre8", "Fri Mar 30 05:03:00 2001 +0000"),
    Version("2.4.4pre1", "2.4.3", "Sat Apr  7 00:56:00 2001 +0000", "patch-2.4.4-pre1.gz"),
    Version("2.4.4pre2", "2.4.4pre1", "Thu Apr 12 02:58:00 2001 +0000", "patch-2.4.4-pre2.gz", patch_base="2.4.3"),
    Version("2.4.4pre3", "2.4.4pre2", "Fri Apr 13 23:30:00 2001 +0000", "patch-2.4.4-pre3.gz", patch_base="2.4.3"),
    Version("2.4.4pre4", "2.4.4pre3", "Wed Apr 18 00:28:00 2001 +0000", "patch-2.4.4-pre4.gz", patch_base="2.4.3"),
    Version("2.4.4pre5", "2.4.4pre4", "Thu Apr 19 21:33:00 2001 +0000", "patch-2.4.4-pre5.gz", patch_base="2.4.3"),
    Version("2.4.4pre6", "2.4.4pre5", "Sat Apr 21 17:58:00 2001 +0000", "patch-2.4.4-pre6.gz", patch_base="2.4.3"),
    Version("2.4.4pre7", "2.4.4pre6", "Wed Apr 25 23:39:00 2001 +0000", "patch-2.4.4-pre7.gz", patch_base="2.4.3"),
    Version("2.4.4pre8", "2.4.4pre7", "Fri Apr 27 05:30:00 2001 +0000", "patch-2.4.4-pre8.gz", patch_base="2.4.3"),
    Version("2.4.4", "2.4.4pre8", "Sat Apr 28 01:43:00 2001 +0000"),
    Version("2.4.5pre1", "2.4.4", "Wed May  2 01:34:00 2001 +0000", "patch-2.4.5-pre1.gz"),
    Version("2.4.5pre2", "2.4.5pre1", "Tue May 15 07:42:00 2001 +0000", "patch-2.4.5-pre2.gz", patch_base="2.4.4"),
    Version("2.4.5pre3", "2.4.5pre2", "Wed May 16 19:40:00 2001 +0000", "patch-2.4.5-pre3.gz", patch_base="2.4.4"),
    Version("2.4.5pre4", "2.4.5pre3", "Sun May 20 01:35:00 2001 +0000", "patch-2.4.5-pre4.gz", patch_base="2.4.4"),
    Version("2.4.5pre5", "2.4.5pre4", "Tue May 22 18:09:00 2001 +0000", "patch-2.4.5-pre5.gz", patch_base="2.4.4"),
    Version("2.4.5pre6", "2.4.5pre5", "Fri May 25 00:47:00 2001 +0000", "patch-2.4.5-pre6.gz", patch_base="2.4.4"),
    Version("2.4.5", "2.4.5pre6", "Sat May 26 01:26:00 2001 +0000"),
    Version("2.4.6pre1", "2.4.5", "Tue Jun  5 02:30:00 2001 +0000", "patch-2.4.6-pre1.gz"),
    Version("2.4.6pre2", "2.4.6pre1", "Fri Jun  8 21:50:00 2001 +0000", "patch-2.4.6-pre2.gz", patch_base="2.4.5"),
    Version("2.4.6pre3", "2.4.6pre2", "Wed Jun 13 01:30:00 2001 +0000", "patch-2.4.6-pre3.gz", patch_base="2.4.5"),
    Version("2.4.6pre4", "2.4.6pre3", "Wed Jun 20 23:24:00 2001 +0000", "patch-2.4.6-pre4.gz", patch_base="2.4.5"),
    Version("2.4.6pre5", "2.4.6pre4", "Thu Jun 21 04:12:00 2001 +0000", "patch-2.4.6-pre5.gz", patch_base="2.4.5"),
    Version("2.4.6pre6", "2.4.6pre5", "Thu Jun 28 00:23:00 2001 +0000", "patch-2.4.6-pre6.gz", patch_base="2.4.5"),
    Version("2.4.6pre7", "2.4.6pre6", "Fri Jun 29 20:35:00 2001 +0000", "patch-2.4.6-pre7.gz", patch_base="2.4.5"),
    Version("2.4.6pre8", "2.4.6pre7", "Sat Jun 30 02:42:00 2001 +0000", "patch-2.4.6-pre8.gz", patch_base="2.4.5"),
    Version("2.4.6pre9", "2.4.6pre8", "Tue Jul  3 00:41:00 2001 +0000", "patch-2.4.6-pre9.gz", patch_base="2.4.5"),
    Version("2.4.6", "2.4.6pre9", "Wed Jul  4 00:07:00 2001 +0000"),
    Version("2.4.7pre1", "2.4.6", "Wed Jul  4 18:55:00 2001 +0000", "patch-2.4.7-pre1.gz"),
    Version("2.4.7pre2", "2.4.7pre1", "Thu Jul  5 03:35:00 2001 +0000", "patch-2.4.7-pre2.gz", patch_base="2.4.6"),
    Version("2.4.7pre3", "2.4.7pre2", "Thu Jul  5 19:01:00 2001 +0000", "patch-2.4.7-pre3.gz", patch_base="2.4.6"),
    Version("2.4.7pre4", "2.4.7pre3", "Mon Jul  9 21:47:00 2001 +0000", "patch-2.4.7-pre4.gz", patch_base="2.4.6"),
    Version("2.4.7pre5", "2.4.7pre4", "Tue Jul 10 01:42:00 2001 +0000", "patch-2.4.7-pre5.gz", patch_base="2.4.6"),
    Version("2.4.7pre6", "2.4.7pre5", "Wed Jul 11 03:20:00 2001 +0000", "patch-2.4.7-pre6.gz", patch_base="2.4.6"),
    Version("2.4.7pre7", "2.4.7pre6", "Wed Jul 18 02:20:00 2001 +0000", "patch-2.4.7-pre7.gz", patch_base="2.4.6"),
    Version("2.4.7pre8", "2.4.7pre7", "Thu Jul 19 01:33:00 2001 +0000", "patch-2.4.7-pre8.gz", patch_base="2.4.6"),
    Version("2.4.7pre9", "2.4.7pre8", "Fri Jul 20 05:03:00 2001 +0000", "patch-2.4.7-pre9.gz", patch_base="2.4.6"),
    Version("2.4.7", "2.4.7pre9", "Fri Jul 20 21:25:00 2001 +0000"),
    Version("2.4.8pre1", "2.4.7", "Fri Jul 27 00:04:00 2001 +0000", "patch-2.4.8-pre1.gz"),
    Version("2.4.8pre2", "2.4.8pre1", "Sun Jul 29 03:20:00 2001 +0000", "patch-2.4.8-pre2.gz", patch_base="2.4.7"),
    Version("2.4.8pre3", "2.4.8pre2", "Mon Jul 30 17:43:00 2001 +0000", "patch-2.4.8-pre3.gz", patch_base="2.4.7"),
    Version("2.4.8pre4", "2.4.8pre3", "Sat Aug  4 06:14:00 2001 +0000", "patch-2.4.8-pre4.gz", patch_base="2.4.7"),
    Version("2.4.8pre5", "2.4.8pre4", "Tue Aug  7 07:39:00 2001 +0000", "patch-2.4.8-pre5.gz", patch_base="2.4.7"),
    Version("2.4.8pre6", "2.4.8pre5", "Tue Aug  7 21:26:00 2001 +0000", "patch-2.4.8-pre6.gz", patch_base="2.4.7"),
    Version("2.4.8pre7", "2.4.8pre6", "Wed Aug  8 18:20:00 2001 +0000", "patch-2.4.8-pre7.gz", patch_base="2.4.7"),
    Version("2.4.8pre8", "2.4.8pre7", "Fri Aug 10 00:34:00 2001 +0000", "patch-2.4.8-pre8.gz", patch_base="2.4.7"),
    Version("2.4.8", "2.4.8pre8", "Sat Aug 11 04:13:00 2001 +0000"),
    Version("2.4.9pre1", "2.4.8", "Sun Aug 12 22:56:00 2001 +0000", "patch-2.4.9-pre1.gz"),
    Version("2.4.9pre2", "2.4.9pre1", "Mon Aug 13 06:11:00 2001 +0000", "patch-2.4.9-pre2.gz", patch_base="2.4.8"),
    Version("2.4.9pre3", "2.4.9pre2", "Mon Aug 13 23:56:00 2001 +0000", "patch-2.4.9-pre3.gz", patch_base="2.4.8"),
    Version("2.4.9pre4", "2.4.9pre3", "Wed Aug 15 02:06:00 2001 +0000", "patch-2.4.9-pre4.gz", patch_base="2.4.8"),
    Version("2.4.9", "2.4.9pre4", "Thu Aug 16 18:32:00 2001 +0000"),
    Version("2.4.10pre1", "2.4.9", "Mon Aug 27 20:24:00 2001 +0000", "patch-2.4.10-pre1.gz"),
    Version("2.4.10pre2", "2.4.10pre1", "Tue Aug 28 18:30:00 2001 +0000", "patch-2.4.10-pre2.gz", patch_base="2.4.9"),
    Version("2.4.10pre3", "2.4.10pre2", "Sat Sep  1 19:14:00 2001 +0000", "patch-2.4.10-pre3.gz", patch_base="2.4.9"),
    Version("2.4.10pre4", "2.4.10pre3", "Sun Sep  2 17:52:00 2001 +0000", "patch-2.4.10-pre4.gz", patch_base="2.4.9"),
    Version("2.4.10pre5", "2.4.10pre4", "Sat Sep  8 04:21:00 2001 +0000", "patch-2.4.10-pre5.gz", patch_base="2.4.9"),
    Version("2.4.10pre6", "2.4.10pre5", "Sun Sep  9 02:53:00 2001 +0000", "patch-2.4.10-pre6.gz", patch_base="2.4.9"),
    Version("2.4.10pre7", "2.4.10pre6", "Mon Sep 10 02:41:00 2001 +0000", "patch-2.4.10-pre7.gz", patch_base="2.4.9"),
    Version("2.4.10pre8", "2.4.10pre7", "Tue Sep 11 00:45:00 2001 +0000", "patch-2.4.10-pre8.gz", patch_base="2.4.9"),
    Version("2.4.10pre9", "2.4.10pre8", "Fri Sep 14 00:48:00 2001 +0000", "patch-2.4.10-pre9.gz", patch_base="2.4.9"),
    Version("2.4.10pre10", "2.4.10pre9", "Sun Sep 16 21:53:00 2001 +0000", "patch-2.4.10-pre10.gz", patch_base="2.4.9"),
    Version("2.4.10pre11", "2.4.10pre10", "Tue Sep 18 00:04:00 2001 +0000", "patch-2.4.10-pre11.gz", patch_base="2.4.9"),
    Version("2.4.10pre12", "2.4.10pre11", "Wed Sep 19 00:38:00 2001 +0000", "patch-2.4.10-pre12.gz", patch_base="2.4.9"),
    Version("2.4.10pre13", "2.4.10pre12", "Fri Sep 21 04:14:00 2001 +0000", "patch-2.4.10-pre13.gz", patch_base="2.4.9"),
    Version("2.4.10pre14", "2.4.10pre13", "Sat Sep 22 05:43:00 2001 +0000", "patch-2.4.10-pre14.gz", patch_base="2.4.9"),
    Version("2.4.10pre15", "2.4.10pre14", "Sun Sep 23 03:58:00 2001 +0000", "patch-2.4.10-pre15.gz", patch_base="2.4.9"),
    Version("2.4.10", "2.4.10pre15", "Sun Sep 23 18:30:00 2001 +0000"),
    Version("2.4.11-dangerous1", "2.4.10", "Tue Sep 25 05:35:00 2001 +0000", "2.4.11-pre-dangerous-dont-use.gz"),
    Version("2.4.11-dangerous2", "2.4.11-dangerous1", "Fri Sep 28 01:35:00 2001 +0000", "2.4.11-pre-dangerous-dont-use-2.gz", patch_base="2.4.10"),
    Version("2.4.11-dangerous3", "2.4.11-dangerous2", "Fri Sep 28 18:42:00 2001 +0000", "2.4.11-pre-dangerous-dont-use-3.gz", patch_base="2.4.10"),
    Version("2.4.11-dangerous4", "2.4.11-dangerous3", "Sat Sep 29 19:58:00 2001 +0000", "2.4.11-pre-dangerous-dont-use-4.gz", patch_base="2.4.10"),
    Version("2.4.11pre1", "2.4.11-dangerous4", "Sun Sep 30 19:29:00 2001 +0000", "patch-2.4.11-pre1.gz", patch_base="2.4.10"),
    Version("2.4.11pre2", "2.4.11pre1", "Mon Oct  1 21:14:00 2001 +0000", "patch-2.4.11-pre2.gz", patch_base="2.4.10"),
    Version("2.4.11pre3", "2.4.11pre2", "Thu Oct  4 06:10:00 2001 +0000", "patch-2.4.11-pre3.gz", patch_base="2.4.10"),
    Version("2.4.11pre4", "2.4.11pre3", "Fri Oct  5 02:51:00 2001 +0000", "patch-2.4.11-pre4.gz", patch_base="2.4.10"),
    Version("2.4.11pre5", "2.4.11pre4", "Sun Oct  7 18:48:00 2001 +0000", "patch-2.4.11-pre5.gz", patch_base="2.4.10"),
    Version("2.4.11pre6", "2.4.11pre5", "Mon Oct  8 21:18:00 2001 +0000", "patch-2.4.11-pre6.gz", patch_base="2.4.10"),
    Version("2.4.11", "2.4.11pre6", "Tue Oct  9 23:55:00 2001 +0000", archive="linux-2.4.11-dontuse.tar.gz"),
    Version("2.4.12", "2.4.11", "Thu Oct 11 07:59:00 2001 +0000"),
    Version("2.4.13pre1", "2.4.12", "Thu Oct 11 21:16:00 2001 +0000", "patch-2.4.13-pre1.gz"),
    Version("2.4.13pre2", "2.4.13pre1", "Sat Oct 13 01:05:00 2001 +0000", "patch-2.4.13-pre2.gz", patch_base="2.4.12"),
    Version("2.4.13pre3", "2.4.13pre2", "Mon Oct 15 23:16:00 2001 +0000", "patch-2.4.13-pre3.gz", patch_base="2.4.12"),
    Version("2.4.13pre4", "2.4.13pre3", "Wed Oct 17 23:02:00 2001 +0000", "patch-2.4.13-pre4.gz", patch_base="2.4.12"),
    Version("2.4.13pre5", "2.4.13pre4", "Fri Oct 19 01:46:00 2001 +0000", "patch-2.4.13-pre5.gz", patch_base="2.4.12"),
    Version("2.4.13pre6", "2.4.13pre5", "Sun Oct 21 17:54:00 2001 +0000", "patch-2.4.13-pre6.gz", patch_base="2.4.12"),
    Version("2.4.13", "2.4.13pre6", "Wed Oct 24 05:28:00 2001 +0000"),
    Version("2.4.14pre1", "2.4.13", "Thu Oct 25 10:46:00 2001 +0000", "patch-2.4.14-pre1.gz"),
    Version("2.4.14pre2", "2.4.14pre1", "Fri Oct 26 02:46:00 2001 +0000", "patch-2.4.14-pre2.gz", patch_base="2.4.13"),
    Version("2.4.14pre3", "2.4.14pre2", "Sat Oct 27 07:20:00 2001 +0000", "patch-2.4.14-pre3.gz", patch_base="2.4.13"),
    Version("2.4.14pre4", "2.4.14pre3", "Mon Oct 29 22:36:00 2001 +0000", "patch-2.4.14-pre4.gz", patch_base="2.4.13"),
    Version("2.4.14pre5", "2.4.14pre4", "Tue Oct 30 01:12:00 2001 +0000", "patch-2.4.14-pre5.gz", patch_base="2.4.13"),
    Version("2.4.14pre6", "2.4.14pre5", "Wed Oct 31 07:51:00 2001 +0000", "patch-2.4.14-pre6.gz", patch_base="2.4.13"),
    Version("2.4.14pre7", "2.4.14pre6", "Fri Nov  2 02:09:00 2001 +0000", "patch-2.4.14-pre7.gz", patch_base="2.4.13"),
    Version("2.4.14pre8", "2.4.14pre7", "Sun Nov  4 01:42:00 2001 +0000", "patch-2.4.14-pre8.gz", patch_base="2.4.13"),
    Version("2.4.14", "2.4.14pre8", "Mon Nov  5 23:30:00 2001 +0000"),
    Version("2.4.15pre1", "2.4.14", "Thu Nov  8 01:47:00 2001 +0000", "patch-2.4.15-pre1.gz"),
    Version("2.4.15pre2", "2.4.15pre1", "Fri Nov  9 23:23:00 2001 +0000", "patch-2.4.15-pre2.gz", patch_base="2.4.14"),
    Version("2.4.15pre3", "2.4.15pre2", "Sun Nov 11 20:14:00 2001 +0000", "patch-2.4.15-pre3.gz", patch_base="2.4.14"),
    Version("2.4.15pre4", "2.4.15pre3", "Mon Nov 12 18:59:00 2001 +0000", "patch-2.4.15-pre4.gz", patch_base="2.4.14"),
    Version("2.4.15pre5", "2.4.15pre4", "Fri Nov 16 01:57:00 2001 +0000", "patch-2.4.15-pre5.gz", patch_base="2.4.14"),
    Version("2.4.15pre6", "2.4.15pre5", "Sun Nov 18 03:10:00 2001 +0000", "patch-2.4.15-pre6.gz", patch_base="2.4.14"),
    Version("2.4.15pre7", "2.4.15pre6", "Tue Nov 20 03:57:00 2001 +0000", "patch-2.4.15-pre7.gz", patch_base="2.4.14"),
    Version("2.4.15pre8", "2.4.15pre7", "Wed Nov 21 06:13:00 2001 +0000", "patch-2.4.15-pre8.gz", patch_base="2.4.14"),
    Version("2.4.15pre9", "2.4.15pre8", "Thu Nov 22 06:46:00 2001 +0000", "patch-2.4.15-pre9.gz", patch_base="2.4.14"),
    Version("2.4.15", "2.4.15pre9", "Fri Nov 23 06:18:00 2001 +0000"),
    # Real history: 2.5.1 forked from 2.4.15, and Linus' own tree (master)
    # moved on to 2.5 development from there -- 2.4.x stable maintenance
    # continues on its own branch from this point (matches the 1.0/1.1,
    # 2.0/2.1, 2.2/2.3 pattern elsewhere in this project).
    Version("2.4.16", "2.4.15", "Mon Nov 26 13:32:00 2001 +0000", branch_create="2.4", branch_checkout="2.4"),
    Version("2.4.17", "2.4.16", "Fri Dec 21 17:52:00 2001 +0000"),
    Version("2.4.18", "2.4.17", "Mon Feb 25 19:40:00 2002 +0000"),
    Version("2.4.19", "2.4.18", "Sat Aug  3 00:39:00 2002 +0000"),
    Version("2.4.20", "2.4.19", "Thu Nov 28 23:53:00 2002 +0000"),
    Version("2.4.21", "2.4.20", "Fri Jun 13 14:52:00 2003 +0000"),
    Version("2.4.22", "2.4.21", "Mon Aug 25 11:44:00 2003 +0000"),
    Version("2.4.23", "2.4.22", "Fri Nov 28 18:26:00 2003 +0000"),
    Version("2.4.24", "2.4.23", "Mon Jan  5 13:54:00 2004 +0000"),
    Version("2.4.25", "2.4.24", "Wed Feb 18 13:36:00 2004 +0000"),
    Version("2.4.26", "2.4.25", "Wed Apr 14 13:07:00 2004 +0000"),
    Version("2.4.27", "2.4.26", "Sat Aug  7 23:26:00 2004 +0000"),
    Version("2.4.28", "2.4.27", "Wed Nov 17 11:54:00 2004 +0000"),
    Version("2.4.29", "2.4.28", "Wed Jan 19 14:19:00 2005 +0000"),
    Version("2.4.30", "2.4.29", "Mon Apr  4 01:42:00 2005 +0000"),
    Version("2.4.31", "2.4.30", "Wed Jun  1 00:56:00 2005 +0000"),
    Version("2.4.32", "2.4.31", "Wed Nov 16 19:12:54 2005 +0000"),
    Version("2.4.33", "2.4.32", "Fri Aug 11 04:18:20 2006 +0000"),
    Version("2.4.33.1", "2.4.33", "Sat Aug 19 12:43:49 2006 +0000"),
    Version("2.4.33.2", "2.4.33.1", "Tue Aug 22 20:13:54 2006 +0000"),
    Version("2.4.33.3", "2.4.33.2", "Thu Aug 31 17:03:20 2006 +0000"),
    Version("2.4.33.4", "2.4.33.3", "Sun Nov 19 18:28:35 2006 +0000"),
    Version("2.4.33.5", "2.4.33.4", "Thu Dec 14 16:29:03 2006 +0000"),
    Version("2.4.33.6", "2.4.33.5", "Mon Dec 18 09:07:06 2006 +0000"),
    Version("2.4.33.7", "2.4.33.6", "Fri Dec 22 22:06:45 2006 +0000"),
    Version("2.4.34", "2.4.33.7", "Sat Dec 23 20:34:20 2006 +0000"),
    Version("2.4.34.1", "2.4.34", "Sat Feb  3 19:43:51 2007 +0000"),
    Version("2.4.34.2", "2.4.34.1", "Sat Mar 24 06:44:54 2007 +0000"),
    Version("2.4.34.3", "2.4.34.2", "Sun Apr 22 09:31:10 2007 +0000"),
    Version("2.4.34.4", "2.4.34.3", "Sun Apr 22 15:52:17 2007 +0000"),
    Version("2.4.34.5", "2.4.34.4", "Wed Jun  6 19:20:53 2007 +0000"),
    Version("2.4.34.6", "2.4.34.5", "Sun Jul 22 13:50:47 2007 +0000"),
    Version("2.4.35", "2.4.34.6", "Thu Jul 26 20:53:41 2007 +0000"),
    Version("2.4.35.1", "2.4.35", "Wed Aug 15 07:49:06 2007 +0000"),
    Version("2.4.35.2", "2.4.35.1", "Sat Sep  8 15:39:42 2007 +0000"),
    Version("2.4.35.3", "2.4.35.2", "Sun Sep 23 22:02:58 2007 +0000"),
]
# fmt: on


def changelog_path(v: Version) -> Path:
    return CHANGELOGS / f"{v.name}.txt"
