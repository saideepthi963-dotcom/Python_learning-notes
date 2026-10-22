
# ================================================================================
# DICTIONARY COMPREHENSION
# ----------------------------------------
# Dictionary comprehension creates a new dictionary
# using a shorter syntax.
#
# Syntax:
# {key_expression: value_expression for item in iterable if condition}
#
# It can:
# 1. Create dictionaries
# 2. Transform keys and values
# 3. Filter data
# ================================================================================


# ---------------------------------------
# 1. Traditional For Loop
# ---------------------------------------
# Create a dictionary of numbers and their squares.

squares = {}

for number in range(1, 5):
    squares[number] = number * number

print(squares)
# -> {1: 1, 2: 4, 3: 9, 4: 16}


# ---------------------------------------
# 2. Dictionary Comprehension
# ---------------------------------------
# Same result using shorter syntax.

squares = {number: number * number for number in range(1, 5)}

print(squares)
# -> {1: 1, 2: 4, 3: 9, 4: 16}


# ---------------------------------------
# 3. Creating Dictionary from Two Lists
# ---------------------------------------
# zip() combines values position by position.

names = ["Maria", "John", "Ali"]
scores = [85, 90, 75]

students = {
    name: score
    for name, score in zip(names, scores)
}

print(students)
# -> {'Maria': 85, 'John': 90, 'Ali': 75}


# ---------------------------------------
# 4. Filtering Dictionary Values
# ---------------------------------------
# Keep students with scores >= 80.

scores = {
    "Maria": 85,
    "John": 90,
    "Ali": 60
}

passed = {
    name: score
    for name, score in scores.items()
    if score >= 80
}

print(passed)
# -> {'Maria': 85, 'John': 90}


# ---------------------------------------
# 5. Transforming Dictionary Values
# ---------------------------------------
# Convert city names to uppercase.

cities = {
    "USA": "new york",
    "India": "hyderabad",
    "Germany": "berlin"
}

result = {
    country: city.upper()
    for country, city in cities.items()
}

print(result)
# -> {'USA': 'NEW YORK', 'India': 'HYDERABAD', 'Germany': 'BERLIN'}


# ---------------------------------------
# 6. Data With Baraa - Data Cleaning
# ---------------------------------------
# Task:
# 1. Keep only values that are strings.
# 2. Convert keys to uppercase.
# 3. Convert string values to lowercase.

user = {
    "id": 1,
    "name": "John",
    "age": 30,
    "city": "Berlin"
}

user_str = {
    key.upper(): value.lower()
    for key, value in user.items()
    if isinstance(value, str)
}

print(user_str)
# -> {'NAME': 'john', 'CITY': 'berlin'}


# ---------------------------------------
# 7. Dictionary Comprehension with if-else
# ---------------------------------------
# Label students based on their scores.

scores = {
    "Maria": 85,
    "John": 40,
    "Ali": 90
}

results = {
    name: "Pass" if score >= 50 else "Fail"
    for name, score in scores.items()
}

print(results)
# -> {'Maria': 'Pass', 'John': 'Fail', 'Ali': 'Pass'}


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. Dictionary comprehension creates a new dictionary.
# 2. It uses curly braces {}.
# 3. Every element contains a key and value.
# 4. We can transform keys and values.
# 5. We can filter elements using if.
# 6. We can use if-else to choose output values.
# 7. Use normal loops when logic becomes complicated.

