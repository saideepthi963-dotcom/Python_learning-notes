
# ================================================================================
# DICTIONARIES IN PYTHON
# ----------------------------------------
# Dictionaries store data as key-value pairs.
#
# Dictionaries are:
# 1. Ordered (Python 3.7+)
# 2. Mutable (changeable)
# 3. Keys must be unique
# 4. Accessed using keys instead of indexes
#
# Syntax: {key: value}
# ================================================================================


# ---------------------------------------
# 1. Creating a Dictionary
# ---------------------------------------
student = {
    "name": "Maria",
    "age": 29,
    "role": "Data Engineer"
}

print(student)
print(type(student))  # -> <class 'dict'>


# ---------------------------------------
# 2. Creating an Empty Dictionary
# ---------------------------------------
empty1 = {}
empty2 = dict()

print(empty1)  # -> {}
print(empty2)  # -> {}


# ---------------------------------------
# 3. Accessing Dictionary Values
# ---------------------------------------
student = {
    "name": "Maria",
    "age": 29,
    "city": "Berlin"
}

print(student["name"])  # -> Maria
print(student["age"])   # -> 29


# ---------------------------------------
# 4. Using get()
# ---------------------------------------
# get() safely accesses a key.
# It returns a default value if the key is missing.

user = {"id": 1, "age": 30, "city": "Berlin"}

print(user.get("city"))             # -> Berlin
print(user.get("name"))             # -> None
print(user.get("name", "Unknown"))  # -> Unknown

# user["name"] would raise KeyError.


# ---------------------------------------
# 5. Duplicate Keys
# ---------------------------------------
# Duplicate keys are not allowed.
# The last assigned value replaces the previous value.

my_dict = {
    "a": 10,
    "b": 20,
    "a": 40
}

print(my_dict)  # -> {'a': 40, 'b': 20}


# ---------------------------------------
# 6. Checking Dictionary Keys
# ---------------------------------------
# in checks whether a key exists.

user = {"id": 1, "age": 30, "city": "Berlin"}

print("age" in user)       # -> True
print("name" in user)      # -> False
print("name" not in user)  # -> True


# ---------------------------------------
# 7. keys(), values(), items()
# ---------------------------------------
# keys()   -> Returns dictionary keys.
# values() -> Returns dictionary values.
# items()  -> Returns key-value pairs.

user = {"id": 1, "age": 30, "city": "Berlin"}

print(user.keys())
# -> dict_keys(['id', 'age', 'city'])

print(user.values())
# -> dict_values([1, 30, 'Berlin'])

print(user.items())
# -> dict_items([('id', 1), ('age', 30), ('city', 'Berlin')])


# ---------------------------------------
# 8. Looping Through a Dictionary
# ---------------------------------------
user = {"id": 1, "age": 30, "city": "Berlin"}

# Loop through keys.
for key in user:
    print(key, user[key])

# Loop through key-value pairs.
for key, value in user.items():
    print(key, value)


# ---------------------------------------
# 9. Adding a New Key
# ---------------------------------------
user = {"id": 1, "age": 30}

user["name"] = "John"

print(user)
# -> {'id': 1, 'age': 30, 'name': 'John'}


# ---------------------------------------
# 10. Updating Dictionary Values
# ---------------------------------------
user = {"id": 1, "age": 30, "city": "Berlin"}

user["age"] = 35

print(user)
# -> {'id': 1, 'age': 35, 'city': 'Berlin'}


# ---------------------------------------
# 11. update()
# ---------------------------------------
# Updates multiple values or adds new keys.

user = {"id": 1, "age": 30, "city": "Berlin"}

user.update({"age": 40, "city": "Paris"})

print(user)
# -> {'id': 1, 'age': 40, 'city': 'Paris'}


# ---------------------------------------
# 12. pop()
# ---------------------------------------
# Removes a key and returns its value.

user = {"id": 1, "age": 30, "city": "Berlin"}

removed = user.pop("age")

print(removed)  # -> 30
print(user)     # -> {'id': 1, 'city': 'Berlin'}

# Provide a default to avoid errors for missing keys.

result = user.pop("salary", "Not Found")

print(result)  # -> Not Found


# ---------------------------------------
# 13. popitem()
# ---------------------------------------
# Removes the last inserted key-value pair.

user = {"id": 1, "age": 30, "city": "Berlin"}

removed = user.popitem()

print(removed)  # -> ('city', 'Berlin')
print(user)     # -> {'id': 1, 'age': 30}


# ---------------------------------------
# 14. Creating Dictionaries with fromkeys()
# ---------------------------------------
# Creates a dictionary with specified keys
# and the same default value.

keys = ["id", "name", "age", "city"]

user = dict.fromkeys(keys, None)

print(user)
# -> {'id': None, 'name': None, 'age': None, 'city': None}


# ---------------------------------------
# 15. Nested Dictionaries
# ---------------------------------------
# A dictionary can contain other dictionaries.

students = {
    "student1": {"name": "Maria", "age": 25},
    "student2": {"name": "John", "age": 28}
}

print(students["student1"]["name"])  # -> Maria
print(students["student2"]["age"])   # -> 28


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. Dictionaries store key-value pairs.
# 2. Dictionaries preserve insertion order.
# 3. Keys must be unique.
# 4. Values are accessed using keys.
# 5. get() safely accesses missing keys.
# 6. keys(), values(), items() inspect dictionary data.
# 7. update() changes or adds multiple values.
# 8. pop() removes a key and returns its value.
# 9. popitem() removes the last inserted pair.
# 10. fromkeys() creates a dictionary with default values.

