#!/bin/bash
# 2.1.x
BRANCH=2.1

if [ ! -d unpack ]; then
  echo run from wrong dir.
  exit
else
  cd unpack
fi

untar()
{
	if [ -d linux-$1 ]; then
		echo $1 already exists, skipping.
	else
		echo Unpacking $1
		tar zxf ../$BRANCH/linux-$1.tar.gz
		mv linux linux-$1
	fi
}

series()
{
	for i in $(seq $1 $2)
	do
		untar 2.1.$i
	done
}

prepatch()
{
	for i in $(seq 1 $2)
	do
		echo Patching to 2.1.$1pre$i
		cp -rl linux-2.1.$(($1-1)) linux-2.1.$1pre$i
		cd linux-2.1.$1pre$i
		zcat ../../2.1/pre-patch-2.1.$1-$i.gz | patch -p1 -s
		cd ..
	done
}

series 0 22
prepatch 23 1
series 23 27
prepatch 28 1
series 28 35
prepatch 36 1
untar 2.1.36
prepatch 37 7
untar 2.1.37
prepatch 38 1
series 38 41

for i in 1 2
do
	echo Patching to 2.1.42pre$i
	cp -rl linux-2.1.41 linux-2.1.42pre$i
	cd linux-2.1.42pre$i
	# Dunno wtf these came from, but to make the patch apply, we need them.
	# (The patch deletes them).
	touch drivers/sound/.version.orig
	cat << EOF > drivers/sound/.version.orig
3.8-beta9
0x030803
EOF
	sync
	zcat ../../2.1/pre-patch-2.1.42-$i.gz | patch -p1 -s
	cd ..
done
untar 2.1.42
prepatch 43 1
untar 2.1.43

echo Patching to 2.1.44pre2
cp -rl linux-2.1.43 linux-2.1.44pre2
cd linux-2.1.44pre2
zcat ../../2.1/pre-patch-2.1.44-2.gz | patch -p1 -s
cd ..
echo Patching to 2.1.44pre3
cp -rl linux-2.1.43 linux-2.1.44pre3
cd linux-2.1.44pre3
zcat ../../2.1/pre-patch-2.1.44-3.gz | patch -p1 -s
cd ..

untar 2.1.44

prepatch 45 10
untar 2.1.45
prepatch 46 1
series 46 47

prepatch 48 4
untar 2.1.48
prepatch 49 1
untar 2.1.49
untar 2.1.50
prepatch 51 1
untar 2.1.51

# need 52pre1
#echo Patching to 2.1.52pre2
#cp -rl linux-2.1.51 linux-2.1.52pre2
#cd linux-2.1.52pre2
#zcat ../../2.1/pre-patch-2.1.52-2.gz | patch -p1 -s
#cd ..

series 52 54
prepatch 55 1
untar 2.1.55
prepatch 56 1
untar 2.1.56

series 57 67
prepatch 68 1
series 68 77

prepatch 78 3
untar 2.1.78

prepatch 79 1
untar 2.1.79
prepatch 80 4
untar 2.1.80
prepatch 81 1
untar 2.1.81
series 82 86
prepatch 87 1
untar 2.1.87
untar 2.1.88
prepatch 89 5
untar 2.1.89
prepatch 90 3
untar 2.1.90
prepatch 91 2
untar 2.1.91
prepatch 92 2
series 92 94
prepatch 95 1
untar 2.1.95
prepatch 96 1
series 96 98
prepatch 99 3
untar 2.1.99
prepatch 100 3
series 100 101
prepatch 102 2
series 102 103
prepatch 104 1
series 104 105
prepatch 106 1
untar 2.1.106
prepatch 107 2
untar 2.1.107
prepatch 108 1
untar 2.1.108
prepatch 109 2
untar 2.1.109
prepatch 110 3
untar 2.1.110
prepatch 111 1
untar 2.1.111
prepatch 112 2
series 112 114
prepatch 115 4
untar 2.1.115
prepatch 116 2
untar 2.1.116
prepatch 117 1
series 117 118
prepatch 119 1
untar 2.1.119
prepatch 120 3
untar 2.1.120
prepatch 121 1
untar 2.1.121
prepatch 122 3
untar 2.1.122
prepatch 123 3
untar 2.1.123
prepatch 124 2
untar 2.1.124
prepatch 125 2
untar 2.1.125
prepatch 126 2
untar 2.1.126

for i in 1 2 3 6 7
do
	echo Patching to 2.1.127pre$i
	cp -rl linux-2.1.126 linux-2.1.127pre$i
	cd linux-2.1.127pre$i
	zcat ../../2.1/pre-patch-2.1.127-$i.gz | patch -p1 -s
	cd ..
done
untar 2.1.127

prepatch 128 1
untar 2.1.128

prepatch 129 6
untar 2.1.129

echo Patching to 2.1.130pre2
cp -rl linux-2.1.129 linux-2.1.130pre2
cd linux-2.1.130pre2
zcat ../../2.1/pre-patch-2.1.130-2.gz | patch -p1 -s
cd ..
echo Patching to 2.1.130pre3
cp -rl linux-2.1.129 linux-2.1.130pre3
cd linux-2.1.130pre3
zcat ../../2.1/pre-patch-2.1.130-3.gz | patch -p1 -s
cd ..
untar 2.1.130

echo Patching to 2.1.131pre2
cp -rl linux-2.1.130 linux-2.1.131pre2
cd linux-2.1.131pre2
zcat ../../2.1/pre-patch-2.1.131-2.gz | patch -p1 -s
cd ..
echo Patching to 2.1.131pre3
cp -rl linux-2.1.130 linux-2.1.131pre3
cd linux-2.1.131pre3
zcat ../../2.1/pre-patch-2.1.131-3.gz | patch -p1 -s
cd ..
untar 2.1.131

prepatch 132 4
untar 2.1.132

for i in 1 3 4 5
do
	echo Patching to 2.1.133pre$i
	cp -rl linux-2.1.132 linux-2.1.133pre$i
	cd linux-2.1.133pre$i
	zcat ../../2.1/pre-patch-2.1.133-$i.gz | patch -p1 -s
	cd ..
done

for i in $(seq 1 9)
do
	untar 2.2.0pre$i
done

