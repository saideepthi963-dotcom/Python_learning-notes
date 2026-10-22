
# ================================================================================
# PYTHON LAMBDA FUNCTIONS
# ----------------------------------------
# A lambda function is a small anonymous function.
# It is useful for writing simple functions in one line.
#
# Syntax:
# lambda arguments: expression
#
# Lambda functions automatically return the expression result.
# ================================================================================


# ---------------------------------------
# 1. Basic Lambda Function
# ---------------------------------------
# Multiply a number by 2.

multiple = lambda x: x * 2

print(multiple(2))  # -> 4


# ---------------------------------------
# 2. Lambda with Two Arguments
# ---------------------------------------
# Add two numbers.

add = lambda x, y: x + y

print(add(1, 2))  # -> 3


# ---------------------------------------
# 3. Lambda with Membership Check
# ---------------------------------------
# Check whether a character exists in a string.

check = lambda i: i in "python"

print(check('z'))  # -> False
print(check('p'))  # -> True


# ---------------------------------------
# 4. Regular Function vs Lambda
# ---------------------------------------
# Both functions perform the same operation.

def square(x):
    return x * x

square_lambda = lambda x: x * x

print(square(5))         # -> 25
print(square_lambda(5))  # -> 25


# ---------------------------------------
# 5. Lambda with map()
# ---------------------------------------
# Apply a function to each element.

numbers = [1, 2, 3, 4]

doubled = list(map(lambda x: x * 2, numbers))

print(doubled)  # -> [2, 4, 6, 8]


# ---------------------------------------
# 6. Convert Price Strings to Floats
# ---------------------------------------
# Remove the $ symbol and convert to float.

prices = ['$12.50', '$9.99', '$100.00']

cleaned = list(
    map(lambda p: float(p.replace('$', '')), prices)
)

print(cleaned)

# -> [12.5, 9.99, 100.0]


# ---------------------------------------
# 7. Lambda with filter()
# ---------------------------------------
# Keep prices greater than or equal to 100.

prices = [120, 30, 300, 80]

result = list(filter(lambda p: p >= 100, prices))

print(result)  # -> [120, 300]


# ---------------------------------------
# 8. Filter Students by Score
# ---------------------------------------
students = [
    ['Maria', 85],
    ['Kumar', 90],
    ['Max', 60]
]

# Keep students scoring above 70.

result = list(filter(lambda row: row[1] > 70, students))

print(result)

# -> [['Maria', 85], ['Kumar', 90]]


# ---------------------------------------
# 9. Filter Names Starting with M
# ---------------------------------------
students = [
    ['Maria', 85],
    ['Kumar', 90],
    ['Max', 60]
]

result = list(
    filter(lambda row: row[0].startswith('M'), students)
)

print(result)

# -> [['Maria', 85], ['Max', 60]]


# ---------------------------------------
# 10. Lambda with sorted()
# ---------------------------------------
# Sort students based on their scores.

students = [
    ['Maria', 85],
    ['Kumar', 90],
    ['Max', 60]
]

result = sorted(students, key=lambda row: row[1])

print(result)

# -> [['Max', 60], ['Maria', 85], ['Kumar', 90]]


# ---------------------------------------
# 11. Sort in Descending Order
# ---------------------------------------
students = [
    ['Maria', 85],
    ['Kumar', 90],
    ['Max', 60]
]

result = sorted(
    students,
    key=lambda row: row[1],
    reverse=True
)

print(result)

# -> [['Kumar', 90], ['Maria', 85], ['Max', 60]]


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. Lambda creates a small anonymous function.
# 2. Syntax: lambda arguments: expression
# 3. Lambda automatically returns the expression result.
# 4. Lambda can accept multiple arguments.
# 5. Lambda can be used with map(), filter(), and sorted().
# 6. Lambda contains only one expression.
# 7. Use def for more complex or reusable functions.

