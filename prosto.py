#!/usr/bin/python

from math import sqrt

a = 197
b = 251

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


c = a * b


e = 4 * int(isqrt(4 * c) / 2)

print "E: %d" % e
print "C: %d" % c

v = e * e
d = v - 4 * c
sd = isqrt(d)
if d == sd * sd:
    print "done: %d" % d
else:
    print "not done %d" % d

f = 0
while f< 2000:
    f = f + 2
    aplusb = sqrt(4 * c + f * f) 
    #if f * f + 4 * c == aplusb * aplusb:
    if aplusb == int(aplusb):
         print "YAY %d" % f
         print "APLUSB %d" % aplusb
         print "A: %d B: %d" % ((aplusb - f) / 2, (aplusb + f) / 2)
