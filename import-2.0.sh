#!/bin/bash

import_2_0()
{
  import 2.0
  for ver in $(seq 1 21)
  do
    import 2.0.$ver
  done

  # 2.0 branched to 2.1 at 2.0.21
  GIT_AUTHOR_EMAIL="alan@lxorguk.ukuu.org.uk"
  GIT_AUTHOR_NAME="Alan Cox"
  GIT_COMMITTER_EMAIL="alan@lxorguk.ukuu.org.uk"
  GIT_COMMITTER_NAME="Alan Cox"
  git branch 2.0
  git checkout 2.0
  for ver in $(seq 22 30)
  do
    import 2.0.$ver
  done

  import 2.0.31pre1

  for ver in $(seq 2 10)
  do
    import 2.0.31pre$ver
  done
  import 2.0.31

  # MISSING: 2.0.32pre3 2.0.32pre4
  import 2.0.32pre1 
  import 2.0.32pre2 
  import 2.0.32pre5 
  import 2.0.32pre6 
  import 2.0.32

  import 2.0.33pre1 
  import 2.0.33pre2 
  import 2.0.33pre3 
  import 2.0.33

  # BROKEN: pre13 and 14 don't apply
  for ver in $(seq 2 10) 11b $(seq 15 16)
  do
    import 2.0.34pre$ver
  done
  # 2.0.34pre16 == 2.0.34
  #import 2.0.34
  git tag 2.0.34

  for ver in $(seq 1 9)
  do
    import 2.0.35pre$ver
  done
  import 2.0.35

  for ver in $(seq 1 22)
  do
    import 2.0.36pre$ver
  done
  # 2.0.36pre22 was released as 2.0.36 without change.
  git tag 2.0.36

  for ver in $(seq 1 12)
  do
    import 2.0.37pre$ver
  done
  import 2.0.37

  import 2.0.38pre1
  # 2.0.38pre1 == 2.0.38 final
  git tag 2.0.38

  GIT_AUTHOR_EMAIL="tao@acc.umu.se"
  GIT_AUTHOR_NAME="David Weinehall"
  GIT_COMMITTER_EMAIL="tao@acc.umu.se"
  GIT_COMMITTER_NAME="David Weinehall"
  for ver in $(seq 1 8)
  do
    import 2.0.39pre$ver
  done
  import 2.0.39

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
  import 2.0.40
}
