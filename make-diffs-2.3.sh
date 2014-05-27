#!/bin/sh
# now do 2.3

diffseries()
{
	for i in $(seq $1 $2)
	do
		if [ ! -d linux-2.3.$(($i-1)) ]; then
			echo eek! no linux-2.3.$(($i-1))
			exit
		fi
		if [ ! -d linux-2.3.$i ]; then
			echo eek! no linux-2.3.$i
			exit
		fi
		echo diffing 2.3.$i
		#echo cmd: diff -urN linux-2.3.$(($i-1)) linux-2.3.$i \>linux-2.3.$i.diff
		diff -urN linux-2.3.$(($i-1)) linux-2.3.$i >linux-2.3.$i.diff
	done
}

onepre()
{
	if [ ! -d linux-2.3.$(($1-1)) ]; then
		echo eek! no linux-2.3.$(($1-1))
		exit
	fi
	if [ ! -d linux-2.3.$1pre1 ]; then
		echo eek! no linux-2.3.$1
		exit
	fi
	echo diffing 2.3.$1pre1
	diff -urN linux-2.3.$(($1-1)) linux-2.3.$1pre1 >linux-2.3.$1pre1.diff
	echo diffing 2.3.$1
	diff -urN linux-2.3.$1pre1 linux-2.3.$1 >linux-2.3.$1.diff
}

preseries()
{
	if [ ! -d linux-2.3.$(($1-1)) ]; then
		echo eek! no linux-2.3.$(($1-1))
		exit
	fi
	if [ ! -d linux-2.3.$1 ]; then
		echo eek! no linux-2.3.$1
		exit
	fi
	echo diffing 2.3.$1pre1
	diff -urN linux-2.3.$(($1-1)) linux-2.3.$1pre1 >linux-2.3.$1pre1.diff
	for i in $(seq 2 $2)
	do
		echo diffing 2.3.$1pre$i
		diff -urN linux-2.3.$1pre$(($i-1)) linux-2.3.$1pre$i >linux-2.3.$1pre$i.diff
	done
}
finaldiff()
{
	echo diffing 2.3.$1
	diff -urN linux-2.3.$1pre$2 linux-2.3.$1 >linux-2.3.$1.diff
}

echo diffing 2.3.0
diff -urN linux-2.2.8 linux-2.3.0 >linux-2.3.0.diff

preseries 1 4
finaldiff 1 4
diffseries 2 3
preseries 4 3
finaldiff 4 3
diffseries 5 5
preseries 6 2
finaldiff 6 2
preseries 7 9
finaldiff 7 9
preseries 8 3
finaldiff 8 3

preseries 9 5
echo diffing 2.3.9pre7
diff -urN linux-2.3.9pre5 linux-2.3.9pre7 >linux-2.3.9pre7.diff
echo diffing 2.3.9pre8
diff -urN linux-2.3.9pre7 linux-2.3.9pre8 >linux-2.3.9pre8.diff
finaldiff 9 8

preseries 10 5
finaldiff 10 5

preseries 11 1
echo diffing 2.3.11pre3
diff -urN linux-2.3.11pre1 linux-2.3.11pre3 >linux-2.3.11pre3.diff
for i in $(seq 4 8)
do
	echo diffing 2.3.11pre$i
	diff -urN linux-2.3.11pre$(($i-1)) linux-2.3.11pre$i >linux-2.3.11pre$i.diff
done
finaldiff 11 8

preseries 12 9
finaldiff 12 9
preseries 13 8
finaldiff 13 8
preseries 14 2
finaldiff 14 2
preseries 15 3
finaldiff 15 3
onepre 16
onepre 17
preseries 18 2
finaldiff 18 2
preseries 19 2
finaldiff 19 2
preseries 20 2
finaldiff 20 2
onepre 21
preseries 22 3
finaldiff 22 3
preseries 23 6
finaldiff 23 6
preseries 24 3
finaldiff 24 3
preseries 25 3
finaldiff 25 3
preseries 26 3
finaldiff 26 3
preseries 27 6
finaldiff 27 6
diffseries 28 28
preseries 29 3
finaldiff 29 3
preseries 30 7
finaldiff 30 7
onepre 31
preseries 32 4
finaldiff 32 4
diffseries 33 33
preseries 34 3
finaldiff 34 3

preseries 35 4
echo diffing 2.3.35pre6
diff -urN linux-2.3.35pre4 linux-2.3.35pre6 >linux-2.3.35pre6.diff
finaldiff 35 6

preseries 36 3
echo diffing 2.3.36pre5
diff -urN linux-2.3.36pre3 linux-2.3.36pre5 >linux-2.3.36pre5.diff
echo diffing 2.3.36pre6
diff -urN linux-2.3.36pre5 linux-2.3.36pre6 >linux-2.3.36pre6.diff
finaldiff 36 6

diffseries 37 37
onepre 38
preseries 39 2
finaldiff 39 2
preseries 40 6
finaldiff 40 6
preseries 41 4
finaldiff 41 4
onepre 42
preseries 43 8
finaldiff 43 8
preseries 44 10
finaldiff 44 10
preseries 45 2
finaldiff 45 2
preseries 46 5
finaldiff 46 5
preseries 47 8
finaldiff 47 8
preseries 48 4
finaldiff 48 4
preseries 49 2
finaldiff 49 2
preseries 50 3
finaldiff 50 3
preseries 51 3
finaldiff 51 3

