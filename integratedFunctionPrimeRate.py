import primefac


# Change the return value to the new function
def base(x):
    return x - 1


def mapping(x, y):
    return int(((x+y)*(x+y+1)/2) + x)


def integrated(x, shift):
    return int(mapping(x + shift, base(x + shift)))


primeRateFactor = 10 ** 6
shift = 1
numPrimes = 0

for x in range(0, primeRateFactor):
    print x
    if primefac.isprime(integrated(x, shift)):
        numPrimes += 1

print "Prime rate out of " + str(primeRateFactor)
print str(float(numPrimes*100)/primeRateFactor) + "%"
print numPrimes
