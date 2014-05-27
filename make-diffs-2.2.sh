#!/bin/sh

# now do 2.2
echo diffing 2.2.0
diff -urN linux-2.2.0pre9 linux-2.2.0 >linux-2.2.0.diff
echo diffing 2.2.1
diff -urN linux-2.2.0 linux-2.2.1 >linux-2.2.1.diff

# 2.2.2
echo diffing 2.2.2pre1
diff -urN linux-2.2.1 linux-2.2.2pre1 > linux-2.2.2pre1.diff
echo diffing 2.2.2pre2
diff -urN linux-2.2.2pre1 linux-2.2.2pre2 > linux-2.2.2pre2.diff
echo diffing 2.2.2pre4
diff -urN linux-2.2.2pre2 linux-2.2.2pre4 > linux-2.2.2pre4.diff
echo diffing 2.2.2pre5
diff -urN linux-2.2.2pre4 linux-2.2.2pre5 > linux-2.2.2pre5.diff
echo diffing 2.2.2
diff -urN linux-2.2.2pre5 linux-2.2.2 >linux-2.2.2.diff

# 2.2.3
echo diffing 2.2.3pre1
diff -urN linux-2.2.2 linux-2.2.3pre1 > linux-2.2.3pre1.diff
echo diffing 2.2.3pre2
diff -urN linux-2.2.3pre1 linux-2.2.3pre2 > linux-2.2.3pre2.diff
echo diffing 2.2.3pre3
diff -urN linux-2.2.3pre2 linux-2.2.3pre3 > linux-2.2.3pre3.diff
echo diffing 2.2.3
diff -urN linux-2.2.3pre3 linux-2.2.3 > linux-2.2.3.diff

# 2.2.4
# MISSING: 2.2.4pre1 through pre3, and pre5
echo diffing 2.2.4pre4
diff -urN linux-2.2.3 linux-2.2.4pre4 >linux-2.2.4pre4.diff
echo diffing 2.2.4pre6
diff -urN linux-2.2.4pre4 linux-2.2.4pre6 >linux-2.2.4pre6.diff
echo diffing 2.2.4
diff -urN linux-2.2.4pre6 linux-2.2.4 >linux-2.2.4.diff

# 2.2.5
echo diffing 2.2.5pre1
diff -urN linux-2.2.4 linux-2.2.5pre1 > linux-2.2.5pre1.diff
echo diffing 2.2.5pre2
diff -urN linux-2.2.5pre1 linux-2.2.5pre2 > linux-2.2.5pre2.diff
echo diffing 2.2.5
diff -urN linux-2.2.5pre2 linux-2.2.5 >linux-2.2.5.diff

# 2.2.6
echo diffing 2.2.6pre1
diff -urN linux-2.2.5 linux-2.2.6pre1 > linux-2.2.6pre1.diff
echo diffing 2.2.6pre2
diff -urN linux-2.2.6pre1 linux-2.2.6pre2 > linux-2.2.6pre2.diff
echo diffing 2.2.6pre3
diff -urN linux-2.2.6pre2 linux-2.2.6pre3 > linux-2.2.6pre3.diff
echo diffing 2.2.6
diff -urN linux-2.2.6pre3 linux-2.2.6 >linux-2.2.6.diff

# 2.2.7
echo diffing 2.2.7pre1
diff -urN linux-2.2.6 linux-2.2.7pre1 > linux-2.2.7pre1.diff
for i in $(seq 2 4)
do
	echo diffing 2.2.7pre$i
	diff -urN linux-2.2.7pre$(($i-1)) linux-2.2.7pre$i >linux-2.2.7pre$i.diff
done
echo diffing 2.2.7
diff -urN linux-2.2.7pre4 linux-2.2.7 >linux-2.2.7.diff

# 2.2.8
echo diffing 2.2.8pre1
diff -urN linux-2.2.7 linux-2.2.8pre1 > linux-2.2.8pre1.diff
for i in $(seq 2 7)
do
	echo diffing 2.2.8pre$i
	diff -urN linux-2.2.8pre$(($i-1)) linux-2.2.8pre$i >linux-2.2.8pre$i.diff
done
echo diffing 2.2.8
diff -urN linux-2.2.8pre7 linux-2.2.8 >linux-2.2.8.diff

# 2.2.9
echo diffing 2.2.9
diff -urN linux-2.2.8 linux-2.2.9 >linux-2.2.9.diff

