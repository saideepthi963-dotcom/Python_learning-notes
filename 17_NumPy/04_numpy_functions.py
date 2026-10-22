
# ================================================================================
# IMPORTANT NUMPY FUNCTIONS
# ----------------------------------------
# NumPy provides built-in functions to analyze
# and transform numerical data.
# ================================================================================

import numpy as np


# ---------------------------------------
# 1. sum()
# ---------------------------------------
# Calculates the total of array elements.

numbers = np.array([10, 20, 30, 40])

print(np.sum(numbers))  # -> 100


# ---------------------------------------
# 2. mean()
# ---------------------------------------
# Calculates the average.

numbers = np.array([10, 20, 30, 40])

print(np.mean(numbers))  # -> 25.0


# ---------------------------------------
# 3. min() and max()
# ---------------------------------------
numbers = np.array([10, 20, 30, 40])

print(np.min(numbers))  # -> 10
print(np.max(numbers))  # -> 40


# ---------------------------------------
# 4. median()
# ---------------------------------------
# Returns the middle value of sorted data.

numbers = np.array([10, 20, 30, 40, 50])

print(np.median(numbers))  # -> 30.0


# ---------------------------------------
# 5. std()
# ---------------------------------------
# Calculates standard deviation.
# Measures how spread out the numbers are.

numbers = np.array([10, 20, 30])

print(round(np.std(numbers), 2))  # -> 8.16


# ---------------------------------------
# 6. reshape()
# ---------------------------------------
# Changes the shape of an array.
# The total number of elements must stay the same.

numbers = np.array([1, 2, 3, 4, 5, 6])

matrix = numbers.reshape(2, 3)

print(matrix)

# Output:
# [[1 2 3]
#  [4 5 6]]


# ---------------------------------------
# 7. flatten()
# ---------------------------------------
# Converts a multidimensional array into 1D.

matrix = np.array([
    [10, 20],
    [30, 40]
])

print(matrix.flatten())  # -> [10 20 30 40]


# ---------------------------------------
# 8. unique()
# ---------------------------------------
# Returns sorted unique values.

numbers = np.array([10, 20, 10, 30, 20])

print(np.unique(numbers))  # -> [10 20 30]


# ---------------------------------------
# 9. concatenate()
# ---------------------------------------
# Joins arrays together.

a = np.array([10, 20])
b = np.array([30, 40])

print(np.concatenate((a, b)))
# -> [10 20 30 40]


# ---------------------------------------
# 10. where()
# ---------------------------------------
# Selects values based on a condition.

scores = np.array([40, 75, 90, 30])

result = np.where(scores >= 50, "Pass", "Fail")

print(result)
# -> ['Fail' 'Pass' 'Pass' 'Fail']


# ---------------------------------------
# 11. Working with Rows and Columns
# ---------------------------------------
# axis=0 performs operations down rows,
# producing one result per column.
#
# axis=1 performs operations across columns,
# producing one result per row.

matrix = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print(np.sum(matrix, axis=0))
# -> [50 70 90] (column totals)

print(np.sum(matrix, axis=1))
# -> [60 150] (row totals)


# ---------------------------------------
# 12. Handling NaN Values
# ---------------------------------------
# NaN represents a missing or undefined numeric value.

numbers = np.array([10, np.nan, 30])

print(np.isnan(numbers))
# -> [False  True False]

print(np.nanmean(numbers))
# -> 20.0 (ignores NaN)


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. sum() calculates totals.
# 2. mean() calculates averages.
# 3. min() and max() find extreme values.
# 4. median() finds the middle value.
# 5. std() calculates standard deviation.
# 6. reshape() changes array dimensions.
# 7. flatten() returns a flattened copy.
# 8. unique() finds distinct elements.
# 9. concatenate() combines arrays.
# 10. where() selects values using conditions.
# 11. axis controls the direction of calculations.
# 12. nanmean() calculates averages ignoring NaN.


