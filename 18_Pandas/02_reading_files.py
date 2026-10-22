
# ================================================================================
# PANDAS - READING AND WRITING FILES
# ----------------------------------------
# Pandas supports different file formats.
#
# Common functions:
# pd.read_csv()   -> Read CSV files.
# pd.read_json()  -> Read JSON files.
# pd.read_excel() -> Read Excel files.
#
# We can also save DataFrames to these formats.
# ================================================================================

import pandas as pd
from pathlib import Path


# ---------------------------------------
# 1. Creating Sample Data
# ---------------------------------------
# Create a small DataFrame for practice.

data = {
    "Name": ["Maria", "John", "Sara"],
    "Age": [25, 30, 28],
    "City": ["Berlin", "Paris", "London"]
}

df = pd.DataFrame(data)

print(df)


# ---------------------------------------
# 2. Creating Sample Files
# ---------------------------------------
# Save files inside the same folder as this script.
# These files will be used in the examples below.

folder = Path(__file__).resolve().parent

csv_file = folder / "students.csv"
json_file = folder / "students.json"
excel_file = folder / "students.xlsx"

df.to_csv(csv_file, index=False)
df.to_json(json_file, orient="records", indent=4)
df.to_excel(excel_file, index=False)

print("Sample files created")


# ---------------------------------------
# 3. Reading a CSV File
# ---------------------------------------
# read_csv() converts a CSV file to a DataFrame.

students = pd.read_csv(csv_file)

print(students)


# ---------------------------------------
# 4. Reading a JSON File
# ---------------------------------------
# read_json() converts JSON data to a DataFrame.

students = pd.read_json(json_file)

print(students)


# ---------------------------------------
# 5. Reading an Excel File
# ---------------------------------------
# read_excel() reads an Excel spreadsheet.
# Requires openpyxl for .xlsx files.

students = pd.read_excel(excel_file)

print(students)


# ---------------------------------------
# 6. Reading Only Selected Columns
# ---------------------------------------
# usecols selects specific CSV columns.

students = pd.read_csv(
    csv_file,
    usecols=["Name", "Age"]
)

print(students)


# ---------------------------------------
# 7. Reading Only a Few Rows
# ---------------------------------------
# nrows limits the number of rows loaded.

students = pd.read_csv(csv_file, nrows=2)

print(students)


# ---------------------------------------
# 8. Previewing Data
# ---------------------------------------
students = pd.read_csv(csv_file)

print(students.head(2))  # First 2 rows
print(students.tail(2))  # Last 2 rows


# ---------------------------------------
# 9. Checking Missing Values
# ---------------------------------------
# isnull().sum() counts missing values by column.

print(students.isnull().sum())

# Expected:
# Name    0
# Age     0
# City    0


# ---------------------------------------
# 10. Saving Data to CSV
# ---------------------------------------
# index=False excludes the DataFrame row index.

students.to_csv(
    folder / "students_output.csv",
    index=False
)

print("CSV saved successfully")


# ---------------------------------------
# 11. Saving Data to JSON
# ---------------------------------------
students.to_json(
    folder / "students_output.json",
    orient="records",
    indent=4
)

print("JSON saved successfully")


# ---------------------------------------
# 12. Saving Data to Excel
# ---------------------------------------
students.to_excel(
    folder / "students_output.xlsx",
    index=False
)

print("Excel saved successfully")


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. read_csv() reads CSV data.
# 2. read_json() reads JSON data.
# 3. read_excel() reads Excel spreadsheets.
# 4. Data is loaded into a DataFrame.
# 5. usecols selects specific CSV columns.
# 6. nrows limits the number of rows read.
# 7. head() and tail() preview data.
# 8. isnull().sum() counts missing values.
# 9. to_csv() saves data as CSV.
# 10. to_json() saves data as JSON.
# 11. to_excel() saves data as Excel.
# 12. index=False excludes row index values.


