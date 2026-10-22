
# ================================================================================
# ITERATION TOOLS (ENUMERATE, REVERSED, ZIP, MAP, FILTER)
# ----------------------------------------
# Python provides built-in tools to work with iterables.
# They help us access, combine, transform, and filter values.
# ================================================================================


# ---------------------------------------
# 1. Basic Iteration with Transformation
# ---------------------------------------
# Convert lowercase letters to uppercase using a for loop.

letters = ['a', 'b', 'c']
new_list = []

for letter in letters:
    new_list.append(letter.upper())

print(new_list)  # -> ['A', 'B', 'C']


# ---------------------------------------
# 2. enumerate()
# ---------------------------------------
# Returns both index and value while looping.

letters = ['a', 'b', 'c']

for index, value in enumerate(letters):
    print(index, value)

# Output:
# 0 a
# 1 b
# 2 c


# ---------------------------------------
# 3. enumerate() with start
# ---------------------------------------
# We can choose the starting counter.

fruits = ['Apple', 'Banana', 'Mango']

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)

# Output:
# 1 Apple
# 2 Banana
# 3 Mango


# ---------------------------------------
# 4. reversed()
# ---------------------------------------
# Iterates over elements in reverse order.

letters = ['a', 'b', 'c']

for letter in reversed(letters):
    print(letter)

# Output:
# c
# b
# a


# ---------------------------------------
# 5. zip()
# ---------------------------------------
# Combines values from different iterables by position.
# Stops at the shortest iterable.

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

for letter, number in zip(letters, numbers):
    print(letter, number)

# Output:
# a 1
# b 2
# c 3


# ---------------------------------------
# 6. map()
# ---------------------------------------
# Applies a function to every element.

letters = ['a', 'b', 'c']

result = list(map(str.upper, letters))

print(result)  # -> ['A', 'B', 'C']


# ---------------------------------------
# 7. map() - Convert Data Types
# ---------------------------------------
# Convert string numbers into integers.

numbers = ['1', '2', '3']

result = list(map(int, numbers))

print(result)  # -> [1, 2, 3]


# ---------------------------------------
# 8. map() - Remove Extra Spaces
# ---------------------------------------
names = [' Maria ', ' John ', ' Kumar ']

result = list(map(str.strip, names))

print(result)  # -> ['Maria', 'John', 'Kumar']


# ---------------------------------------
# 9. filter()
# ---------------------------------------
# Keeps only elements that satisfy a condition.

letters = ['a', '', 'b', None, 'c', False]

result = list(filter(bool, letters))

print(result)  # -> ['a', 'b', 'c']

# Empty strings, None, and False are removed.


# ---------------------------------------
# 10. filter() - Alphabetic Values
# ---------------------------------------
# Keep only strings containing letters.

items = ['sql', '123', 'python', '42']

result = list(filter(str.isalpha, items))

print(result)  # -> ['sql', 'python']


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. enumerate() gives index and value.
# 2. reversed() iterates in reverse order.
# 3. zip() pairs elements from iterables.
# 4. map() applies a function to every element.
# 5. filter() keeps elements that satisfy a condition.
# 6. map(), filter(), and zip() return iterators.
# 7. list() converts their results into lists.