# 2.2.10
echo diffing 2.2.10pre1
diff -urN linux-2.2.9 linux-2.2.10pre1 >linux-2.2.10pre1.diff
for i in $(seq 2 5)
do
	echo diffing 2.2.10pre$i
	diff -urN linux-2.2.10pre$(($i-1)) linux-2.2.10pre$i >linux-2.2.10pre$i.diff
done
echo diffing 2.2.10
diff -urN linux-2.2.10pre5 linux-2.2.10 >linux-2.2.10.diff

# 2.2.11
echo diffing 2.2.11pre1
diff -urN linux-2.2.10 linux-2.2.11pre1 >linux-2.2.11pre1.diff
for i in $(seq 2 7)
do
        echo diffing 2.2.11pre$i
        diff -urN linux-2.2.11pre$(($i-1)) linux-2.2.11pre$i >linux-2.2.11pre$i.diff
done
echo diffing 2.2.11
diff -urN linux-2.2.11pre7 linux-2.2.11 >linux-2.2.11.diff

# 2.2.12
# MISSING: 2.2.12pre2
echo diffing 2.2.12pre1
diff -urN linux-2.2.11 linux-2.2.12pre1 > linux-2.2.12pre1.diff
echo diffing 2.2.12pre3
diff -urN linux-2.2.12pre1 linux-2.2.12pre3 > linux-2.2.12pre3.diff
for i in  $(seq 4 8)
do
	echo diffing 2.2.12pre$i
	diff -urN linux-2.2.12pre$(($i-1)) linux-2.2.12pre$i >linux-2.2.12pre$i.diff
done
echo diffing 2.2.12
diff -urN linux-2.2.12pre8 linux-2.2.12 >linux-2.2.12.diff

# 2.2.13
echo diffing 2.2.13pre1
diff -urN linux-2.2.12 linux-2.2.13pre1 > linux-2.2.13pre1.diff
for i in $(seq 2 18)
do
	echo diffing 2.2.13pre$i
	diff -urN linux-2.2.13pre$(($i-1)) linux-2.2.13pre$i >linux-2.2.13pre$i.diff
done
echo diffing 2.2.13
diff -urN linux-2.2.13pre18 linux-2.2.13 >linux-2.2.13.diff

# 2.2.14
echo diffing 2.2.14pre1
diff -urN linux-2.2.13 linux-2.2.14pre1 > linux-2.2.14pre1.diff
for i in $(seq 2 18)
do
	echo diffing 2.2.14pre$i
	diff -urN linux-2.2.14pre$(($i-1)) linux-2.2.14pre$i >linux-2.2.14pre$i.diff
done
echo diffing 2.2.14
diff -urN linux-2.2.14pre18 linux-2.2.14 >linux-2.2.14.diff

# 2.2.15
echo diffing 2.2.15pre1
diff -urN linux-2.2.14 linux-2.2.15pre1 > linux-2.2.15pre1.diff
for i in $(seq 2 20)
do
	echo diffing 2.2.15pre$i
	diff -urN linux-2.2.15pre$(($i-1)) linux-2.2.15pre$i >linux-2.2.15pre$i.diff
done
echo diffing 2.2.15
diff -urN linux-2.2.15pre20 linux-2.2.15 >linux-2.2.15.diff

# 2.2.16
# MISSING: linux-2.2.16pre1
echo diffing 2.2.16pre2
diff -urN linux-2.2.15 linux-2.2.16pre2 > linux-2.2.16pre2.diff
for i in $(seq 3 8)
do
	echo diffing 2.2.16pre$i
	diff -urN linux-2.2.16pre$(($i-1)) linux-2.2.16pre$i >linux-2.2.16pre$i.diff
done
echo diffing 2.2.16
diff -urN linux-2.2.16pre8 linux-2.2.16 >linux-2.2.16.diff

# 2.2.17
echo diffing 2.2.17pre1
diff -urN linux-2.2.16 linux-2.2.17pre1 > linux-2.2.17pre1.diff
for i in $(seq 2 20)
do
	echo diffing 2.2.17pre$i
	diff -urN linux-2.2.17pre$(($i-1)) linux-2.2.17pre$i >linux-2.2.17pre$i.diff
done
echo diffing 2.2.17
diff -urN linux-2.2.17pre20 linux-2.2.17 >linux-2.2.17.diff

# 2.2.18
echo diffing 2.2.18pre1
diff -urN linux-2.2.17 linux-2.2.18pre1 > linux-2.2.18pre1.diff
for i in $(seq 2 27)
do
	echo diffing 2.2.18pre$i
	diff -urN linux-2.2.18pre$(($i-1)) linux-2.2.18pre$i >linux-2.2.18pre$i.diff
