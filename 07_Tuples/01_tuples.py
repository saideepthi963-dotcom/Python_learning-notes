
# ================================================================================
# TUPLES IN PYTHON
# ----------------------------------------
# Tuples are ordered, immutable collections.
#
# Tuples:
# 1. Maintain order
# 2. Cannot be changed after creation
# 3. Allow duplicate values
# 4. Support indexing and slicing
# ================================================================================


# ---------------------------------------
# 1. Creating a Tuple
# ---------------------------------------
numbers = (10, 20, 30, 40)

print(numbers)        # -> (10, 20, 30, 40)
print(type(numbers))  # -> <class 'tuple'>


# ---------------------------------------
# 2. Empty and Single-Element Tuples
# ---------------------------------------
empty = ()

single = (10,)

print(empty)   # -> ()
print(single)  # -> (10,)

# The comma is required for a single-element tuple.


# ---------------------------------------
# 3. Accessing Tuple Elements
# ---------------------------------------
numbers = (10, 20, 30, 40)

print(numbers[0])   # -> 10
print(numbers[-1])  # -> 40
print(numbers[1:3]) # -> (20, 30)


# ---------------------------------------
# 4. Tuples Allow Duplicates
# ---------------------------------------
numbers = (10, 20, 10, 30)

print(numbers)  # -> (10, 20, 10, 30)


# ---------------------------------------
# 5. Tuples Are Immutable
# ---------------------------------------
numbers = (10, 20, 30)

# numbers[0] = 100
# TypeError: tuple object does not support item assignment

# Tuple elements cannot be reassigned.


# ---------------------------------------
# 6. Tuple Methods
# ---------------------------------------
numbers = (10, 20, 20, 30)

print(numbers.count(20))  # -> 2
print(numbers.index(30))  # -> 3


# ---------------------------------------
# 7. Tuple Unpacking
# ---------------------------------------
person = ("Maria", 29, "Spain")

name, age, country = person

print(name)     # -> Maria
print(age)      # -> 29
print(country)  # -> Spain


# ---------------------------------------
# 8. Looping Through a Tuple
# ---------------------------------------
fruits = ("Apple", "Banana", "Mango")

for fruit in fruits:
    print(fruit)

# Output:
# Apple
# Banana
# Mango


# ---------------------------------------
# 9. Sorting a Tuple
# ---------------------------------------
numbers = (30, 10, 20)

result = sorted(numbers)

print(result)  # -> [10, 20, 30]

# sorted() returns a new list.
# The original tuple is unchanged.


# ---------------------------------------
# 10. Converting Tuple to List
# ---------------------------------------
numbers = (10, 20, 30)

numbers_list = list(numbers)
numbers_list.append(40)

print(numbers_list)  # -> [10, 20, 30, 40]

new_tuple = tuple(numbers_list)

print(new_tuple)  # -> (10, 20, 30, 40)


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. Tuples are ordered and immutable.
# 2. Tuples allow duplicate values.
# 3. Indexing starts from 0.
# 4. Tuples support slicing.
# 5. count() counts occurrences.
# 6. index() finds the first matching position.
# 7. Tuples support unpacking.
# 8. sorted() returns a list, not a tuple.
# 9. A tuple can contain mutable objects such as lists.


