#!/bin/bash

# First normalise the tarball filenames to make parsing easier.
if [ -f pre-0.96.tar.bz2 ]; then
	mv pre-0.96.tar.bz2 linux-0.96pre.tar.bz2
fi

# Seeing as we're renaming and unpacking, repack them as bzips to save some space.
for i in 0.99.1 0.99.2 0.99.3 0.99.4 0.99.5 0.99.6 0.99.7 0.99.7A 0.99.8 0.99.9 0.99.10
do
	if [ -f linux-$i.tar.z ]; then
		gzip -d linux-$i.tar.z
		bzip2 -9 linux-$i.tar
	fi
	if [ -f linux-$i.tar.Z ]; then
		gzip -d linux-$i.tar.Z
		bzip2 -9 linux-$i.tar
	fi
done

#
mkdir -p unpack

./untar-0.x.sh
./untar-1.x.sh
./untar-2.0.sh
./untar-2.1.sh
./untar-2.2.sh
./untar-2.3.sh

