
# ================================================================================
# LIST UNPACKING
# ----------------------------------------
# List unpacking assigns list elements to multiple variables.
#
# The * operator collects remaining values into a list.
# The _ variable is commonly used to ignore values.
# ================================================================================


# ---------------------------------------
# 1. Basic List Unpacking
# ---------------------------------------
fruits = ['Apple', 'Banana', 'Mango']

a, b, c = fruits

print(a)  # -> Apple
print(b)  # -> Banana
print(c)  # -> Mango


# ---------------------------------------
# 2. Unpacking with *
# ---------------------------------------
# * collects the remaining middle elements.

person = ['Maria', 29, 'Data Engineer', 'City', 'Spain']

name, *details, country = person

print(name)      # -> Maria
print(details)   # -> [29, 'Data Engineer', 'City']
print(country)   # -> Spain


# ---------------------------------------
# 3. Star at the Beginning
# ---------------------------------------
# * can collect values from the beginning.

person = ['Maria', 29, 'Data Engineer', 'City', 'Spain']

*details, city, country = person

print(details)   # -> ['Maria', 29, 'Data Engineer']
print(city)      # -> City
print(country)   # -> Spain


# ---------------------------------------
# 4. Unpacking Strings
# ---------------------------------------
# Strings are iterable, so they can be unpacked.

word = 'Hi'

first, *rest = word

print(first)  # -> H
print(rest)   # -> ['i']


# ---------------------------------------
# 5. Empty List with *
# ---------------------------------------
# If no remaining values exist, * collects an empty list.

word = 'H'

first, *rest = word

print(first)  # -> H
print(rest)   # -> []


# ---------------------------------------
# 6. Ignoring Values with _
# ---------------------------------------
# _ is used for values we do not need.

person = ['Maria', 29, 'Data Engineer', 'Spain']

name, _, role, _ = person

print(name)  # -> Maria
print(role)  # -> Data Engineer


# ---------------------------------------
# 7. Ignoring Multiple Values
# ---------------------------------------
# *_ collects values that we do not need.

person = ['Maria', 29, 'Data Engineer', 'Spain']

*_, country = person

print(country)  # -> Spain


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. Unpacking assigns elements to separate variables.
# 2. Without *, variable count must match element count.
# 3. * collects remaining values into a list.
# 4. * can appear at the beginning, middle, or end.
# 5. _ is a convention for ignored values.
# 6. Unpacking also works with strings and tuples.

