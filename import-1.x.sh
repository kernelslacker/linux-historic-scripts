#!/bin/bash

import_1_x()
{
  import 1.0   "Sat Mar 12 12:00:00 1994 -0600"
  import 1.0.1 "Wed Mar 16 11:06:17 1994 +0000"
  import 1.0.2 "Fri Mar 18 10:31:01 1994 +0000"
  import 1.0.3 "Mon Mar 21 17:05:21 1994 +0000"
  import 1.0.4 "Tue Mar 22 16:54:31 1994 +0000"
  import 1.0.5 "Mon Mar 28 11:40:19 1994 +0000"
  import 1.0.6 "Sun Apr  3 14:43:03 1994 +0000"

  # 1.0 branched to 1.1 at 1.0.6
  git branch 1.0
  git checkout 1.0
  import 1.0.7 "Wed Apr  6 13:13:35 1994 +0000"
  import 1.0.8 "Thu Apr  7 08:36:20 1994 +0000"
  import 1.0.9 "Sun Apr 17 00:17:39 1994 +0000"

  # Now do 1.1
  git checkout master

  import 1.1.0  "Tue Apr  5 11:00:00 1994 -0600"
  import 1.1.1  "Thu Apr  7 08:15:17 1994 +0000"
  import 1.1.2  "Mon Apr 11 15:32:05 1994 +0000"
  import 1.1.3  "Wed Apr 13 11:35:38 1994 +0000"
  import 1.1.4  "Wed Apr 13 19:34:08 1994 +0000"
  import 1.1.5  "Fri Apr 15 02:23:51 1994 +0000"
  import 1.1.6  "Tue Apr 19 10:58:57 1994 +0000"
  import 1.1.7  "Tue Apr 19 22:20:38 1994 +0000"
  import 1.1.8  "Thu Apr 21 14:14:55 1994 +0000"
  import 1.1.9  "Mon Apr 25 21:27:48 1994 +0000"
  import 1.1.10 "Thu Apr 28 23:39:19 1994 +0000"
  import 1.1.11 "Mon May  2 19:07:32 1994 +0000"
  import 1.1.12 "Sat May  7 14:13:00 1994 +0000"
  import 1.1.13 "Mon May 23 11:53:54 1994 +0000"
  import 1.1.14 "Tue May 24 00:58:23 1994 +0000"
  import 1.1.15 "Wed May 25 16:27:36 1994 +0000"
  import 1.1.16 "Fri May 27 11:59:10 1994 +0000"
  import 1.1.17 "Tue May 31 12:43:17 1994 +0000"
  import 1.1.18 "Thu Jun  2 12:36:00 1994 +0000"
  import 1.1.19 "Thu Jun  9 18:48:56 1994 +0000"
  import 1.1.20 "Fri Jun 17 15:36:19 1994 +0000"
  import 1.1.21 "Tue Jun 21 14:10:14 1994 +0000"
  import 1.1.22 "Thu Jun 23 23:09:19 1994 +0000"
  import 1.1.23 "Mon Jun 27 17:32:02 1994 +0000"
  import 1.1.24 "Tue Jun 28 22:27:14 1994 +0000"
  import 1.1.25 "Thu Jul  7 21:26:55 1994 +0000"
  import 1.1.26 "Fri Jul  8 13:23:21 1994 +0000"
  import 1.1.27 "Sat Jul  9 11:56:20 1994 +0000"
  import 1.1.28 "Wed Jul 13 01:16:06 1994 +0000"
  import 1.1.29 "Thu Jul 14 10:55:24 1994 +0000"
  import 1.1.30 "Sun Jul 17 16:28:26 1994 +0000"
  import 1.1.31 "Mon Jul 18 22:51:14 1994 +0000"
  import 1.1.32 "Wed Jul 20 22:11:10 1994 +0000"
  import 1.1.33 "Thu Jul 21 15:10:42 1994 +0000"
  import 1.1.34 "Sat Jul 23 00:43:38 1994 +0000"
  import 1.1.35 "Sun Jul 24 22:27:55 1994 +0000"
  import 1.1.36 "Tue Jul 26 12:17:16 1994 +0000"
  import 1.1.37 "Fri Jul 29 15:25:33 1994 +0000"
  import 1.1.38 "Tue Aug  2 13:56:05 1994 +0000"
  import 1.1.39 "Thu Aug  4 08:47:27 1994 +0000"
  import 1.1.40 "Sat Aug  6 23:11:37 1994 +0000"
  import 1.1.41 "Sun Aug  7 16:08:48 1994 +0000"
  import 1.1.42 "Tue Aug  9 13:23:13 1994 +0000"
  import 1.1.43 "Thu Aug 11 11:56:27 1994 +0000"
  import 1.1.44 "Thu Aug 11 21:35:49 1994 +0000"
  import 1.1.45 "Mon Aug 15 15:15:50 1994 +0000"
  import 1.1.46 "Fri Aug 19 14:25:49 1994 +0000"
  import 1.1.47 "Mon Aug 22 10:29:24 1994 +0000"
  import 1.1.48 "Thu Aug 25 15:17:39 1994 +0000"
  import 1.1.49 "Tue Aug 30 08:16:13 1994 +0000"
  import 1.1.50 "Thu Sep  8 09:53:07 1994 +0000"
  import 1.1.51 "Sun Sep 18 05:48:30 1994 +0000"
  import 1.1.52 "Thu Oct  6 10:39:41 1994 +0000"
  import 1.1.53 "Mon Oct 10 12:05:29 1994 +0000"
  import 1.1.54 "Fri Oct 14 10:44:52 1994 +0000"
  import 1.1.55 "Thu Oct 20 09:54:33 1994 +0000"
  import 1.1.56 "Fri Oct 21 17:04:12 1994 +0000"
  import 1.1.57 "Mon Oct 24 09:12:28 1994 +0000"
  import 1.1.58 "Wed Oct 26 09:42:22 1994 +0000"
  import 1.1.59 "Fri Oct 28 12:54:44 1994 +0000"
  import 1.1.60 "Mon Oct 31 07:18:11 1994 +0000"
  import 1.1.61 "Wed Nov  2 13:47:52 1994 +0000"
  import 1.1.62 "Sun Nov  6 18:02:00 1994 +0000"
  import 1.1.63 "Mon Nov 14 12:04:03 1994 +0000"
  import 1.1.64 "Tue Nov 15 15:35:08 1994 +0000"
  import 1.1.65 "Mon Nov 21 13:31:41 1994 +0000"
  import 1.1.66 "Fri Nov 25 14:00:17 1994 +0000"
  import 1.1.67 "Mon Nov 28 13:38:20 1994 +0000"
  import 1.1.68 "Tue Nov 29 17:10:13 1994 +0000"
  import 1.1.69 "Thu Dec  1 12:41:29 1994 +0000"
  import 1.1.70 "Fri Dec  2 14:06:17 1994 +0000"
  import 1.1.71 "Mon Dec  5 00:07:40 1994 +0000"
  import 1.1.72 "Tue Dec  6 16:44:51 1994 +0000"
  import 1.1.73 "Thu Dec 15 09:22:01 1994 +0000"
  import 1.1.74 "Fri Dec 23 13:36:25 1994 +0000"
  import 1.1.75 "Thu Dec 29 12:19:40 1994 +0000"
  import 1.1.76 "Fri Dec 30 08:29:42 1994 +0000"
  import 1.1.77 "Sat Jan  7 13:51:26 1995 +0000"
  import 1.1.78 "Mon Jan  9 10:05:54 1995 +0000"
  import 1.1.79 "Wed Jan 11 11:41:04 1995 +0000"
  import 1.1.80 "Thu Jan 12 13:14:16 1995 +0000"
  import 1.1.81 "Fri Jan 13 13:35:12 1995 +0000"
  import 1.1.82 "Mon Jan 16 13:41:14 1995 +0000"
  import 1.1.83 "Wed Jan 18 23:33:09 1995 +0000"
  import 1.1.84 "Sun Jan 22 22:13:59 1995 +0000"
  import 1.1.85 "Mon Jan 23 23:53:10 1995 +0000"
  import 1.1.86 "Fri Jan 27 12:35:01 1995 +0000"
  import 1.1.87 "Mon Jan 30 06:51:02 1995 +0000"
  import 1.1.88 "Tue Jan 31 17:32:12 1995 +0000"
  import 1.1.89 "Sun Feb  5 14:48:46 1995 +0000"
  import 1.1.90 "Wed Feb  8 13:54:00 1995 +0000"
  import 1.1.91 "Sun Feb 12 21:15:05 1995 +0000"
  import 1.1.92 "Wed Feb 15 21:31:24 1995 +0000"
  import 1.1.93 "Mon Feb 20 10:57:10 1995 +0000"
  import 1.1.94 "Wed Feb 22 16:25:04 1995 +0000"
  import 1.1.95 "Mon Feb 27 11:16:24 1995 +0000"

  # Now do 1.2
  import 1.2.0  "Tue Mar  7 18:13:07 1995 +0200"
  import 1.2.1  "Fri Mar 17 14:31:51 1995 +0000"
  import 1.2.2  "Sun Mar 26 15:48:40 1995 +0000"
  import 1.2.3  "Sun Apr  2 10:21:20 1995 +0000"
  import 1.2.4  "Thu Apr  6 11:54:28 1995 +0000"
  import 1.2.5  "Wed Apr 12 21:24:17 1995 +0000"
  import 1.2.6  "Sun Apr 23 19:18:13 1995 +0000"
  import 1.2.7  "Sat Apr 29 10:20:21 1995 +0000"
  import 1.2.8  "Wed May  3 07:17:10 1995 +0000"
  import 1.2.9  "Thu Jun  1 11:53:40 1995 +0000"
  import 1.2.10 "Mon Jun 12 19:23:35 1995 +0000"

  # 1.2 branched to 1.3 at 1.2.10
  git branch 1.2
  git checkout 1.2
  import 1.2.11 "Mon Jun 26 16:17:56 1995 +0000"
  import 1.2.12 "Mon Jul 17 15:20:24 1995 +0000"
  import 1.2.13 "Thu Jul 27 09:08:11 1995 +0000"

  # Now do 1.3
  git checkout master

  import 1.3.0  "Sun Jun 11 11:00:00 1995 -0600"
  import 1.3.1  "Tue Jun 13 14:40:59 1995 +0000"
  import 1.3.2  "Fri Jun 16 21:43:32 1995 +0000"
  import 1.3.3  "Sun Jun 18 18:15:08 1995 +0000"
  import 1.3.4  "Mon Jun 26 16:18:15 1995 +0000"
  import 1.3.5  "Thu Jun 29 13:02:13 1995 +0000"
  import 1.3.6  "Fri Jun 30 15:30:56 1995 +0000"
  import 1.3.7  "Thu Jul  6 14:04:43 1995 +0000"
  import 1.3.8  "Fri Jul  7 13:17:32 1995 +0000"
  import 1.3.9  "Tue Jul 11 08:29:44 1995 +0000"
  import 1.3.10 "Thu Jul 13 13:09:52 1995 +0000"
  import 1.3.11 "Tue Jul 18 15:29:26 1995 +0000"
  import 1.3.12 "Tue Jul 25 10:39:23 1995 +0000"
  import 1.3.13 "Thu Jul 27 09:48:45 1995 +0000"
  import 1.3.14 "Mon Jul 31 14:44:46 1995 +0000"
  import 1.3.15 "Wed Aug  2 09:55:38 1995 +0000"
  import 1.3.16 "Tue Aug  8 11:38:33 1995 +0000"
  import 1.3.17 "Wed Aug  9 14:29:51 1995 +0000"
  import 1.3.18 "Sun Aug 13 14:04:58 1995 +0000"
  import 1.3.19 "Tue Aug 15 20:16:43 1995 +0000"
  import 1.3.20 "Wed Aug 16 15:22:59 1995 +0000"
  import 1.3.21 "Mon Aug 28 14:25:17 1995 +0000"
  import 1.3.22 "Fri Sep  1 16:32:40 1995 +0000"
  import 1.3.23 "Sun Sep  3 14:06:00 1995 +0000"
  import 1.3.24 "Tue Sep  5 14:16:35 1995 +0000"
  import 1.3.25 "Sat Sep  9 11:19:51 1995 +0000"
  import 1.3.26 "Wed Sep 13 12:30:48 1995 +0000"
  import 1.3.27 "Thu Sep 14 15:10:19 1995 +0000"
  import 1.3.28 "Mon Sep 18 13:31:14 1995 +0000"
  import 1.3.29 "Sat Sep 23 18:39:44 1995 +0000"
  import 1.3.30 "Wed Sep 27 14:07:00 1995 +0000"
  import 1.3.31 "Wed Oct  4 08:22:36 1995 +0000"
  import 1.3.32 "Fri Oct  6 12:28:09 1995 +0000"
  import 1.3.33 "Tue Oct 10 15:59:36 1995 +0000"
  import 1.3.34 "Fri Oct 13 11:03:11 1995 +0000"
  import 1.3.35 "Mon Oct 16 15:23:25 1995 +0000"
  import 1.3.36 "Mon Oct 23 11:08:50 1995 +0000"
  import 1.3.37 "Sat Oct 28 17:52:34 1995 +0000"
  import 1.3.38 "Tue Nov  7 20:10:17 1995 +0000"
  import 1.3.39 "Thu Nov  9 10:39:02 1995 +0000"
  import 1.3.40 "Sat Nov 11 15:04:32 1995 +0000"
  import 1.3.41 "Mon Nov 13 08:54:55 1995 +0000"
  import 1.3.42 "Thu Nov 16 09:28:19 1995 +0000"
  import 1.3.43 "Tue Nov 21 12:09:33 1995 +0000"
  import 1.3.44 "Sat Nov 25 18:23:09 1995 +0000"
  import 1.3.45 "Mon Nov 27 11:22:19 1995 +0000"
  import 1.3.46 "Mon Dec 11 11:34:40 1995 +0000"
  import 1.3.47 "Wed Dec 13 08:13:41 1995 +0000"
  import 1.3.48 "Sun Dec 17 11:17:20 1995 +0000"
  import 1.3.49 "Thu Dec 21 07:00:31 1995 +0000"
  import 1.3.50 "Sun Dec 24 11:49:14 1995 +0000"
  import 1.3.51 "Wed Dec 27 08:33:51 1995 +0000"
  import 1.3.52 "Fri Dec 29 16:21:49 1995 +0000"
  import 1.3.53 "Tue Jan  2 15:39:15 1996 +0000"
  import 1.3.54 "Thu Jan  4 20:26:25 1996 +0000"
  import 1.3.55 "Sat Jan  6 18:42:37 1996 +0000"
  import 1.3.56 "Mon Jan  8 13:09:54 1996 +0000"
  import 1.3.57 "Fri Jan 12 15:08:44 1996 +0000"
  import 1.3.58 "Thu Jan 18 10:35:20 1996 +0000"
  import 1.3.59 "Wed Jan 24 00:21:21 1996 +0000"
  import 1.3.60 "Wed Feb  7 14:04:11 1996 +0000"
  import 1.3.61 "Fri Feb  9 17:21:43 1996 +0000"
  import 1.3.62 "Sun Feb 11 14:52:58 1996 +0000"
  import 1.3.63 "Wed Feb 14 13:21:30 1996 +0000"
  import 1.3.64 "Thu Feb 15 14:55:36 1996 +0000"
  import 1.3.65 "Sat Feb 17 11:10:58 1996 +0000"
  import 1.3.66 "Sat Feb 17 17:42:52 1996 +0000"
  import 1.3.67 "Tue Feb 20 14:01:03 1996 +0000"
  import 1.3.68 "Thu Feb 22 16:50:46 1996 +0000"
  import 1.3.69 "Tue Feb 27 15:19:02 1996 +0000"
  import 1.3.70 "Fri Mar  1 10:38:34 1996 +0000"
  import 1.3.71 "Mon Mar  4 11:47:36 1996 +0000"
  import 1.3.72 "Fri Mar  8 16:28:42 1996 +0000"
  import 1.3.73 "Tue Mar 12 17:30:14 1996 +0000"
  import 1.3.74 "Thu Mar 14 17:06:09 1996 +0000"
  import 1.3.75 "Sat Mar 16 20:17:27 1996 +0000"
  import 1.3.76 "Tue Mar 19 15:06:27 1996 +0000"
  import 1.3.77 "Thu Mar 21 18:08:30 1996 +0000"
  import 1.3.78 "Mon Mar 25 11:56:11 1996 +0000"
  import 1.3.79 "Tue Mar 26 21:47:42 1996 +0000"
  import 1.3.80 "Thu Mar 28 16:14:59 1996 +0000"
  import 1.3.81 "Sat Mar 30 14:03:16 1996 +0000"
  import 1.3.82 "Tue Apr  2 12:28:47 1996 +0000"
  import 1.3.83 "Wed Apr  3 14:12:34 1996 +0000"
  import 1.3.84 "Thu Apr  4 17:05:01 1996 +0000"
  import 1.3.85 "Mon Apr  8 18:29:25 1996 +0000"
  import 1.3.86 "Wed Apr 10 16:46:03 1996 +0000"
  import 1.3.87 "Fri Apr 12 15:04:10 1996 +0000"
  import 1.3.88 "Sat Apr 13 14:33:07 1996 +0000"
  import 1.3.89 "Mon Apr 15 12:06:49 1996 +0000"
  import 1.3.90 "Tue Apr 16 17:21:57 1996 +0000"
  import 1.3.91 "Thu Apr 18 15:26:45 1996 +0000"
  import 1.3.92 "Sat Apr 20 21:35:21 1996 +0000"
  import 1.3.93 "Sun Apr 21 18:10:15 1996 +0000"
  import 1.3.94 "Mon Apr 22 15:48:38 1996 +0000"
  import 1.3.95 "Wed Apr 24 16:40:03 1996 +0000"
  import 1.3.96 "Sat Apr 27 15:10:26 1996 +0000"
  import 1.3.97 "Mon Apr 29 17:26:12 1996 +0000"
  import 1.3.98 "Fri May  3 11:00:00 1996 -0600"
  import 1.3.99 "Tue May  7 15:24:31 1996 +0000"
  import 1.3.100 "Thu May  9 11:00:00 1996 -0600"

  import pre2.0.1  "Sat May 11 11:00:00 1996 -0600"
  import pre2.0.2  "Sun May 12 09:15:33 1996 +0000"
  import pre2.0.3  "Mon May 13 15:31:18 1996 +0000"
  import pre2.0.4  "Tue May 14 13:46:36 1996 +0000"
  import pre2.0.5  "Fri May 17 15:24:15 1996 +0000"
  import pre2.0.6  "Sun May 19 17:02:31 1996 +0000"
  import pre2.0.7  "Tue May 21 14:43:55 1996 +0000"
  import pre2.0.8  "Mon May 27 15:47:32 1996 +0000"
  import pre2.0.9  "Wed May 29 18:47:38 1996 +0000"
  import pre2.0.10 "Fri May 31 16:47:46 1996 +0000"
  import pre2.0.11 "Mon Jun  3 16:19:44 1996 +0000"
  import pre2.0.12 "Tue Jun  4 16:53:05 1996 +0000"
  import pre2.0.13 "Thu Jun  6 16:39:31 1996 +0000"
  import pre2.0.14 "Thu Jun  6 22:23:08 1996 +0000"
}
