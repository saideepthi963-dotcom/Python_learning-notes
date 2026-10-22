
# ================================================================================
# LIST COMPREHENSIONS
# ----------------------------------------
# List comprehension creates a new list using shorter syntax.
#
# It combines:
# 1. Iteration
# 2. Transformation
# 3. Optional filtering
#
# Syntax:
# [expression for item in iterable if condition]
# ================================================================================


# ---------------------------------------
# 1. Traditional For Loop
# ---------------------------------------
# Create a list of numbers from 1 to 5.

numbers = []

for number in range(1, 6):
    numbers.append(number)

print(numbers)  # -> [1, 2, 3, 4, 5]


# ---------------------------------------
# 2. List Comprehension
# ---------------------------------------
# Same result using shorter syntax.

numbers = [number for number in range(1, 6)]

print(numbers)  # -> [1, 2, 3, 4, 5]


# ---------------------------------------
# 3. Transforming Values
# ---------------------------------------
# Multiply each number by 2.

numbers = [1, 2, 3, 4, 5]

doubled = [number * 2 for number in numbers]

print(doubled)  # -> [2, 4, 6, 8, 10]


# ---------------------------------------
# 4. Filtering Values
# ---------------------------------------
# Keep only even numbers.

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [number for number in numbers if number % 2 == 0]

print(even_numbers)  # -> [2, 4, 6]


# ---------------------------------------
# 5. Converting Strings to Uppercase
# ---------------------------------------
fruits = ['apple', 'banana', 'mango']

uppercase_fruits = [fruit.upper() for fruit in fruits]

print(uppercase_fruits)
# -> ['APPLE', 'BANANA', 'MANGO']


# ---------------------------------------
# 6. Filtering Strings
# ---------------------------------------
# Keep words with more than 4 characters.

words = ['SQL', 'Python', 'Java', 'Databricks']

long_words = [word for word in words if len(word) > 4]

print(long_words)  # -> ['Python', 'Databricks']


# ---------------------------------------
# 7. Data With Baraa - Domain Cleaning
# ---------------------------------------
# Task:
# 1. Keep domains containing a dot.
# 2. Convert domains to lowercase.

domains = [
    'www.google.com',
    'openai.com',
    'localhost',
    'WWW.DATAWITHBARAA.COM'
]

cleaned = [
    domain.lower()
    for domain in domains
    if '.' in domain
]

print(cleaned)

# Output:
# ['www.google.com', 'openai.com', 'www.datawithbaraa.com']


# ---------------------------------------
# 8. List Comprehension with if-else
# ---------------------------------------
# Label numbers as Even or Odd.

numbers = [1, 2, 3, 4, 5]

result = ['Even' if number % 2 == 0 else 'Odd' for number in numbers]

print(result)

# -> ['Odd', 'Even', 'Odd', 'Even', 'Odd']


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. List comprehension creates a new list.
# 2. It provides shorter syntax than a for loop.
# 3. It can transform values.
# 4. It can filter values using if.
# 5. if-else can be used to choose output values.
# 6. Use normal loops when comprehension becomes difficult to read.


