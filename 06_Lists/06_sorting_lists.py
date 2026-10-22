
# ================================================================================
# SORTING AND REVERSING LISTS
# ----------------------------------------
# Python provides methods to sort and reverse lists.
#
# sort()    -> Changes the original list.
# sorted()  -> Returns a new sorted list.
# reverse() -> Reverses the original list.
# reversed()-> Returns an iterator in reverse order.
# ================================================================================


# ---------------------------------------
# 1. sort() - Ascending Order
# ---------------------------------------
# sort() modifies the original list.

letters = ['c', 'a', 'b']

letters.sort()

print(letters)  # -> ['a', 'b', 'c']


# ---------------------------------------
# 2. sort() - Descending Order
# ---------------------------------------
# reverse=True sorts from largest to smallest.

letters = ['c', 'a', 'b']

letters.sort(reverse=True)

print(letters)  # -> ['c', 'b', 'a']


# ---------------------------------------
# 3. Sorting Numbers
# ---------------------------------------
numbers = [50, 10, 40, 20, 30]

numbers.sort()

print(numbers)  # -> [10, 20, 30, 40, 50]

numbers.sort(reverse=True)

print(numbers)  # -> [50, 40, 30, 20, 10]


# ---------------------------------------
# 4. sorted() - Creates a New List
# ---------------------------------------
# sorted() does not modify the original list.

letters = ['c', 'a', 'b']

new_list = sorted(letters)

print("Original:", letters)  # -> ['c', 'a', 'b']
print("Sorted:", new_list)   # -> ['a', 'b', 'c']


# ---------------------------------------
# 5. sorted() - Descending Order
# ---------------------------------------
letters = ['c', 'a', 'b']

new_list = sorted(letters, reverse=True)

print("Original:", letters)  # -> ['c', 'a', 'b']
print("Sorted:", new_list)   # -> ['c', 'b', 'a']


# ---------------------------------------
# 6. reverse() - Reverse Original List
# ---------------------------------------
# reverse() changes the original list.
# It does not sort the elements.

letters = ['c', 'a', 'b']

letters.reverse()

print(letters)  # -> ['b', 'a', 'c']


# ---------------------------------------
# 7. reversed() - Create Reverse Iterator
# ---------------------------------------
# Convert the iterator into a list using list().

letters = ['c', 'a', 'b']

new_list = list(reversed(letters))

print("Original:", letters)  # -> ['c', 'a', 'b']
print("Reversed:", new_list) # -> ['b', 'a', 'c']


# ---------------------------------------
# 8. Sorting Nested Lists
# ---------------------------------------
# Nested lists are compared element by element.

matrix = [
    ['d', 'e', 'f'],
    ['a', 'z', 'i'],
    ['a', 'a', 'c']
]

matrix.sort()

print(matrix)

# Output:
# [['a', 'a', 'c'], ['a', 'z', 'i'], ['d', 'e', 'f']]


# ---------------------------------------
# 9. Sorting One Row in a Nested List
# ---------------------------------------
matrix = [
    ['d', 'e', 'f'],
    ['z', 'a', 'i'],
    ['a', 'a', 'c']
]

matrix[1].sort()

print(matrix)

# Output:
# [['d', 'e', 'f'], ['a', 'i', 'z'], ['a', 'a', 'c']]


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. sort() modifies the original list.
# 2. sorted() returns a new sorted list.
# 3. reverse=True sorts in descending order.
# 4. reverse() reverses the original list.
# 5. reversed() returns a reverse iterator.
# 6. Reversing a list is different from sorting it.
# 7. Nested lists can also be sorted.
# 8. sort() and reverse() return None.

