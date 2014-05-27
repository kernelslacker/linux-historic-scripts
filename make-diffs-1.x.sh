#!/bin/sh

echo diffing 1.0
diff -urN linux-1.0alpha linux-1.0 >linux-1.0.diff
echo diffing 1.0.1
diff -urN linux-1.0 linux-1.0.1 >linux-1.0.1.diff
for i in $(seq 2 9)
do
	echo diffing 1.0.$i
	diff -urN linux-1.0.$(($i-1)) linux-1.0.$i >linux-1.0.$i.diff
done

echo diffing 1.1.0
diff -urN linux-1.0.6 linux-1.1.0 >linux-1.1.0.diff
for i in $(seq 1 95)
do
	echo diffing 1.1.$i
	diff -urN linux-1.1.$(($i-1)) linux-1.1.$i >linux-1.1.$i.diff
done

echo diffing 1.2.0
diff -urN linux-1.1.95 linux-1.2.0 >linux-1.2.0.diff
for i in $(seq 1 13)
do
	echo diffing 1.2.$i
	diff -urN linux-1.2.$(($i-1)) linux-1.2.$i >linux-1.2.$i.diff
done

echo diffing 1.3.0
diff -urN linux-1.2.10 linux-1.3.0 >linux-1.3.0.diff
for i in $(seq 1 100)
do
	echo diffing 1.3.$i
	diff -urN linux-1.3.$(($i-1)) linux-1.3.$i >linux-1.3.$i.diff
done

echo diffing pre2.0.1
diff -urN linux-1.3.100 linux-pre2.0.1 >linux-pre2.0.1.diff
for i in $(seq 2 14)
do
	echo diffing pre2.0.$i
	diff -urN linux-pre2.0.$(($i-1)) linux-pre2.0.$i >linux-pre2.0.$i.diff
done

