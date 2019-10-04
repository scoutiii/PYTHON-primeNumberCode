import math
import primefac
import numpy

coArray = numpy.zeros((100, 100))

for row in range(0, 100):
    for col in range(0, 100):
        coArray[row, col] = row ** col

# print "orig Array"
# print coArray
coArrayInverse = numpy.linalg.inv(coArray)
# print "inverse Array"
# print coArrayInverse

vec1 = numpy.zeros((100,1))
vec2 = numpy.zeros((100,1))
vec3 = numpy.zeros((100,1))
vec4 = numpy.zeros((100,1))
vec5 = numpy.zeros((100,1))
vec6 = numpy.zeros((100,1))
vec7 = numpy.zeros((100,1))
vec8 = numpy.zeros((100,1))
vec9 = numpy.zeros((100,1))
vec10 = numpy.zeros((100,1))
vec11 = numpy.zeros((100,1))
vec12 = numpy.zeros((100,1))
vec13 = numpy.zeros((100,1))

for i in range(0, 100):
    if 0 <= i <= 5:
        vec1[i] = 1
    elif 6 <= i <= 14:
        vec2[i] = 1
    elif 15 <= i <= 22:
        vec3[i] = 1
    elif 23 <= i <= 29:
        vec4[i] = 1
    elif 30 <= i <= 38:
        vec5[i] = 1
    elif 39 <= i <= 48:
        vec6[i] = 1
    elif 49 <= i <= 55:
        vec7[i] = 1
    elif 56 <= i <= 63:
        vec8[i] = 1
    elif 64 <= i <= 70:
        vec9[i] = 1
    elif 71 <= i <= 77:
        vec10[i] = 1
    elif 78 <= i <= 84:
        vec11[i] = 1
    elif 85 <= i <= 91:
        vec12[i] = 1
    else:
        vec13[i] = 1

# print vec1
# print vec13

co1 = numpy.matmul(coArrayInverse, vec1).astype(float)
print co1

print coArray
