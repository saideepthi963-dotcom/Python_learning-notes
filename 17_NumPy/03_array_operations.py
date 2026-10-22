
# ================================================================================
# NUMPY ARRAY OPERATIONS
# ----------------------------------------
# NumPy performs mathematical operations on arrays.
#
# Most operations work element by element.
# We can perform calculations without writing loops.
# ================================================================================

import numpy as np


# ---------------------------------------
# 1. Addition
# ---------------------------------------
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a + b)  # -> [11 22 33]


# ---------------------------------------
# 2. Subtraction
# ---------------------------------------
a = np.array([10, 20, 30])
b = np.array([1, 2, 3])

print(a - b)  # -> [9 18 27]


# ---------------------------------------
# 3. Multiplication
# ---------------------------------------
# * multiplies corresponding elements.

a = np.array([10, 20, 30])
b = np.array([2, 3, 4])

print(a * b)  # -> [20 60 120]


# ---------------------------------------
# 4. Division
# ---------------------------------------
a = np.array([10, 20, 30])
b = np.array([2, 4, 5])

print(a / b)  # -> [5. 5. 6.]


# ---------------------------------------
# 5. Operations with a Single Number
# ---------------------------------------
# NumPy applies the operation to every element.

numbers = np.array([10, 20, 30])

print(numbers + 5)  # -> [15 25 35]
print(numbers * 2)  # -> [20 40 60]
print(numbers / 10) # -> [1. 2. 3.]


# ---------------------------------------
# 6. Power Operations
# ---------------------------------------
numbers = np.array([2, 3, 4])

print(numbers ** 2)  # -> [4 9 16]
print(numbers ** 3)  # -> [8 27 64]


# ---------------------------------------
# 7. Comparison Operations
# ---------------------------------------
# Comparisons return Boolean arrays.

numbers = np.array([10, 20, 30, 40])

print(numbers > 20)
# -> [False False  True  True]

print(numbers == 20)
# -> [False  True False False]


# ---------------------------------------
# 8. Boolean Filtering
# ---------------------------------------
# Select values that satisfy a condition.

numbers = np.array([10, 20, 30, 40, 50])

result = numbers[numbers >= 30]

print(result)  # -> [30 40 50]


# ---------------------------------------
# 9. Combining Conditions
# ---------------------------------------
# Use & for AND and | for OR with NumPy arrays.
# Put each comparison inside parentheses.

numbers = np.array([10, 20, 30, 40, 50])

result = numbers[(numbers > 10) & (numbers < 50)]

print(result)  # -> [20 30 40]


# ---------------------------------------
# 10. Operations on 2D Arrays
# ---------------------------------------
a = np.array([
    [1, 2],
    [3, 4]
])

b = np.array([
    [10, 20],
    [30, 40]
])

print(a + b)

# Output:
# [[11 22]
#  [33 44]]


# ---------------------------------------
# 11. Broadcasting
# ---------------------------------------
# Broadcasting allows compatible arrays
# with different shapes to work together.

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

values = np.array([1, 2, 3])

print(matrix + values)

# Output:
# [[11 22 33]
#  [41 52 63]]


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. NumPy supports element-wise operations.
# 2. A single number can be applied to an array.
# 3. Comparisons create Boolean arrays.
# 4. Boolean indexing filters matching elements.
# 5. Use & and | for element-wise logical conditions.
# 6. Broadcasting works with compatible array shapes.
# 7. NumPy makes numerical calculations concise.


