
# ================================================================================
# PYTHON FUNCTIONS - BASICS
# ----------------------------------------
# A function is a reusable block of code that performs a specific task.
#
# Functions help us:
# 1. Avoid repeating code
# 2. Organize programs
# 3. Reuse logic
#
# Syntax:
# def function_name():
#     statements
# ================================================================================


# ---------------------------------------
# 1. Creating a Function
# ---------------------------------------
# Use def to define a function.

def greet():
    print("Hello, Python!")

greet()

# Output: Hello, Python!


# ---------------------------------------
# 2. Calling a Function Multiple Times
# ---------------------------------------
# A function runs whenever we call it.

def welcome():
    print("Welcome to Python")

welcome()
welcome()
welcome()

# Output:
# Welcome to Python
# Welcome to Python
# Welcome to Python


# ---------------------------------------
# 3. Function with Multiple Statements
# ---------------------------------------
# A function can contain multiple lines of code.

def student_info():
    name = "Maria"
    age = 25

    print("Name:", name)
    print("Age:", age)

student_info()

# Output:
# Name: Maria
# Age: 25


# ---------------------------------------
# 4. Function with Conditions
# ---------------------------------------
# We can use if-else inside functions.

def check_age():
    age = 20

    if age >= 18:
        print("Adult")
    else:
        print("Minor")

check_age()

# Output: Adult


# ---------------------------------------
# 5. Function with a Loop
# ---------------------------------------
# Functions can contain loops.

def print_numbers():
    for number in range(1, 4):
        print(number)

print_numbers()

# Output:
# 1
# 2
# 3


# ---------------------------------------
# 6. Function Definition vs Function Call
# ---------------------------------------
# Defining a function does not execute its body.
# The function runs when it is called.

def say_hello():
    print("Hello!")

# Nothing is printed yet.

say_hello()

# Output: Hello!


# ---------------------------------------
# 7. Built-in Functions
# ---------------------------------------
# Python already provides built-in functions.

numbers = [10, 20, 30]

print(len(numbers))  # -> 3
print(max(numbers))  # -> 30
print(min(numbers))  # -> 10
print(sum(numbers))  # -> 60


# ---------------------------------------
# 8. pass Statement in Functions
# ---------------------------------------
# pass allows us to create an empty function.

def future_function():
    pass

future_function()

# No output.


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. def is used to create a function.
# 2. A function runs when it is called.
# 3. Functions help avoid repeating code.
# 4. Functions can contain conditions and loops.
# 5. Indentation defines the function body.
# 6. Python provides built-in functions.
# 7. pass is used as a placeholder.

