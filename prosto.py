#!/usr/bin/python

from math import sqrt
from decimal import *
from datetime import datetime

def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x

def getfactorization(bignumber):
    print "Factorizing %d ..." % bignumber
    f = 0
    while f < isqrt(4 * bignumber):
        if f % 100000 == 0:
             print "F: %d" % f
             print datetime.now()

        f = f + 2
        aplusb = Decimal(4 * bignumber + f * f).sqrt()
        #print aplusb
        #if f * f + 4 * bignumber == aplusb * aplusb:
        if aplusb == int(aplusb):
             #print "YAY %d" % f
             #print "APLUSB %d" % aplusb
             print "A: %d B: %d" % ((aplusb - f) / 2, (aplusb + f) / 2)
             break


getfactorization(197 * 251)
getfactorization(15331738237 * 15331750531)
getfactorization(25331757331 * 25331757413)
getfactorization(15331750531 * 25331757413)

