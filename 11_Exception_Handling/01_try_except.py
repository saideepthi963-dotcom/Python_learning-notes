
# ================================================================================
# EXCEPTION HANDLING IN PYTHON
# ----------------------------------------
# Exception handling helps us manage errors in a program.
#
# Main keywords:
# try     -> Runs code that might cause an error.
# except  -> Handles the error.
# else    -> Runs when no exception occurs.
# finally -> Runs whether an exception occurs or not.
# ================================================================================


# ---------------------------------------
# 1. Basic try-except
# ---------------------------------------
# Handle division by zero.

try:
    result = 10 / 0
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero")

# Output: Cannot divide by zero


# ---------------------------------------
# 2. Handling ValueError
# ---------------------------------------
# ValueError occurs when conversion fails.

try:
    number = int("abc")
    print(number)
except ValueError:
    print("Invalid number")

# Output: Invalid number


# ---------------------------------------
# 3. Handling Multiple Exceptions
# ---------------------------------------
# Different errors can have different handlers.

try:
    number = int("10")
    result = 100 / number
    print(result)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Output: 10.0


# ---------------------------------------
# 4. Handling IndexError
# ---------------------------------------
# IndexError occurs when the index does not exist.

numbers = [10, 20, 30]

try:
    print(numbers[5])
except IndexError:
    print("Index does not exist")

# Output: Index does not exist


# ---------------------------------------
# 5. try-except-else
# ---------------------------------------
# else runs only when no exception occurs.

try:
    result = 10 / 2
except ZeroDivisionError:
    print("Division error")
else:
    print("Result:", result)

# Output: Result: 5.0


# ---------------------------------------
# 6. try-except-finally
# ---------------------------------------
# finally runs whether an error occurs or not.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error handled")
finally:
    print("Execution completed")

# Output:
# Error handled
# Execution completed


# ---------------------------------------
# 7. Getting the Error Message
# ---------------------------------------
# as e stores the exception object.

try:
    number = int("hello")
except ValueError as e:
    print("Error:", e)

# Output:
# Error: invalid literal for int() with base 10: 'hello'


# ---------------------------------------
# 8. Raising an Exception
# ---------------------------------------
# raise allows us to create an exception.

age = -5

try:
    if age < 0:
        raise ValueError("Age cannot be negative")
except ValueError as e:
    print(e)

# Output: Age cannot be negative


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. try contains code that might fail.
# 2. except handles matching exceptions.
# 3. else runs if no exception occurs.
# 4. finally runs regardless of the result.
# 5. as e captures the exception object.
# 6. raise creates an exception.
# 7. Handle specific exceptions whenever possible.

