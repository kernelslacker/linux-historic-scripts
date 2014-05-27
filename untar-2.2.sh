#!/bin/bash
# Unpack 2.2
BRANCH=2.2

if [ ! -d unpack ]; then
  echo run from wrong dir.
  exit
else
  cd unpack
fi

untar()
{
	echo Unpacking $1
	tar zxf ../$BRANCH/linux-$1.tar.gz
	mv linux linux-$1
}

untar 2.2.0
untar 2.2.1

# 2.2.2
# MISSING: 2.2.2-pre3
for i in 1 2 4 5
do
	echo Patching to 2.2.2pre$i
	cp -rl linux-2.2.1 linux-2.2.2pre$i
	cd linux-2.2.2pre$i
	zcat ../../2.2/patch-2.2.2-pre$i.gz | patch -p1 -s
	cd ..
done
untar 2.2.2

# 2.2.3
for i in $(seq 1 3)
do
	echo Patching to 2.2.3pre$i
	cp -rl linux-2.2.2 linux-2.2.3pre$i
	cd linux-2.2.3pre$i
	zcat ../../2.2/patch-2.2.3-pre$i.gz | patch -p1 -s
	cd ..
done
untar 2.2.3

# 2.2.4
# MISSING 2.2.4-pre1 through pre3, and pre5
echo Patching to 2.2.4pre4
cp -rl linux-2.2.3 linux-2.2.4pre4
cd linux-2.2.4pre4
zcat ../../2.2/patch-2.2.4-pre4.gz | patch -p1 -s
cd ..
echo Patching to 2.2.4pre6
cp -rl linux-2.2.3 linux-2.2.4pre6
cd linux-2.2.4pre6
zcat ../../2.2/patch-2.2.4-pre6.gz | patch -p1 -s
cd ..
untar 2.2.4

# 2.2.5
echo Patching to 2.2.5pre1
cp -rl linux-2.2.4 linux-2.2.5pre1
cd linux-2.2.5pre1
zcat ../../2.2/patch-2.2.5-pre1.gz | patch -p1 -s
cd ..
echo Patching to 2.2.5pre2
cp -rl linux-2.2.4 linux-2.2.5pre2
cd linux-2.2.5pre2
zcat ../../2.2/patch-2.2.5-pre2.gz | patch -p1 -s
cd ..
untar 2.2.5

# 2.2.6
for i in $(seq 1 3)
do
	echo Patching to 2.2.6pre$i
	cp -rl linux-2.2.5 linux-2.2.6pre$i
	cd linux-2.2.6pre$i
	zcat ../../2.2/patch-2.2.6-pre$i.gz | patch -p1 -s
	cd ..
done
untar 2.2.6

# 2.2.7
for i in $(seq 1 4)
do
	echo Patching to 2.2.7pre$i
	cp -rl linux-2.2.6 linux-2.2.7pre$i
	cd linux-2.2.7pre$i
	zcat ../../2.2/patch-2.2.7-pre$i.gz | patch -p1 -s
	cd ..
done
untar 2.2.7

# 2.2.8
for i in $(seq 1 7)
do
	echo Patching to 2.2.8pre$i
	cp -rl linux-2.2.7 linux-2.2.8pre$i
	cd linux-2.2.8pre$i
	zcat ../../2.2/patch-2.2.8-pre$i.gz | patch -p1 -s
	cd ..
done
untar 2.2.8

untar 2.2.9

# 2.2.10
for i in $(seq 1 5)
do
	echo Patching to 2.2.10pre$i
	cp -rl linux-2.2.9 linux-2.2.10pre$i
	cd linux-2.2.10pre$i
	zcat ../../2.2/patch-2.2.10-pre$i.gz | patch -p1 -s
	cd ..
done
untar 2.2.10

# 2.2.11
echo Patching to 2.2.11pre1
cp -rl linux-2.2.10 linux-2.2.11pre1
cd linux-2.2.11pre1
zcat ../../2.2/patch-2.2.11-pre1.gz | patch -p1 -s
cd ..
echo Patching to 2.2.11pre2
cp -rl linux-2.2.10 linux-2.2.11pre2
cd linux-2.2.11pre2
zcat ../../2.2/patch-2.2.11-pre2.gz | patch -p1 -s
cd ..

for i in $(seq 3 7)
do
	echo Patching to 2.2.11pre$i
	cp -rl linux-2.2.11pre$(($i-1)) linux-2.2.11pre$i
	cd linux-2.2.11pre$i
	zcat ../../2.2/patch-2.2.11pre$(($i-1))-pre$i.gz | patch -p1 -s
	cd ..
done

untar 2.2.11

# 2.2.12
# MISSING: 2.2.12pre2
for i in 1 $(seq 3 8)
do
	echo Patching to 2.2.12pre$i
	cp -rl linux-2.2.11 linux-2.2.12pre$i
	cd linux-2.2.12pre$i
	zcat ../../2.2/patch-2.2.12-pre$i.gz | patch -p1 -s
	cd ..
done
untar 2.2.12

# 2.2.13
for i in $(seq 1 18)
do
	echo Patching to 2.2.13pre$i
	cp -rl linux-2.2.12 linux-2.2.13pre$i
	cd linux-2.2.13pre$i
	zcat ../../2.2/patch-2.2.13-pre$i.gz | patch -p1 -s
	cd ..
done
untar 2.2.13

# 2.2.14
for i in $(seq 1 18)
do
	echo Patching to 2.2.14pre$i
	cp -rl linux-2.2.13 linux-2.2.14pre$i
	cd linux-2.2.14pre$i
	zcat ../../2.2/pre-patch-2.2.14-$i.gz | patch -p1 -s
	cd ..
