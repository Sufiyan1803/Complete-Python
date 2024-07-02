
# Basic operations
x = 2
y = 3
z = 4

print(x + y)

# dont do this
print(40 + 2.23)
# print("hitesh" + 3)


# convert float to int
x = 2.23
a = int(x)
print(a)

# convert int to float
y=4
b=float(y)
print(b)


# operator overloading
print('chai' + 'code')


# Tuple
x = 2
y = 3
z = 4
print(x, y, z)
print(x+y,y*z)



# cal remainder
r = y % 2
print(r)



# power value 
p = z ** 4
print(p)

# python is capable to handle large numbers 
big = z ** 100                                             
print(big)








# LEARN ABOUT
# 1        Returns the result as a string without any formatting or rounding, suitable for debugging.
repr('chai')

# 2        Used to convert an object to its string representation.
str('chai')

# 3        Used to print the desired message on a device's screen. 
print('chai')


# comparison
print(2>1)

print(5 == 5)


print(4 != 5)



# Common library

# 1
import math

# math.floor gives value closest bottom value
f = math.floor(3.5)
print(f)

g = math.floor(-3.5)
print(g)


# math.trunc gives value closest to zero
s = math.trunc(2.5)
t = math.trunc(-3.5)

print(s)
print(t)



# 2
import random

i = random.random()
print(i)

L1 = ['lemon','masala','ginger','mint']
g = random.choice(L1)
print(g)

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






# SET
setone = {1, 2, 3, 4}
# intersection
print(setone & {1,2,5})
# union
print(setone | {1,2,5})

# Empty set is Dictionary
print(setone - {1,2,3,4})

# Used to define type
e=type({})
print(e)


# BOOLEAN
q = type(True)
print(q)







