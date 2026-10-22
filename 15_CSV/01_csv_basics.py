
# ================================================================================
# CSV FILE HANDLING IN PYTHON
# ----------------------------------------
# CSV stands for Comma-Separated Values.
# CSV files store tabular data in rows and columns.
#
# Python provides a built-in csv module.
#
# Common tools:
# csv.reader()     -> Read rows as lists.
# csv.writer()     -> Write rows.
# csv.DictReader() -> Read rows as dictionaries.
# csv.DictWriter() -> Write rows using dictionary keys.
# ================================================================================

import csv


# ---------------------------------------
# 1. Writing Data to a CSV File
# ---------------------------------------
# writerow() writes one row.
# writerows() writes multiple rows.

with open("students.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "City"])
    writer.writerow(["Maria", 25, "Berlin"])
    writer.writerow(["John", 30, "Paris"])

print("CSV file created")


# ---------------------------------------
# 2. Reading a CSV File
# ---------------------------------------
# reader() reads each row as a list.

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)

# Output:
# ['Name', 'Age', 'City']
# ['Maria', '25', 'Berlin']
# ['John', '30', 'Paris']


# ---------------------------------------
# 3. Reading CSV Using DictReader
# ---------------------------------------
# Uses column names as dictionary keys.

with open("students.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["Name"], row["City"])

# Output:
# Maria Berlin
# John Paris


# ---------------------------------------
# 4. Writing CSV Using DictWriter
# ---------------------------------------
# Write dictionaries using field names.

students = [
    {"Name": "Maria", "Age": 25},
    {"Name": "John", "Age": 30}
]

with open("employees.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "Age"])

    writer.writeheader()
    writer.writerows(students)

print("Employees CSV created")


# ---------------------------------------
# 5. Appending to a CSV File
# ---------------------------------------
# a mode adds new rows without overwriting.

with open("students.csv", "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Sara", 28, "London"])

print("New student added")


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. CSV stores data in rows and columns.
# 2. Python provides a built-in csv module.
# 3. csv.reader() reads rows as lists.
# 4. csv.writer() writes CSV rows.
# 5. DictReader uses column names as keys.
# 6. DictWriter writes dictionaries to CSV.
# 7. Use newline="" when opening CSV files.
# 8. CSV values are read as strings by default.
# 9. w overwrites files; a appends data.