echo diffing 2.3.52pre1
diff -urN linux-2.3.51 linux-2.3.52pre1 >linux-2.3.52pre1.diff
echo diffing 2.3.52pre2
diff -urN linux-2.3.52pre1 linux-2.3.52pre2 >linux-2.3.52pre2.diff
echo diffing 2.3.52pre3
diff -urN linux-2.3.52pre2 linux-2.3.52pre3 >linux-2.3.52pre3.diff

echo diffing 2.3.99-pre1
diff -urN linux-2.3.52pre3 linux-2.3.99-pre1 >linux-2.3.99pre1.diff

pre99series()
{
	if [ ! -d linux-2.3.99-pre$(($1-1)) ]; then
		echo eek! no linux-2.3.99-pre$(($1-1))
		exit
	fi
	if [ ! -d linux-2.3.99-pre$1-1 ]; then
		echo eek! no linux-2.3.99-pre$1-1
		exit
	fi
	echo diffing 2.3.99-pre$1-1
	diff -urN linux-2.3.99-pre$(($1-1)) linux-2.3.99-pre$1-1 >linux-2.3.99pre$1-1.diff
	for i in $(seq 2 $2)
	do
		if [ ! -d linux-2.3.99-pre$1-$(($i-1)) ]; then
			echo eek! no linux-2.3.99-pre$1-$(($i-1))
			exit
		fi
		if [ ! -d linux-2.3.99-pre$1-$i ]; then
			echo eek! no linux-2.3.99-pre$1-$i
			exit
		fi
		echo diffing 2.3.99-pre$1-$i
		diff -urN linux-2.3.99-pre$1-$(($i-1)) linux-2.3.99-pre$1-$i >linux-2.3.99pre$1-$i.diff
	done
	if [ ! -d linux-2.3.99-pre$1 ]; then
		echo eek! no linux-2.3.99-pre$1
		exit
	fi
	echo diffing 2.3.99-pre$1
	diff -urN linux-2.3.99-pre$1-$i linux-2.3.99-pre$1 >linux-2.3.99pre$1.diff
}

pre99series 2 5
pre99series 3 8
pre99series 4 5
echo diffing 2.3.99-pre5
diff -urN linux-2.3.99-pre4 linux-2.3.99-pre5 >linux-2.3.99pre5.diff
pre99series 6 7
pre99series 7 9
echo diffing 2.3.99-pre8
diff -urN linux-2.3.99-pre7 linux-2.3.99-pre8 >linux-2.3.99pre8.diff
pre99series 9 5
echo diffing 2.3.99-pre10-1
diff -urN linux-2.3.99-pre9 linux-2.3.99-pre10-1 >linux-2.3.99pre10-1.diff
echo diffing 2.3.99-pre10-2
diff -urN linux-2.3.99-pre10-1 linux-2.3.99-pre10-2 >linux-2.3.99pre10-2.diff
echo diffing 2.3.99-pre10-3
diff -urN linux-2.3.99-pre10-2 linux-2.3.99-pre10-3 >linux-2.3.99pre10-3.diff
echo diffing 2.4.0-test1
diff -urN linux-2.3.99-pre10-3 linux-2.4.0-test1 >linux-2.4.0-test1.diff

testseries()
{
	if [ ! -d linux-2.4.0-test$1 ]; then
		echo eek! no linux-2.4.0-test$1
		exit
	fi
	if [ ! -d linux-2.4.0-test$1pre1 ]; then
		echo eek! no linux-2.4.0-test$1pre1
		exit
	fi
	echo diffing 2.4.0-test$1-1
	diff -urN linux-2.4.0-test$(($1-1)) linux-2.4.0-test$1pre1 >linux-2.4.0-test$1pre1.diff
	for i in $(seq 2 $2)
	do
		if [ ! -d linux-2.4.0-test$1pre$(($i-1)) ]; then
			echo eek! no linux-2.4.0-test$1pre$(($i-1))
			exit
		fi
		if [ ! -d linux-2.4.0-test$1pre$i ]; then
			echo eek! no linux-2.4.0-test$1pre$i
			exit
		fi
		echo diffing 2.4.0-test$1-$i
		diff -urN linux-2.4.0-test$1pre$(($i-1)) linux-2.4.0-test$1pre$i >linux-2.4.0-test$1pre$i.diff
	done
	echo diffing 2.4.0-test$1
	diff -urN linux-2.4.0-test$1pre$i linux-2.4.0-test$1 >linux-2.4.0-test$1.diff
}

testseries 2 12
testseries 3 9
testseries 4 6
testseries 5 6
testseries 6 10
testseries 7 7
testseries 8 6
testseries 9 9
testseries 10 7
testseries 11 7
testseries 12 8

echo diffing 2.4.0-test13pre1
diff -urN linux-2.4.0-test12 linux-2.4.0-test13pre1 >linux-2.4.0-test13pre1.diff
for i in $(seq 2 7)
do
	echo diffing 2.4.0-test13-$i
	diff -urN linux-2.4.0-test13pre$(($i-1)) linux-2.4.0-test13pre$i >linux-2.4.0-test13pre$i.diff
done

echo diffing 2.4.0-prerelease
diff -urN linux-2.4.0-test13pre7 linux-2.4.0-prerelease >linux-2.4.0-prerelease.diff

