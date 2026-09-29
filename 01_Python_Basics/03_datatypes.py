# ============== Datatypes ==================
# There are several data types in python, To identify the data type we use the (type) in-built function. 
# Common types include integers, floats, strings, booleans, and NoneType.

#Examples of data types

name = "sai"  #string  (Double quote)
n = 'Deepthi'  #string (single quote) Note that strings can be represented with single quotes or double quotes, but you can't mix (e.g., "1.3')
p = "1526" #string 
a = 54     #int
b = 6.34   #float "numbers with decimals"
c = True   #Boolean need to be T and F capital
e = False  #Boolean
d = None   #NoneType means "no value", "nothing" or "unknown" it's used to show the absence of data.
i = ""        # str - empty string
j = " "       # str - contains a single space, Blank is a string value with no characters inside, it is not same as None.

# using type() we can check the data type

n = "python"
b = 272

print(type(n))
print(type(b))


# Exploring Methods for Each Data Type

print(n.upper())           # "HI" (string method)
print(b.bit_length())    # 4   (integer method) This method returns the exact number of bits necessary to represent the integer in binary.
#str doesn't have bit_length


# ================================================================================
# TYPE CONVERSION
# ================================================================================
# Type conversion means changing a value from one data type to another.
#
# Common conversion functions:
# int()   -> converts to integer
# float() -> converts to decimal number
# str()   -> converts to string
# list()  -> converts an iterable into a list
# ================================================================================


# ---------------------------------------
# Integer to Float
# ---------------------------------------

num_int = 10

num_float = float(num_int)

print("Integer:", num_int)
print("Float:", num_float)


# ---------------------------------------
# Float to Integer
# ---------------------------------------
# int() removes the decimal part.
# It does not round the number.

gravity = 9.81

gravity_int = int(gravity)

print("Gravity as float:", gravity)
print("Gravity as integer:", gravity_int)


# ---------------------------------------
# Integer to String
# ---------------------------------------

age = 25

age_string = str(age)

print("Age:", age)
print("Age as string:", age_string)

print(type(age))
print(type(age_string))


# ---------------------------------------
# String to Integer
# ---------------------------------------
# The string must contain a valid whole number.

number = "100"

converted_number = int(number)

print("String value:", number)
print("Integer value:", converted_number)


# ---------------------------------------
# String to Float
# ---------------------------------------

price = "19.99"

price_float = float(price)

print("Price as string:", price)
print("Price as float:", price_float)


# ---------------------------------------
# Decimal String to Integer
# ---------------------------------------
# "10.6" cannot be converted directly with int().
#
# First convert it to float, then convert the float to int.

number = "10.6"

number_float = float(number)
number_int = int(number_float)

print("Float:", number_float)
print("Integer:", number_int)


# ---------------------------------------
# String to List
# ---------------------------------------
# Each character in the string becomes one item in the list.

name = "Deepthi"

name_list = list(name)

print("Name:", name)
print("Name as list:", name_list)


# ---------------------------------------
# input() and Type Conversion
# ---------------------------------------
# input() always returns a string.
# Convert it when you need a number.

user_age = int(input("Enter your age: "))

print("Your age is:", user_age)
print("Data type:", type(user_age))

""" Numbers
Number data types in Python:

1) Integers: Integer(negative, zero and positive) numbers Example: ... -3, -2, -1, 0, 1, 2, 3 ...

2) Floating Point Numbers(Decimal numbers) Example: ... -3.5, -2.25, -1.0, 0.0, 1.1, 2.2, 3.5 ...

3) Complex Numbers Example: 1 + j, 2 + 4j, 1 - 1j """

