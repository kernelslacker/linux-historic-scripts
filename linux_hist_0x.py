"""Shared version table and helpers for untar-0.x.py / make-diffs-0.x.py / import-0.x.py."""

import dataclasses

from pathlib import Path

from linux_hist_common import CHANGELOGS, LINUS, ROOT  # noqa: F401 (re-exported)

BINARIES = ROOT / "binaries" / "0.x"


@dataclasses.dataclass
class Version:
    # fmt: off
    name: str
    base: str | None       # predecessor tree; None only for the very first version
    date: str              # git --date value for the import commit
    patch: str | None = None       # filename under BINARIES; None means "extract the tarball"
    compression: str = "bz2"       # bz2 -> bzcat, gz -> zcat (only meaningful when patch is set)
    fix_perms: bool = False        # 0.97's tarball had broken directory permissions
    # fmt: on


# fmt: off
VERSIONS: list[Version] = [
    Version("0.01", None, "Tue Sep 17 17:29:55 1991 +0000"),
    # Time-of-day from the earliest RCS checkin found inside the 0.10
    # tarball itself (RCS/Makefile,v) -- see dates/0.x.txt. The changelog
    # marks this date "???"; this is the best evidence available for it.
    Version("0.10", "0.01", "Mon Nov 11 20:03:45 1991 +0000"),
    Version("0.11", "0.10", "Sun Dec 8 12:00:00 1991 -0600"),
    Version("0.12", "0.11", "Wed Jan 15 12:00:00 1992 -0600"),
    Version("0.95", "0.12", "Sun Mar 8 12:00:00 1992 -0600"),
    Version("0.95a", "0.95", "Tue Mar 17 12:00:00 1992 -0600"),
    Version("0.95c+", "0.95a", "Thu Apr 9 11:00:00 1992 -0600"),
    Version("0.96a", "0.95c+", "Fri May 22 11:00:00 1992 -0600"),
    Version("0.96a-patch1", "0.96a", "Sun May 24 11:46:43 1992 -0600", "linux-0.96a.patch1.bz2"),
    Version("0.96a-patch2", "0.96a-patch1", "Wed May 27 17:09:23 1992 -0600", "linux-0.96a.patch2.bz2"),
    Version("0.96a-patch3", "0.96a-patch2", "Mon Jun 15 00:56:45 1992 -0600", "linux-0.96a.patch3.bz2"),
    Version("0.96a-patch4", "0.96a-patch3", "Wed Jun 17 20:57:52 1992 -0600", "linux-0.96a.patch4.bz2"),
    Version("0.96b", "0.96a-patch4", "Sun Jun 21 11:00:00 1992 -0600"),
    Version("0.96b-patch1", "0.96b", "Wed Jun 24 02:45:11 1992 -0600", "linux-0.96b.patch1.bz2"),
    Version("0.96b-patch2", "0.96b-patch1", "Fri Jun 26 15:42:35 1992 -0600", "linux-0.96b.patch2.bz2"),
    Version("0.96c", "0.96b-patch2", "Sat Jul 4 11:00:00 1992 -0600"),
    Version("0.96c-patch1", "0.96c", "Sat Jul 11 20:40:11 1992 -0600", "linux-0.96c.patch1.bz2"),
    Version("0.96c-patch2", "0.96c-patch1", "Sat Jul 18 20:54:48 1992 -0600", "linux-0.96c.patch2.bz2"),
    Version("0.96pre", "0.96c-patch2", "Tue Apr 21 11:00:00 1992 -0600"),
    Version("0.97", "0.96pre", "Sat Aug 1 11:00:00 1992 -0600", fix_perms=True),
    Version("0.97.1", "0.97", "Thu Aug 6 11:00:00 1992 -0600", "linux-0.97.patch1.gz", "gz"),
    Version("0.97.2", "0.97.1", "Sun Aug 23 11:00:00 1992 -0600", "linux-0.97.patch2.gz", "gz"),
    Version("0.97.3", "0.97.2", "Sat Sep 5 11:00:00 1992 -0600", "linux-0.97.patch3.gz", "gz"),
    Version("0.97.4", "0.97.3", "Mon Sep 7 11:00:00 1992 -0600", "linux-0.97.patch4.gz", "gz"),
    Version("0.97.5", "0.97.4", "Sat Sep 12 11:00:00 1992 -0600", "linux-0.97.patch5.gz", "gz"),
    # 0.97.6 has both a tarball and a patch6.gz upstream; NOTES says prefer the
    # tarball where one exists, so this intentionally isn't a Patch entry.
    Version("0.97.6", "0.97.5", "Sun Sep 20 11:00:00 1992 -0600"),
    Version("0.98", "0.97.6", "Tue Sep 29 11:00:00 1992 -0600"),
    Version("0.98.1", "0.98", "Mon Oct 5 11:00:00 1992 -0600"),
    Version("0.98.2", "0.98.1", "Sun Oct 18 11:00:00 1992 -0600"),
    Version("0.98.3", "0.98.2", "Tue Oct 27 12:00:00 1992 -0600"),
    Version("0.98.4", "0.98.3", "Mon Nov 9 12:00:00 1992 -0600"),
    Version("0.98.5", "0.98.4", "Sun Nov 15 12:00:00 1992 -0600"),
    Version("0.98.6", "0.98.5", "Wed Dec 2 12:00:00 1992 -0600"),
    Version("0.99", "0.98.6", "Sun Dec 13 12:00:00 1992 -0600"),
    Version("0.99.1", "0.99", "Mon Dec 21 12:00:00 1992 -0600"),
    Version("0.99.2", "0.99.1", "Fri Jan 1 12:00:00 1993 -0600"),
    Version("0.99.3", "0.99.2", "Wed Jan 13 12:00:00 1993 -0600"),
    Version("0.99.4", "0.99.3", "Wed Jan 20 12:00:00 1993 -0600"),
    Version("0.99.5", "0.99.4", "Tue Feb 9 12:00:00 1993 -0600"),
    Version("0.99.6", "0.99.5", "Sun Feb 21 12:00:00 1993 -0600"),
    Version("0.99.7", "0.99.6", "Sat Mar 13 12:00:00 1993 -0600"),
    Version("0.99.7A", "0.99.7", "Sun Mar 21 12:00:00 1993 -0600"),
    Version("0.99.8", "0.99.7A", "Thu Apr 8 11:00:00 1993 -0600"),
    Version("0.99.9", "0.99.8", "Fri Apr 23 11:00:00 1993 -0600"),
    Version("0.99.10", "0.99.9", "Mon Jun 7 11:00:00 1993 -0600"),
    Version("0.99.11", "0.99.10", "Sat Jul 17 11:00:00 1993 -0600"),
    Version("0.99.11-patch1", "0.99.11", "Mon Jul 19 12:25:58 1993 -0600", "0.99.11-patch1.diff.bz2"),
    Version("0.99.12", "0.99.11-patch1", "Sat Aug 15 11:00:00 1993 -0600"),
    Version("0.99.12-patch1", "0.99.12", "Wed Aug 18 09:50:58 1993 -0400", "0.99.12-patch1.diff.bz2"),
    Version("0.99.13", "0.99.12-patch1", "Sun Sep 19 11:00:00 1993 -0600"),
    Version("0.99.13k", "0.99.13", "Sun Sep 19 11:00:00 1993 -0600", "0.99.13k.diff.bz2"),
    Version("0.99.14", "0.99.13k", "Sun Nov 28 12:00:00 1993 -0600"),
    Version("0.99.14a", "0.99.14", "Fri Dec  3 12:00:00 1993 -0600"),
    Version("0.99.14b", "0.99.14a", "Thu Dec  9 12:00:00 1993 -0600"),
    Version("0.99.14c", "0.99.14b", "Fri Dec 10 12:00:00 1993 -0600"),
    Version("0.99.14d", "0.99.14c", "Mon Dec 13 12:00:00 1993 -0600"),
    Version("0.99.14e", "0.99.14d", "Tue Dec 14 12:00:00 1993 -0600"),
    Version("0.99.14f", "0.99.14e", "Thu Dec 16 12:00:00 1993 -0600"),
    Version("0.99.14g", "0.99.14f", "Thu Dec 23 12:00:00 1993 -0600"),
    Version("0.99.14h", "0.99.14g", "Mon Dec 27 12:00:00 1993 -0600"),
    Version("0.99.14i", "0.99.14h", "Thu Dec 30 12:00:00 1993 -0600"),
    Version("0.99.14j", "0.99.14i", "Fri Dec 31 12:00:00 1993 -0600"),
    Version("0.99.14k", "0.99.14j", "Mon Jan  3 12:00:00 1994 -0600"),
    Version("0.99.14l", "0.99.14k", "Tue Jan  4 12:00:00 1994 -0600"),
    Version("0.99.14m", "0.99.14l", "Wed Jan  5 12:00:00 1994 -0600"),
    Version("0.99.14n", "0.99.14m", "Fri Jan  7 12:00:00 1994 -0600"),
    Version("0.99.14o", "0.99.14n", "Sat Jan  8 12:00:00 1994 -0600"),
    Version("0.99.14p", "0.99.14o", "Thu Jan 13 12:00:00 1994 -0600"),
    Version("0.99.14q", "0.99.14p", "Mon Jan 17 12:00:00 1994 -0600"),
    Version("0.99.14r", "0.99.14q", "Tue Jan 18 12:00:00 1994 -0600"),
    Version("0.99.14s", "0.99.14r", "Wed Jan 19 12:00:00 1994 -0600"),
    Version("0.99.14t", "0.99.14s", "Fri Jan 21 12:00:00 1994 -0600"),
    Version("0.99.14u", "0.99.14t", "Tue Jan 25 12:00:00 1994 -0600"),
    Version("0.99.14v", "0.99.14u", "Wed Jan 26 12:00:00 1994 -0600"),
    Version("0.99.14w", "0.99.14v", "Thu Jan 27 12:00:00 1994 -0600"),
    Version("0.99.14x", "0.99.14w", "Fri Jan 29 12:00:00 1994 -0600"),
    Version("0.99.14y", "0.99.14x", "Wed Feb  2 12:00:00 1994 -0600"),
    Version("0.99.14z", "0.99.14y", "Wed Feb  2 12:00:00 1994 -0600"),
    Version("0.99.15", "0.99.14z", "Thu Feb  3 12:00:00 1994 -0600"),
    Version("0.99.15a", "0.99.15", "Mon Feb  7 12:00:00 1994 -0600"),
    Version("0.99.15b", "0.99.15a", "Wed Feb  9 12:00:00 1994 -0600"),
    Version("0.99.15c", "0.99.15b", "Sun Feb 13 12:00:00 1994 -0600"),
    Version("0.99.15d", "0.99.15c", "Mon Feb 14 12:00:00 1994 -0600"),
    Version("0.99.15e", "0.99.15d", "Wed Feb 16 12:00:00 1994 -0600"),
    Version("0.99.15f", "0.99.15e", "Fri Feb 18 12:00:00 1994 -0600"),
    Version("0.99.15g", "0.99.15f", "Mon Feb 21 12:00:00 1994 -0600"),
    Version("0.99.15h", "0.99.15g", "Tue Feb 22 12:00:00 1994 -0600"),
    Version("0.99.15i", "0.99.15h", "Tue Mar  1 12:00:00 1994 -0600"),
    Version("0.99.15j", "0.99.15i", "Wed Mar  2 12:00:00 1994 -0600"),
    Version("1.0pre1", "0.99.15j", "Sun Mar  6 16:14:51 1994 +0000", "1.0pre1.diff.bz2"),
    Version("1.0alpha", "1.0pre1", "Sun Mar 13 01:55:41 1994 +0200", "1.0alpha.diff.bz2"),
]
# fmt: on


def changelog_path(v: Version) -> Path:
    return CHANGELOGS / f"{v.name}.txt"
