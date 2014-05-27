#!/bin/bash

if [ ! -d unpack ]; then
  echo run from wrong dir.
  exit
else
  cd unpack
fi

GIT_AUTHOR_EMAIL="torvalds@linuxfoundation.org"
GIT_AUTHOR_NAME="Linus Torvalds"
GIT_COMMITTER_EMAIL="torvalds@linuxfoundation.org"
GIT_COMMITTER_NAME="Linus Torvalds"

rm -f ../changelogs/missing_changelogs.txt
if [ -d applied ]; then
	mv applied/* .
else
	mkdir -p applied
fi
cp -rl linux-0.01 linux-git
cd linux-git
git-init-db
find . -name .git -prune  -o -print | xargs git-add
git commit -a -F ../../changelogs/0.01.txt

import()
{
	echo importing $*
	git apply --whitespace=nowarn ../linux-$*.diff
	if [ $? -ne "0" ]; then
		echo something bad happened.
		exit
	fi
	find . -name .git -prune  -o -print | xargs git-add
	for i in $(git status | grep deleted: |sed s/#// | sed s/deleted://)
	do
		git-rm --quiet $i
	done

	git-update-index --add
	git-update-index --remove

	if [ -f ../../changelogs/$*.txt ]; then
		git commit -F ../../changelogs/$*.txt
		cp ../../changelogs/$*.txt ../applied/
	else
		echo $* >> ../../changelogs/missing_changelogs.txt
		git commit -m "Import $*"
	fi
	git tag $*
	mv ../linux-$*.diff ../applied/
	echo
}

importseries()
{
	for ver in $@
	do
		import $ver
	done
}


for ver in  0.10 0.11 0.12 \
	0.95 0.95a 0.95c+ \
	0.96a 0.96a-patch1 0.96a-patch2 0.96a-patch3 0.96a-patch4 0.96b 0.96b-patch1 0.96b-patch2 0.96c 0.96c-patch1 0.96c-patch2 0.96pre \
	0.97 0.97.1 0.97.2 0.97.3 0.97.4 0.97.5 0.97.6 \
	0.98 0.98.1 0.98.2 0.98.3 0.98.4 0.98.5 0.98.6 \
	0.99 0.99.1 0.99.2 0.99.3 0.99.4 0.99.5 0.99.6 0.99.7 0.99.7A 0.99.8 0.99.9 0.99.10 0.99.11 0.99.11-patch1 0.99.12 0.99.12-patch1 0.99.13 0.99.13k 0.99.14 \
	0.99.14a 0.99.14b 0.99.14c 0.99.14d 0.99.14e 0.99.14f 0.99.14g 0.99.14h 0.99.14i 0.99.14j 0.99.14k 0.99.14l 0.99.14m \
	0.99.14n 0.99.14o 0.99.14p 0.99.14q 0.99.14r 0.99.14s 0.99.14t 0.99.14u 0.99.14v 0.99.14w 0.99.14x 0.99.14y 0.99.14z \
	0.99.15 0.99.15a 0.99.15b 0.99.15c 0.99.15d 0.99.15e 0.99.15f 0.99.15g 0.99.15h 0.99.15i 0.99.15j 1.0pre1 1.0alpha \
	1.0 1.0.1 1.0.2 1.0.3 1.0.4 1.0.5 1.0.6
do
	import $ver
done

# 1.0 branched to 1.1 at 1.0.6
git branch 1.0
git checkout 1.0
importseries 1.0.7 1.0.8 1.0.9

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
importseries 1.2.11 1.2.12 1.2.13

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


# Now do 2.0
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
importseries 2.0.32pre1 2.0.32pre2 2.0.32pre5 2.0.32pre6 2.0.32

importseries 2.0.33pre1 2.0.33pre2 2.0.33pre3 2.0.33

# BROKEN: pre13 and 14 don't apply
for ver in $(seq 2 10) 11b $(seq 15 16)
do
	import 2.0.34pre$ver
done
# 2.0.34pre16 == 2.0.34
#import 2.0.34
git tag 2.0.34
mv linux-2.0.34.diff applied/

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
mv linux-2.0.36.diff applied/

for ver in $(seq 1 12)
do
	import 2.0.37pre$ver
done
import 2.0.37

import 2.0.38pre1
# 2.0.38pre1 == 2.0.38 final
git tag 2.0.38
mv linux-2.0.38.diff applied/

GIT_AUTHOR_EMAIL="tao@acc.umu.se"
GIT_AUTHOR_NAME="David Weinehall"
GIT_COMMITTER_EMAIL="tao@acc.umu.se"
GIT_COMMITTER_NAME="David Weinehall"
for ver in $(seq 1 8)
do
	import 2.0.39pre$ver
done
import 2.0.39

importseries 2.0.40pre1 2.0.40pre2 2.0.40pre3
for ver in $(seq 1 8)
do
	import 2.0.40-rc$ver
done
import 2.0.40


# Now do 2.1
GIT_AUTHOR_EMAIL="torvalds@linuxfoundation.org"
GIT_AUTHOR_NAME="Linus Torvalds"
GIT_COMMITTER_EMAIL="torvalds@linuxfoundation.org"
GIT_COMMITTER_NAME="Linus Torvalds"
git checkout master

for ver in $(seq 0 22)
do
	import 2.1.$ver
done
import 2.1.23pre1
import 2.1.23
import 2.1.24
import 2.1.25
import 2.1.26
import 2.1.27
importseries 2.1.28pre1 2.1.28
import 2.1.29
import 2.1.30
import 2.1.31
import 2.1.32
import 2.1.33
import 2.1.34
import 2.1.35
importseries 2.1.36pre1 2.1.36
importseries 2.1.37pre1 2.1.37pre2 2.1.37pre3 2.1.37pre4 2.1.37pre5 2.1.37pre6 2.1.37pre7 2.1.37
importseries 2.1.38pre1 2.1.38
import 2.1.39
import 2.1.40
import 2.1.41
importseries 2.1.42pre1 2.1.42pre2 2.1.42
importseries 2.1.43pre1 2.1.43
importseries 2.1.44pre2 2.1.44pre3 2.1.44
importseries 2.1.45pre1 2.1.45pre2 2.1.45pre3 2.1.45pre4 2.1.45pre5 2.1.45pre6 2.1.45pre7 2.1.45pre8 2.1.45pre9 2.1.45pre10 2.1.45
importseries 2.1.46pre1 2.1.46
import 2.1.47
importseries 2.1.48pre1 2.1.48pre2 2.1.48pre3 2.1.48pre4 2.1.48
importseries 2.1.49pre1 2.1.49
import 2.1.50
import 2.1.51pre1
import 2.1.51
#importseries 2.1.52pre1 2.1.52pre2
import 2.1.52
import 2.1.53
import 2.1.54
importseries 2.1.55pre1 2.1.55
importseries 2.1.56pre1 2.1.56
import 2.1.57
import 2.1.58
import 2.1.59
import 2.1.60
import 2.1.61
import 2.1.62
import 2.1.63
import 2.1.64
import 2.1.65
import 2.1.66
import 2.1.67
importseries 2.1.68pre1 2.1.68
import 2.1.69
import 2.1.70
import 2.1.71
import 2.1.72
import 2.1.73
import 2.1.74
import 2.1.75
import 2.1.76
import 2.1.77
importseries 2.1.78pre1 2.1.78pre2 2.1.78pre3 2.1.78
importseries 2.1.79pre1 2.1.79
importseries 2.1.80pre1 2.1.80pre2 2.1.80pre3 2.1.80pre4 2.1.80
importseries 2.1.81pre1 2.1.81
import 2.1.82
import 2.1.83
import 2.1.84
import 2.1.85
import 2.1.86
importseries 2.1.87pre1 2.1.87
import 2.1.88
importseries 2.1.89pre1 2.1.89pre2 2.1.89pre3 2.1.89pre4 2.1.89pre5 2.1.89
importseries 2.1.90pre1 2.1.90pre2 2.1.90pre3 2.1.90
importseries 2.1.91pre1 2.1.91pre2 2.1.91
importseries 2.1.92pre1 2.1.92pre2 2.1.92
import 2.1.93
import 2.1.94
importseries 2.1.95pre1 2.1.95
importseries 2.1.96pre1 2.1.96
import 2.1.97
import 2.1.98
importseries 2.1.99pre1 2.1.99pre2 2.1.99pre3 2.1.99
importseries 2.1.100pre1 2.1.100pre2 2.1.100pre3 2.1.100
import 2.1.101
importseries 2.1.102pre1 2.1.102pre2 2.1.102
import 2.1.103
importseries 2.1.104pre1 2.1.104
import 2.1.105
importseries 2.1.106pre1 2.1.106
importseries 2.1.107pre1 2.1.107pre2 2.1.107
importseries 2.1.108pre1 2.1.108
importseries 2.1.109pre1 2.1.109pre2 2.1.109
importseries 2.1.110pre1 2.1.110pre2 2.1.110pre3 2.1.110
importseries 2.1.111pre1 2.1.111
importseries 2.1.112pre1 2.1.112pre2 2.1.112
import 2.1.113
import 2.1.114
importseries 2.1.115pre1 2.1.115pre2 2.1.115pre3 2.1.115pre4 2.1.115
importseries 2.1.116pre1 2.1.116pre2 2.1.116
importseries 2.1.117pre1 2.1.117
import 2.1.118
importseries 2.1.119pre1 2.1.119
importseries 2.1.120pre1 2.1.120pre2 2.1.120pre3 2.1.120
importseries 2.1.121pre1 2.1.121
importseries 2.1.122pre1 2.1.122pre2 2.1.122pre3 2.1.122
importseries 2.1.123pre1 2.1.123pre2 2.1.123pre3 2.1.123
importseries 2.1.124pre1 2.1.124pre2 2.1.124
importseries 2.1.125pre1 2.1.125pre2 2.1.125
importseries 2.1.126pre1 2.1.126pre2 2.1.126
importseries 2.1.127pre1 2.1.127pre2 2.1.127pre3 2.1.127pre6 2.1.127pre7 2.1.127
importseries 2.1.128pre1 2.1.128
importseries 2.1.129pre1 2.1.129pre2 2.1.129pre3 2.1.129pre4 2.1.129pre5 2.1.129pre6 2.1.129
importseries 2.1.130pre2 2.1.130pre3 2.1.130
importseries 2.1.131pre2 2.1.131pre3 2.1.131
importseries 2.1.132pre1 2.1.132pre2 2.1.132pre3 2.1.132pre4 2.1.132
importseries 2.1.133pre1 2.1.133pre3 2.1.133pre4 2.1.133pre5
importseries 2.2.0pre1 2.2.0pre2 2.2.0pre3 2.2.0pre4 2.2.0pre5 2.2.0pre6 2.2.0pre7 2.2.0pre8 2.2.0pre9

# Now do 2.2

import 2.2.0
import 2.2.1

# 2.2.2
for ver in 2.2.2pre1 2.2.2pre2 2.2.2pre4 2.2.2pre5 2.2.2
do
	import $ver
done

# 2.2.3
importseries 2.2.3pre1 2.2.3pre2 2.2.3pre3 2.2.3

# 2.2.4
# MISSING: 2.2.4pre1 through pre3, and pre5
importseries 2.2.4pre4 2.2.4pre6 2.2.4

# 2.2.5
importseries 2.2.5pre1 2.2.5pre2 2.2.5

# 2.2.6
importseries 2.2.6pre1 2.2.6pre2 2.2.6pre3 2.2.6

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


importseries 2.2.10pre1 2.2.10pre2 2.2.10pre3 2.2.10pre4 2.2.10pre5 2.2.10

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
# git27 was git26 with some binary files removed.
# git27 == final
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

importseries 2.2.23-rc1 2.2.23-rc2 2.2.23

for ver in $(seq 1 5)
do
	import 2.2.24-rc$ver
done
import 2.2.24
import 2.2.25
import 2.2.26
importseries 2.2.27pre1 2.2.27pre2 2.2.27-rc1 2.2.27-rc2

# Now do 2.3
GIT_AUTHOR_EMAIL="torvalds@linuxfoundation.org"
GIT_AUTHOR_NAME="Linus Torvalds"
GIT_COMMITTER_EMAIL="torvalds@linuxfoundation.org"
GIT_COMMITTER_NAME="Linus Torvalds"
git checkout master

import 2.3.0
import 2.3.1pre1
import 2.3.1pre2
import 2.3.1pre3
import 2.3.1pre4
import 2.3.1
import 2.3.2
import 2.3.3
import 2.3.4pre1
import 2.3.4pre2
import 2.3.4pre3
import 2.3.4
import 2.3.5
import 2.3.6pre1
import 2.3.6pre2
import 2.3.6
import 2.3.7pre1
import 2.3.7pre2
import 2.3.7pre3
import 2.3.7pre4
import 2.3.7pre5
import 2.3.7pre6
import 2.3.7pre7
import 2.3.7pre8
import 2.3.7pre9
import 2.3.7
import 2.3.8pre1
import 2.3.8pre2
import 2.3.8pre3
# 2.3.8pre3 == final
git tag 2.3.8

import 2.3.9pre1
import 2.3.9pre2
import 2.3.9pre3
import 2.3.9pre4
import 2.3.9pre5
import 2.3.9pre7
import 2.3.9pre8
import 2.3.9

import 2.3.10pre1
import 2.3.10pre2
import 2.3.10pre3
import 2.3.10pre4
import 2.3.10pre5
import 2.3.10

import 2.3.11pre1
import 2.3.11pre3
import 2.3.11pre4
import 2.3.11pre5
import 2.3.11pre6
import 2.3.11pre7
import 2.3.11pre8
import 2.3.11

import 2.3.12pre1
import 2.3.12pre2
import 2.3.12pre3
import 2.3.12pre4
import 2.3.12pre5
import 2.3.12pre6
import 2.3.12pre7
import 2.3.12pre8
import 2.3.12pre9
import 2.3.12

import 2.3.13pre1
import 2.3.13pre2
import 2.3.13pre3
import 2.3.13pre4
import 2.3.13pre5
import 2.3.13pre6
import 2.3.13pre7
import 2.3.13pre8
import 2.3.13

import 2.3.14pre1
import 2.3.14pre2
import 2.3.14

import 2.3.15pre1
import 2.3.15pre2
import 2.3.15pre3
import 2.3.15

import 2.3.16pre1
import 2.3.16

import 2.3.17pre1
import 2.3.17

import 2.3.18pre1
import 2.3.18pre2
import 2.3.18

import 2.3.19pre1
import 2.3.19pre2
import 2.3.19

import 2.3.20pre1
import 2.3.20pre2
import 2.3.20

import 2.3.21pre1
import 2.3.21

import 2.3.22pre1
import 2.3.22pre2
import 2.3.22pre3
import 2.3.22

import 2.3.23pre1
import 2.3.23pre2
import 2.3.23pre3
import 2.3.23pre4
import 2.3.23pre5
import 2.3.23pre6
import 2.3.23

import 2.3.24pre1
import 2.3.24pre2
import 2.3.24pre3
import 2.3.24

import 2.3.25pre1
import 2.3.25pre2
import 2.3.25pre3
import 2.3.25

import 2.3.26pre1
import 2.3.26pre2
import 2.3.26pre3
import 2.3.26

import 2.3.27pre1
import 2.3.27pre2
import 2.3.27pre3
import 2.3.27pre4
import 2.3.27pre5
import 2.3.27pre6
import 2.3.27

import 2.3.28

import 2.3.29pre1
import 2.3.29pre2
import 2.3.29pre3
import 2.3.29

import 2.3.30pre1
import 2.3.30pre2
import 2.3.30pre3
import 2.3.30pre4
import 2.3.30pre5
import 2.3.30pre6
import 2.3.30pre7
import 2.3.30

import 2.3.31pre1
import 2.3.31

import 2.3.32pre1
import 2.3.32pre2
import 2.3.32pre3
import 2.3.32pre4
import 2.3.32

import 2.3.33

import 2.3.34pre1
import 2.3.34pre2
import 2.3.34pre3
import 2.3.34

import 2.3.35pre1
import 2.3.35pre2
import 2.3.35pre3
import 2.3.35pre4
import 2.3.35pre6
import 2.3.35

import 2.3.36pre1
import 2.3.36pre2
import 2.3.36pre3
import 2.3.36pre5
import 2.3.36pre6
import 2.3.36

import 2.3.37

import 2.3.38pre1
import 2.3.38

import 2.3.39pre1
import 2.3.39pre2
import 2.3.39

import 2.3.40pre1
import 2.3.40pre2
import 2.3.40pre3
import 2.3.40pre4
import 2.3.40pre5
import 2.3.40pre6
import 2.3.40

import 2.3.41pre1
import 2.3.41pre2
import 2.3.41pre3
import 2.3.41pre4
import 2.3.41

import 2.3.42pre1
import 2.3.42

import 2.3.43pre1
import 2.3.43pre2
import 2.3.43pre3
import 2.3.43pre4
import 2.3.43pre5
import 2.3.43pre6
import 2.3.43pre7
import 2.3.43pre8
import 2.3.43

import 2.3.44pre1
import 2.3.44pre2
import 2.3.44pre3
import 2.3.44pre4
import 2.3.44pre5
import 2.3.44pre6
import 2.3.44pre7
import 2.3.44pre8
import 2.3.44pre9
import 2.3.44pre10
import 2.3.44

import 2.3.45pre1
import 2.3.45pre2
import 2.3.45

import 2.3.46pre1
import 2.3.46pre2
import 2.3.46pre3
import 2.3.46pre4
import 2.3.46pre5
import 2.3.46

import 2.3.47pre1
import 2.3.47pre2
import 2.3.47pre3
import 2.3.47pre4
import 2.3.47pre5
import 2.3.47pre6
import 2.3.47pre7
import 2.3.47pre8
import 2.3.47

import 2.3.48pre1
import 2.3.48pre2
import 2.3.48pre3
import 2.3.48pre4
import 2.3.48

import 2.3.49pre1
import 2.3.49pre2
import 2.3.49

import 2.3.50pre1
import 2.3.50pre2
import 2.3.50pre3
import 2.3.50

import 2.3.51pre1
import 2.3.51pre2
import 2.3.51pre3
import 2.3.51

import 2.3.52pre1
import 2.3.52pre2
import 2.3.52pre3

import 2.3.99pre1

import 2.3.99pre2-1
import 2.3.99pre2-2
import 2.3.99pre2-3
import 2.3.99pre2-4
import 2.3.99pre2-5
import 2.3.99pre2

import 2.3.99pre3-1
import 2.3.99pre3-2
import 2.3.99pre3-3
import 2.3.99pre3-4
import 2.3.99pre3-5
import 2.3.99pre3-6
import 2.3.99pre3-7
import 2.3.99pre3-8
import 2.3.99pre3

import 2.3.99pre4-1
import 2.3.99pre4-2
import 2.3.99pre4-3
import 2.3.99pre4-4
import 2.3.99pre4-5
import 2.3.99pre4

import 2.3.99pre5

import 2.3.99pre6-1
import 2.3.99pre6-2
import 2.3.99pre6-3
import 2.3.99pre6-4
import 2.3.99pre6-5
import 2.3.99pre6-6
import 2.3.99pre6-7
import 2.3.99pre6

import 2.3.99pre7-1
import 2.3.99pre7-2
import 2.3.99pre7-3
import 2.3.99pre7-4
import 2.3.99pre7-5
import 2.3.99pre7-6
import 2.3.99pre7-7
import 2.3.99pre7-8
import 2.3.99pre7-9
import 2.3.99pre7

import 2.3.99pre8

import 2.3.99pre9-1
import 2.3.99pre9-2
import 2.3.99pre9-3
import 2.3.99pre9-4
import 2.3.99pre9-5
import 2.3.99pre9

import 2.3.99pre10-1
import 2.3.99pre10-2
import 2.3.99pre10-3

import 2.4.0-test1

import 2.4.0-test2pre1
import 2.4.0-test2pre2
import 2.4.0-test2pre3
import 2.4.0-test2pre4
import 2.4.0-test2pre5
import 2.4.0-test2pre6
import 2.4.0-test2pre7
import 2.4.0-test2pre8
import 2.4.0-test2pre9
import 2.4.0-test2pre10
import 2.4.0-test2pre11
import 2.4.0-test2pre12
import 2.4.0-test2

import 2.4.0-test3pre1
import 2.4.0-test3pre2
import 2.4.0-test3pre3
import 2.4.0-test3pre4
import 2.4.0-test3pre5
import 2.4.0-test3pre6
import 2.4.0-test3pre7
import 2.4.0-test3pre8
import 2.4.0-test3pre9
# pre9 == test3
git tag 2.4.0-test3

import 2.4.0-test4pre1
import 2.4.0-test4pre2
import 2.4.0-test4pre3
import 2.4.0-test4pre4
import 2.4.0-test4pre5
import 2.4.0-test4pre6
import 2.4.0-test4

import 2.4.0-test5pre1
import 2.4.0-test5pre2
import 2.4.0-test5pre3
import 2.4.0-test5pre4
import 2.4.0-test5pre5
import 2.4.0-test5pre6
import 2.4.0-test5

import 2.4.0-test6pre1
import 2.4.0-test6pre2
import 2.4.0-test6pre3
import 2.4.0-test6pre4
import 2.4.0-test6pre5
import 2.4.0-test6pre6
import 2.4.0-test6pre7
import 2.4.0-test6pre8
import 2.4.0-test6pre9
import 2.4.0-test6pre10
import 2.4.0-test6

import 2.4.0-test7pre1
import 2.4.0-test7pre2
import 2.4.0-test7pre3
import 2.4.0-test7pre4
import 2.4.0-test7pre5
import 2.4.0-test7pre6
import 2.4.0-test7pre7
import 2.4.0-test7

import 2.4.0-test8pre1
import 2.4.0-test8pre2
import 2.4.0-test8pre3
import 2.4.0-test8pre4
import 2.4.0-test8pre5
import 2.4.0-test8pre6
import 2.4.0-test8

import 2.4.0-test9pre1
import 2.4.0-test9pre2
import 2.4.0-test9pre3
import 2.4.0-test9pre4
import 2.4.0-test9pre5
import 2.4.0-test9pre6
import 2.4.0-test9pre7
import 2.4.0-test9pre8
import 2.4.0-test9pre9
import 2.4.0-test9

import 2.4.0-test10pre1
import 2.4.0-test10pre2
import 2.4.0-test10pre3
import 2.4.0-test10pre4
import 2.4.0-test10pre5
import 2.4.0-test10pre6
import 2.4.0-test10pre7
import 2.4.0-test10

import 2.4.0-test11pre1
import 2.4.0-test11pre2
import 2.4.0-test11pre3
import 2.4.0-test11pre4
import 2.4.0-test11pre5
import 2.4.0-test11pre6
import 2.4.0-test11pre7
import 2.4.0-test11

import 2.4.0-test12pre1
import 2.4.0-test12pre2
import 2.4.0-test12pre3
import 2.4.0-test12pre4
import 2.4.0-test12pre5
import 2.4.0-test12pre6
import 2.4.0-test12pre7
import 2.4.0-test12pre8
import 2.4.0-test12

import 2.4.0-test13pre1
import 2.4.0-test13pre2
import 2.4.0-test13pre3
import 2.4.0-test13pre4
import 2.4.0-test13pre5
import 2.4.0-test13pre6
import 2.4.0-test13pre7

import 2.4.0-prerelease

find .. -maxdepth 1 -type f -empty -name "*.diff" -exec rm {} \;
