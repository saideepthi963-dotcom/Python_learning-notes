
# ================================================================================
# PANDAS - MERGING, JOINING, AND CONCATENATING DATAFRAMES
# ----------------------------------------
# Pandas combines data from multiple DataFrames.
#
# merge()  -> Combines data using matching keys.
# concat() -> Combines DataFrames vertically or horizontally.
#
# Common join types:
# inner, left, right, outer
# ================================================================================

import pandas as pd


# ---------------------------------------
# 1. Creating Sample DataFrames
# ---------------------------------------
employees = pd.DataFrame({
    "Employee_ID": [1, 2, 3],
    "Name": ["Maria", "John", "Sara"]
})

departments = pd.DataFrame({
    "Employee_ID": [1, 2, 4],
    "Department": ["IT", "HR", "Finance"]
})

print(employees)
print(departments)


# ---------------------------------------
# 2. INNER JOIN
# ---------------------------------------
# Keeps only matching Employee_ID values
# from both DataFrames.

result = pd.merge(
    employees,
    departments,
    on="Employee_ID",
    how="inner"
)

print(result)

# Output:
# Employee_ID  Name   Department
# 1            Maria  IT
# 2            John   HR


# ---------------------------------------
# 3. LEFT JOIN
# ---------------------------------------
# Keeps all rows from the left DataFrame.
# Missing matches contain NaN.

result = pd.merge(
    employees,
    departments,
    on="Employee_ID",
    how="left"
)

print(result)

# Employee_ID 3 (Sara) has no Department match.


# ---------------------------------------
# 4. RIGHT JOIN
# ---------------------------------------
# Keeps all rows from the right DataFrame.

result = pd.merge(
    employees,
    departments,
    on="Employee_ID",
    how="right"
)

print(result)

# Employee_ID 4 has no matching Name.


# ---------------------------------------
# 5. OUTER JOIN
# ---------------------------------------
# Keeps all keys from both DataFrames.

result = pd.merge(
    employees,
    departments,
    on="Employee_ID",
    how="outer"
)

print(result)

# Keeps Employee_ID values 1, 2, 3, 4.
# Unmatched values are missing (NaN).


# ---------------------------------------
# 6. Joining Using Different Column Names
# ---------------------------------------
# left_on and right_on specify different key names.

employees = pd.DataFrame({
    "Employee_ID": [1, 2, 3],
    "Name": ["Maria", "John", "Sara"]
})

departments = pd.DataFrame({
    "Emp_ID": [1, 2, 4],
    "Department": ["IT", "HR", "Finance"]
})

result = pd.merge(
    employees,
    departments,
    left_on="Employee_ID",
    right_on="Emp_ID",
    how="left"
)

print(result)


# ---------------------------------------
# 7. Concatenating Rows
# ---------------------------------------
# concat() with axis=0 stacks DataFrames vertically.
# ignore_index=True creates a fresh row index.

df1 = pd.DataFrame({
    "Name": ["Maria", "John"],
    "Age": [25, 30]
})

df2 = pd.DataFrame({
    "Name": ["Sara", "Ali"],
    "Age": [28, 22]
})

result = pd.concat(
    [df1, df2],
    axis=0,
    ignore_index=True
)

print(result)

# Output:
#     Name  Age
# 0  Maria   25
# 1   John   30
# 2   Sara   28
# 3    Ali   22


# ---------------------------------------
# 8. Concatenating Columns
# ---------------------------------------
# axis=1 places DataFrames side by side.
# Rows align using their indexes.

df1 = pd.DataFrame({
    "Name": ["Maria", "John"]
})

df2 = pd.DataFrame({
    "Salary": [60000, 75000]
})

result = pd.concat([df1, df2], axis=1)

print(result)

# Output:
#     Name  Salary
# 0  Maria   60000
# 1   John   75000


# ---------------------------------------
# 9. Handling Duplicate Column Names
# ---------------------------------------
# suffixes distinguish columns with the same name.

employees = pd.DataFrame({
    "Employee_ID": [1, 2],
    "Name": ["Maria", "John"]
})

managers = pd.DataFrame({
    "Employee_ID": [1, 2],
    "Name": ["Alex", "David"]
})

result = pd.merge(
    employees,
    managers,
    on="Employee_ID",
    suffixes=("_Employee", "_Manager")
)

print(result)


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. merge() combines DataFrames using matching keys.
# 2. inner keeps matching keys from both sides.
# 3. left keeps all rows from the left side.
# 4. right keeps all rows from the right side.
# 5. outer keeps all keys from both sides.
# 6. Unmatched values appear as missing values.
# 7. left_on and right_on join different column names.
# 8. concat(axis=0) stacks rows.
# 9. concat(axis=1) combines columns by index.
# 10. suffixes handle duplicate column names.
# 11. Pandas joins are similar to SQL joins.


