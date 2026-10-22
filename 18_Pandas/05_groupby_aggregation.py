
# ================================================================================
# PANDAS - GROUPBY AND AGGREGATION
# ----------------------------------------
# groupby() groups rows based on one or more columns.
# Aggregation calculates results for each group.
#
# Common aggregation functions:
# sum(), mean(), count(), min(), max(), size()
# ================================================================================

import pandas as pd


# ---------------------------------------
# 1. Creating Sample Data
# ---------------------------------------
data = {
    "Name": ["Maria", "John", "Sara", "Ali", "Max"],
    "Department": ["IT", "HR", "IT", "HR", "IT"],
    "Salary": [60000, 50000, 70000, 55000, 80000],
    "Age": [25, 30, 28, 22, 35]
}

df = pd.DataFrame(data)

print(df)


# ---------------------------------------
# 2. Grouping by One Column
# ---------------------------------------
# Calculate total salary for each department.

result = df.groupby("Department")["Salary"].sum()

print(result)

# Output:
# Department
# HR    105000
# IT    210000


# ---------------------------------------
# 3. Average Salary by Department
# ---------------------------------------
# mean() calculates the average.

result = df.groupby("Department")["Salary"].mean()

print(result)

# Output:
# Department
# HR    52500.0
# IT    70000.0


# ---------------------------------------
# 4. Counting Employees
# ---------------------------------------
# size() counts rows in each group.

result = df.groupby("Department").size()

print(result)

# Output:
# Department
# HR    2
# IT    3


# ---------------------------------------
# 5. Minimum and Maximum Salary
# ---------------------------------------
result = df.groupby("Department")["Salary"].min()

print(result)

# HR -> 50000
# IT -> 60000

result = df.groupby("Department")["Salary"].max()

print(result)

# HR -> 55000
# IT -> 80000


# ---------------------------------------
# 6. Multiple Aggregations with agg()
# ---------------------------------------
# agg() applies multiple calculations.

result = df.groupby("Department")["Salary"].agg(
    ["sum", "mean", "min", "max"]
)

print(result)


# ---------------------------------------
# 7. Named Aggregations
# ---------------------------------------
# Create meaningful output column names.

result = df.groupby("Department").agg(
    Total_Salary=("Salary", "sum"),
    Average_Salary=("Salary", "mean"),
    Employee_Count=("Name", "count")
)

print(result)


# ---------------------------------------
# 8. Grouping by Multiple Columns
# ---------------------------------------
# Group by Department and Age.

result = df.groupby(
    ["Department", "Age"]
)["Salary"].sum()

print(result)


# ---------------------------------------
# 9. Using reset_index()
# ---------------------------------------
# Convert grouped index back into a column.

result = (
    df.groupby("Department")["Salary"]
    .sum()
    .reset_index()
)

print(result)

# Output:
#   Department  Salary
# 0         HR  105000
# 1         IT  210000


# ---------------------------------------
# 10. Sorting Aggregation Results
# ---------------------------------------
# Sort departments by highest total salary.

result = (
    df.groupby("Department")["Salary"]
    .sum()
    .sort_values(ascending=False)
)

print(result)

# IT -> 210000
# HR -> 105000


# ---------------------------------------
# 11. count() vs size()
# ---------------------------------------
# count() counts non-missing values.
# size() counts all rows, including those with missing values.

sample = pd.DataFrame({
    "Department": ["IT", "IT", "HR"],
    "Salary": [60000, None, 50000]
})

print(sample.groupby("Department")["Salary"].count())

# HR -> 1
# IT -> 1

print(sample.groupby("Department").size())

# HR -> 1
# IT -> 2


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. groupby() groups rows based on column values.
# 2. sum() calculates group totals.
# 3. mean() calculates group averages.
# 4. count() counts non-missing values.
# 5. size() counts rows.
# 6. min() and max() find group extremes.
# 7. agg() performs multiple aggregations.
# 8. reset_index() converts group labels into columns.
# 9. sort_values() sorts aggregation results.
# 10. groupby() is similar to GROUP BY in SQL.


