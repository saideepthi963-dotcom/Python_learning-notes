
# ================================================================================
# NUMPY BASICS
# ----------------------------------------
# NumPy stands for Numerical Python.
# It is used to work with numerical arrays.
#
# NumPy provides:
# 1. Arrays
# 2. Fast numerical operations
# 3. Multidimensional data handling
#
# Import NumPy using the alias np.
# ================================================================================

import numpy as np


# ---------------------------------------
# 1. Creating a NumPy Array
# ---------------------------------------
# np.array() creates a NumPy array.

numbers = np.array([10, 20, 30, 40])

print(numbers)        # -> [10 20 30 40]
print(type(numbers))  # -> <class 'numpy.ndarray'>


# ---------------------------------------
# 2. Python List vs NumPy Array
# ---------------------------------------
# Python lists and NumPy arrays behave differently
# during mathematical operations.

numbers_list = [1, 2, 3]
numbers_array = np.array([1, 2, 3])

print(numbers_list * 2)   # -> [1, 2, 3, 1, 2, 3]
print(numbers_array * 2)  # -> [2 4 6]

# Lists repeat elements when multiplied by an integer.
# NumPy arrays multiply each element.


# ---------------------------------------
# 3. One-Dimensional Array (1D)
# ---------------------------------------
# A 1D array contains a single sequence of values.

arr = np.array([10, 20, 30])

print(arr)       # -> [10 20 30]
print(arr.ndim)  # -> 1


# ---------------------------------------
# 4. Two-Dimensional Array (2D)
# ---------------------------------------
# A 2D array contains rows and columns.

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr)

# Output:
# [[10 20 30]
#  [40 50 60]]

print(arr.ndim)  # -> 2


# ---------------------------------------
# 5. Array Shape
# ---------------------------------------
# shape returns the size of each dimension.

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr.shape)  # -> (2, 3)

# 2 rows and 3 columns.


# ---------------------------------------
# 6. Array Size
# ---------------------------------------
# size returns the total number of elements.

arr = np.array([10, 20, 30, 40])

print(arr.size)  # -> 4


# ---------------------------------------
# 7. Array Data Type
# ---------------------------------------
# dtype shows the data type of array elements.

arr = np.array([10, 20, 30])

print(arr.dtype)

# Output: An integer dtype, such as int64.
# Exact integer width may depend on the platform.


# ---------------------------------------
# 8. Creating Arrays with zeros()
# ---------------------------------------
# Creates an array filled with zeros.

arr = np.zeros(4, dtype=int)

print(arr)  # -> [0 0 0 0]


# ---------------------------------------
# 9. Creating Arrays with ones()
# ---------------------------------------
# Creates an array filled with ones.

arr = np.ones(4, dtype=int)

print(arr)  # -> [1 1 1 1]


# ---------------------------------------
# 10. Creating Arrays with arange()
# ---------------------------------------
# Similar to Python's range().

arr = np.arange(1, 6)

print(arr)  # -> [1 2 3 4 5]


# ---------------------------------------
# 11. Creating Arrays with linspace()
# ---------------------------------------
# Creates evenly spaced numbers between
# a start and an end value.

arr = np.linspace(0, 10, 5)

print(arr)  # -> [ 0.   2.5  5.   7.5 10. ]


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. NumPy is used for numerical computing.
# 2. np is the common NumPy alias.
# 3. np.array() creates an array.
# 4. ndarray is NumPy's array type.
# 5. ndim returns the number of dimensions.
# 6. shape returns the dimensions of an array.
# 7. size returns the total number of elements.
# 8. dtype returns the element data type.
# 9. zeros(), ones(), arange(), and linspace()
#    create arrays.


