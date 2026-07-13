#!/bin/bash
# Unpack 2.4
BRANCH=2.4
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
		echo Patching to 2.4.$1pre$i
		cp -rl linux-2.4.$(($1-1)) linux-2.4.$1pre$i
		cd linux-2.4.$1pre$i
		zcat $FROM/2.4/patch-2.4.$1-pre$i.gz | patch -p1 -s
		cd ..
	done
}

untar 2.4.0
prepatch 1 12

untar 2.4.1
prepatch 2 4

untar 2.4.2
prepatch 3 8

untar 2.4.3
prepatch 4 8

untar 2.4.4
prepatch 5 6

untar 2.4.5
prepatch 6 9

untar 2.4.6
prepatch 7 9

untar 2.4.7
prepatch 8 8

untar 2.4.8
prepatch 9 4

untar 2.4.9
prepatch 10 15

untar 2.4.10
prepatch 11 6

untar 2.4.11

untar 2.4.12
prepatch 13 6

untar 2.4.13
prepatch 14 8

untar 2.4.14
prepatch 15 9

untar 2.4.15

