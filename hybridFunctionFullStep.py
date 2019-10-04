# this file counts consecutive primes for hybrid function, doesn't alternate between lines

import primefac
import math


def c1(x):
    return int(abs(math.cos((math.pi/2)*x)))


def c2(x):
    return int(abs(math.sin((math.pi/2)*x)))


def f1(x):
    return int(x + 397)


def f2(x):
    return int(x - 59)


def G1(x, y):
    return int(((x + y)*(x + y + 1)/2) + x)


def F(x):
    return int(c1(x) * G1(x/2, f1(x/2)) + c2(x) * G1(((x-1)/2)+59, f2(((x-1)/2)+59)))


xStart = 0
xEnd = 1000  # 0000
consecutivePrimes = []
consecutiveNonPri = []

while xStart <= xEnd:
    print xStart
    if primefac.isprime(F(xStart)):
        xOrig = xStart
        numOrig = F(xOrig)
        count = 0
        while primefac.isprime(F(xStart + 1)):
            xStart += 1
            count += 1
        consecutivePrimes += [(xOrig, numOrig, count)]
    else:
        xOrig = xStart
        numOrig = F(xOrig)
        count = 0
        while not primefac.isprime(F(xStart + 1)):
            xStart += 1
            count += 1
        consecutiveNonPri += [(xOrig, numOrig, count)]
    xStart += 1

sortedPrimes = sorted(consecutivePrimes, key=lambda s: s[2], reverse=True)
sortedNonPri = sorted(consecutiveNonPri, key=lambda s: s[2], reverse=True)

print "non Primes: "
print consecutiveNonPri[:20]
print sortedNonPri[:20]
print "Primes: "
print consecutivePrimes[:20]
print sortedPrimes[:20]

raw_input("enter to continue to prime rate. ")

xStart = 0
xEnd = 1000
numPrimes = 0

while xStart <= xEnd:
    print xStart
    if primefac.isprime(F(xStart)):
        numPrimes += 1
    xStart += 1

print "prime rate out of " + str(xEnd)
print numPrimes
print str(float(numPrimes * 100)/xEnd) + "%"
