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

# each number in the fibonacci sequence is the sum of the previous 2 numbers. The first 2 are 1 and 1. compute the 10th.

# write a function to compute the Nth Fibonacci number, where N is greater or equal to 3.

# A Monte Carol Simulation
# random numbers
import random
print(random.random())
# will never be 1, can be 0.
# Boolean Expressions
# <,<=,>,>=,==,!=
# Compoud Boolean expressions
# and, or, not
dogWeight = 25
print(dogWeight == 25)
catWeight = 15
print(dogWeight >= 25 and catWeight <= 10)
print(not catWeight <= 10)
# Decision making skills
alan = 20
bob = 15
karen = 25
ans = 0
if alan > 20:
    if bob < 50:
        ans = 150
    else:
        ans = 300
else:
    if karen > 500:
        ans = 200
    else:
        ans = 75
print(ans)
value = 75
if value > 100:
    print("bigger than 100")
elif value > 80:
    print("bigger than 80")
elif value > 45:
    print("bigger than 45")

def montePi(numDarts):

    inCircle = 0

    for i in range(numDarts):
        x = random.random()
        y = random.random()

        distance = math.sqrt(x**2 + y**2)

        if distance <= 1:
            inCircle = inCircle + 1

    pi = inCircle / numDarts * 4
    return pi

print(montePi(100))

import turtle

def showMontePi(numDarts):
    scn = turtle.Screen()
    t = turtle.Turtle()

    scn.setworldcoordinates(-2, -2, 2, 2)

    t.penup()
    t.goto(-1, 0)
    t.pendown()
    t.goto(1, 0)

    t.penup()
    t.goto(0, 1)
    t.pendown()
    t.goto(0, -1)

    inCircle = 0
    t.penup()

    for i in range(numDarts):
        x = random.randrange(-100, 100) / 100
        y = random.randrange(-100, 100) / 100

        distance = math.sqrt(x**2 + y**2)
        t.goto(x, y)

        if distance <= 1:
            inCircle = inCircle + 1
            t.color("blue")
        else:
            t.color("red")

        t.dot()

    pi = inCircle / numDarts * 4
    scn.exitonclick()
    return pi
print(showMontePi(1000))

# Plot points in the entire circle.
