import primefac
import math


def f(x, slope, intercept):
    return int(slope * x + intercept)


def G(x, y):
    return int((x+y)*(x+y+1)/2 + x)


def F(x, slope, intercept):
    return int(G(x, f(x, slope, intercept)))


# This works for lines of slope 1 and positive y intercept
# primeRate = 10**3
# slope = 1
# intercept = 0
# numLinesToCheck = 5
# data = []
# countPrime = 0
#
# for yInt in range(intercept, intercept + numLinesToCheck):
#     print yInt
#     # If slope is fractional, need to adjust x step
#     if slope < 1:
#         # Slope < 1, yInt is positive, we will start x at 0
#         if yInt > 0:
#             for x in range(0, int(1/slope)*primeRate, int(1/slope)):
#                 if primefac.isprime(F(x, slope, yInt)):
#                     countPrime += 1
#         # Slope < 1, yInt is negative, need to change where x starts
#         else:
#             for x in range(int(math.ceil(-yInt/slope)), int(1/slope)*primeRate + int(math.ceil(-yInt/slope)), int(1/slope)):
#                 if primefac.isprime(F(x, slope, yInt)):
#                     countPrime += 1
#     # This is for slope > 0, and positive y intercept x starts at 0
#     elif yInt > 0:
#         for x in range(0, primeRate):
#             if primefac.isprime(F(x, slope, yInt)):
#                 countPrime += 1
#     # Case for slope > 0, negative yInt, needs to start at different x
#     else:
#         for x in range(int(math.ceil(-yInt/slope)), primeRate + int(math.ceil(-yInt/slope))):
#             if primefac.isprime(F(x, slope, yInt)):
#                 countPrime += 1
#     data += [(yInt, countPrime)]
#     countPrime = 0
#
# sortedData = sorted(data, key=lambda s: s[1], reverse=True)
# print slope
# print data[:20]
# print sortedData[:20]

consecutivePrimes = []
consecutiveNonPri = []
slope = 1
intercept = -254
numToCheck = 100000
xStart = 254
count = 0

while xStart <= numToCheck:
    print xStart
    if primefac.isprime(F(xStart, slope, intercept)):
        xOrig = xStart
        numOrig = F(xOrig, slope, intercept)
        count = 1
        while primefac.isprime(F(xStart + 1, slope, intercept)):
            count += 1
            xStart += 1
        consecutivePrimes += [(xOrig, numOrig, F(xStart, slope, intercept), count)]
    else:
        xOrig = xStart
        numOrig = F(xOrig, slope, intercept)
        count = 1
        while not primefac.isprime(F(xStart + 1, slope, intercept)):
            count += 1
            xStart += 1
        consecutiveNonPri += [(xOrig, numOrig, F(xStart, slope, intercept), count)]
    xStart += 1

sortedPrimes = sorted(consecutivePrimes, key=lambda s: s[3], reverse=True)
sortedNonPri = sorted(consecutiveNonPri, key=lambda s: s[3], reverse=True)

print consecutivePrimes[:30]
print sortedPrimes[:30]

# tops = []
# for x in range(0, 11):
#     tops += [(sortedPrimes[x])]
#
# tops += [(sortedPrimes[14])]
#
# print tops
# tops = sorted(tops, key=lambda s: s[0])
# print tops