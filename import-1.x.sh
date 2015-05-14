#!/bin/bash

import_1_x()
{
  import 1.0 
  import 1.0.1 
  import 1.0.2 
  import 1.0.3 
  import 1.0.4 
  import 1.0.5 
  import 1.0.6 

  # 1.0 branched to 1.1 at 1.0.6
  git branch 1.0
  git checkout 1.0
  import 1.0.7
  import 1.0.8
  import 1.0.9

  # Now do 1.1
  git checkout master
  for ver in $(seq 0 95)
  do
    import 1.1.$ver
  done

  # Now do 1.2
  for ver in $(seq 0 10)
  do
    import 1.2.$ver
  done
  # 1.2 branched to 1.3 at 1.2.10
  git branch 1.2
  git checkout 1.2
  import 1.2.11
  import 1.2.12
  import 1.2.13

  # Now do 1.3
  git checkout master
  for ver in $(seq 0 100)
  do
    import 1.3.$ver
  done
  for ver in $(seq 1 14)
  do
    import pre2.0.$ver
  done
}
