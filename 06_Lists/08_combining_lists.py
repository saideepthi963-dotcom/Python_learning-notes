
# ================================================================================
# COMBINING LISTS
# ----------------------------------------
# Python provides different ways to combine lists.
#
# 1. + operator
# 2. append()
# 3. extend()
# 4. zip()
# ================================================================================


# ---------------------------------------
# 1. Combining Lists Using +
# ---------------------------------------
# + creates a new list.
# The original lists remain unchanged.

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

combined = letters + numbers

print(combined)
# -> ['a', 'b', 'c', 1, 2, 3]

print(letters)  # -> ['a', 'b', 'c']
print(numbers)  # -> [1, 2, 3]


# ---------------------------------------
# 2. append() with Another List
# ---------------------------------------
# append() adds the entire list as one element.

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

numbers.append(letters)

print(numbers)
# -> [1, 2, 3, ['a', 'b', 'c']]

# Notice the nested list.


# ---------------------------------------
# 3. extend()
# ---------------------------------------
# extend() adds each element individually.
# It modifies the original list.

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

numbers.extend(letters)

print(numbers)
# -> [1, 2, 3, 'a', 'b', 'c']


# ---------------------------------------
# 4. append() vs extend()
# ---------------------------------------
a = [1, 2]
b = [3, 4]

a.append(b)

print(a)
# -> [1, 2, [3, 4]]

a = [1, 2]

a.extend(b)

print(a)
# -> [1, 2, 3, 4]


# ---------------------------------------
# 5. Combining Lists Using zip()
# ---------------------------------------
# zip() pairs elements based on their positions.
# It stops at the shortest iterable by default.

letters = ['a', 'b', 'c']
numbers = [1, 2, 3]

combined = list(zip(letters, numbers))

print(combined)
# -> [('a', 1), ('b', 2), ('c', 3)]

# Each pair is a tuple.


# ---------------------------------------
# 6. zip() with Different Lengths
# ---------------------------------------
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]

combined = list(zip(letters, numbers))

print(combined)
# -> [('a', 1), ('b', 2), ('c', 3)]

# The extra number 4 is not included.


# ---------------------------------------
# 7. zip() with Three Iterables
# ---------------------------------------
letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4]
word = "Hi"

combined = list(zip(letters, numbers, word))

print(combined)
# -> [('a', 1, 'H'), ('b', 2, 'i')]


# ---------------------------------------
# 8. Practical Example: IDs and Names
# ---------------------------------------
ids = [101, 102, 103]
names = ['Ali', 'Sara', 'John']

employees = list(zip(ids, names))

print(employees)
# -> [(101, 'Ali'), (102, 'Sara'), (103, 'John')]


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. + combines lists into a new list.
# 2. append() adds one object to the end.
# 3. append(list) creates a nested list.
# 4. extend() adds elements individually.
# 5. extend() changes the original list.
# 6. zip() combines values position by position.
# 7. zip() returns an iterator of tuples.
# 8. zip() stops at the shortest iterable by default.

