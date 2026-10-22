
# ================================================================================
# PYTHON FUNCTIONS - PARAMETERS AND ARGUMENTS
# ----------------------------------------
# Parameters are variables defined inside function parentheses.
# Arguments are actual values passed when calling the function.
#
# Functions can accept one or multiple arguments.
# ================================================================================


# ---------------------------------------
# 1. Function with One Parameter
# ---------------------------------------
# name is a parameter.
# "Maria" is an argument.

def greet(name):
    print("Hello", name)

greet("Maria")

# Output: Hello Maria


# ---------------------------------------
# 2. Function with Multiple Parameters
# ---------------------------------------
def student_info(name, age):
    print("Name:", name)
    print("Age:", age)

student_info("Maria", 25)

# Output:
# Name: Maria
# Age: 25


# ---------------------------------------
# 3. Positional Arguments
# ---------------------------------------
# Arguments are assigned based on position.

def employee(name, role):
    print(name, "works as", role)

employee("John", "Data Engineer")

# Output: John works as Data Engineer


# ---------------------------------------
# 4. Keyword Arguments
# ---------------------------------------
# Arguments can be passed using parameter names.
# Order does not matter when using keyword arguments.

def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=22, name="Sara")

# Output:
# Name: Sara
# Age: 22


# ---------------------------------------
# 5. Default Parameters
# ---------------------------------------
# A default value is used when no argument is supplied.

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Maria")

# Output:
# Hello Guest
# Hello Maria


# ---------------------------------------
# 6. Mixing Positional and Keyword Arguments
# ---------------------------------------
# Positional arguments come before keyword arguments.

def employee(name, role, city):
    print(name, role, city)

employee("John", role="Engineer", city="Berlin")

# Output: John Engineer Berlin


# ---------------------------------------
# 7. Functions with *args
# ---------------------------------------
# *args accepts any number of positional arguments.
# The collected arguments form a tuple.

def add_numbers(*numbers):
    print(sum(numbers))

add_numbers(10, 20)
add_numbers(10, 20, 30)

# Output:
# 30
# 60


# ---------------------------------------
# 8. Functions with **kwargs
# ---------------------------------------
# **kwargs accepts multiple keyword arguments.
# The collected arguments form a dictionary.

def show_details(**details):
    print(details)

show_details(name="Maria", age=25)

# Output:
# {'name': 'Maria', 'age': 25}


# ---------------------------------------
# 9. Calling Functions with Different Values
# ---------------------------------------
# The same function can process different inputs.

def check_score(score):
    if score >= 60:
        print("Passed")
    else:
        print("Failed")

check_score(85)
check_score(40)

# Output:
# Passed
# Failed


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. Parameters are defined in function parentheses.
# 2. Arguments are values passed during function calls.
# 3. Positional arguments depend on order.
# 4. Keyword arguments use parameter names.
# 5. Default parameters provide optional values.
# 6. *args accepts multiple positional arguments.
# 7. **kwargs accepts multiple keyword arguments.
# 8. Functions can be called with different values.

