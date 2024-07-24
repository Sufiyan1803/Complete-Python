
# Common library

# 1
import math


#-------------------------------------------------------------
print('--------------------------Math Built in------------------------')
# Built in Math - Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

# Min and Max
print(min(1, 2, 3))  # 1
print(max(1, 2, 3))  # 3

# Absolute - returns positive numbers
print(abs(-7521))  # 7521

# Power - returns the value of x to the power y
print(pow(3, 2))  # 9



# math.floor Rounds a number downwards to it's nearest integer
f = math.floor(3.5)
print(f)

g = math.floor(-3.5)
print(g)


# math.trunc gives value closest to zero
s = math.trunc(2.5)
t = math.trunc(-3.5)

print(s)
print(t)

# Square root of a number
print(math.sqrt(4))  # 2.0


# Ceil - Rounds a number upwards to it's nearest integer
print(math.ceil(3.5))  # 4
print(math.ceil(-3.5))  # -3


# PI - returns the value of pi
print(math.pi)



# 2
import random

# Returns a random float number between 0 and 1
i = random.random()
print(i)


# choice to select random from list
L1 = ['lemon','masala','ginger','mint']
g = random.choice(L1)
print(g)

# shuffle the list
L2 = ['lemon','masala','ginger','mint']
k = random.shuffle(L2)
print(L2)



# 3
from decimal import Decimal
u = Decimal('0.1') + Decimal('0.1') + Decimal('0.1')
print(u)


# 4
from fractions import Fraction
myFra = Fraction(4 , 2)
print(myFra)


# methods to cal diff base value
#1. oct()
#2. hex()
#3. bin()

# Also can use int('num',type())





