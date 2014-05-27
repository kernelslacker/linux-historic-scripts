#!/bin/sh

echo diffing 2.0
diff -urN linux-pre2.0.14 linux-2.0 >linux-2.0.diff
echo diffing 2.0.1
diff -urN linux-2.0 linux-2.0.1 >linux-2.0.1.diff
for i in $(seq 2 30)
do
	echo diffing 2.0.$i
	diff -urN linux-2.0.$(($i-1)) linux-2.0.$i >linux-2.0.$i.diff
done

echo diffing 2.0.31pre1
diff -urN linux-2.0.30 linux-2.0.31pre1 >linux-2.0.31pre1.diff
for i in $(seq 2 10)
do
	echo diffing 2.0.31pre$i
	diff -urN linux-2.0.31pre$(($i-1)) linux-2.0.31pre$i >linux-2.0.31pre$i.diff
done
echo diffing 2.0.31
diff -urN linux-2.0.31pre10 linux-2.0.31 >linux-2.0.31.diff

echo diffing 2.0.32pre1
diff -urN linux-2.0.31 linux-2.0.32pre1 >linux-2.0.32pre1.diff
echo diffing 2.0.32pre2
diff -urN linux-2.0.32pre1 linux-2.0.32pre2 >linux-2.0.32pre2.diff
# MISSING: 2.0.32pre3 2.0.32pre4
echo diffing 2.0.32pre5
diff -urN linux-2.0.32pre2 linux-2.0.32pre5 >linux-2.0.32pre5.diff
echo diffing 2.0.32pre6
diff -urN linux-2.0.32pre5 linux-2.0.32pre6 >linux-2.0.32pre6.diff
echo diffing 2.0.32
diff -urN linux-2.0.32pre6 linux-2.0.32 >linux-2.0.32.diff

echo diffing 2.0.33pre1
diff -urN linux-2.0.32 linux-2.0.33pre1 >linux-2.0.33pre1.diff
echo diffing 2.0.33pre2
diff -urN linux-2.0.33pre1 linux-2.0.33pre2 >linux-2.0.33pre2.diff
echo diffing 2.0.33pre3
diff -urN linux-2.0.33pre2 linux-2.0.33pre3 >linux-2.0.33pre3.diff
echo diffing 2.0.33
diff -urN linux-2.0.33pre3 linux-2.0.33 >linux-2.0.33.diff

echo diffing 2.0.34pre2
diff -urN linux-2.0.33 linux-2.0.34pre2 >linux-2.0.34pre2.diff
# BROKEN: pre13 and 14 don't apply.
for i in $(seq 3 10)
do
	echo diffing 2.0.34pre$i
	diff -urN linux-2.0.34pre$(($i-1)) linux-2.0.34pre$i >linux-2.0.34pre$i.diff
done
echo diffing 2.0.34pre11b
diff -urN linux-2.0.34pre10 linux-2.0.34pre11b >linux-2.0.34pre11b.diff
echo diffing 2.0.34pre15
diff -urN linux-2.0.34pre11b linux-2.0.34pre15 >linux-2.0.34pre15.diff
echo diffing 2.0.34pre16
diff -urN linux-2.0.34pre15 linux-2.0.34pre16 >linux-2.0.34pre16.diff
echo diffing 2.0.34
diff -urN linux-2.0.34pre16 linux-2.0.34 >linux-2.0.34.diff

echo diffing 2.0.35pre1
diff -urN linux-2.0.34 linux-2.0.35pre1 >linux-2.0.35pre1.diff
for i in $(seq 2 9)
do
	echo diffing 2.0.35pre$i
        diff -urN linux-2.0.35pre$(($i-1)) linux-2.0.35pre$i >linux-2.0.35pre$i.diff
done
echo diffing 2.0.35
diff -urN linux-2.0.35pre9 linux-2.0.35 >linux-2.0.35.diff

echo diffing 2.0.36pre1
diff -urN linux-2.0.35 linux-2.0.36pre1 >linux-2.0.36pre1.diff
for i in $(seq 2 22)
do
	echo diffing 2.0.36pre$i
        diff -urN linux-2.0.36pre$(($i-1)) linux-2.0.36pre$i >linux-2.0.36pre$i.diff
done
echo diffing 2.0.36
diff -urN linux-2.0.36pre22 linux-2.0.36 >linux-2.0.36.diff

echo diffing 2.0.37pre1
diff -urN linux-2.0.36 linux-2.0.37pre1 >linux-2.0.37pre1.diff
for i in $(seq 2 12)
do
	echo diffing 2.0.37pre$i
        diff -urN linux-2.0.37pre$(($i-1)) linux-2.0.37pre$i >linux-2.0.37pre$i.diff
done
echo diffing 2.0.37
diff -urN linux-2.0.37pre12 linux-2.0.37 >linux-2.0.37.diff

echo diffing 2.0.38pre1
diff -urN linux-2.0.37 linux-2.0.38pre1 >linux-2.0.38pre1.diff
echo diffing 2.0.38
diff -urN linux-2.0.38pre1 linux-2.0.38 >linux-2.0.38.diff

echo diffing 2.0.39pre1
diff -urN linux-2.0.38 linux-2.0.39pre1 >linux-2.0.39pre1.diff
for i in $(seq 2 8)
do
	echo diffing 2.0.39pre$i
	diff -urN linux-2.0.39pre$(($i-1)) linux-2.0.39pre$i >linux-2.0.39pre$i.diff
done
echo diffing 2.0.39
diff -urN linux-2.0.39pre8 linux-2.0.39 >linux-2.0.39.diff

echo diffing 2.0.40pre1
diff -urN linux-2.0.39 linux-2.0.40pre1 > linux-2.0.40pre1.diff
echo diffing 2.0.40pre2
diff -urN linux-2.0.40pre1 linux-2.0.40pre2 >linux-2.0.40pre2.diff
echo diffing 2.0.40pre3
diff -urN linux-2.0.40pre2 linux-2.0.40pre3 >linux-2.0.40pre3.diff
echo diffing 2.0.40rc1
diff -urN linux-2.0.40pre3 linux-2.0.40-rc1 >linux-2.0.40-rc1.diff
for i in $(seq 2 8)
do
	echo diffing 2.0.40-rc$i
	diff -urN linux-2.0.40-rc$(($i-1)) linux-2.0.40-rc$i >linux-2.0.40-rc$i.diff
done
echo diffing 2.0.40
diff -urN linux-2.0.40-rc8 linux-2.0.40 >linux-2.0.40.diff

