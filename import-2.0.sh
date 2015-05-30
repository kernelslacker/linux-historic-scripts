#!/bin/bash

import_2_0()
{
  import 2.0
  import 2.0.1  "Wed Jul  3 11:12:00 1996 +0000"
  import 2.0.2  "Fri Jul  5 11:59:00 1996 +0000"
  import 2.0.3  "Sat Jul  6 06:38:00 1996 +0000"
  import 2.0.4  "Mon Jul  8 08:39:00 1996 +0000"
  import 2.0.5  "Wed Jul 10 08:11:00 1996 +0000"
  import 2.0.6  "Fri Jul 12 05:30:00 1996 +0000"
  import 2.0.7  "Mon Jul 15 07:23:00 1996 +0000"
  import 2.0.8  "Sat Jul 20 02:29:00 1996 +0000"
  import 2.0.9  "Fri Jul 26 03:55:00 1996 +0000"
  import 2.0.10 "Sat Jul 27 06:31:00 1996 +0000"
  import 2.0.11 "Mon Aug  5 02:26:00 1996 +0000"
  import 2.0.12 "Fri Aug  9 09:43:00 1996 +0000"
  import 2.0.13 "Fri Aug 16 04:40:00 1996 +0000"
  import 2.0.14 "Tue Aug 20 11:20:00 1996 +0000"
  import 2.0.15 "Sun Aug 25 03:04:00 1996 +0000"
  import 2.0.16 "Sat Aug 31 13:53:00 1996 +0000"
  import 2.0.17 "Mon Sep  2 03:56:00 1996 +0000"
  import 2.0.18 "Thu Sep  5 08:45:00 1996 +0000"
  import 2.0.19 "Wed Sep 11 08:21:00 1996 +0000"
  import 2.0.20 "Fri Sep 13 08:46:00 1996 +0000"
  import 2.0.21 "Fri Sep 20 09:26:00 1996 +0000"

  # 2.0 branched to 2.1 at 2.0.21
  GIT_AUTHOR_EMAIL="alan@lxorguk.ukuu.org.uk"
  GIT_AUTHOR_NAME="Alan Cox"
  GIT_COMMITTER_EMAIL="alan@lxorguk.ukuu.org.uk"
  GIT_COMMITTER_NAME="Alan Cox"
  git branch 2.0
  git checkout 2.0

  import 2.0.22 "Tue Oct  8 12:51:00 1996 +0000"
  import 2.0.23 "Fri Oct 18 08:11:00 1996 +0000"
  import 2.0.24 "Tue Oct 29 22:00:00 1996 +0000"
  import 2.0.25 "Fri Nov  8 01:44:00 1996 +0000"
  import 2.0.26 "Fri Nov 22 05:13:00 1996 +0000"
  import 2.0.27 "Sun Dec  1 13:08:00 1996 +0000"
  import 2.0.28 "Tue Jan 14 07:21:00 1997 +0000"
  import 2.0.29 "Fri Feb  7 07:34:00 1997 +0000"
  import 2.0.30 "Tue Apr  8 12:14:00 1997 +0000"

  import 2.0.31pre1  "Sun Aug  3 15:40:59 1997 +0000"
  import 2.0.31pre2  "Mon Aug  4 15:41:59 1997 +0000"
  import 2.0.31pre3  "Mon Aug  4 17:35:57 1997 +0000"
  import 2.0.31pre4  "Mon Aug 11 13:42:11 1997 +0000"
  import 2.0.31pre5  "Tue Aug 12 14:47:16 1997 +0000"
  import 2.0.31pre6  "Thu Aug 14 11:19:48 1997 +0000"
  import 2.0.31pre7  "Sun Aug 17 13:35:10 1997 +0000"
  import 2.0.31pre8  "Sun Aug 31 08:49:57 1997 +0000"
  import 2.0.31pre9  "Fri Sep  5 20:43:59 1997 +0000"
  import 2.0.31pre10 "Tue Sep 23 21:04:20 1997 +0000"
  import 2.0.31      "Fri Oct 17 17:05:00 1997 +0000"

  # MISSING: 2.0.32pre3 2.0.32pre4
  import 2.0.32pre1 "Fri Nov  7 10:51:05 1997 +0000"
  import 2.0.32pre2 "Fri Nov  7 16:58:01 1997 +0000"
  import 2.0.32pre5 "Fri Nov 14 10:55:32 1997 +0000"
  import 2.0.32pre6 "Sun Nov 16 17:17:04 1997 +0000"
  import 2.0.32     "Mon Nov 17 21:25:00 1997 +0000"

  import 2.0.33pre1 "Tue Dec  2 14:18:13 1997 +0000"
  import 2.0.33pre2 "Thu Dec  4 13:13:23 1997 +0000"
  import 2.0.33pre3 "Wed Dec 10 18:21:47 1997 +0000"
  import 2.0.33     "Mon Dec 15 21:37:00 1997 +0000"

  # pre1 is lost
  import 2.0.34pre2   "Fri Jan 23 00:42:42 1998 +0000"
  import 2.0.34pre3   "Sat Jan 31 10:00:00 1998 +0000"
  import 2.0.34pre4   "Thu Mar 26 10:30:08 1998 +0000"
  import 2.0.34pre5   "Tue Mar 31 20:01:59 1998 +0000"
  import 2.0.34pre6   "Sat Apr  4 19:56:20 1998 +0000"
  import 2.0.34pre7   "Sun Apr  5 18:59:27 1998 +0000"
  import 2.0.34pre8   "Tue Apr 14 22:42:58 1998 +0000"
  import 2.0.34pre9   "Sun Apr 19 18:52:55 1998 +0000"
  import 2.0.34pre10  "Mon Apr 20 09:04:32 1998 +0000"
  import 2.0.34pre11b "Wed Apr 22 00:33:18 1998 +0000"
  # MISSING: pre12 is lost
  # BROKEN: pre13 and 14 don't apply
  import 2.0.34pre15  "Sun May 17 18:46:05 1998 +0000"
  import 2.0.34pre16  "Thu May 21 01:03:34 1998 +0000"
  # 2.0.34pre16 == 2.0.34
  #import 2.0.34
  git tag 2.0.34    #  "Wed Jun  3 18:31:00 1998 +0000"

  import 2.0.35pre1 "Sun Jun 21 19:54:01 1998 +0000"
  import 2.0.35pre2 "Mon Jun 29 17:46:22 1998 +0000"
  import 2.0.35pre3 "Tue Jun 30 18:03:32 1998 +0000"
  import 2.0.35pre4 "Wed Jul  1 16:24:11 1998 +0000"
  import 2.0.35pre5 "Thu Jul  2 13:08:48 1998 +0000"
  import 2.0.35pre6 "Thu Jul  9 15:26:44 1998 +0000"
  import 2.0.35pre7 "Sat Jul 11 15:09:43 1998 +0000"
  import 2.0.35pre8 "Mon Jul 13 09:51:38 1998 +0000"
  # pre9 just removed a patch, so we can't get the date from the diff.
  import 2.0.35pre9 "Mon Jul 13 09:51:38 1998 +0000"
  import 2.0.35     "Mon Jul 13 16:59:00 1998 +0000"

  import 2.0.36pre1  "Fri Jul 24 17:29:06 1998 +0000"
  import 2.0.36pre2  "Tue Aug  4 02:17:33 1998 +0000"
  import 2.0.36pre3  "Tue Aug 11 18:21:52 1998 +0000"
  import 2.0.36pre4  "Wed Aug 12 18:35:14 1998 +0000"
  import 2.0.36pre5  "Wed Aug 12 18:35:14 1998 +0000"
  import 2.0.36pre6  "Tue Aug 18 14:39:27 1998 +0000"
  import 2.0.36pre7  "Mon Aug 31 22:51:25 1998 +0000"
  import 2.0.36pre8  "Mon Sep  7 16:42:06 1998 +0000"
  import 2.0.36pre9  "Fri Sep 11 05:51:10 1998 +0000"
  import 2.0.36pre10 "Tue Sep 15 18:39:29 1998 +0000"
  import 2.0.36pre11 "Wed Sep 23 16:18:57 1998 +0000"
  import 2.0.36pre12 "Fri Sep 25 01:15:03 1998 +0000"
  import 2.0.36pre13 "Sun Oct  4 22:34:28 1998 +0000"
  import 2.0.36pre14 "Thu Oct  8 19:00:04 1998 +0000"
  import 2.0.36pre15 "Thu Oct 15 00:13:37 1998 +0000"
  import 2.0.36pre16 "Fri Oct 30 17:38:59 1998 +0000"
  import 2.0.36pre17 "Thu Nov  5 23:45:27 1998 +0000"
  import 2.0.36pre18 "Mon Nov  9 15:41:39 1998 +0000"
  import 2.0.36pre19 "Mon Nov  9 20:15:26 1998 +0000"
  import 2.0.36pre20 "Tue Nov 10 21:29:41 1998 +0000"
  import 2.0.36pre21 "Wed Nov 11 15:10:48 1998 +0000"
  import 2.0.36pre22 "Sat Nov 14 02:15:46 1998 +0000"
  # 2.0.36pre22 was released as 2.0.36 without change.
  git tag 2.0.36     # "Sun Nov 15 13:48:00 1998 +0000"

  # the dates in the patches are screwed. got them from the announce emails.
  import 2.0.37pre1  "Tue Dec  8 03:06:00 1998 +0000"
  import 2.0.37pre2  "Fri Dec 11 23:11:00 1998 +0000"
  import 2.0.37pre3  ""
  import 2.0.37pre4  ""
  import 2.0.37pre5  ""
  import 2.0.37pre6  ""
  import 2.0.37pre7  ""
  import 2.0.37pre8  ""
  import 2.0.37pre9  ""
  import 2.0.37pre10 ""
  import 2.0.37pre11 ""
  import 2.0.37pre12 ""
  import 2.0.37      "Sun Jun 13 14:01:00 1999 +0000"

  import 2.0.38pre1
  # 2.0.38pre1 == 2.0.38 final
  git tag 2.0.38 # "Wed Aug 25 18:08:00 1999 +0000"

  GIT_AUTHOR_EMAIL="tao@acc.umu.se"
  GIT_AUTHOR_NAME="David Weinehall"
  GIT_COMMITTER_EMAIL="tao@acc.umu.se"
  GIT_COMMITTER_NAME="David Weinehall"
  import 2.0.39pre1
  import 2.0.39pre2
  import 2.0.39pre3
  import 2.0.39pre4
  import 2.0.39pre5
  import 2.0.39pre6
  import 2.0.39pre7
  import 2.0.39pre8
  import 2.0.39 "Tue Jan 9 16:29:00 2001 +0000"

  import 2.0.40pre1
  import 2.0.40pre2
  import 2.0.40pre3
  import 2.0.40-rc1
  import 2.0.40-rc2
  import 2.0.40-rc3
  import 2.0.40-rc4
  import 2.0.40-rc5
  import 2.0.40-rc6
  import 2.0.40-rc7
  import 2.0.40-rc8
  import 2.0.40 "Sun Feb 8 02:13:00 2004 +0000"
}
