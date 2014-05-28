#!/bin/bash
# Unpack 2.3
BRANCH=2.3
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

prepatch()
{
	for i in $(seq 1 $2)
	do
		echo Patching to 2.3.$1pre$i
		cp -rl linux-2.3.$(($1-1)) linux-2.3.$1pre$i
		cd linux-2.3.$1pre$i
		zcat $FROM/2.3/pre-patch-2.3.$1-$i.gz | patch -p1 -s
		cd ..
	done
}

untar 2.3.0
prepatch 1 4

for i in $(seq 1 3)
do
	untar 2.3.$i
done

prepatch 4 3
untar 2.3.4
untar 2.3.5

prepatch 6 2
untar 2.3.6

echo Patching to 2.3.7pre1
cp -rl linux-2.3.6 linux-2.3.7pre1
cd linux-2.3.7pre1
zcat $FROM/2.3/pre-patch-2.3.7-1-dangerous.gz | patch -p1 -s
cd ..
echo Patching to 2.3.7pre2
cp -rl linux-2.3.6 linux-2.3.7pre2
cd linux-2.3.7pre2
zcat $FROM/2.3/pre-patch-2.3.7-2-dangerous.gz | patch -p1 -s
cd ..
echo Patching to 2.3.7pre3
cp -rl linux-2.3.6 linux-2.3.7pre3
cd linux-2.3.7pre3
zcat $FROM/2.3/pre-patch-2.3.7-3-REALLY-DANGEROUS.gz | patch -p1 -s
cd ..
echo Patching to 2.3.7pre4
cp -rl linux-2.3.6 linux-2.3.7pre4
cd linux-2.3.7pre4
zcat $FROM/2.3/pre-patch-2.3.7-4-dagerous.gz | patch -p1 -s
cd ..
for i in $(seq 5 9)
do
	echo Patching to 2.3.7pre$i
	cp -rl linux-2.3.6 linux-2.3.7pre$i
	cd linux-2.3.7pre$i
	zcat $FROM/2.3/pre-patch-2.3.7-$i.gz | patch -p1 -s
	cd ..
done
untar 2.3.7
prepatch 8 3
untar 2.3.8
prepatch 9 5
echo Patching to 2.3.9pre7
cp -rl linux-2.3.8 linux-2.3.9pre7
cd linux-2.3.9pre7
zcat $FROM/2.3/pre-patch-2.3.9-7.gz | patch -p1 -s
cd ..
echo Patching to 2.3.9pre8
cp -rl linux-2.3.8 linux-2.3.9pre8
cd linux-2.3.9pre8
zcat $FROM/2.3/pre-patch-2.3.9-8.gz | patch -p1 -s
cd ..
untar 2.3.9
prepatch 10 5
untar 2.3.10
prepatch 11 1
for i in $(seq 3 8)
do
	echo Patching to 2.3.11pre$i
	cp -rl linux-2.3.10 linux-2.3.11pre$i
	cd linux-2.3.11pre$i
	zcat $FROM/2.3/pre-patch-2.3.11-$i.gz | patch -p1 -s
	cd ..
done
untar 2.3.11
prepatch 12 9
untar 2.3.12
prepatch 13 8
untar 2.3.13
prepatch 14 2
untar 2.3.14
prepatch 15 3
untar 2.3.15
prepatch 16 1
untar 2.3.16
prepatch 17 1
untar 2.3.17
prepatch 18 2
untar 2.3.18
prepatch 19 1
echo Patching to 2.3.19pre2
cp -rl linux-2.3.18 linux-2.3.19pre2
cd linux-2.3.19pre2
zcat $FROM/2.3/pre-patch-2.3.19-2-for-alan-only.gz | patch -p1 -s
cd ..
untar 2.3.19
prepatch 20 2
untar 2.3.20
echo Patching to 2.3.21pre1
cp -rl linux-2.3.20 linux-2.3.21pre1
cd linux-2.3.21pre1
zcat $FROM/2.3/pre-patch-2.3.21-1-for-alan-only.gz | patch -p1 -s
cd ..
untar 2.3.21
prepatch 22 3
untar 2.3.22
prepatch 23 6
untar 2.3.23
prepatch 24 3
untar 2.3.24
prepatch 25 3
untar 2.3.25
prepatch 26 3
untar 2.3.26
prepatch 27 6
untar 2.3.27
untar 2.3.28
prepatch 29 3
untar 2.3.29
prepatch 30 7
untar 2.3.30
prepatch 31 1
untar 2.3.31
prepatch 32 4
untar 2.3.32
untar 2.3.33
prepatch 34 3
untar 2.3.34
prepatch 35 4
echo Patching to 2.3.35pre6
cp -rl linux-2.3.34 linux-2.3.35pre6
cd linux-2.3.35pre6
zcat $FROM/2.3/pre-patch-2.3.35-6.gz | patch -p1 -s
cd ..
untar 2.3.35
prepatch 36 3
echo Patching to 2.3.36pre5
cp -rl linux-2.3.35 linux-2.3.36pre5
cd linux-2.3.36pre5
zcat $FROM/2.3/pre-patch-2.3.36-5.gz | patch -p1 -s
cd ..
echo Patching to 2.3.36pre6
cp -rl linux-2.3.35 linux-2.3.36pre6
cd linux-2.3.36pre6
zcat $FROM/2.3/pre-patch-2.3.36-6.gz | patch -p1 -s
cd ..
untar 2.3.36
untar 2.3.37
prepatch 38 1
untar 2.3.38
prepatch 39 2
untar 2.3.39
prepatch 40 4
echo Patching to 2.3.40pre5
cp -rl linux-2.3.39 linux-2.3.40pre5
cd linux-2.3.40pre5
zcat $FROM/2.3/pre-patch-2.3.40-5-for-al.gz | patch -p1 -s
cd ..
echo Patching to 2.3.40pre6
cp -rl linux-2.3.39 linux-2.3.40pre6
cd linux-2.3.40pre6
zcat $FROM/2.3/pre-patch-2.3.40-6.gz | patch -p1 -s
cd ..
untar 2.3.40
prepatch 41 4
untar 2.3.41
prepatch 42 1
untar 2.3.42
prepatch 43 8
untar 2.3.43
prepatch 44 10
untar 2.3.44
prepatch 45 2
untar 2.3.45
prepatch 46 5
untar 2.3.46
prepatch 47 8
untar 2.3.47
prepatch 48 4
untar 2.3.48
prepatch 49 2
untar 2.3.49
prepatch 50 3
untar 2.3.50
prepatch 51 3
untar 2.3.51
prepatch 52 3

