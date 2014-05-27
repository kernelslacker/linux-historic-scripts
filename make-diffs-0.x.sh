#!/bin/sh

echo diffing 0.10
diff -urN linux-0.01 linux-0.10 >linux-0.10.diff
echo diffing 0.11
diff -urN linux-0.10 linux-0.11 >linux-0.11.diff
echo diffing 0.12
diff -urN linux-0.11 linux-0.12 >linux-0.12.diff
echo diffing 0.95
diff -urN linux-0.12 linux-0.95 >linux-0.95.diff
echo diffing 0.95a
diff -urN linux-0.95 linux-0.95a >linux-0.95a.diff
echo diffing 0.95c+
diff -urN linux-0.95a linux-0.95c+ >linux-0.95c+.diff
echo diffing 0.96a
diff -urN linux-0.95c+ linux-0.96a >linux-0.96a.diff
echo diffing 0.96a-patch1
diff -urN linux-0.96a linux-0.96a-patch1 >linux-0.96a-patch1.diff
for i in 2 3 4
do
	echo diffing 0.96a-patch$i
	diff -urN linux-0.96a-patch$(($i-1)) linux-0.96a-patch$i >linux-0.96a-patch$i.diff
done
echo diffing 0.96b
diff -urN linux-0.96a-patch4 linux-0.96b >linux-0.96b.diff
echo diffing 0.96b-patch1
diff -urN linux-0.96b linux-0.96b-patch1 >linux-0.96b-patch1.diff
echo diffing 0.96b-patch2
diff -urN linux-0.96b-patch1 linux-0.96b-patch2 >linux-0.96b-patch2.diff
echo diffing 0.96c
diff -urN linux-0.96b-patch2 linux-0.96c >linux-0.96c.diff
echo diffing 0.96c-patch1
diff -urN linux-0.96c linux-0.96c-patch1 >linux-0.96c-patch1.diff
echo diffing 0.96c-patch2
diff -urN linux-0.96c-patch1 linux-0.96c-patch2 >linux-0.96c-patch2.diff
echo diffing 0.96pre
diff -urN linux-0.96c-patch2 linux-0.96pre >linux-0.96pre.diff
echo diffing 0.97
diff -urN linux-0.96pre linux-0.97 >linux-0.97.diff
echo diffing 0.97.1
diff -urN linux-0.97 linux-0.97.1 >linux-0.97.1.diff
for i in $(seq 2 6)
do
	echo diffing 0.97.$i
	diff -urN linux-0.97.$(($i-1)) linux-0.97.$i >linux-0.97.$i.diff
done

echo diffing 0.98
diff -urN linux-0.97.6 linux-0.98 >linux-0.98.diff
echo diffing 0.98.1
diff -urN linux-0.98 linux-0.98.1 >linux-0.98.1.diff
for i in $(seq 2 6)
do
        echo diffing 0.98.$i
        diff -urN linux-0.98.$(($i-1)) linux-0.98.$i >linux-0.98.$i.diff
done

echo diffing 0.99
diff -urN linux-0.98.6 linux-0.99 >linux-0.99.diff
echo diffing 0.99.1
diff -urN linux-0.99 linux-0.99.1 >linux-0.99.1.diff
for i in $(seq 2 7)
do
        echo diffing 0.99.$i
        diff -urN linux-0.99.$(($i-1)) linux-0.99.$i >linux-0.99.$i.diff
done
echo diffing 0.99.7A
diff -urN linux-0.99.7 linux-0.99.7A >linux-0.99.7A.diff
echo diffing 0.99.8
diff -urN linux-0.99.7A linux-0.99.8 >linux-0.99.8.diff
for i in $(seq 9 11)
do
        echo diffing 0.99.$i
        diff -urN linux-0.99.$(($i-1)) linux-0.99.$i >linux-0.99.$i.diff