done
echo diffing 2.2.18
diff -urN linux-2.2.18pre27 linux-2.2.18 >linux-2.2.18.diff

# 2.2.19
echo diffing 2.2.19pre1
diff -urN linux-2.2.18 linux-2.2.19pre1 > linux-2.2.19pre1.diff
for i in $(seq 2 18)
do
	echo diffing 2.2.19pre$i
	diff -urN linux-2.2.19pre$(($i-1)) linux-2.2.19pre$i >linux-2.2.19pre$i.diff
done
echo diffing 2.2.19
diff -urN linux-2.2.19pre18 linux-2.2.19 >linux-2.2.19.diff

# 2.2.20
echo diffing 2.2.20pre1
diff -urN linux-2.2.19 linux-2.2.20pre1 > linux-2.2.20pre1.diff
for i in $(seq 2 12)
do
	echo diffing 2.2.20pre$i
	diff -urN linux-2.2.20pre$(($i-1)) linux-2.2.20pre$i >linux-2.2.20pre$i.diff
done
echo diffing 2.2.20
diff -urN linux-2.2.20pre12 linux-2.2.20 >linux-2.2.20.diff

# 2.2.21
echo diffing 2.2.21pre1
diff -urN linux-2.2.20 linux-2.2.21pre1 >linux-2.2.21pre1.diff
for i in $(seq 2 4)
do
	echo diffing 2.2.21pre$i
	diff -urN linux-2.2.21pre$(($i-1)) linux-2.2.21pre$i >linux-2.2.21pre$i.diff
done
echo diffing 2.2.21-rc1
diff -urN linux-2.2.21pre4 linux-2.2.21-rc1 >linux-2.2.21-rc1.diff
for i in $(seq 2 4)
do
	echo diffing 2.2.21-rc$i
	diff -urN linux-2.2.21-rc$(($i-1)) linux-2.2.21-rc$i >linux-2.2.21-rc$i.diff
done
echo diffing 2.2.21
diff -urN linux-2.2.21-rc4 linux-2.2.21 >linux-2.2.21.diff

echo diffing 2.2.22-rc1
diff -urN linux-2.2.21 linux-2.2.22-rc1 >linux-2.2.22-rc1.diff
echo diffing 2.2.22-rc2
diff -urN linux-2.2.22-rc1 linux-2.2.22-rc2 >linux-2.2.22-rc2.diff
echo diffing 2.2.22-rc3
diff -urN linux-2.2.22-rc2 linux-2.2.22-rc3 >linux-2.2.22-rc3.diff
echo diffing 2.2.22
diff -urN linux-2.2.22-rc3 linux-2.2.22 >linux-2.2.22.diff

echo diffing 2.2.23-rc1
diff -urN linux-2.2.22 linux-2.2.23-rc1 >linux-2.2.23-rc1.diff
echo diffing 2.2.23-rc2
diff -urN linux-2.2.23-rc1 linux-2.2.23-rc2 >linux-2.2.23-rc2.diff
echo diffing 2.2.23
diff -urN linux-2.2.23-rc2 linux-2.2.23 >linux-2.2.23.diff

echo diffing 2.2.24-rc1
diff -urN linux-2.2.23 linux-2.2.24-rc1 >linux-2.2.24-rc1.diff
for i in $(seq 2 5)
do
	echo diffing 2.2.24-rc$i
	diff -urN linux-2.2.24-rc$(($i-1)) linux-2.2.24-rc$i >linux-2.2.24-rc$i.diff
done
echo diffing 2.2.24
diff -urN linux-2.2.24-rc5 linux-2.2.24 >linux-2.2.24.diff

echo diffing 2.2.25
diff -urN linux-2.2.24 linux-2.2.25 > linux-2.2.25.diff

echo diffing 2.2.26
diff -urN linux-2.2.25 linux-2.2.26 > linux-2.2.26.diff

echo diffing 2.2.27pre1
diff -urN linux-2.2.26 linux-2.2.27pre1 > linux-2.2.27pre1.diff
echo diffing 2.2.27pre2
diff -urN linux-2.2.27pre1 linux-2.2.27pre2 > linux-2.2.27pre2.diff
echo diffing 2.2.27-rc1
diff -urN linux-2.2.27pre2 linux-2.2.27-rc1 > linux-2.2.27-rc1.diff
echo diffing 2.2.27-rc2
diff -urN linux-2.2.27-rc1 linux-2.2.27-rc2 > linux-2.2.27-rc2.diff

