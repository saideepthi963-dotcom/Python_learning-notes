"""
STRINGS: A string is a sequence of characters used to store text in Python.

Strings can contain:
- letters
- numbers
- spaces
- symbols

Strings are written inside quotes.
"""

# String Length

# len() returns number of characters.

password = "123a58478as"

print(len(password))  # -> 11 len() returns the number of characters.

if len(password) < 8:
    print("Your Password is too short!")


# Repeating Strings

print("ha" * 3)              # ➜ hahaha
print("=" * 30)              # ➜ ==============================


# Counting Substrings

# count() checks how many times something appears.
# It is case-sensitive.

text = """
Python is easy to learn.
Python is powerful$.
Many people love python.
"""

print(text.count("Python"))  # -> 2  (case-sensitive)
print(text.count("python"))  # -> 1
print(text.count("$"))       # -> 1

#String Concatenation
# + joins strings together.

first_name = "Deepthi"
last_name = "Sai"

full_name = first_name + " " + last_name

print(full_name)


# f-Strings

# f-strings are a modern and readable way to insert
# variables and expressions inside strings.

name = "Deepthi"
language = "Python"

print(f"My name is {name}")
print(f"I am learning {language}")

# Output:
# My name is Deepthi
# I am learning Python


# Expressions inside f-strings

a = 10
b = 5

print(f"{a} + {b} = {a + b}")
print(f"{a} * {b} = {a * b}")

# Output:
# 10 + 5 = 15
# 10 * 5 = 50


# Formatting decimal numbers
# .2f means show 2 digits after the decimal point.

price = 19.9876

print(f"Price: {price:.2f}")

# Output:
# Price: 19.99


# Formatting percentages
# .2% converts the decimal value into a percentage
# and shows 2 digits after the decimal point.

score = 85
total = 100

percentage = score / total

print(f"Percentage: {percentage:.2%}")

# Output:
# Percentage: 85.00%


# Formatting large numbers
# , adds commas as thousands separators.

population = 1234567

print(f"Population: {population:,}")

# Output:
# Population: 1,234,567


# Using f-strings with user input

user_name = input("Enter your name: ")

print(f"Hello {user_name}")

