
# ================================================================================
# PYTHON LISTS - ACCESSING LIST ELEMENTS
# ----------------------------------------
# We can access individual elements in a list using indexing.
# We can access multiple elements using slicing.
#
# Python list indexing starts from 0.
# ================================================================================


# ---------------------------------------
# 1. Positive Indexing
# ---------------------------------------
# Indexing starts from 0.

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[0])  # Apple
print(fruits[1])  # Banana
print(fruits[2])  # Mango
print(fruits[3])  # Orange


# ---------------------------------------
# 2. Negative Indexing
# ---------------------------------------
# Negative indexing starts from the end.
# -1 represents the last element.

fruits = ["Apple", "Banana", "Mango", "Orange"]

print(fruits[-1])  # Orange
print(fruits[-2])  # Mango
print(fruits[-3])  # Banana
print(fruits[-4])  # Apple


# ---------------------------------------
# 3. List Slicing
# ---------------------------------------
# Syntax: list[start:stop]
# Start is included, stop is excluded.

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[1:4])  # [20, 30, 40]
print(numbers[0:3])  # [10, 20, 30]
print(numbers[2:5])  # [30, 40, 50]


# ---------------------------------------
# 4. Slicing Without Start or Stop
# ---------------------------------------
# Leaving start empty means start from index 0.
# Leaving stop empty means continue to the end.

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[:3])  # [10, 20, 30]
print(numbers[3:])  # [40, 50, 60]
print(numbers[:])   # [10, 20, 30, 40, 50, 60]


# ---------------------------------------
# 5. Slicing with Step
# ---------------------------------------
# Syntax: list[start:stop:step]
# Step determines how many positions to move.

numbers = [10, 20, 30, 40, 50, 60]

print(numbers[::2])   # [10, 30, 50]
print(numbers[1::2])  # [20, 40, 60]
print(numbers[::3])   # [10, 40]


# ---------------------------------------
# 6. Reversing a List Using Slicing
# ---------------------------------------
# A negative step moves backward.

numbers = [10, 20, 30, 40, 50]

print(numbers[::-1])  # [50, 40, 30, 20, 10]


# ---------------------------------------
# 7. Accessing Nested Lists
# ---------------------------------------
# Nested lists contain lists inside another list.

students = [
    ["Alice", 90],
    ["Bob", 85],
    ["Charlie", 95]
]

print(students[0])     # ['Alice', 90]
print(students[0][0])  # Alice
print(students[1][1])  # 85
print(students[2][0])  # Charlie


# ---------------------------------------
# 8. Accessing First and Last Elements
# ---------------------------------------
fruits = ["Apple", "Banana", "Mango"]

print(fruits[0])   # Apple
print(fruits[-1])  # Mango


# ---------------------------------------
# 9. Index Out of Range
# ---------------------------------------
# Accessing an index that does not exist
# raises an IndexError.

fruits = ["Apple", "Banana", "Mango"]

# print(fruits[5])  # IndexError

# Slicing beyond the list length is allowed.

print(fruits[0:10])  # ['Apple', 'Banana', 'Mango']


# ---------------------------------------
# 10. Checking List Length
# ---------------------------------------
# len() returns the number of elements.

fruits = ["Apple", "Banana", "Mango"]

print(len(fruits))  # 3


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. Positive indexing starts from 0.
# 2. Negative indexing starts from -1.
# 3. Slicing extracts multiple elements.
# 4. The stop index is excluded.
# 5. Step controls how positions are selected.
# 6. [::-1] returns a reversed copy of a list.
# 7. Nested lists use multiple indexes.
# 8. Invalid indexes raise IndexError.
# 9. len() returns the number of elements.
