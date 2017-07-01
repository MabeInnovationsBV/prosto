# prosto

Implementation of a simple method "PROSTO" to factor large numbers.

Basic idea:

a, b = unknown to us prime numbers, always uneven
c = known to us large number, `c = a * b`
f is always even

```
+-------------+---------------------------+
|     a       |             b             |
|             |                           |
|             |        c=a*b             a|
|             |                           |
|             |                           |
|b            +-------------+-------------+
|             |      f      |      a      |
|             |             |             |
|             |f  F=f^2    f|             |
|             |             |             |
|             |      f      |             |
+-------------+-------------+            b|
|                           |             |
|                           |             |
|a                          |             |
|                           |             |
|             b             |      a      |
+---------------------------+-------------+
```



(a + b)^2 = 4(a * b) + f^2 <= 

a * b = c

b = (sqrt(c) - sqrt(c - 4(a + b)))/2
