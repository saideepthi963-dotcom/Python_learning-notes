
# ================================================================================
# NUMPY ARRAY INDEXING AND SLICING
# ----------------------------------------
# Indexing accesses individual elements.
# Slicing accesses multiple elements.
#
# NumPy supports:
# 1. Positive indexing
# 2. Negative indexing
# 3. Array slicing
# 4. Row and column indexing
# 5. Boolean indexing
# ================================================================================

import numpy as np


# ---------------------------------------
# 1. Positive Indexing (1D Array)
# ---------------------------------------
# Indexing starts from 0.

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])  # -> 10
print(arr[2])  # -> 30
print(arr[4])  # -> 50


# ---------------------------------------
# 2. Negative Indexing
# ---------------------------------------
# Negative indexes start from the end.

arr = np.array([10, 20, 30, 40, 50])

print(arr[-1])  # -> 50
print(arr[-2])  # -> 40


# ---------------------------------------
# 3. Array Slicing
# ---------------------------------------
# Syntax: array[start:stop]
# Start is included and stop is excluded.

arr = np.array([10, 20, 30, 40, 50])

print(arr[1:4])  # -> [20 30 40]
print(arr[:3])   # -> [10 20 30]
print(arr[2:])   # -> [30 40 50]


# ---------------------------------------
# 4. Slicing with Step
# ---------------------------------------
# Syntax: array[start:stop:step]

arr = np.array([10, 20, 30, 40, 50, 60])

print(arr[::2])   # -> [10 30 50]
print(arr[1::2])  # -> [20 40 60]
print(arr[::-1])  # -> [60 50 40 30 20 10]


# ---------------------------------------
# 5. Accessing 2D Array Elements
# ---------------------------------------
# Syntax: array[row, column]

arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(arr[0, 0])  # -> 10
print(arr[0, 2])  # -> 30
print(arr[1, 1])  # -> 50


# ---------------------------------------
# 6. Accessing Entire Rows
# ---------------------------------------
arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[0])     # -> [10 20 30]
print(arr[1])     # -> [40 50 60]
print(arr[-1])    # -> [70 80 90]


# ---------------------------------------
# 7. Accessing Entire Columns
# ---------------------------------------
# : means select all rows.

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[:, 0])  # -> [10 40 70]
print(arr[:, 1])  # -> [20 50 80]
print(arr[:, 2])  # -> [30 60 90]


# ---------------------------------------
# 8. Slicing a 2D Array
# ---------------------------------------
# Select the first two rows and columns.

arr = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(arr[0:2, 0:2])

# Output:
# [[10 20]
#  [40 50]]


# ---------------------------------------
# 9. Boolean Indexing
# ---------------------------------------
# Use a condition to select matching values.

arr = np.array([10, 20, 30, 40, 50])

print(arr[arr > 25])  # -> [30 40 50]


# ---------------------------------------
# 10. Updating Array Elements
# ---------------------------------------
# Arrays are mutable.

arr = np.array([10, 20, 30, 40])

arr[1] = 200

print(arr)  # -> [ 10 200  30  40]


# ---------------------------------------
# 11. Slicing vs Copying
# ---------------------------------------
# NumPy slices usually share data with the original array.

arr = np.array([10, 20, 30])

part = arr[:2]
part[0] = 100

print(arr)  # -> [100  20  30]

# Use copy() when you need an independent copy.

arr = np.array([10, 20, 30])

part = arr[:2].copy()
part[0] = 100

print(arr)  # -> [10 20 30]


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. Indexing starts at 0.
# 2. Negative indexing accesses elements from the end.
# 3. Slicing selects multiple elements.
# 4. The stop index is excluded.
# 5. array[row, column] accesses 2D values.
# 6. : selects all elements along a dimension.
# 7. Boolean indexing filters values.
# 8. Array elements can be updated.
# 9. NumPy slices usually return views, not copies.
# 10. copy() creates an independent array.


