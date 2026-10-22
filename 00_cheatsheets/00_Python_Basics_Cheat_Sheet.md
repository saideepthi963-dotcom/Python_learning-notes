# Module 1 Cheat Sheet: Python Basics

| Package / Method | Description | Code Example |
|---|---|---|
| Comments | Comments are ignored by the Python interpreter and are used to explain code. | `# This is a comment` |
| Concatenation | Combines strings together using `+`. | `result = "Hello" + " John"` |
| Data Types | Common basic data types include `int`, `float`, `bool`, and `str`. | `x = 7`<br>`y = 12.4`<br>`is_valid = True`<br>`name = "John"` |
| Indexing | Accesses a character at a specific position in a string. Indexing starts at `0`. | `my_string = "Hello"`<br>`char = my_string[0]` |
| `len()` | Returns the number of characters or items in an object. | `my_string = "Hello"`<br>`length = len(my_string)` |
| `lower()` | Converts all characters in a string to lowercase. | `my_string = "Hello"`<br>`lowercase_text = my_string.lower()` |
| `print()` | Displays text, values, or variables on the screen. | `print("Hello, world")`<br>`print(a + b)` |
| Arithmetic Operators | Used to perform mathematical operations. `+` addition, `-` subtraction, `*` multiplication, `/` division, `//` floor division, `%` modulus, `**` exponent. | `x = 9`<br>`y = 4`<br>`x + y`<br>`x - y`<br>`x * y`<br>`x / y`<br>`x // y`<br>`x % y`<br>`x ** y` |
| Comparison Operators | Compare values and return `True` or `False`. | `x == y`<br>`x != y`<br>`x > y`<br>`x < y`<br>`x >= y`<br>`x <= y` |
| Logical Operators | Combine or reverse Boolean conditions using `and`, `or`, and `not`. | `age >= 18 and has_id`<br>`x > 5 or y > 5`<br>`not is_active` |
| Assignment Operators | Assign or update values in variables. | `x = 5`<br>`x += 2`<br>`x -= 1`<br>`x *= 3` |
| `replace()` | Replaces part of a string with another value. | `my_string = "Hello"`<br>`new_text = my_string.replace("Hello", "Hi")` |
| Slicing | Extracts part of a string using start and end indexes. | `my_string = "Hello"`<br>`substring = my_string[0:4]` |
| `split()` | Splits a string into a list based on a separator. | `skills = "Python,SQL,Git"`<br>`skills_list = skills.split(",")` |
| `strip()` | Removes whitespace from the beginning and end of a string. | `my_string = "  Hello  "`<br>`trimmed = my_string.strip()` |
| `upper()` | Converts all characters in a string to uppercase. | `my_string = "Hello"`<br>`uppercase_text = my_string.upper()` |
| Variable Assignment | Stores a value inside a variable using `=`. | `name = "John"`<br>`x = 5` |
| Type Checking | `type()` returns the data type of a value or variable. | `age = 25`<br>`print(type(age))` |
| Type Conversion | Converts a value from one data type to another. | `int("10")`<br>`float(10)`<br>`str(25)` |
| `input()` | Reads input entered by the user. `input()` returns a string. | `name = input("Enter your name: ")` |
| Membership Operators | Check whether a value exists inside another object using `in` or `not in`. | `"Py" in "Python"`<br>`"Java" not in "Python"` |
| Identity Operators | Check whether two variables refer to the same object using `is` or `is not`. | `value is None` |
| Boolean | Represents either `True` or `False`. | `is_learning = True`<br>`is_finished = False` |
| Escape Sequences | Special characters used inside strings. Common examples are `\n`, `\t`, `\"`, and `\\`. | `print("Hello\nPython")`<br>`print("Hello\tPython")` |
| String Repetition | Repeats a string multiple times using `*`. | `print("Hi " * 3)` |
| String Formatting | f-strings allow variables to be inserted directly into strings. | `name = "Deepthi"`<br>`print(f"My name is {name}")` |



## Python Basics Glossary

