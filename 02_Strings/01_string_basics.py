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