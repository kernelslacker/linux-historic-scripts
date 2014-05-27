#!/bin/sh
# now do 2.1

diffseries()
{
	for i in $(seq $1 $2)
	do
		if [ ! -d linux-2.1.$(($i-1)) ]; then
			echo eek! no linux-2.1.$(($i-1))
			exit
		fi
		if [ ! -d linux-2.1.$i ]; then
			echo eek! no linux-2.1.$i
			exit
		fi
		echo diffing 2.1.$i
		#echo cmd: diff -urN linux-2.1.$(($i-1)) linux-2.1.$i \>linux-2.1.$i.diff
		diff -urN linux-2.1.$(($i-1)) linux-2.1.$i >linux-2.1.$i.diff
	done
}

prediff()
{
	if [ ! -d linux-2.1.$(($1-1)) ]; then
		echo eek! no linux-2.1.$(($1-1))
		exit
	fi
	if [ ! -d linux-2.1.$1pre1 ]; then
		echo eek! no linux-2.1.$1
		exit
	fi
	echo diffing 2.1.$1pre1
	diff -urN linux-2.1.$(($1-1)) linux-2.1.$1pre1 >linux-2.1.$1pre1.diff
	echo diffing 2.1.$1
	diff -urN linux-2.1.$1pre1 linux-2.1.$1 >linux-2.1.$1.diff
}

preseries()
{
	if [ ! -d linux-2.1.$(($1-1)) ]; then
		echo eek! no linux-2.1.$(($1-1))
		exit
	fi
	if [ ! -d linux-2.1.$1 ]; then
		echo eek! no linux-2.1.$1
		exit
	fi
	echo diffing 2.1.$1pre1
	diff -urN linux-2.1.$(($1-1)) linux-2.1.$1pre1 >linux-2.1.$1pre1.diff
	for i in $(seq 2 $2)
	do
		echo diffing 2.1.$1pre$i
		diff -urN linux-2.1.$1pre$(($i-1)) linux-2.1.$1pre$i >linux-2.1.$1pre$i.diff
	done
	echo diffing 2.1.$1
	diff -urN linux-2.1.$1pre$i linux-2.1.$1 >linux-2.1.$1.diff
}


echo diffing 2.1.0
diff -urN linux-2.0.21 linux-2.1.0 >linux-2.1.0.diff

diffseries 1 22
prediff 23
diffseries 24 27
prediff 28
diffseries 29 35
prediff 36
preseries 37 7
prediff 38
diffseries 39 41
preseries 42 2
prediff 43

# MISSING: 2.1.44pre1
echo diffing 2.1.44pre2
diff -urN linux-2.1.43 linux-2.1.44pre2 >linux-2.1.44pre2.diff
echo diffing 2.1.44pre3
diff -urN linux-2.1.44pre2 linux-2.1.44pre3 >linux-2.1.44pre3.diff
echo diffing 2.1.44
diff -urN linux-2.1.44pre3 linux-2.1.44 >linux-2.1.44.diff

preseries 45 10
prediff 46
diffseries 47 47
preseries 48 4
prediff 49
diffseries 50 50
prediff 51

# MISSING: 2.1.52pre1
#echo diffing 2.1.52pre2
#diff -urN linux-2.1.51 linux-2.1.52pre2 >linux-2.1.52pre2.diff
#echo diffing 2.1.52
#diff -urN linux-2.1.52pre2 linux-2.1.52 >linux-2.1.52.diff
echo diffing 2.1.52
diff -urN linux-2.1.51 linux-2.1.52 >linux-2.1.52.diff

diffseries 53 54
prediff 55
prediff 56
diffseries 57 67
prediff 68
diffseries 69 77
preseries 78 3
prediff 79
preseries 80 4
prediff 81
diffseries 82 86
prediff 87
diffseries 88 88
preseries 89 5
preseries 90 3
preseries 91 2
preseries 92 2
diffseries 93 94
prediff 95
prediff 96
diffseries 97 98
preseries 99 3
preseries 100 3
diffseries 101 101
preseries 102 2
diffseries 103 103
prediff 104
diffseries 105 105
prediff 106
preseries 107 2
prediff 108
preseries 109 2
preseries 110 3
prediff 111
preseries 112 2
diffseries 113 114
preseries 115 4
preseries 116 2
prediff 117
diffseries 118 118
prediff 119
preseries 120 3
prediff 121
preseries 122 3
preseries 123 3
preseries 124 2
preseries 125 2
preseries 126 2

echo diffing 2.1.127pre1
diff -urN linux-2.1.126 linux-2.1.127pre1 >linux-2.1.127pre1.diff
echo diffing 2.1.127pre2
diff -urN linux-2.1.127pre1 linux-2.1.127pre2 >linux-2.1.127pre2.diff
echo diffing 2.1.127pre3
diff -urN linux-2.1.127pre2 linux-2.1.127pre3 >linux-2.1.127pre3.diff
# MISSING: 2.1.127pre4 & pre5
echo diffing 2.1.127pre6
diff -urN linux-2.1.127pre3 linux-2.1.127pre6 >linux-2.1.127pre6.diff
echo diffing 2.1.127pre7
diff -urN linux-2.1.127pre6 linux-2.1.127pre7 >linux-2.1.127pre7.diff
echo diffing 2.1.127
diff -urN linux-2.1.127pre7 linux-2.1.127 >linux-2.1.127.diff

prediff 128
preseries 129 6

# MISSING 2.1.130pre1
echo diffing 2.1.130pre2
diff -urN linux-2.1.129 linux-2.1.130pre2 >linux-2.1.130pre2.diff
echo diffing 2.1.130pre3
diff -urN linux-2.1.130pre2 linux-2.1.130pre3 > linux-2.1.130pre3.diff
echo diffing 2.1.130
diff -urN linux-2.1.130pre3 linux-2.1.130 >linux-2.1.130.diff

# MISSING 2.1.131pre1
echo diffing 2.1.131pre2
diff -urN linux-2.1.130 linux-2.1.131pre2 >linux-2.1.131pre2.diff
echo diffing 2.1.131pre3
diff -urN linux-2.1.131pre2 linux-2.1.131pre3 > linux-2.1.131pre3.diff
echo diffing 2.1.131
diff -urN linux-2.1.131pre3 linux-2.1.131 >linux-2.1.131.diff

preseries 132 4

# MISSING 2.1.133pre2
echo diffing 2.1.133pre1
diff -urN linux-2.1.132 linux-2.1.133pre1 >linux-2.1.133pre1.diff
echo diffing 2.1.133pre3
diff -urN linux-2.1.133pre1 linux-2.1.133pre3 >linux-2.1.133pre3.diff
echo diffing 2.1.133pre4
diff -urN linux-2.1.133pre3 linux-2.1.133pre4 >linux-2.1.133pre4.diff
echo diffing 2.1.133pre5
diff -urN linux-2.1.133pre4 linux-2.1.133pre5 >linux-2.1.133pre5.diff

echo diffing 2.2.0pre1
diff -urN linux-2.1.133pre5 linux-2.2.0pre1 >linux-2.2.0pre1.diff
for i in $(seq 2 9)
do
	echo diffing 2.2.0pre$i
	diff -urN linux-2.2.0pre$(($i-1)) linux-2.2.0pre$i >linux-2.2.0pre$i.diff
done

