# Number Validation

# Number validation means checking whether a value can safely be treated as a number before using it in calculations.



# Simple integer validation

user_input = input("Enter a whole number: ")

if user_input.isdigit():
    number = int(user_input)
    print("Valid integer:", number)
else:
    print("Invalid whole number")


# Handling negative integers

user_input = input("Enter an integer: ")

if user_input.lstrip("-").isdigit():
    number = int(user_input)
    print("Valid integer:", number)
else:
    print("Invalid integer")


# Explanation:
# lstrip("-") removes a leading minus sign before checking digits.


# Validating decimal numbers
# replace() can remove one decimal point before checking digits.

user_input = input("Enter a decimal number: ")

if user_input.replace(".", "", 1).isdigit():
    number = float(user_input)
    print("Valid decimal:", number)
else:
    print("Invalid decimal")


# Note:
# This works for simple positive decimals like:
# 12.5
# 3.14
#
# More advanced validation is better handled with try/except.


# Best practical approach: try/except

user_input = input("Enter a number: ")

try:
    number = float(user_input)
    print("Valid number:", number)

except ValueError:
    print("Invalid number")


