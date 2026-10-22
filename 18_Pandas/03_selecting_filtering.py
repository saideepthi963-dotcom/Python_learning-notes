
# ================================================================================
# PANDAS - SELECTING AND FILTERING DATA
# ----------------------------------------
# Pandas allows us to select specific rows and columns
# from a DataFrame.
#
# Important concepts:
# 1. Selecting columns
# 2. loc[]  -> Select by row/column labels
# 3. iloc[] -> Select by integer positions
# 4. Filtering rows using conditions
# ================================================================================

import pandas as pd


# ---------------------------------------
# 1. Creating a Sample DataFrame
# ---------------------------------------
data = {
    "Name": ["Maria", "John", "Sara", "Ali", "Max"],
    "Age": [25, 30, 28, 22, 35],
    "City": ["Berlin", "Paris", "London", "Berlin", "Paris"],
    "Salary": [60000, 75000, 70000, 50000, 90000]
}

df = pd.DataFrame(data)

print(df)


# ---------------------------------------
# 2. Selecting One Column
# ---------------------------------------
# A single column returns a Series.

print(df["Name"])

# Output:
# 0    Maria
# 1     John
# 2     Sara
# 3      Ali
# 4      Max


# ---------------------------------------
# 3. Selecting Multiple Columns
# ---------------------------------------
# Double brackets return a DataFrame.

print(df[["Name", "Salary"]])


# ---------------------------------------
# 4. Selecting Rows Using loc[]
# ---------------------------------------
# loc selects rows using index labels.
# Our DataFrame currently has labels 0, 1, 2, 3, 4.

print(df.loc[0])

# Select first three rows by label.
# Both endpoints are included with loc slicing.

print(df.loc[0:2])


# ---------------------------------------
# 5. Selecting Specific Rows and Columns
# ---------------------------------------
# Syntax: df.loc[row_labels, column_labels]

print(df.loc[0, "Name"])  # -> Maria

print(df.loc[0:2, ["Name", "Age"]])


# ---------------------------------------
# 6. Selecting Rows Using iloc[]
# ---------------------------------------
# iloc selects rows and columns by integer position.

print(df.iloc[0])  # First row
print(df.iloc[2])  # Third row

# Stop position is excluded.

print(df.iloc[0:3])  # First three rows


# ---------------------------------------
# 7. Selecting Rows and Columns with iloc[]
# ---------------------------------------
# Syntax: df.iloc[row_positions, column_positions]

print(df.iloc[0, 0])  # -> Maria
print(df.iloc[1, 1])  # -> 30

print(df.iloc[0:3, 0:2])

# First 3 rows and first 2 columns.


# ---------------------------------------
# 8. Filtering Rows Using a Condition
# ---------------------------------------
# Select employees older than 25.

result = df[df["Age"] > 25]

print(result)


# ---------------------------------------
# 9. Filtering with Multiple Conditions
# ---------------------------------------
# & means AND.
# Both conditions must be True.
# Always use parentheses around conditions.

result = df[
    (df["Age"] > 25) &
    (df["Salary"] >= 70000)
]

print(result)


# ---------------------------------------
# 10. Filtering Using OR
# ---------------------------------------
# | means OR.
# At least one condition must be True.

result = df[
    (df["City"] == "Berlin") |
    (df["Salary"] > 80000)
]

print(result)


# ---------------------------------------
# 11. Filtering with isin()
# ---------------------------------------
# isin() checks whether values belong to a list.

result = df[df["City"].isin(["Berlin", "Paris"])]

print(result)


# ---------------------------------------
# 12. Filtering Using between()
# ---------------------------------------
# between() includes both boundaries by default.

result = df[df["Age"].between(25, 30)]

print(result)


# ---------------------------------------
# 13. Filtering Strings with str.contains()
# ---------------------------------------
# Select names containing the letter "a".

result = df[
    df["Name"].str.contains("a", case=False, na=False)
]

print(result)


# ---------------------------------------
# 14. Selecting Only Matching Columns
# ---------------------------------------
# Filter rows and select specific columns together.

result = df.loc[
    df["Salary"] >= 70000,
    ["Name", "Salary"]
]

print(result)


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. df["column"] selects a Series.
# 2. df[["col1", "col2"]] selects a DataFrame.
# 3. loc[] uses labels.
# 4. iloc[] uses integer positions.
# 5. loc slicing includes the ending label.
# 6. iloc slicing excludes the stop position.
# 7. Conditions filter matching rows.
# 8. Use & for AND and | for OR.
# 9. Use parentheses around combined conditions.
# 10. isin() checks multiple possible values.
# 11. between() checks whether values fall in a range.
# 12. str.contains() searches text values.


