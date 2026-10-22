# Module 5 Cheat Sheet: Python Utilities

## Exception Handling

| Method / Concept | Description | Code Example |
|---|---|---|
| `try` | Contains code that might raise an exception. | `try: result = 10 / 0` |
| `except` | Handles a matching exception. | `except ZeroDivisionError: print("Error")` |
| `else` | Runs when no exception occurs in `try`. | `else: print("Success")` |
| `finally` | Runs when leaving the `try` statement, whether an error occurs or not. | `finally: print("Finished")` |
| `as e` | Captures the exception object. | `except ValueError as e:` |
| `raise` | Raises an exception explicitly. | `raise ValueError("Invalid age")` |
| `ValueError` | Occurs when a valid operation receives an inappropriate value. | `int("abc")` |
| `TypeError` | Occurs when an operation receives an inappropriate type. | `"10" + 5` |
| `ZeroDivisionError` | Occurs when dividing a number by zero. | `10 / 0` |
| `IndexError` | Occurs when accessing an invalid sequence index. | `[1, 2][5]` |
| `KeyError` | Occurs when accessing a missing dictionary key. | `{"a": 1}["b"]` |
| `FileNotFoundError` | Occurs when a requested file is not found. | `open("missing.txt", "r")` |

## File Handling

| Method / Concept | Description | Code Example |
|---|---|---|
| `open()` | Opens a file. | `open("data.txt", "r")` |
| `"r"` | Opens a file for reading. | `open("data.txt", "r")` |
| `"w"` | Writes to a file, overwriting existing content. | `open("data.txt", "w")` |
| `"a"` | Appends data to a file. | `open("data.txt", "a")` |
| `"x"` | Creates a new file; errors if it already exists. | `open("new.txt", "x")` |
| `with` | Automatically closes the file when leaving the block. | `with open("data.txt") as f:` |
| `read()` | Reads file contents as a string. | `content = file.read()` |
| `readline()` | Reads one line. | `line = file.readline()` |
| `readlines()` | Reads all lines into a list. | `lines = file.readlines()` |
| `write()` | Writes a string to a file. | `file.write("Hello")` |
| `Path.exists()` | Checks whether a path exists. | `Path("data.txt").exists()` |

## Modules and Packages

| Method / Concept | Description | Code Example |
|---|---|---|
| `import` | Imports a module. | `import random` |
| `from ... import` | Imports a specific name from a module. | `from pathlib import Path` |
| `as` | Creates an import alias. | `import random as rnd` |
| Custom Module | Imports code from another Python file. | `import calculator` |
| Package | Organizes related Python modules. | `from my_package import calculator` |
| `__name__` | Special variable identifying a module. | `print(__name__)` |
| `__main__` | Value assigned to `__name__` when a module runs directly as the main program. | `if __name__ == "__main__":` |
| `pip` | Installs third-party Python packages. | `python -m pip install requests` |

## JSON

| Method / Concept | Description | Code Example |
|---|---|---|
| `import json` | Imports Python's JSON module. | `import json` |
| `json.loads()` | Converts a JSON string into a Python object. | `json.loads('{"a": 1}')` |
| `json.dumps()` | Converts a Python object into a JSON string. | `json.dumps({"a": 1})` |
| `json.load()` | Reads JSON data from an open file. | `data = json.load(file)` |
| `json.dump()` | Writes Python data as JSON to an open file. | `json.dump(data, file)` |
| `indent` | Adds indentation for readable JSON. | `json.dumps(data, indent=4)` |
| `JSONDecodeError` | Exception raised for invalid JSON. | `except json.JSONDecodeError:` |

## CSV

| Method / Concept | Description | Code Example |
|---|---|---|
| `import csv` | Imports Python's CSV module. | `import csv` |
| `csv.reader()` | Reads CSV rows as lists. | `reader = csv.reader(file)` |
| `csv.writer()` | Creates a CSV writer. | `writer = csv.writer(file)` |
| `writerow()` | Writes one CSV row. | `writer.writerow(["Name", "Age"])` |
| `writerows()` | Writes multiple rows. | `writer.writerows(rows)` |
| `csv.DictReader()` | Reads CSV rows as dictionaries. | `reader = csv.DictReader(file)` |
| `csv.DictWriter()` | Writes CSV rows using dictionary keys. | `csv.DictWriter(file, fieldnames=["Name", "Age"])` |
| `writeheader()` | Writes CSV column names. | `writer.writeheader()` |
| `newline=""` | Prevents unwanted newline handling when working with CSV files. | `open("data.csv", "w", newline="")` |

## Date and Time

| Method / Concept | Description | Code Example |
|---|---|---|
| `date.today()` | Returns the current local date. | `date.today()` |
| `datetime.now()` | Returns the current local date and time. | `datetime.now()` |
| `date()` | Creates a date object. | `date(2026, 10, 22)` |
| `strftime()` | Formats a date or datetime as a string. | `today.strftime("%Y-%m-%d")` |
| `strptime()` | Parses a string into a datetime. | `datetime.strptime("2026-10-22", "%Y-%m-%d")` |
| `timedelta()` | Represents a duration. | `timedelta(days=7)` |
| `.year` | Gets the year from a date. | `today.year` |
| `.month` | Gets the month. | `today.month` |
| `.day` | Gets the day. | `today.day` |

## Common Date Format Codes

| Code | Meaning | Example |
|---|---|---|
| `%Y` | Four-digit year | `2026` |
| `%m` | Two-digit month | `10` |
| `%d` | Two-digit day | `22` |
| `%H` | Hour in 24-hour format | `14` |
| `%M` | Minutes | `30` |
| `%S` | Seconds | `45` |
| `%B` | Full month name | `October` |

## Python Utilities Glossary

| Term | Definition |
|---|---|
| Exception | An error or unusual event raised during program execution. |
| Exception Handling | Managing errors using `try` and `except`. |
| File Mode | A setting that determines how a file is opened. |
| Module | A Python file containing reusable code. |
| Package | A way of organizing related Python modules. |
| Standard Library | Modules included with Python. |
| JSON | A text-based format for structured data exchange. |
| CSV | A text-based format for tabular data. |
| Serialization | Converting data into a format suitable for storage or transfer. |
| Deserialization | Converting stored or transferred data back into program objects. |
| Timestamp | A representation of a specific point in time. |
| Date Formatting | Converting dates into a specified text format. |
| Parsing | Interpreting text according to a format to produce structured data. |
| `timedelta` | A Python object representing a duration. |