
# ================================================================================
# MODIFYING LISTS (ADD, REMOVE, UPDATE)
# ----------------------------------------
# Lists are mutable, which means we can change their elements.
#
# We can:
# 1. Add elements
# 2. Remove elements
# 3. Update existing elements
# ================================================================================


# ================================================================================
# 1. ADDING ELEMENTS
# ================================================================================


# ---------------------------------------
# append()
# ---------------------------------------
# Adds one element at the end of a list.

letters = ['a', 'b', 'c']

letters.append('x')
letters.append('y')

print(letters)  # -> ['a', 'b', 'c', 'x', 'y']


# ---------------------------------------
# insert()
# ---------------------------------------
# Adds an element at a specific index.
# Existing elements shift to the right.

letters = ['a', 'b', 'c']

letters.insert(0, 'x')
letters.insert(3, 'y')

print(letters)  # -> ['x', 'a', 'b', 'y', 'c']


# ---------------------------------------
# Adding Rows to Nested Lists
# ---------------------------------------
# A nested list contains other lists.

matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

matrix.append(['x', 'y', 'z'])
matrix.insert(0, ['a', 'a', 'a'])

print(matrix)

# Output:
# [['a', 'a', 'a'], ['a', 'b', 'c'],
#  ['d', 'e', 'f'], ['g', 'h', 'i'],
#  ['x', 'y', 'z']]


# ---------------------------------------
# Adding Elements Inside Nested Lists
# ---------------------------------------
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

matrix[1].append('x')
matrix[0].insert(0, 'z')

print(matrix)

# Output:
# [['z', 'a', 'b', 'c'], ['d', 'e', 'f', 'x'],
#  ['g', 'h', 'i']]


# ================================================================================
# 2. REMOVING ELEMENTS
# ================================================================================


# ---------------------------------------
# clear()
# ---------------------------------------
# Removes all elements from the list.

letters = ['a', 'b', 'c']

letters.clear()

print(letters)  # -> []


# ---------------------------------------
# remove()
# ---------------------------------------
# Removes the first occurrence of a value.

letters = ['a', 'b', 'a']

letters.remove('a')

print(letters)  # -> ['b', 'a']

# If the value does not exist, remove() raises ValueError.


# ---------------------------------------
# pop()
# ---------------------------------------
# Removes an element using its index.
# Also returns the removed element.

letters = ['a', 'b', 'c']

removed = letters.pop(1)

print(letters)  # -> ['a', 'c']
print(removed)  # -> b


# ---------------------------------------
# pop() Without Index
# ---------------------------------------
# Removes the last element by default.

letters = ['a', 'b', 'c']

removed = letters.pop()

print(letters)  # -> ['a', 'b']
print(removed)  # -> c


# ---------------------------------------
# del Statement
# ---------------------------------------
# Removes an element using its index.

letters = ['a', 'b', 'c']

del letters[1]

print(letters)  # -> ['a', 'c']


# ---------------------------------------
# Removing Elements from Nested Lists
# ---------------------------------------
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

matrix[1].remove('e')
matrix[-1].pop(0)
matrix[0].pop()

print(matrix)

# Output:
# [['a', 'b'], ['d', 'f'], ['h', 'i']]


# ================================================================================
# 3. UPDATING ELEMENTS
# ================================================================================


# ---------------------------------------
# Updating List Values
# ---------------------------------------
# We can change elements using their indexes.

letters = ['a', 'b', 'c']

letters[0] = 'x'
letters[1] = 'y'
letters[2] = 'z'

print(letters)  # -> ['x', 'y', 'z']


# ---------------------------------------
# Updating Multiple Elements
# ---------------------------------------
# Slicing can replace multiple elements.

numbers = [10, 20, 30, 40]

numbers[1:3] = [200, 300]

print(numbers)  # -> [10, 200, 300, 40]


# ---------------------------------------
# Updating Nested Lists
# ---------------------------------------
matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]

matrix[-1] = ['x', 'y', 'z']
matrix[0][0] = '-'
matrix[1][1] = '-'
matrix[-1][-1] = '-'

print(matrix)

# Output:
# [['-', 'b', 'c'], ['d', '-', 'f'],
#  ['x', 'y', '-']]


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. Lists are mutable (changeable).
# 2. append() adds one element at the end.
# 3. insert() adds an element at a specific index.
# 4. clear() removes all elements.
# 5. remove() removes the first matching value.
# 6. pop() removes and returns an element.
# 7. del removes an element using its index.
# 8. Index assignment updates existing elements.
# 9. Slicing can update multiple elements.
# 10. Nested lists can also be modified.

