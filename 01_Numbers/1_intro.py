# There are 3 numeric types
# int, float, complex

x = 1  #int
y = 1.2  #float
z = 1j  #complex
print(x, y, z)

#  To Verify the type of Object , use type() function
print(type(x), type(y), type(z))

#-------------------------------------------------------------
print('----------------------Type Conversion-------------------------')
# Type Conversion

## Convert from int to float
a = float(x)
print(a)  #1.0

## Convert from float to int
b = int(y)
print(b)  # 1

## Convert from float to int
c = complex(x)
print(c)  #(1+0j)

### NOTE: You cannot convert complex number to int
print('-------------------Python Powerful Number handling---------------')
# Python Powerful Number Handling
print(2 ** 100)
print(2**1000)
print(2**2000)


# ---------------------------------------------------------
print('-------------------Complex Numbers Calculation---------------')
# Complex Numbers Calculations
print(2+1j) # (2+ 1j)
print(2+1j * 3)  # (2+3j)
print((2+1j) * 3)  # (6 + 3j)


# ---------------------------------------------------------
print('-------------------Boolean---------------')

print(True == 1) # True
print(False == 0) # True

print(True is 1) # False

print(True + 4) # 5


# ---------------------------------------------------------
print('-------------------Base Numbers to Decimals ---------------')
# Base Numbers to Decimal
print(0o20) # Octal -> 16
print(0xff) # Hexadecimal -> 255
print(0b1000) # Binary -> 8

# ---------------------------------------------------------
print('-------------------Decimals to Base Numbers---------------')
# Decimals to Base Numbers Methods
print(oct(16)) # 0o20
print(hex(255)) # 0xff
print(bin(8)) # 0b1000