done
echo diffing 0.99.11-patch1
diff -urN linux-0.99.11 linux-0.99.11-patch1 >linux-0.99.11-patch1.diff
echo diffing 0.99.12
diff -urN linux-0.99.11-patch1 linux-0.99.12 >linux-0.99.12.diff
echo diffing 0.99.12-patch1
diff -urN linux-0.99.12 linux-0.99.12-patch1 >linux-0.99.12-patch1.diff
echo diffing 0.99.13
diff -urN linux-0.99.12-patch1 linux-0.99.13 >linux-0.99.13.diff
echo diffing 0.99.13k
diff -urN linux-0.99.13 linux-0.99.13k >linux-0.99.13k.diff
echo diffing 0.99.14
diff -urN linux-0.99.13k linux-0.99.14 >linux-0.99.14.diff
echo diffing 0.99.14a
diff -urN linux-0.99.14 linux-0.99.14a >linux-0.99.14a.diff
echo diffing 0.99.14b
diff -urN linux-0.99.14a linux-0.99.14b >linux-0.99.14b.diff
echo diffing 0.99.14c
diff -urN linux-0.99.14b linux-0.99.14c >linux-0.99.14c.diff
echo diffing 0.99.14d
diff -urN linux-0.99.14c linux-0.99.14d >linux-0.99.14d.diff
echo diffing 0.99.14e
diff -urN linux-0.99.14d linux-0.99.14e >linux-0.99.14e.diff
echo diffing 0.99.14f
diff -urN linux-0.99.14e linux-0.99.14f >linux-0.99.14f.diff
echo diffing 0.99.14g
diff -urN linux-0.99.14f linux-0.99.14g >linux-0.99.14g.diff
echo diffing 0.99.14h
diff -urN linux-0.99.14g linux-0.99.14h >linux-0.99.14h.diff
echo diffing 0.99.14i
diff -urN linux-0.99.14h linux-0.99.14i >linux-0.99.14i.diff
echo diffing 0.99.14j
diff -urN linux-0.99.14i linux-0.99.14j >linux-0.99.14j.diff
echo diffing 0.99.14k
diff -urN linux-0.99.14j linux-0.99.14k >linux-0.99.14k.diff
echo diffing 0.99.14l
diff -urN linux-0.99.14k linux-0.99.14l >linux-0.99.14l.diff
echo diffing 0.99.14m
diff -urN linux-0.99.14l linux-0.99.14m >linux-0.99.14m.diff
echo diffing 0.99.14n
diff -urN linux-0.99.14m linux-0.99.14n >linux-0.99.14n.diff
echo diffing 0.99.14o
diff -urN linux-0.99.14n linux-0.99.14o >linux-0.99.14o.diff
echo diffing 0.99.14p
diff -urN linux-0.99.14o linux-0.99.14p >linux-0.99.14p.diff
echo diffing 0.99.14q
diff -urN linux-0.99.14p linux-0.99.14q >linux-0.99.14q.diff
echo diffing 0.99.14r
diff -urN linux-0.99.14q linux-0.99.14r >linux-0.99.14r.diff
echo diffing 0.99.14s
diff -urN linux-0.99.14r linux-0.99.14s >linux-0.99.14s.diff
echo diffing 0.99.14t
diff -urN linux-0.99.14s linux-0.99.14t >linux-0.99.14t.diff
echo diffing 0.99.14u
diff -urN linux-0.99.14t linux-0.99.14u >linux-0.99.14u.diff
echo diffing 0.99.14v
diff -urN linux-0.99.14u linux-0.99.14v >linux-0.99.14v.diff
echo diffing 0.99.14w
diff -urN linux-0.99.14v linux-0.99.14w >linux-0.99.14w.diff
echo diffing 0.99.14x
diff -urN linux-0.99.14w linux-0.99.14x >linux-0.99.14x.diff
echo diffing 0.99.14y
diff -urN linux-0.99.14x linux-0.99.14y >linux-0.99.14y.diff
echo diffing 0.99.14z
diff -urN linux-0.99.14y linux-0.99.14z >linux-0.99.14z.diff
echo diffing 0.99.15
diff -urN linux-0.99.14z linux-0.99.15 >linux-0.99.15.diff
echo diffing 0.99.15a
diff -urN linux-0.99.15 linux-0.99.15a >linux-0.99.15a.diff
echo diffing 0.99.15b
diff -urN linux-0.99.15a linux-0.99.15b >linux-0.99.15b.diff
echo diffing 0.99.15c
diff -urN linux-0.99.15b linux-0.99.15c >linux-0.99.15c.diff
echo diffing 0.99.15d
diff -urN linux-0.99.15c linux-0.99.15d >linux-0.99.15d.diff
echo diffing 0.99.15e
diff -urN linux-0.99.15d linux-0.99.15e >linux-0.99.15e.diff
echo diffing 0.99.15f
diff -urN linux-0.99.15e linux-0.99.15f >linux-0.99.15f.diff
echo diffing 0.99.15g
diff -urN linux-0.99.15f linux-0.99.15g >linux-0.99.15g.diff
echo diffing 0.99.15h
diff -urN linux-0.99.15g linux-0.99.15h >linux-0.99.15h.diff
echo diffing 0.99.15i
diff -urN linux-0.99.15h linux-0.99.15i >linux-0.99.15i.diff
echo diffing 0.99.15j
diff -urN linux-0.99.15i linux-0.99.15j >linux-0.99.15j.diff
echo diffing 1.0pre1
diff -urN linux-0.99.15j linux-1.0pre1 >linux-1.0pre1.diff
echo diffing 1.0alpha
diff -urN linux-1.0pre1 linux-1.0alpha >linux-1.0alpha.diff

