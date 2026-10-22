# Module 2 Cheat Sheet: Python Control Flow

## Conditional Statements

| Method / Concept | Description | Code Example |
|---|---|---|
| `if` | Runs code when a condition is True. | `if age >= 18: print("Adult")` |
| `else` | Runs when the `if` condition is False. | `if age >= 18: print("Adult")` followed by `else: print("Minor")` |
| `elif` | Checks another condition if previous conditions are False. | `elif score >= 80: print("B")` |
| Nested `if` | An `if` statement inside another `if`. | `if age >= 18:` followed by `if has_id: print("Allowed")` |
| `and` | Both conditions must be True. | `age >= 18 and has_id` |
| `or` | At least one condition must be True. | `has_id or has_passport` |
| `not` | Reverses the truth value. | `not is_logged_in` |
| Ternary Expression | Writes a simple `if-else` in one expression. | `result = "Adult" if age >= 18 else "Minor"` |
| `match-case` | Matches values against different patterns. Python 3.10+. | `match status:` followed by `case 200: print("OK")` |

## Loops

| Method / Concept | Description | Code Example |
|---|---|---|
| `for` | Iterates through a sequence or iterable. | `for x in range(5): print(x)` |
| `while` | Repeats code while a condition is True. | `while count < 5: count += 1` |
| `range(stop)` | Generates numbers from 0 to stop − 1. | `range(5)` |
| `range(start, stop)` | Generates numbers starting at start, excluding stop. | `range(1, 6)` |
| `range(start, stop, step)` | Controls the interval between numbers. | `range(2, 11, 2)` |
| `break` | Stops the nearest enclosing loop. | `if x == 3: break` |
| `continue` | Skips to the next loop iteration. | `if x == 3: continue` |
| `pass` | Placeholder that does nothing. | `if x == 3: pass` |
| Nested Loop | A loop inside another loop. | `for i in range(2):` followed by `for j in range(3): print(i, j)` |
| Loop `else` | Runs when a loop finishes without executing `break`. | `for x in range(3): print(x)` followed by `else: print("Done")` |

## Python Control Flow Glossary

| Term | Definition |
|---|---|
| Condition | An expression evaluated as True or False. |
| Conditional Statement | Executes code depending on a condition. |
| Branch | One possible path of execution in a conditional statement. |
| Iteration | One repetition of a loop. |
| Iterable | An object whose elements can be processed one at a time. |
| Loop | A structure that repeats code. |
| Nested Loop | A loop placed inside another loop. |
| Infinite Loop | A loop that continues indefinitely unless stopped. |
| Loop Counter | A variable used to track loop iterations. |
| Boolean Expression | An expression whose result is True or False. |