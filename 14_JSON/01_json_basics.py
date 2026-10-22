
# ================================================================================
# JSON IN PYTHON
# ----------------------------------------
# JSON stands for JavaScript Object Notation.
# It is commonly used to store and exchange data.
#
# Python provides a built-in json module.
#
# Important functions:
# json.loads() -> JSON string to Python object
# json.dumps() -> Python object to JSON string
# json.load()  -> JSON file to Python object
# json.dump()  -> Python object to JSON file
# ================================================================================

import json


# ---------------------------------------
# 1. JSON String to Python Dictionary
# ---------------------------------------
# loads() converts a JSON string to a Python object.

json_data = '{"name": "Maria", "age": 25, "city": "Berlin"}'

person = json.loads(json_data)

print(person)
# -> {'name': 'Maria', 'age': 25, 'city': 'Berlin'}

print(type(person))  # -> <class 'dict'>


# ---------------------------------------
# 2. Accessing JSON Data
# ---------------------------------------
# After conversion, access values using dictionary keys.

print(person["name"])  # -> Maria
print(person["age"])   # -> 25


# ---------------------------------------
# 3. Python Dictionary to JSON String
# ---------------------------------------
# dumps() converts a Python object into a JSON string.

student = {
    "name": "John",
    "age": 30,
    "city": "Paris"
}

json_string = json.dumps(student)

print(json_string)
# -> {"name": "John", "age": 30, "city": "Paris"}

print(type(json_string))  # -> <class 'str'>


# ---------------------------------------
# 4. Formatting JSON with indent
# ---------------------------------------
# indent makes JSON easier to read.

student = {
    "name": "Maria",
    "age": 25,
    "skills": ["Python", "SQL"]
}

formatted = json.dumps(student, indent=4)

print(formatted)


# ---------------------------------------
# 5. Python and JSON Data Types
# ---------------------------------------
# Python             JSON
# dict               object
# list               array
# str                string
# int / float        number
# True / False       true / false
# None               null

data = {
    "name": "Maria",
    "active": True,
    "salary": None
}

print(json.dumps(data))
# -> {"name": "Maria", "active": true, "salary": null}


# ---------------------------------------
# 6. Writing JSON to a File
# ---------------------------------------
# dump() writes Python data to a JSON file.
# The file is created in the current working directory.

employee = {
    "id": 101,
    "name": "Maria",
    "role": "Data Engineer"
}

with open("employee.json", "w", encoding="utf-8") as file:
    json.dump(employee, file, indent=4)

print("JSON file created")


# ---------------------------------------
# 7. Reading JSON from a File
# ---------------------------------------
# load() reads and converts JSON file content.

with open("employee.json", "r", encoding="utf-8") as file:
    employee_data = json.load(file)

print(employee_data)
# -> {'id': 101, 'name': 'Maria', 'role': 'Data Engineer'}


# ---------------------------------------
# 8. Working with Nested JSON
# ---------------------------------------
# JSON can contain nested objects and arrays.

json_data = """
{
    "name": "Maria",
    "skills": ["Python", "SQL"],
    "address": {
        "city": "Berlin",
        "country": "Germany"
    }
}
"""

person = json.loads(json_data)

print(person["skills"][0])       # -> Python
print(person["address"]["city"]) # -> Berlin


# ---------------------------------------
# 9. Handling Invalid JSON
# ---------------------------------------
# Invalid JSON raises JSONDecodeError.

invalid_json = '{"name": "Maria",}'

try:
    data = json.loads(invalid_json)
except json.JSONDecodeError:
    print("Invalid JSON format")

# Output: Invalid JSON format


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. JSON is used for storing and exchanging data.
# 2. json.loads() reads a JSON string.
# 3. json.dumps() creates a JSON string.
# 4. json.load() reads a JSON file.
# 5. json.dump() writes a JSON file.
# 6. JSON objects become Python dictionaries.
# 7. JSON arrays become Python lists.
# 8. indent makes JSON easier to read.
# 9. JSON is widely used in APIs and data pipelines.