| Term | Definition |
|---|---|
| AI | Artificial Intelligence is the ability of computer systems to perform tasks that normally require human intelligence, such as recognizing patterns, understanding language, or making decisions. |
| Application Development | The process of planning, designing, building, testing, and deploying software applications. |
| Arithmetic Operations | Basic mathematical operations such as addition, subtraction, multiplication, division, modulus, floor division, and exponentiation. |
| Array | A collection of values stored in an organized structure. In Python, lists are commonly used for general-purpose collections, while libraries such as NumPy provide array objects. |
| Assignment Operator | The `=` operator assigns a value to a variable. Example: `age = 25`. |
| Asterisk | The `*` symbol. In Python it can be used for multiplication, string repetition, unpacking, and function arguments. |
| Backslash | The `\` character is used to begin escape sequences inside strings, such as `\n` for a new line. |
| Boolean | A data type with two possible values: `True` and `False`. |
| Colon | The `:` symbol is used in Python syntax for structures such as `if`, `for`, `while`, functions, classes, dictionaries, and slicing. |
| Concatenate | To join two or more strings or sequences together. |
| Data Engineering | The field focused on collecting, transforming, storing, and preparing data so it can be used for analytics, reporting, and applications. |
| Data Science | A field that uses programming, statistics, and analytical techniques to extract useful insights from data. |
| Data Type | A classification that describes what kind of value a variable contains and what operations can be performed on it. |
| Double Quote | The `"` symbol can be used to create strings in Python. Example: `"Python"`. |
| Escape Sequence | A special character sequence beginning with `\` that represents formatting or special characters, such as `\n`, `\t`, and `\\`. |
| Expression | A combination of values, variables, and operators that Python evaluates to produce a result. |
| Float | A data type used to represent decimal numbers, such as `3.14` or `9.81`. |
| Forward Slash | The `/` symbol is used for regular division in Python. |
| Foundational | Something that forms the basic or essential knowledge needed to understand more advanced concepts. |
| Immutable | An object that cannot be changed after it is created. Examples include strings, integers, floats, booleans, and tuples. |
| Integer | A whole number without a decimal point, such as `-5`, `0`, or `100`. |
| Manipulate | To modify, transform, or work with data. In string manipulation, this can include replacing, splitting, slicing, or formatting strings. |
| Mathematical Convention | A commonly accepted mathematical rule, notation, or way of representing information. |
| Mathematical Expression | A combination of numbers, variables, and operators that evaluates to a value. |
| Mathematical Operation | A calculation performed using values and mathematical operators. |
| Negative Indexing | A way to access items from the end of a sequence. For example, `text[-1]` returns the last character. |
| Operand | A value or variable that an operator acts on. In `5 + 3`, both `5` and `3` are operands. |
| Operator | A symbol or keyword used to perform an operation on values or variables. Examples include `+`, `-`, `==`, `and`, and `in`. |
| Parentheses | The `()` symbols are used for function calls, grouping expressions, tuples, and controlling evaluation order. |
| Replicate | To create a copy or duplicate of something. |
| Sequence | An ordered collection of items. Common Python sequences include strings, lists, tuples, and ranges. |
| Single Quote | The `'` symbol can be used to create strings in Python. Example: `'Python'`. |
| Slicing | A way to extract part of a sequence using syntax such as `sequence[start:stop:step]`. |
| Special Character | A character that is not a regular letter or number, such as `@`, `#`, `$`, `%`, `\`, or `*`. |
| Stride / Step Value | In Python slicing, the step value controls how many positions to move between selected elements. Example: `text[::2]`. |
| String | A sequence of Unicode characters used to represent text in Python. |
| Substring | A smaller sequence of characters contained inside a larger string. |
| Type Casting | Converting a value from one data type to another using functions such as `int()`, `float()`, `str()`, and `list()`. |
| Python Types | Categories of data in Python, such as `int`, `float`, `str`, `bool`, `list`, `tuple`, `set`, and `dict`. |
| Variable | A name that refers to a value stored in memory. Variables make values reusable and updateable throughout a program. |