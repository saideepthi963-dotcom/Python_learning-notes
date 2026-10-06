# Rounding and Math

# round()
# round() rounds a number to the nearest value.

number = 7.6
print(round(number))

# Output:
# 8


number = 7.4
print(round(number))

# Output:
# 7


# Round to a specific number of decimal places.

price = 19.9876
print(round(price, 2))

# Output:
# 19.99


# abs()
# abs() returns the absolute value of a number.

number = -25
print(abs(number))

# Output:
# 25


# Import the math module.
# The math module provides extra mathematical functions.

import math


# math.floor()
# Rounds down to the nearest integer.

number = 7.9
print(math.floor(number))

# Output:
# 7


# math.ceil()
# Rounds up to the nearest integer.

number = 7.1
print(math.ceil(number))

# Output:
# 8


# math.trunc()
# Removes the decimal part without rounding.

number = 8.99
print(math.trunc(number))

# Output:
# 8


# math.sqrt()
# Returns the square root of a number.

print(math.sqrt(25))

# Output:
# 5.0


# math.pi
# Gives the value of pi.

print(math.pi)

# Output:
# 3.141592653589793


# Calculate the area of a circle.

radius = 5
area = math.pi * radius ** 2

print(round(area, 2))

# Output:
# 78.54


# math.pow()
# Raises a number to a power.
# math.pow() returns a float.

print(math.pow(2, 3))

# Output:
# 8.0


# Compare ** and math.pow()

print(2 ** 3)
print(math.pow(2, 3))

# Output:
# 8
# 8.0


# Difference between round(), floor(), ceil(), and trunc()

number = 6.7

print(round(number))
print(math.floor(number))
print(math.ceil(number))
print(math.trunc(number))

# Output:
# 7
# 6
# 7
# 6


# Negative Number Example

number = -6.7

print(round(number))
print(math.floor(number))
print(math.ceil(number))
print(math.trunc(number))

# Output:
# -7
# -7
# -6
# -6


