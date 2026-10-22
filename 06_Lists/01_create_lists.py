
# ================================================================================
# PYTHON LISTS - CREATING LISTS
# ----------------------------------------
# A list stores multiple values in a single variable.
#
# Lists are:
# 1. Ordered
# 2. Changeable (Mutable)
# 3. Allow duplicate values
# 4. Can store different data types
#
# Lists are created using square brackets [].
# ================================================================================


# ---------------------------------------
# 1. Creating a List
# ---------------------------------------
fruits = ["Apple", "Banana", "Mango"]

print(fruits)

# Output: ['Apple', 'Banana', 'Mango']


# ---------------------------------------
# 2. Creating an Empty List
# ---------------------------------------
fruits = []

print(fruits)        # []
print(type(fruits))  # <class 'list'>


# ---------------------------------------
# 3. List of Numbers
# ---------------------------------------
numbers = [10, 20, 30, 40, 50]

print(numbers)

# Output: [10, 20, 30, 40, 50]


# ---------------------------------------
# 4. List of Strings
# ---------------------------------------
countries = ["USA", "India", "Germany"]

print(countries)

# Output: ['USA', 'India', 'Germany']


# ---------------------------------------
# 5. List with Different Data Types
# ---------------------------------------
# A list can store different types of values.

student = ["Deepthi", 25, 85.5, True]

print(student)

# Output: ['Deepthi', 25, 85.5, True]


# ---------------------------------------
# 6. List with Duplicate Values
# ---------------------------------------
# Lists allow repeated values.

numbers = [10, 20, 10, 30, 20]

print(numbers)

# Output: [10, 20, 10, 30, 20]


# ---------------------------------------
# 7. Creating a List Using list()
# ---------------------------------------
# list() converts an iterable into a list.

letters = list("Python")

print(letters)

# Output: ['P', 'y', 't', 'h', 'o', 'n']


# ---------------------------------------
# 8. Creating a List Using range()
# ---------------------------------------
numbers = list(range(1, 6))

print(numbers)

# Output: [1, 2, 3, 4, 5]


# ---------------------------------------
# 9. Nested Lists
# ---------------------------------------
# A nested list is a list inside another list.

students = [
    ["Alice", 90],
    ["Bob", 85],
    ["Charlie", 95]
]

print(students)

# Output:
# [['Alice', 90], ['Bob', 85], ['Charlie', 95]]


# ---------------------------------------
# 10. Checking the List Data Type
# ---------------------------------------
fruits = ["Apple", "Banana", "Mango"]

print(type(fruits))  # <class 'list'>


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. Lists are created using square brackets [].
# 2. Lists store multiple values.
# 3. Lists maintain insertion order.
# 4. Lists are mutable (can be changed).
# 5. Lists allow duplicate values.
# 6. Lists can contain different data types.
# 7. list() can create lists from iterables.
# 8. Lists can contain other lists.

