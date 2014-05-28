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
	tar jxf $FROM/0.x/linux-$1.tar.bz2
	if [ -d linux ]; then
		mv linux linux-$1
	fi
}


for ver in 0.01 0.10 0.11 0.12 \
	0.95 0.95a 0.95c+ 0.96a
do
	untar $ver
done

# patches only for these releases.
# 0.96a.patch1,2,3,4
echo patching to 0.96a-patch1
cp -rl linux-0.96a linux-0.96a-patch1
cd linux-0.96a-patch1
bzcat $FROM/0.x/linux-0.96a.patch1.bz2 | patch -p1 -s
cd ..
echo patching to 0.96a-patch2
cp -rl linux-0.96a-patch1 linux-0.96a-patch2
cd linux-0.96a-patch2
bzcat $FROM/0.x/linux-0.96a.patch2.bz2 | patch -p1 -s
cd ..
echo patching to 0.96a-patch3
cp -rl linux-0.96a-patch2 linux-0.96a-patch3
cd linux-0.96a-patch3
bzcat $FROM/0.x/linux-0.96a.patch3.bz2 | patch -p1 -s
cd ..
echo patching to 0.96a-patch4
cp -rl linux-0.96a-patch3 linux-0.96a-patch4
cd linux-0.96a-patch4
bzcat $FROM/0.x/linux-0.96a.patch4.bz2 | patch -p1 -s
cd ..

untar 0.96b
echo patching to 0.96b-patch1
cp -rl linux-0.96b linux-0.96b-patch1
cd linux-0.96b-patch1
bzcat $FROM/0.x/linux-0.96b.patch1.bz2 | patch -p1 -s
cd ..
echo patching to 0.96b-patch2
cp -rl linux-0.96b-patch1 linux-0.96b-patch2
cd linux-0.96b-patch2
bzcat $FROM/0.x/linux-0.96b.patch2.bz2 | patch -p1 -s
cd ..

untar 0.96c
echo patching to 0.96c-patch1
cp -rl linux-0.96c linux-0.96c-patch1
cd linux-0.96c-patch1
bzcat $FROM/0.x/linux-0.96c.patch1.bz2 | patch -p1 -s
cd ..
echo patching to 0.96c-patch2
cp -rl linux-0.96c-patch1 linux-0.96c-patch2
cd linux-0.96c-patch2
bzcat $FROM/0.x/linux-0.96c.patch2.bz2 | patch -p1 -s
cd ..

untar 0.96pre

untar 0.97
# 0.97 had fucked up permissions.
find linux-0.97 -type d -exec chmod +x {} \;

# patches only for these releases.
# 0.97.1 0.97.2 0.97.3 0.97.4 0.97.5 0.97.6
echo patching to 0.97.1
cp -rl linux-0.97 linux-0.97.1
cd linux-0.97.1
zcat $FROM/0.x/linux-0.97.patch1.gz | patch -p1 -s
cd ..
echo patching to 0.97.2
cp -rl linux-0.97.1 linux-0.97.2
cd linux-0.97.2
zcat $FROM/0.x/linux-0.97.patch2.gz | patch -p1 -s
cd ..
echo patching to 0.97.3
cp -rl linux-0.97.2 linux-0.97.3
cd linux-0.97.3
zcat $FROM/0.x/linux-0.97.patch3.gz | patch -p1 -s
cd ..
echo patching to 0.97.4
cp -rl linux-0.97.3 linux-0.97.4
cd linux-0.97.4
zcat $FROM/0.x/linux-0.97.patch4.gz | patch -p1 -s
cd ..
echo patching to 0.97.5
cp -rl linux-0.97.4 linux-0.97.5
cd linux-0.97.5
zcat $FROM/0.x/linux-0.97.patch5.gz | patch -p1 -s
cd ..


for ver in 0.97.6 \
	0.98 0.98.1 0.98.2 0.98.3 0.98.4 0.98.5 0.98.6 \
	0.99 0.99.1 0.99.2 0.99.3 0.99.4 0.99.5 0.99.6 0.99.7 0.99.7A \
	0.99.8 0.99.9 0.99.10 0.99.11
do
	untar $ver
done

echo patching to 0.99.11-patch1
cp -rl linux-0.99.11 linux-0.99.11-patch1
cd linux-0.99.11-patch1
bzcat $FROM/0.x/0.99.11-patch1.diff.bz2 | patch -p1 -s
cd ..

untar 0.99.12
echo patching to 0.99.12-patch1
cp -rl linux-0.99.12 linux-0.99.12-patch1
cd linux-0.99.12-patch1
bzcat $FROM/0.x/0.99.12-patch1.diff.bz2 | patch -p1 -s
cd ..

untar 0.99.13
echo patching to 0.99.13k
cp -rl linux-0.99.13 linux-0.99.13k
cd linux-0.99.13k
bzcat $FROM/0.x/0.99.13k.diff.bz2 | patch -p1 -s
cd ..

for ver in 0.99.14 0.99.14a 0.99.14b 0.99.14c 0.99.14d 0.99.14e 0.99.14f 0.99.14g 0.99.14h 0.99.14i 0.99.14j 0.99.14k 0.99.14l \
	0.99.14m 0.99.14n 0.99.14o 0.99.14p 0.99.14q 0.99.14r 0.99.14s 0.99.14t 0.99.14u 0.99.14v 0.99.14w 0.99.14x \
	0.99.14y 0.99.14z \
	0.99.15 \
	0.99.15a 0.99.15b 0.99.15c 0.99.15d 0.99.15e 0.99.15f 0.99.15g 0.99.15h 0.99.15i 0.99.15j
do
	untar $ver
done


echo patching to 1.0pre1
cp -rl linux-0.99.15j linux-1.0pre1
cd linux-1.0pre1
bzcat $FROM/0.x/1.0pre1.diff.bz2 | patch -p1 -s
cd ..
echo patching to 1.0alpha
cp -rl linux-1.0pre1 linux-1.0alpha
cd linux-1.0alpha
bzcat $FROM/0.x/1.0alpha.diff.bz2 | patch -p1 -s
cd ..

