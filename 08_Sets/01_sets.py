
# ================================================================================
# SETS IN PYTHON
# ----------------------------------------
# Sets are unordered collections of unique values.
#
# Sets:
# 1. Do not allow duplicates
# 2. Are mutable
# 3. Do not support indexing
# 4. Support mathematical set operations
# ================================================================================


# ---------------------------------------
# 1. Creating a Set
# ---------------------------------------
numbers = {10, 20, 30}

print(numbers)        # Order may vary
print(type(numbers))  # -> <class 'set'>


# ---------------------------------------
# 2. Removing Duplicate Values
# ---------------------------------------
numbers = {10, 30, 20, 10}

print(numbers)  # -> {10, 20, 30} (order may vary)


# ---------------------------------------
# 3. Creating an Empty Set
# ---------------------------------------
empty_set = set()

print(empty_set)        # -> set()
print(type(empty_set))  # -> <class 'set'>

# {} creates an empty dictionary, not a set.


# ---------------------------------------
# 4. Adding Elements
# ---------------------------------------
numbers = {10, 20, 30}

numbers.add(40)

print(numbers)  # Contains 10, 20, 30, 40


# ---------------------------------------
# 5. Adding Multiple Elements
# ---------------------------------------
numbers = {10, 20}

numbers.update([30, 40])

print(numbers)  # Contains 10, 20, 30, 40


# ---------------------------------------
# 6. Removing Elements
# ---------------------------------------
numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)  # Contains 10, 30

# remove() raises KeyError if the value does not exist.


# ---------------------------------------
# 7. discard()
# ---------------------------------------
# Removes an element if it exists.
# Does not raise an error for a missing value.

numbers = {10, 20, 30}

numbers.discard(100)

print(numbers)  # Contains 10, 20, 30


# ---------------------------------------
# 8. Union
# ---------------------------------------
# Combines all unique elements.

a = {10, 20, 30}
b = {30, 40, 50}

print(a.union(b))
print(a | b)

# Both contain 10, 20, 30, 40, 50


# ---------------------------------------
# 9. Intersection
# ---------------------------------------
# Returns elements common to both sets.

a = {10, 20, 30}
b = {30, 40, 50}

print(a.intersection(b))  # -> {30}
print(a & b)              # -> {30}


# ---------------------------------------
# 10. Difference
# ---------------------------------------
# Returns elements in one set but not another.

a = {10, 20, 30}
b = {30, 40, 50}

print(a.difference(b))  # Contains 10, 20
print(a - b)            # Contains 10, 20


# ---------------------------------------
# 11. Symmetric Difference
# ---------------------------------------
# Returns elements that belong to either set,
# but not both.

a = {10, 20, 30}
b = {30, 40, 50}

print(a.symmetric_difference(b))
print(a ^ b)

# Both contain 10, 20, 40, 50


# ---------------------------------------
# 12. Subset and Superset
# ---------------------------------------
a = {10, 20}
b = {10, 20, 30, 40}

print(a.issubset(b))    # -> True
print(b.issuperset(a))  # -> True


# ---------------------------------------
# 13. Disjoint Sets
# ---------------------------------------
# Two sets are disjoint if they share no elements.

a = {10, 20}
b = {30, 40}

print(a.isdisjoint(b))  # -> True


# ---------------------------------------
# 14. Membership Check
# ---------------------------------------
numbers = {10, 20, 30}

print(20 in numbers)      # -> True
print(50 not in numbers)  # -> True


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. Sets store unique values.
# 2. Sets are unordered and not indexed.
# 3. set() creates an empty set.
# 4. add() inserts one element.
# 5. update() adds multiple elements.
# 6. remove() raises an error if a value is missing.
# 7. discard() safely removes a value.
# 8. Union combines unique values.
# 9. Intersection finds common values.
# 10. Difference finds values missing from another set.
# 11. Symmetric difference finds values not shared.
# 12. Subset, superset, and disjoint check relationships.


