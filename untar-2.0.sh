#!/bin/bash
BRANCH=2.0

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

untar 2.0

for i in $(seq 1 30)
do
	untar 2.0.$i
done

# 2.0.31pre
for i in $(seq 1 10)
do
  echo Patching to 2.0.31pre$i
  cp -rl linux-2.0.30 linux-2.0.31pre$i
  cd linux-2.0.31pre$i
  zcat ../../2.0/patch-2.0.31-pre$i.gz | patch -p1 -s
  cd ..
done

untar 2.0.31

# 2.0.32pre
echo Patching to 2.0.32pre1
cp -rl linux-2.0.31 linux-2.0.32pre1
cd linux-2.0.32pre1
zcat ../../2.0/patch-2.0.32-pre1.gz | patch -p1 -s
cd ..
echo Patching to 2.0.32pre2
cp -rl linux-2.0.31 linux-2.0.32pre2
cd linux-2.0.32pre2
zcat ../../2.0/patch-2.0.32-pre2.gz | patch -p1 -s
cd ..
# MISSING: 2.0.32pre3 2.0.32pre4
echo Patching to 2.0.32pre5
cp -rl linux-2.0.31 linux-2.0.32pre5
cd linux-2.0.32pre5
zcat ../../2.0/patch-2.0.32-pre5.gz | patch -p1 -s
cd ..
echo Patching to 2.0.32pre6
cp -rl linux-2.0.31 linux-2.0.32pre6
cd linux-2.0.32pre6
zcat ../../2.0/patch-2.0.32-pre6.gz | patch -p1 -s
cd ..

untar 2.0.32

# 2.0.33
for i in $(seq 1 3)
do
  echo Patching to 2.0.33pre$i
  cp -rl linux-2.0.32 linux-2.0.33pre$i
  cd linux-2.0.33pre$i
  zcat ../../2.0/patch-2.0.33-pre$i.gz | patch -p1 -s
  cd ..
done

untar 2.0.33

# 2.0.34
# MISSING: 2.0.34-pre1
echo Patching to 2.0.34pre2
cp -rl linux-2.0.33 linux-2.0.34pre2
cd linux-2.0.34pre2
zcat ../../2.0/patch-2.0.34-pre2.gz | patch -p1 -s
cd ..
echo Patching to 2.0.34pre3
cp -rl linux-2.0.33 linux-2.0.34pre3
cd linux-2.0.34pre3
zcat ../../2.0/patch-2.0.34-pre3.gz | patch -p1 -s
cd ..
# MISSING: pre12
# BROKEN: pre13 and 14 don't apply.
for i in $(seq 4 10) 11b $(seq 15 16)
do
	echo Patching to 2.0.34pre$i
	cp -rl linux-2.0.33 linux-2.0.34pre$i
	cd linux-2.0.34pre$i
	zcat ../../2.0/patch-2.0.34pre$i.gz | patch -p1 -s
	cd ..
done

untar 2.0.34

# 2.0.35
for i in $(seq 1 9)
do
	echo Patching to 2.0.35pre$i
	cp -rl linux-2.0.34 linux-2.0.35pre$i
	cd linux-2.0.35pre$i
	zcat ../../2.0/2.0.35-pre-patch-$i.gz | patch -p1 -s
	cd ..
done

untar 2.0.35

# 2.0.36
for i in $(seq 1 22)
do
	echo Patching to 2.0.36pre$i
	cp -rl linux-2.0.35 linux-2.0.36pre$i
	cd linux-2.0.36pre$i
	zcat ../../2.0/2.0.36-pre-patch-$i.gz | patch -p1 -s
	cd ..
done

untar 2.0.36

# 2.0.37
for i in $(seq 1 12)
do
  echo Patching to 2.0.37pre$i
  cp -rl linux-2.0.36 linux-2.0.37pre$i
  cd linux-2.0.37pre$i
  zcat ../../2.0/patch-2.0.37-pre$i.gz | patch -p1 -s
  cd ..
done

untar 2.0.37

# 2.0.38
echo Patching to 2.0.38pre1
cp -rl linux-2.0.37 linux-2.0.38pre1
cd linux-2.0.38pre1
zcat ../../2.0/patch-2.0.38-pre1.gz | patch -p1 -s
cd ..

untar 2.0.38

# 2.0.39
for i in $(seq 1 8)
do
  echo Patching to 2.0.39pre$i
  cp -rl linux-2.0.38 linux-2.0.39pre$i
  cd linux-2.0.39pre$i
  zcat ../../2.0/patch-2.0.39-pre$i.gz | patch -p1 -s
  cd ..
done

untar 2.0.39

# 2.0.40
for i in $(seq 1 3)
do
  echo Patching to 2.0.40pre$i
  cp -rl linux-2.0.39 linux-2.0.40pre$i
  cd linux-2.0.40pre$i
  zcat ../../2.0/patch-2.0.40-pre$i.gz | patch -p1 -s
  cd ..
done
for i in $(seq 1 8)
do
  echo Patching to 2.0.40-rc$i
  cp -rl linux-2.0.39 linux-2.0.40-rc$i
  cd linux-2.0.40-rc$i
  zcat ../../2.0/patch-2.0.40-rc$i.gz | patch -p1 -s
  cd ..
done
echo Unpacking 2.0.40
tar zxf ../2.0/linux-2.0.40.tar.gz

