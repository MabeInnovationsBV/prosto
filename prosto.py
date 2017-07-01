#!/usr/bin/python

from math import sqrt, ceil
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
    f = 10000000000
    f = 0000000000
    nextsquare = Decimal(4 * bignumber + f * f).sqrt().to_integral_exact(rounding=ROUND_CEILING)

    if nextsquare % 2 == 1:
        nextsquare = nextsquare + 1

    realsquare = nextsquare * nextsquare
    limit = isqrt(4 * bignumber)

    while f < limit:
        if f % 100000 == 0:
             print "F: %d" % f
             print datetime.now()

        f = f + 2
        tocompare = f * f + 4 * bignumber

        if tocompare == realsquare:
             aplusb = Decimal(4 * bignumber + f * f).sqrt()
             print "A: %d B: %d" % ((aplusb - f) / 2, (aplusb + f) / 2)
             break
        elif tocompare > realsquare:
            nextsquare = nextsquare + 2
            realsquare = nextsquare * nextsquare

getfactorization(197 * 251)
getfactorization(15331738237 * 15331750531)
getfactorization(25331757331 * 25331757413)
getfactorization(15331750531 * 25331757413)

