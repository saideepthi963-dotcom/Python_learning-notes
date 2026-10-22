
# ================================================================================
# PYTHON FUNCTIONS - RETURN VALUES
# ----------------------------------------
# The return statement sends a value back to the caller.
#
# Functions can:
# 1. Return a single value
# 2. Return multiple values
# 3. Return values based on conditions
# 4. Return results for use in other calculations
# ================================================================================


# ---------------------------------------
# 1. Basic Return Statement
# ---------------------------------------
# return sends the result back to the caller.

def add(a, b):
    return a + b

result = add(10, 20)

print(result)  # -> 30


# ---------------------------------------
# 2. print() vs return
# ---------------------------------------
# print() displays a value.
# return sends a value back for later use.

def show_total(a, b):
    print(a + b)

def get_total(a, b):
    return a + b

show_total(10, 20)  # -> 30

result = get_total(10, 20)
print(result)       # -> 30

# The returned result can be stored in a variable.


# ---------------------------------------
# 3. Using Returned Values
# ---------------------------------------
# We can use returned values in calculations.

def multiply(a, b):
    return a * b

result = multiply(5, 4)

print(result)       # -> 20
print(result + 10)  # -> 30


# ---------------------------------------
# 4. Returning Multiple Values
# ---------------------------------------
# Python packs multiple returned values into a tuple.

def calculate(a, b):
    total = a + b
    difference = a - b
    return total, difference

result = calculate(10, 5)

print(result)  # -> (15, 5)


# ---------------------------------------
# 5. Unpacking Returned Values
# ---------------------------------------
# We can assign returned values to separate variables.

def calculate(a, b):
    return a + b, a * b

total, product = calculate(10, 5)

print(total)    # -> 15
print(product)  # -> 50


# ---------------------------------------
# 6. Return with If-Else
# ---------------------------------------
# A function can return different values
# depending on a condition.

def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

print(check_age(25))  # -> Adult
print(check_age(15))  # -> Minor


# ---------------------------------------
# 7. Return Ends Function Execution
# ---------------------------------------
# Code after return in the same block is not executed.

def greet():
    return "Hello"
    print("This will not run")

print(greet())  # -> Hello


# ---------------------------------------
# 8. Function Without Return
# ---------------------------------------
# A function without return returns None.

def welcome():
    print("Welcome to Python")

result = welcome()

print(result)

# Output:
# Welcome to Python
# None


# ---------------------------------------
# 9. Returning a List
# ---------------------------------------
# A function can return any data type.

def get_numbers():
    return [10, 20, 30]

numbers = get_numbers()

print(numbers)  # -> [10, 20, 30]


# ---------------------------------------
# 10. Returning a Dictionary
# ---------------------------------------
def get_student():
    return {
        "name": "Maria",
        "age": 25
    }

student = get_student()

print(student)
# -> {'name': 'Maria', 'age': 25}


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. return sends a value back to the caller.
# 2. print() displays a value but does not return it.
# 3. Returned values can be stored and reused.
# 4. Functions can return multiple values as a tuple.
# 5. Returned values can be unpacked.
# 6. return immediately exits the function.
# 7. Functions without return return None.
# 8. Functions can return numbers, strings, lists,
#    dictionaries, and other Python objects.

