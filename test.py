import primefac
import math


def f(x, slope, intercept):
    return int(slope * x + intercept)


def G(x, y):
    return int((x+y)*(x+y+1)/2 + x)


def F(x, slope, intercept):
    return int(G(x, f(x, slope, intercept)))


# This works for lines of slope 1 and positive y intercept
primeRate = 10**3
slope = 1/5.
intercept = -50000
numLinesToCheck = 50000
data = []
countPrime = 0

for yInt in range(intercept, intercept + numLinesToCheck):
    print yInt
    # If slope is fractional, need to adjust x step
    if slope < 1:
        # Slope < 1, yInt is positive, we will start x at 0
        if yInt > 0:
            for x in range(0, int(1/slope)*primeRate, int(1/slope)):
                if primefac.isprime(F(x, slope, yInt)):
                    countPrime += 1
        # Slope < 1, yInt is negative, need to change where x starts
        else:
            for x in range(int(math.ceil(-yInt/slope)), int(1/slope)*primeRate + int(math.ceil(-yInt/slope)), int(1/slope)):
                if primefac.isprime(F(x, slope, yInt)):
                    countPrime += 1
    # This is for slope > 0, and positive y intercept x starts at 0
    elif yInt > 0:
        for x in range(0, primeRate):
            if primefac.isprime(F(x, slope, yInt)):
                countPrime += 1
    # Case for slope > 0, negative yInt, needs to start at different x
    else:
        for x in range(int(math.ceil(-yInt/slope)), primeRate + int(math.ceil(-yInt/slope))):
            if primefac.isprime(F(x, slope, yInt)):
                countPrime += 1
    data += [(yInt, countPrime)]
    countPrime = 0

sortedData = sorted(data, key=lambda s: s[1], reverse=True)
print slope
print data[:20]
print sortedData[:20]




# import primefac
#
# def _f(x):
#     return int(2*x +1822)
#
#
# def G(x, y):
#     return int((x+y)*(x+y+1)/2 + x)
#
#
# def F(x):
#     return int(G(x, _f(x)))
#
#
# numPrimes = 0
# for x in range(0, 1000):
#     print x
#     if primefac.isprime(F(x)):
#         numPrimes += 1
#
# print "prime count " + str(numPrimes)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# # def F(x):
# #     return x**2 + x + 41
# #
# #
# # primeCount = 0
# #
# # for x in range(0, 1):
# #     print x
# #     if primefac.isprime(F(x)):
# #         primeCount += 1
# #
# # print "prime count: " + str(primeCount)
# #
# # xStart = 0
# # xEnd = 1000000
# # consecutivePrimes = []
# # consecutiveNonPri = []
# #
# # while xStart <= xEnd:
# #     print xStart
# #     if primefac.isprime(F(xStart)):
# #         xOrig = xStart
# #         numOrig = F(xStart)
# #         count = 0
# #         while primefac.isprime(F(xStart + 1)):
# #             count += 1
# #             xStart += 1
# #         consecutivePrimes += [(xOrig, numOrig, count)]
# #     else:
# #         xOrig = xStart
# #         numOrig = F(xStart)
# #         count = 0
# #         while not primefac.isprime(F(xStart + 1)):
# #             count += 1
# #             xStart += 1
# #         consecutiveNonPri += [(xOrig, numOrig, count)]
# #     xStart += 1
# #
# # sortedPrimes = sorted(consecutivePrimes, key=lambda s: s[2], reverse=True)
# # sortedNonPri = sorted(consecutiveNonPri, key=lambda s: s[2], reverse=True)
# #
# # print "primes: "
# # print consecutivePrimes[:20]
# # print sortedPrimes[:20]
# # # print "non primes: "
# # # print consecutiveNonPri[:20]
# # # print sortedNonPri[:20]
