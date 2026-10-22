
# ================================================================================
# PANDAS - DATA CLEANING
# ----------------------------------------
# Data cleaning prepares raw data for analysis.
#
# Common tasks:
# 1. Find missing values
# 2. Remove missing values
# 3. Fill missing values
# 4. Remove duplicates
# 5. Change data types
# 6. Clean text values
# ================================================================================

import pandas as pd


# ---------------------------------------
# 1. Creating Sample Data
# ---------------------------------------
data = {
    "Name": ["Maria", "John", "Sara", "Sara", None],
    "Age": [25, 30, None, None, 28],
    "City": ["Berlin", "Paris", "London", "London", None],
    "Salary": ["60000", "75000", "70000", "70000", "50000"]
}

df = pd.DataFrame(data)

print(df)


# ---------------------------------------
# 2. Finding Missing Values
# ---------------------------------------
# isna() returns True for missing values.

print(df.isna())

# Count missing values in each column.

print(df.isna().sum())


# ---------------------------------------
# 3. Removing Missing Values
# ---------------------------------------
# dropna() removes rows containing missing values.
# It returns a new DataFrame by default.

cleaned = df.dropna()

print(cleaned)

# Original df remains unchanged.


# ---------------------------------------
# 4. Filling Missing Values
# ---------------------------------------
# fillna() replaces missing values.

filled = df.fillna({
    "Name": "Unknown",
    "Age": 0,
    "City": "Unknown"
})

print(filled)


# ---------------------------------------
# 5. Filling Missing Values with Mean
# ---------------------------------------
# mean() calculates the average of numeric values.
# Missing numeric values are skipped by default.

df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df)

# Mean Age: (25 + 30 + 28) / 3 = 27.666...


# ---------------------------------------
# 6. Finding Duplicate Rows
# ---------------------------------------
# duplicated() identifies repeated rows.

print(df.duplicated())

print("Duplicate Count:", df.duplicated().sum())

# Expected duplicate count: 1


# ---------------------------------------
# 7. Removing Duplicate Rows
# ---------------------------------------
# drop_duplicates() keeps the first occurrence.

cleaned = df.drop_duplicates()

print(cleaned)


# ---------------------------------------
# 8. Converting Data Types
# ---------------------------------------
# Salary values are currently strings.
# astype() converts them to integers.

df["Salary"] = df["Salary"].astype(int)

print(df.dtypes)

# Salary -> int64 (commonly)


# ---------------------------------------
# 9. Cleaning Text with str.strip()
# ---------------------------------------
# Remove extra spaces from text values.

names = pd.Series([" Maria ", " John ", " Sara "])

cleaned_names = names.str.strip()

print(cleaned_names)

# Output:
# Maria
# John
# Sara


# ---------------------------------------
# 10. Converting Text to Lowercase
# ---------------------------------------
cities = pd.Series(["BERLIN", "Paris", "LONDON"])

print(cities.str.lower())

# Output:
# berlin
# paris
# london


# ---------------------------------------
# 11. Replacing Values
# ---------------------------------------
# replace() changes matching values.

cities = pd.Series(["NY", "LA", "NY"])

result = cities.replace({
    "NY": "New York",
    "LA": "Los Angeles"
})

print(result)


# ---------------------------------------
# 12. Renaming Columns
# ---------------------------------------
# rename() changes column names.

renamed = df.rename(columns={
    "Name": "Employee_Name",
    "Salary": "Annual_Salary"
})

print(renamed.columns)


# ---------------------------------------
# 13. Resetting the Index
# ---------------------------------------
# reset_index(drop=True) creates a fresh index.

cleaned = df.drop_duplicates().reset_index(drop=True)

print(cleaned)


# ---------------------------------------
# 14. Converting Strings to Dates
# ---------------------------------------
# to_datetime() converts text into dates.

dates = pd.Series(["2026-01-10", "2026-02-15"])

converted = pd.to_datetime(dates)

print(converted)


# ---------------------------------------
# 15. Checking Data After Cleaning
# ---------------------------------------
print(df.info())

print(df.isna().sum())

print(df.head())


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. isna() identifies missing values.
# 2. isna().sum() counts missing values.
# 3. dropna() removes rows with missing values.
# 4. fillna() replaces missing values.
# 5. mean() can help fill missing numeric values.
# 6. duplicated() identifies duplicate rows.
# 7. drop_duplicates() removes duplicates.
# 8. astype() converts data types.
# 9. str.strip() removes extra spaces.
# 10. str.lower() converts text to lowercase.
# 11. replace() changes matching values.
# 12. rename() updates column names.
# 13. reset_index() resets row numbering.
# 14. to_datetime() converts values to dates.