untar 2.3.99-pre1

for i in $(seq 1 5)
do
	echo Patching to linux-2.3.99pre2-$i
	cp -rl linux-2.3.99-pre1 linux-2.3.99-pre2-$i
	cd linux-2.3.99-pre2-$i
	zcat $FROM/2.3/pre2-$i.gz | patch -p1 -s
	cd ..
done
untar 2.3.99-pre2
for i in $(seq 1 8)
do
	echo Patching to linux-2.3.99pre3-$i
	cp -rl linux-2.3.99-pre2 linux-2.3.99-pre3-$i
	cd linux-2.3.99-pre3-$i
	zcat $FROM/2.3/pre3-$i.gz | patch -p1 -s
	cd ..
done
untar 2.3.99-pre3
for i in $(seq 1 5)
do
	echo Patching to linux-2.3.99pre4-$i
	cp -rl linux-2.3.99-pre3 linux-2.3.99-pre4-$i
	cd linux-2.3.99-pre4-$i
	zcat $FROM/2.3/pre4-$i.gz | patch -p1 -s
	cd ..
done
untar 2.3.99-pre4
untar 2.3.99-pre5
for i in $(seq 1 7)
do
	echo Patching to linux-2.3.99pre6-$i
	cp -rl linux-2.3.99-pre5 linux-2.3.99-pre6-$i
	cd linux-2.3.99-pre6-$i
	zcat $FROM/2.3/pre6-$i.gz | patch -p1 -s
	cd ..
done
untar 2.3.99-pre6
for i in $(seq 1 9)
do
	echo Patching to linux-2.3.99pre7-$i
	cp -rl linux-2.3.99-pre6 linux-2.3.99-pre7-$i
	cd linux-2.3.99-pre7-$i
	zcat $FROM/2.3/pre7-$i.gz | patch -p1 -s
	cd ..
done
untar 2.3.99-pre7
untar 2.3.99-pre8
for i in $(seq 1 5)
do
	echo Patching to linux-2.3.99-pre9-$i
	cp -rl linux-2.3.99-pre8 linux-2.3.99-pre9-$i
	cd linux-2.3.99-pre9-$i
	zcat $FROM/2.3/pre9-$i.gz | patch -p1 -s
	cd ..
done
untar 2.3.99-pre9
for i in $(seq 1 3)
do
	echo Patching to linux-2.3.99pre10-$i
	cp -rl linux-2.3.99-pre9 linux-2.3.99-pre10-$i
	cd linux-2.3.99-pre10-$i
	zcat $FROM/2.3/pre10-$i.gz | patch -p1 -s
	cd ..
done

prepatch()
{
	for i in $(seq 1 $2)
	do
		echo Patching to 2.4.0test$1pre$i
		cp -rl linux-2.4.0-test$(($1-1)) linux-2.4.0-test$1pre$i
		cd linux-2.4.0-test$1pre$i
		zcat $FROM/2.3/test$1-pre$i.gz | patch -p1 -s
		cd ..
	done
}

untar 2.4.0-test1
prepatch 2 12
untar 2.4.0-test2
prepatch 3 9
untar 2.4.0-test3
prepatch 4 6
untar 2.4.0-test4
prepatch 5 6
untar 2.4.0-test5
prepatch 6 10
untar 2.4.0-test6
prepatch 7 7
untar 2.4.0-test7
prepatch 8 2
echo Patching to 2.4.0test8pre3
cp -rl linux-2.4.0-test7 linux-2.4.0-test8pre3
cd linux-2.4.0-test8pre3
zcat $FROM/2.3/test8-pre3.for-al-only.gz | patch -p1 -s
cd ..
for i in 4 5 6
do
	echo Patching to 2.4.0test8pre$i
	cp -rl linux-2.4.0-test7 linux-2.4.0-test8pre$i
	cd linux-2.4.0-test8pre$i
	zcat $FROM/2.3/test8-pre$i.gz | patch -p1 -s
	cd ..
done
untar 2.4.0-test8
prepatch 9 9
untar 2.4.0-test9
prepatch 10 7
untar 2.4.0-test10
prepatch 11 7
untar 2.4.0-test11
prepatch 12 8
untar 2.4.0-test12
prepatch 13 7

untar 2.4.0-prerelease

