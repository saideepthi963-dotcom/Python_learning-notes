
# ================================================================================
# EXPLORING & ANALYZING LISTS
# ----------------------------------------
# Python provides built-in functions and methods to analyze lists.
#
# We can find maximum, minimum, total, length, count,
# index positions, and compare list values.
# ================================================================================


# ---------------------------------------
# 1. Basic Analysis Functions
# ---------------------------------------
numbers = [1, 5, 5, 4, 3]

print("Max:", max(numbers))      # -> 5
print("Min:", min(numbers))      # -> 1
print("Sum:", sum(numbers))      # -> 18
print("Length:", len(numbers))   # -> 5


# ---------------------------------------
# 2. all()
# ---------------------------------------
# Returns True if all elements are truthy.

print(all(numbers))          # -> True
print(all([1, 0, 2]))        # -> False
print(all(['a', '', 'b']))   # -> False
print(all(['a', 'c', 'b']))  # -> True

# 0 and empty strings are falsy.


# ---------------------------------------
# 3. any()
# ---------------------------------------
# Returns True if at least one element is truthy.

print(any(numbers))          # -> True
print(any([1, 0, 2]))        # -> True
print(any(['a', '', 'b']))   # -> True
print(any([0, 0, 0]))        # -> False


# ---------------------------------------
# 4. count()
# ---------------------------------------
# Counts how many times a value appears.

numbers = [1, 5, 5, 4, 3]

print(numbers.count(5))  # -> 2
print(numbers.count(1))  # -> 1


# ---------------------------------------
# 5. index()
# ---------------------------------------
# Returns the index of the first matching value.

numbers = [1, 5, 5, 4, 3]

print(numbers.index(5))  # -> 1
print(numbers.index(4))  # -> 3

# If the value does not exist, index() raises ValueError.


# ---------------------------------------
# 6. Membership Operators
# ---------------------------------------
# in checks whether a value exists.
# not in checks whether a value does not exist.

numbers = [1, 5, 5, 4, 3]

print(5 in numbers)      # -> True
print(8 in numbers)      # -> False
print(8 not in numbers)  # -> True


# ---------------------------------------
# 7. Equality Comparison
# ---------------------------------------
# == compares list values.

list1 = [1, 2, 3, 4]
list2 = [1, 2, 3]

print(list1 == list2)  # -> False

list3 = [1, 2, 3]

print(list2 == list3)  # -> True


# ---------------------------------------
# 8. Lexicographical Comparison
# ---------------------------------------
# Lists are compared element by element,
# starting from the first element.

list1 = [1, 2, 3]
list2 = [5, 2, 3]

print(list1 < list2)  # -> True
print(list1 > list2)  # -> False


# ---------------------------------------
# 9. Identity Comparison
# ---------------------------------------
# is checks whether two variables reference
# the exact same object.

list1 = [5, 8, 3]
list2 = [5, 8, 3]

print(list1 == list2)  # -> True
print(list1 is list2)  # -> False

# == checks values.
# is checks object identity.


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. max() returns the largest value.
# 2. min() returns the smallest value.
# 3. sum() calculates the total of numeric values.
# 4. len() returns the number of elements.
# 5. all() checks whether all elements are truthy.
# 6. any() checks whether at least one element is truthy.
# 7. count() counts occurrences of a value.
# 8. index() finds the first matching index.
# 9. in and not in check membership.
# 10. == compares values; is compares identity.

