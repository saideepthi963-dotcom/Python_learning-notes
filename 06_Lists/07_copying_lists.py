
# ================================================================================
# COPYING LISTS (REFERENCE, SHALLOW COPY, DEEP COPY)
# ----------------------------------------
# In Python, assigning a list to another variable
# does not automatically create a new list.
#
# There are three important concepts:
# 1. Assignment (Reference)
# 2. Shallow Copy
# 3. Deep Copy
# ================================================================================


# ---------------------------------------
# 1. Assignment (Reference)
# ---------------------------------------
# Both variables refer to the same list.

letters = ['a', 'b', 'c']

letters_copy = letters
letters_copy.append('z')

print("Original:", letters)
# -> ['a', 'b', 'c', 'z']

print("Copy:", letters_copy)
# -> ['a', 'b', 'c', 'z']

# Both changed because they refer to the same object.


# ---------------------------------------
# 2. Shallow Copy Using copy()
# ---------------------------------------
# copy() creates a new outer list.

letters = ['a', 'b', 'c']

letters_copy = letters.copy()
letters_copy.append('z')

print("Original:", letters)
# -> ['a', 'b', 'c']

print("Copy:", letters_copy)
# -> ['a', 'b', 'c', 'z']

# The original list is unchanged.


# ---------------------------------------
# 3. Shallow Copy Using list()
# ---------------------------------------
# list() can also create a shallow copy.

numbers = [10, 20, 30]

numbers_copy = list(numbers)
numbers_copy.append(40)

print("Original:", numbers)
# -> [10, 20, 30]

print("Copy:", numbers_copy)
# -> [10, 20, 30, 40]


# ---------------------------------------
# 4. Shallow Copy with Nested Lists
# ---------------------------------------
# The outer list is copied.
# Inner lists are still shared.

matrix = [
    ['a', 'b'],
    ['c', 'd']
]

matrix_copy = matrix.copy()

matrix_copy[0].append('z')

print("Original:", matrix)
# -> [['a', 'b', 'z'], ['c', 'd']]

print("Copy:", matrix_copy)
# -> [['a', 'b', 'z'], ['c', 'd']]

# Changing an inner list affects both.


# ---------------------------------------
# 5. Deep Copy
# ---------------------------------------
# deepcopy() copies the outer and inner lists.
# Import the copy module first.

import copy

matrix = [
    ['a', 'b'],
    ['c', 'd']
]

matrix_copy = copy.deepcopy(matrix)

matrix_copy[0].append('z')

print("Original:", matrix)
# -> [['a', 'b'], ['c', 'd']]

print("Copy:", matrix_copy)
# -> [['a', 'b', 'z'], ['c', 'd']]

# Changing the nested copy does not affect the original.


# ---------------------------------------
# 6. Identity Comparison Using is
# ---------------------------------------
# is checks whether variables refer to the same object.

original = [10, 20, 30]

copy1 = original
copy2 = original.copy()

print(original is copy1)  # -> True
print(original is copy2)  # -> False

# Assignment shares the same object.
# copy() creates a different list object.


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. Assignment does not create a new list.
# 2. copy() creates a shallow copy.
# 3. list() can also create a shallow copy.
# 4. Shallow copies share nested mutable objects.
# 5. deepcopy() creates independent nested copies.
# 6. is checks whether objects are identical.
# 7. == checks whether values are equal.

