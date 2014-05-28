#!/bin/bash

FROM=$(pwd)/binaries

if [ ! -d unpack ]; then
  echo run from wrong dir.
  exit
else
  cd unpack
fi

untar()
{
	echo Unpacking $1
	tar zxf $FROM/$BRANCH/linux-$1.tar.gz
	mv linux linux-$1
}
BRANCH=1.0

untar 1.0

echo patching to 1.0.1
cp -rl linux-1.0 linux-1.0.1
cd linux-1.0.1
cat $FROM/1.0/patch1 | patch -p1 -s
cd ..

for i in $(seq 2 9)
do
	echo patching to 1.0.$i
	cp -rl linux-1.0.$(($i-1)) linux-1.0.$i
	cd linux-1.0.$i
	cat $FROM/1.0/patch$i | patch -p1 -s
	cd ..
done

BRANCH=1.1
untar 1.1.0

echo patching to 1.1.1
cp -rl linux-1.1.0 linux-1.1.1
cd linux-1.1.1
cat $FROM/1.1/patch1 | patch -p1 -s
cd ..

for i in $(seq 2 12)
do
	echo patching to 1.1.$i
	cp -rl linux-1.1.$(($i-1)) linux-1.1.$i
	cd linux-1.1.$i
	cat $FROM/1.1/patch$i | patch -p1 -s
	cd ..
done

untar 1.1.13

for i in $(seq 14 22)
do
	echo patching to 1.1.$i
	cp -rl linux-1.1.$(($i-1)) linux-1.1.$i
	cd linux-1.1.$i
	cat $FROM/1.1/patch$i | patch -p1 -s
	cd ..
done

untar 1.1.23

for i in $(seq 24 28)
do
	echo patching to 1.1.$i
	cp -rl linux-1.1.$(($i-1)) linux-1.1.$i
	cd linux-1.1.$i
	cat $FROM/1.1/patch$i | patch -p1 -s
	cd ..
done

untar 1.1.29

for i in $(seq 30 32)
do
	echo patching to 1.1.$i
	cp -rl linux-1.1.$(($i-1)) linux-1.1.$i
	cd linux-1.1.$i
	cat $FROM/1.1/patch$i | patch -p1 -s
	cd ..
done

untar 1.1.33

echo patching to 1.1.34
cp -rl linux-1.1.33 linux-1.1.34
cd linux-1.1.34
cat $FROM/1.1/patch34 | patch -p1 -s
cd ..

untar 1.1.35

for i in $(seq 36 44)
do
	echo patching to 1.1.$i
	cp -rl linux-1.1.$(($i-1)) linux-1.1.$i
	cd linux-1.1.$i
	cat $FROM/1.1/patch$i | patch -p1 -s
	cd ..
done

untar 1.1.45

for i in $(seq 46 51)
do
	echo patching to 1.1.$i
	cp -rl linux-1.1.$(($i-1)) linux-1.1.$i
	cd linux-1.1.$i
	cat $FROM/1.1/patch$i | patch -p1 -s
	cd ..
done

untar 1.1.52

for i in $(seq 53 54)
do
	echo patching to 1.1.$i
	cp -rl linux-1.1.$(($i-1)) linux-1.1.$i
	cd linux-1.1.$i
	cat $FROM/1.1/patch$i | patch -p1 -s
	cd ..
done

for i in $(seq 55 58)
do
	echo patching to 1.1.$i
	cp -rl linux-1.1.$(($i-1)) linux-1.1.$i
	cd linux-1.1.$i
	cat $FROM/1.1/patch$i | patch -p1 -s
	cd ..
done

untar 1.1.59

for i in $(seq 60 62)
do
	echo patching to 1.1.$i
	cp -rl linux-1.1.$(($i-1)) linux-1.1.$i
	cd linux-1.1.$i
	cat $FROM/1.1/patch$i | patch -p1 -s
	cd ..
done

untar 1.1.63
untar 1.1.64

for i in $(seq 65 66)
do
	echo patching to 1.1.$i
	cp -rl linux-1.1.$(($i-1)) linux-1.1.$i
	cd linux-1.1.$i
	cat $FROM/1.1/patch$i | patch -p1 -s
	cd ..
done

untar 1.1.67

for i in $(seq 68 69)
do
	echo patching to 1.1.$i
	cp -rl linux-1.1.$(($i-1)) linux-1.1.$i
	cd linux-1.1.$i
	cat $FROM/1.1/patch$i | patch -p1 -s
	cd ..
done

untar 1.1.70
untar 1.1.71

echo patching to 1.1.72
cp -rl linux-1.1.71 linux-1.1.72
cd linux-1.1.72
cat $FROM/1.1/patch72 | patch -p1 -s
cd ..

for i in $(seq 73 76)
do
  untar 1.1.$i
done

echo patching to 1.1.77
cp -rl linux-1.1.76 linux-1.1.77
cd linux-1.1.77
chmod +w drivers/char/cyclades.c
cat $FROM/1.1/patch77 | patch -p1 -s
cd ..

for i in $(seq 78 95)
do
	untar 1.1.$i
done

BRANCH=1.2
for i in $(seq 0 13)
do
	untar 1.2.$i
done

BRANCH=1.3
untar 1.3.0

echo Patching to 1.3.1
cp -rl linux-1.3.0 linux-1.3.1
cd linux-1.3.1
cat $FROM/1.3/patch-1.3.1 | patch -p1 -s
cd ..

for i in $(seq 2 100)
do
	untar 1.3.$i
done

for i in $(seq 1 14)
do
	echo Unpacking pre2.0.$i
	tar zxf $FROM/1.3/linux-pre2.0.$i.tar.gz
	mv linux linux-pre2.0.$i
done