done
untar 2.2.14

# 2.2.15
for i in $(seq 1 19)
do
	echo Patching to 2.2.15pre$i
	cp -rl linux-2.2.14 linux-2.2.15pre$i
	cd linux-2.2.15pre$i
	zcat ../../2.2/pre-patch-2.2.15-$i.gz | patch -p1 -s
	cd ..
done
echo Patching to 2.2.15pre20
cp -rl linux-2.2.15pre19 linux-2.2.15pre20
cd linux-2.2.15pre20
zcat ../../2.2/pre-patch-2.2.15-19to20.gz | patch -p1 -s
cd ..
untar 2.2.15

# 2.2.16
# MISSING: /pre-patch-2.2.16-1
for i in $(seq 2 8)
do
	echo Patching to 2.2.16pre$i
	cp -rl linux-2.2.15 linux-2.2.16pre$i
	cd linux-2.2.16pre$i
	zcat ../../2.2/pre-patch-2.2.16-$i.gz | patch -p1 -s
	cd ..
done
untar 2.2.16

# 2.2.17
for i in $(seq 1 20)
do
	echo Patching to 2.2.17pre$i
	cp -rl linux-2.2.16 linux-2.2.17pre$i
	cd linux-2.2.17pre$i
	zcat ../../2.2/pre-patch-2.2.17-$i.gz | patch -p1 -s
	cd ..
done
untar 2.2.17

# 2.2.18
# Alan horked the beginning of this patchset. Its based on 2.2.17pre20
for i in $(seq 1 3)
do
	echo Patching to 2.2.18pre$i
	cp -rl linux-2.2.17pre20 linux-2.2.18pre$i
	cd linux-2.2.18pre$i
	zcat ../../2.2/pre-patch-2.2.18-$i.gz | patch -p1 -s
	cd ..
done
# pre-patch-2.2.18-4 had some i386 vmlinux.lds cruft in it which stopped it applying. Deleted.
# Same thing in pre-patch-2.2.18-26
for i in $(seq 4 27)
do
	echo Patching to 2.2.18pre$i
	cp -rl linux-2.2.17 linux-2.2.18pre$i
	cd linux-2.2.18pre$i
	zcat ../../2.2/pre-patch-2.2.18-$i.gz | patch -p1 -s
	cd ..
done
untar 2.2.18

# 2.2.19
for i in $(seq 1 18)
do
	echo Patching to 2.2.19pre$i
	cp -rl linux-2.2.18 linux-2.2.19pre$i
	cd linux-2.2.19pre$i
	zcat ../../2.2/pre-patch-2.2.19-$i.gz | patch -p1 -s
	cd ..
done
untar 2.2.19

# 2.2.20
# Another oddity.  pre-patch-2.2.20-4 adds a drivers/sound/ad1848.c
# which already exists. No diff, so deleted.
for i in $(seq 1 12)
do
	echo Patching to 2.2.20pre$i
	cp -rl linux-2.2.19 linux-2.2.20pre$i
	cd linux-2.2.20pre$i
	zcat ../../2.2/pre-patch-2.2.20-$i.gz | patch -p1 -s
	cd ..
done
untar 2.2.20

# 2.2.21
for i in $(seq 1 4)
do
	echo Patching to 2.2.21pre$i
	cp -rl linux-2.2.20 linux-2.2.21pre$i
	cd linux-2.2.21pre$i
	zcat ../../2.2/patch-2.2.21-pre$i.gz | patch -p1 -s
	cd ..
done
for i in $(seq 1 4)
do
	echo Patching to 2.2.21-rc$i
	cp -rl linux-2.2.20 linux-2.2.21-rc$i
	cd linux-2.2.21-rc$i
	zcat ../../2.2/patch-2.2.21-rc$i.gz | patch -p1 -s
	cd ..
done
untar 2.2.21

# 2.2.22
for i in $(seq 1 3)
do
	echo Patching to 2.2.22-rc$i
	cp -rl linux-2.2.21 linux-2.2.22-rc$i
	cd linux-2.2.22-rc$i
	zcat ../../2.2/patch-2.2.22-rc$i.gz | patch -p1 -s
	cd ..
done
untar 2.2.22

# 2.2.23
for i in $(seq 1 2)
do
	echo Patching to 2.2.23-rc$i
	cp -rl linux-2.2.22 linux-2.2.23-rc$i
	cd linux-2.2.23-rc$i
	zcat ../../2.2/patch-2.2.23-rc$i.gz | patch -p1 -s
	cd ..
done
untar 2.2.23

# 2.2.24
for i in $(seq 1 5)
do
	echo Patching to 2.2.24-rc$i
	cp -rl linux-2.2.23 linux-2.2.24-rc$i
	cd linux-2.2.24-rc$i
	zcat ../../2.2/patch-2.2.24-rc$i.gz | patch -p1 -s
	cd ..
done
untar 2.2.24

untar 2.2.25

echo Unpacking 2.2.26
tar zxf ../2.2/linux-2.2.26.tar.gz

for i in $(seq 1 2)
do
	echo Patching to 2.2.27pre$i
	cp -rl linux-2.2.26 linux-2.2.27pre$i
	cd linux-2.2.27pre$i
	zcat ../../2.2/patch-2.2.27-pre$i.gz | patch -p1 -s
	cd ..
done
for i in $(seq 1 2)
do
	echo Patching to 2.2.27-rc$i
	cp -rl linux-2.2.26 linux-2.2.27-rc$i
	cd linux-2.2.27-rc$i
	zcat ../../2.2/patch-2.2.27-rc$i.gz | patch -p1 -s
	cd ..
done

