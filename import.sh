#!/bin/bash

FROM=$(pwd)

# defaults. Override where necessary.
linus()
{
  GIT_AUTHOR_EMAIL="torvalds@linuxfoundation.org"
  GIT_AUTHOR_NAME="Linus Torvalds"
  GIT_COMMITTER_EMAIL="torvalds@linuxfoundation.org"
  GIT_COMMITTER_NAME="Linus Torvalds"
}

import()
{
	VERSION=$1
	if [ ! -z "$2" ]; then
	  DATE=$2
	else
	  # This is just placeholder stuff until every import is annotated.
	  DATE=$(date -R --date='@700000000')
	fi
	echo importing $VERSION
	git apply --whitespace=nowarn $FROM/diffs/linux-$VERSION.diff
	if [ $? -ne "0" ]; then
		echo something bad happened.
		exit
	fi
	git add --all
	for i in $(git status | grep deleted: |sed s/#// | sed s/deleted://)
	do
		git rm --ignore-unmatch --quiet $i
	done
	find . -type f -empty -exec git rm -f "{}" \;

	git update-index --add
	git update-index --remove

	if [ -f $FROM/changelogs/$VERSION.txt ]; then
		git commit -F $FROM/changelogs/$VERSION.txt --date="$DATE"
	else
		git commit -m "Import $VERSION" --date="$DATE"
	fi

	git tag $VERSION
	echo
}

if [ ! -d unpack ]; then
  echo run from wrong dir.
  exit
else
  cd unpack
fi

# Set up the initial tree.
rm -rf linux-git
cp -rl linux-0.01 linux-git
cd linux-git
git init .
git add --all
git commit -a -F $FROM/changelogs/0.01.txt --date="Tue Sep 17 17:29:55 1991 +0000"


# Now start applying patches.
. $FROM/import-0.x.sh
. $FROM/import-1.x.sh
. $FROM/import-2.0.sh
. $FROM/import-2.1.sh
. $FROM/import-2.2.sh
. $FROM/import-2.3.sh
import_0_x
import_1_x
import_2_0
import_2_1
import_2_2
import_2_3
