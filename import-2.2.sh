#!/bin/bash

import_2_2()
{
  import 2.2.0
  import 2.2.1

  # 2.2.2
  import 2.2.2pre1 
  import 2.2.2pre2 
  import 2.2.2pre4 
  import 2.2.2pre5 
  import 2.2.2

  # 2.2.3
  import 2.2.3pre1 
  import 2.2.3pre2 
  import 2.2.3pre3 
  import 2.2.3

  # 2.2.4
  # MISSING: 2.2.4pre1 through pre3, and pre5
  import 2.2.4pre4 
  import 2.2.4pre6 
  import 2.2.4

  # 2.2.5
  import 2.2.5pre1 
  import 2.2.5pre2 
  import 2.2.5

  # 2.2.6
  import 2.2.6pre1 
  import 2.2.6pre2 
  import 2.2.6pre3 
  import 2.2.6

  # 2.2.7
  for ver in $(seq 1 4)
  do
    import 2.2.7pre$ver
  done
  import 2.2.7

  # 2.2.8
  for ver in $(seq 1 7)
  do
    import 2.2.8pre$ver
  done
  import 2.2.8

  # 2.2 branched to 2.3 at 2.2.8
  git branch 2.2
  git checkout 2.2

  import 2.2.9

  import 2.2.10pre1 
  import 2.2.10pre2 
  import 2.2.10pre3 
  import 2.2.10pre4 
  import 2.2.10pre5 
  import 2.2.10

  # Alan took over at 2.2.11pre
  GIT_AUTHOR_EMAIL="alan@lxorguk.ukuu.org.uk"
  GIT_AUTHOR_NAME="Alan Cox"
  GIT_COMMITTER_EMAIL="alan@lxorguk.ukuu.org.uk"
  GIT_COMMITTER_NAME="Alan Cox"

  for ver in $(seq 1 7)
  do
    import 2.2.11pre$ver
  done
  import 2.2.11

  # MISSING: 2.2.12pre2
  for ver in 1 $(seq 3 8)
  do
    import 2.2.12pre$ver
  done
  import 2.2.12

  for ver in $(seq 1 18)
  do
    import 2.2.13pre$ver
  done
  import 2.2.13

  for ver in $(seq 1 18)
  do
    import 2.2.14pre$ver
  done
  import 2.2.14

  for ver in $(seq 1 20)
  do
    import 2.2.15pre$ver
  done
  import 2.2.15

  # MISSING: linux-2.2.16pre1
  for ver in $(seq 2 8)
  do
    import 2.2.16pre$ver
  done
  import 2.2.16

  for ver in $(seq 1 20)
  do
    import 2.2.17pre$ver
  done
  import 2.2.17

  for ver in $(seq 1 26)
  do
    import 2.2.18pre$ver
  done
  # pre27 was pre26 with some binary files removed.
  # pre27 == final
  git tag 2.2.18pre27
  git tag 2.2.18

  for ver in $(seq 1 18)
  do
    import 2.2.19pre$ver
  done
  import 2.2.19

  for ver in $(seq 1 12)
  do
    import 2.2.20pre$ver
  done
  import 2.2.20

  for ver in $(seq 1 4)
  do
    import 2.2.21pre$ver
  done
  for ver in $(seq 1 4)
  do
    import 2.2.21-rc$ver
  done
  import 2.2.21

  for ver in $(seq 1 3)
  do
    import 2.2.22-rc$ver
  done
  import 2.2.22

  import 2.2.23-rc1
  import 2.2.23-rc2 
  import 2.2.23

  for ver in $(seq 1 5)
  do
    import 2.2.24-rc$ver
  done
  import 2.2.24
  import 2.2.25
  import 2.2.26
  import 2.2.27pre1 
  import 2.2.27pre2 
  import 2.2.27-rc1 
  import 2.2.27-rc2
}
