# Module 4 Cheat Sheet: Python Functions

## Functions and Syntax

| Method / Concept | Description | Code Example |
|---|---|---|
| `def` | Defines a reusable function. | `def greet(): print("Hello")` |
| Function Call | Executes a function. | `greet()` |
| Parameter | Variable declared in a function definition. | `def greet(name):` |
| Argument | Actual value passed to a function. | `greet("Maria")` |
| Multiple Parameters | Accepts more than one value. | `def add(a, b): return a + b` |
| Positional Arguments | Arguments matched by their position. | `add(10, 20)` |
| Keyword Arguments | Arguments passed by parameter name. | `student(age=25, name="Maria")` |
| Default Parameters | Provides a value when an argument is omitted. | `def greet(name="Guest"):` |
| `return` | Sends a result back to the caller. | `return a + b` |
| Multiple Return Values | Returns multiple values packed into a tuple. | `return total, difference` |
| Return Unpacking | Assigns returned values to separate variables. | `total, difference = calculate(10, 5)` |
| `print()` vs `return` | `print()` displays output; `return` provides a reusable result. | `print(10)` vs `return 10` |
| `*args` | Accepts multiple positional arguments as a tuple. | `def total(*numbers): return sum(numbers)` |
| `**kwargs` | Accepts multiple keyword arguments as a dictionary. | `def details(**info): print(info)` |
| `pass` | Placeholder for an empty function body. | `def future(): pass` |
| Function Without Return | Returns `None` automatically. | `def greet(): print("Hi")` |

## Lambda Functions

| Method / Concept | Description | Code Example |
|---|---|---|
| `lambda` | Creates a small anonymous function. | `double = lambda x: x * 2` |
| Multiple Arguments | Lambda can accept more than one argument. | `add = lambda x, y: x + y` |
| Lambda with `map()` | Applies a transformation to each element. | `list(map(lambda x: x * 2, [1, 2, 3]))` |
| Lambda with `filter()` | Keeps elements satisfying a condition. | `list(filter(lambda x: x > 5, [3, 7, 9]))` |
| Lambda with `sorted()` | Specifies a custom sorting key. | `sorted(students, key=lambda row: row[1])` |
| Lambda Return | Automatically returns the expression result. | `(lambda x: x ** 2)(4)` |

## Functions Glossary

| Term | Definition |
|---|---|
| Function | A reusable block of code that performs a task. |
| Function Definition | Creating a function using `def`. |
| Function Call | Executing a function using its name and parentheses. |
| Parameter | A variable specified in a function definition. |
| Argument | A value supplied when calling a function. |
| Positional Argument | An argument assigned based on its position. |
| Keyword Argument | An argument supplied using its parameter name. |
| Default Argument Value | A value used when the caller omits an optional argument. |
| Return Value | The result sent back by a function. |
| Local Variable | A variable defined within a function and normally accessible only there. |
| Scope | Determines where a variable can be accessed. |
| Lambda Function | A small anonymous function defined using `lambda`. |
| Anonymous Function | A function created without a conventional function name. |
| Reusability | Writing code once and calling it multiple times. |