
# ================================================================================
# MODULES AND PACKAGES IN PYTHON
# ----------------------------------------
# A module is a Python file containing reusable code.
# A package is a folder containing related Python modules.
#
# Modules help organize and reuse Python code.
# ================================================================================


# ---------------------------------------
# 1. Importing a Module
# ---------------------------------------
# Python provides many built-in modules.

import math

print(math.sqrt(25))  # -> 5.0
print(math.pi)        # -> 3.141592653589793


# ---------------------------------------
# 2. Importing Specific Functions
# ---------------------------------------
# from allows us to import only what we need.

from math import sqrt, ceil, floor

print(sqrt(36))    # -> 6.0
print(ceil(4.2))   # -> 5
print(floor(4.8))  # -> 4


# ---------------------------------------
# 3. Importing with an Alias
# ---------------------------------------
# as gives a module a shorter name.

import math as m

print(m.sqrt(49))  # -> 7.0


# ---------------------------------------
# 4. Random Module
# ---------------------------------------
# random provides functions for random values.

import random

number = random.randint(1, 10)

print(number)  # -> Random integer between 1 and 10


# ---------------------------------------
# 5. Creating Your Own Module
# ---------------------------------------
# A module is simply a Python file.
#
# Example: calculator.py
#
# def add(a, b):
#     return a + b
#
# In another Python file in the same folder:
#
# import calculator
# print(calculator.add(10, 20))
#
# Output: 30


# ---------------------------------------
# 6. Importing from Your Own Module
# ---------------------------------------
# We can import specific functions.
#
# Example:
#
# from calculator import add
#
# print(add(5, 10))
#
# Output: 15


# ---------------------------------------
# 7. Understanding Packages
# ---------------------------------------
# A package organizes related modules.
#
# Example:
#
# my_package/
#     __init__.py
#     calculator.py
#     greetings.py
#
# Importing from a package:
#
# from my_package.calculator import add
#
# print(add(10, 20))


# ---------------------------------------
# 8. __name__ == "__main__"
# ---------------------------------------
# This block runs when the file is executed directly.
# It does not run when the file is imported as a module.

def greet():
    print("Hello Python")

if __name__ == "__main__":
    greet()

# Output when run directly:
# Hello Python


# ---------------------------------------
# 9. Third-Party Packages
# ---------------------------------------
# Third-party packages can be installed using pip.
#
# Example terminal command:
#
# python -m pip install requests
#
# requests is useful for working with HTTP APIs.
#
# Installation commands run in the terminal,
# not inside Python code.


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. A module is a Python file.
# 2. A package organizes related modules.
# 3. import loads a module.
# 4. from imports specific names.
# 5. as creates an alias.
# 6. Python has many standard-library modules.
# 7. pip installs third-party packages.
# 8. __name__ == "__main__" checks direct execution.


