# Fun with math skillz
# We are going to look at approximations of Pi
# as well as looking at the math Module

print(22 / 7)
print(355 / 113)
import math

print(9801 / (2206 * math.sqrt(2)))


def archimedes(numSides):
    innerAngleB = 360.0 / numSides
    halfAngleA = innerAngleB / 2
    oneHalfSidesS = math.sin(math.radians(halfAngleA))
    sideS = oneHalfSidesS * 2
    polygonCircumference = numSides * sideS
    pi = polygonCircumference / 2
    return pi
# return returns your answer

print(archimedes(4))
print(archimedes(8))
print(archimedes(16))

for sides in range(8, 100, 8):
    print(sides, archimedes(sides))
    print(sides, archimedes(sides) - math.pi)

# See the loop above. In addition to the value of pi, print the difference between the values calculated by the
# archimedes function and by math.pi. How many sides does it take to make the two close?

# takes 96 sides to get close
# Accumulators

acc = 0
for val in range(1, 6):
    acc = acc + val

print(acc)
acc = 0
# compute the sum of the first 100 even numbers
for even in range(0, 202, 2):
    acc = acc + even
print(acc)
# compute the sum of the first 50 odd numbers
acc = 0
for odd in range(1, 51, 2):
    acc = acc + odd
print(acc)
# compute the average of the first 100 odd numbers
acc = 0
for odd in range(1, 200, 2):
    acc = acc + odd
print(acc/100)
# write a function that returns the average of the first N numbers, where N is a parameter
def averageNumber(N):
    acc = 0
    for averageNumber in range(0, N, 1):
        acc = acc + N
print(averageNumber(50))
# write a function called factorial that computes the product of the first N numbers.
def factorial():

# each number in the fibonacci sequence is the sum of the previous 2 numbers. The first 2 are 1 and 1. compute the 10th.

# write a function to compute the Nth Fibonacci number, where N is greater or equal to 3. 