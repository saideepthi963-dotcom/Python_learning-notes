
# ================================================================================
# PANDAS BASICS
# ----------------------------------------
# Pandas is a Python library used for working with tabular data.
#
# Main data structures:
# 1. Series    -> One-dimensional labeled data.
# 2. DataFrame -> Two-dimensional data with rows and columns.
#
# Import Pandas using the alias pd.
# ================================================================================

import pandas as pd


# ---------------------------------------
# 1. Creating a Series
# ---------------------------------------
# A Series stores one-dimensional data.

numbers = pd.Series([10, 20, 30, 40])

print(numbers)

# Output:
# 0    10
# 1    20
# 2    30
# 3    40
# dtype: int64 (may vary by platform)


# ---------------------------------------
# 2. Creating a DataFrame
# ---------------------------------------
# A DataFrame stores data in rows and columns.

data = {
    "Name": ["Maria", "John", "Sara"],
    "Age": [25, 30, 28],
    "City": ["Berlin", "Paris", "London"]
}

df = pd.DataFrame(data)

print(df)

# Output:
#     Name  Age    City
# 0  Maria   25  Berlin
# 1   John   30   Paris
# 2   Sara   28  London


# ---------------------------------------
# 3. Understanding DataFrame Shape
# ---------------------------------------
# shape returns (number_of_rows, number_of_columns).

print(df.shape)  # -> (3, 3)


# ---------------------------------------
# 4. Getting Column Names
# ---------------------------------------
# columns returns the DataFrame column labels.

print(df.columns)

# -> Index(['Name', 'Age', 'City'], dtype='object')


# ---------------------------------------
# 5. Viewing First and Last Rows
# ---------------------------------------
# head() shows the first 5 rows by default.
# tail() shows the last 5 rows by default.

print(df.head(2))
print(df.tail(2))


# ---------------------------------------
# 6. Selecting a Column
# ---------------------------------------
# Selecting one column returns a Series.

print(df["Name"])

# Output:
# 0    Maria
# 1     John
# 2     Sara


# ---------------------------------------
# 7. Selecting Multiple Columns
# ---------------------------------------
# Selecting multiple columns returns a DataFrame.

print(df[["Name", "Age"]])


# ---------------------------------------
# 8. Checking Data Types
# ---------------------------------------
# dtypes shows the data type of each column.

print(df.dtypes)

# Name    object
# Age      int64
# City    object
# Exact dtypes may vary.


# ---------------------------------------
# 9. DataFrame Information
# ---------------------------------------
# info() displays a summary of the DataFrame.

df.info()

# Shows row count, column names, types,
# non-null counts, and memory usage.


# ---------------------------------------
# 10. Basic Statistics
# ---------------------------------------
# describe() summarizes numerical columns.

print(df.describe())

# Includes count, mean, std, min, max,
# and quartiles for the Age column.


# ---------------------------------------
# 11. Adding a New Column
# ---------------------------------------
# A new column can be created through assignment.

df["Salary"] = [60000, 75000, 70000]

print(df)


# ---------------------------------------
# 12. Basic Column Calculations
# ---------------------------------------
# Operations apply to the entire numeric column.

df["Age_Next_Year"] = df["Age"] + 1

print(df[["Name", "Age", "Age_Next_Year"]])

# Output:
#     Name  Age  Age_Next_Year
# 0  Maria   25             26
# 1   John   30             31
# 2   Sara   28             29


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. Pandas is used for tabular data processing.
# 2. pd.Series() creates a one-dimensional Series.
# 3. pd.DataFrame() creates a table.
# 4. shape returns (rows, columns).
# 5. head() and tail() preview rows.
# 6. columns returns column names.
# 7. dtypes shows column data types.
# 8. info() summarizes the DataFrame.
# 9. describe() provides summary statistics.
# 10. New columns can be created using assignment.


