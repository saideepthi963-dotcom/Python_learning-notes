# Module 3 Cheat Sheet: Python Data Structures

## Data Structures Overview

| Structure | Ordered | Mutable | Duplicates | Access |
|---|---|---|---|---|
| List | Yes | Yes | Allowed | Index |
| Tuple | Yes | No | Allowed | Index |
| Set | No | Yes | Not allowed | Membership |
| Dictionary | Yes | Yes | Keys unique | Key |

## Lists

| Method / Concept | Description | Code Example |
|---|---|---|
| Creating List | Creates an ordered collection. | `items = [10, 20, 30]` |
| Indexing | Accesses an element by index. | `items[0]` |
| Negative Indexing | Accesses elements from the end. | `items[-1]` |
| Slicing | Extracts a portion of a list. | `items[1:3]` |
| `append()` | Adds one element at the end. | `items.append(40)` |
| `extend()` | Adds elements from another iterable. | `items.extend([40, 50])` |
| `insert()` | Inserts an element at an index. | `items.insert(1, 15)` |
| `remove()` | Removes the first matching value. | `items.remove(20)` |
| `pop()` | Removes and returns an element. | `items.pop()` |
| `clear()` | Removes all elements. | `items.clear()` |
| `len()` | Returns the number of elements. | `len(items)` |
| `count()` | Counts occurrences of a value. | `items.count(20)` |
| `index()` | Finds the first matching index. | `items.index(20)` |
| `sort()` | Sorts the original list. | `items.sort()` |
| `sorted()` | Returns a new sorted list. | `sorted(items)` |
| `reverse()` | Reverses the original list. | `items.reverse()` |
| `copy()` | Creates a shallow copy. | `new_items = items.copy()` |
| `sum()` | Calculates the total of numeric values. | `sum(items)` |
| `min()` / `max()` | Finds the smallest/largest value. | `min(items)` / `max(items)` |
| List Unpacking | Assigns elements to variables. | `a, b, c = [10, 20, 30]` |
| Star Unpacking | Collects remaining elements. | `first, *rest = items` |
| List Comprehension | Creates a list using compact syntax. | `[x * 2 for x in items]` |

## Iteration Tools

| Method | Description | Code Example |
|---|---|---|
| `enumerate()` | Returns indexes and values. | `enumerate(items)` |
| `zip()` | Pairs elements from iterables. | `list(zip(names, ages))` |
| `map()` | Applies a function to every element. | `list(map(int, ["1", "2"]))` |
| `filter()` | Selects elements satisfying a condition. | `list(filter(bool, items))` |
| `reversed()` | Iterates in reverse order. | `list(reversed(items))` |
| `all()` | Checks whether all elements are truthy. | `all([True, True])` |
| `any()` | Checks whether at least one element is truthy. | `any([False, True])` |

## Tuples

| Method / Concept | Description | Code Example |
|---|---|---|
| Creating Tuple | Creates an immutable ordered collection. | `values = (10, 20, 30)` |
| Single-Element Tuple | Requires a trailing comma. | `value = (10,)` |
| Indexing | Accesses an element. | `values[0]` |
| Slicing | Extracts multiple elements. | `values[1:3]` |
| `count()` | Counts occurrences. | `values.count(10)` |
| `index()` | Finds the first matching index. | `values.index(20)` |
| Tuple Unpacking | Assigns tuple values to variables. | `a, b = (10, 20)` |

## Sets

| Method / Concept | Description | Code Example |
|---|---|---|
| Creating Set | Creates a collection of unique values. | `numbers = {10, 20, 30}` |
| Empty Set | Creates an empty set. | `numbers = set()` |
| `add()` | Adds one element. | `numbers.add(40)` |
| `update()` | Adds multiple elements. | `numbers.update([40, 50])` |
| `remove()` | Removes an element; errors if missing. | `numbers.remove(20)` |
| `discard()` | Removes an element without error if missing. | `numbers.discard(20)` |
| Union | Combines unique elements. | `a \| b` |
| Intersection | Finds common elements. | `a & b` |
| Difference | Finds elements in one set but not the other. | `a - b` |
| Symmetric Difference | Finds elements belonging to only one set. | `a ^ b` |
| `issubset()` | Checks whether one set is contained in another. | `a.issubset(b)` |
| `issuperset()` | Checks whether a set contains another set. | `a.issuperset(b)` |
| `isdisjoint()` | Checks whether sets share no elements. | `a.isdisjoint(b)` |

## Dictionaries

| Method / Concept | Description | Code Example |
|---|---|---|
| Creating Dictionary | Stores key-value pairs. | `user = {"name": "Maria", "age": 25}` |
| Key Access | Accesses a value using its key. | `user["name"]` |
| `get()` | Safely retrieves a value. | `user.get("city", "Unknown")` |
| `keys()` | Returns a view of keys. | `user.keys()` |
| `values()` | Returns a view of values. | `user.values()` |
| `items()` | Returns key-value pairs. | `user.items()` |
| Adding Key | Adds a new key-value pair. | `user["city"] = "Berlin"` |
| Updating Value | Changes an existing value. | `user["age"] = 30` |
| `update()` | Adds or updates several entries. | `user.update({"age": 30})` |
| `pop()` | Removes a key and returns its value. | `user.pop("age")` |
| `popitem()` | Removes the last inserted pair. | `user.popitem()` |
| `fromkeys()` | Creates keys with a shared default value. | `dict.fromkeys(["a", "b"], 0)` |
| Dictionary Comprehension | Creates a dictionary with compact syntax. | `{x: x*x for x in range(3)}` |

## Data Structures Glossary

| Term | Definition |
|---|---|
| Mutable | An object that can be changed after creation. |
| Immutable | An object that cannot be changed after creation. |
| Ordered | Elements follow a defined order. |
| Index | Numeric position of an element in a sequence. |
| Key | A unique identifier used to access a dictionary value. |
| Value | Data associated with a dictionary key. |
| Duplicate | A repeated element or value. |
| Nested Collection | A collection containing another collection. |
| Shallow Copy | A new outer collection that shares references to nested objects. |
| Deep Copy | A copy that recursively copies nested objects. |
| Comprehension | Compact syntax for creating collections from iterables. |
| Iterator | An object that provides elements one at a time. |
| Unpacking | Assigning collection elements to separate variables. |