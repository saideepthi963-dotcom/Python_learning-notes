# If and Else Statements

# Conditional statements allow Python to make decisions.
# A condition is checked first.
# If the condition is True, Python runs one block of code.
# If the condition is False, Python can run another block.


# Basic if statement

age = 20

if age >= 18:
    print("You are an adult")

# Output:
# You are an adult


# if and else

age = 16

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# Output:
# You are a minor


# Comparison operators are commonly used in conditions.

number = 10

if number > 5:
    print("Number is greater than 5")

# Output:
# Number is greater than 5


# Checking equality

language = "Python"

if language == "Python":
    print("You are learning Python")

# Output:
# You are learning Python


# Checking not equal

password = "python123"

if password != "admin":
    print("Password is not admin")

# Output:
# Password is not admin


# Positive or negative number

number = -5

if number > 0:
    print("Positive number")
else:
    print("Negative number")

# Output:
# Negative number


# Even or odd number

number = 12

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Output:
# Even number


# Boolean value in a condition

is_logged_in = True

if is_logged_in:
    print("Welcome back")
else:
    print("Please log in")

# Output:
# Welcome back


# not with conditions

is_raining = False

if not is_raining:
    print("You can go outside")

# Output:
# You can go outside


# Using user input

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible")
else:
    print("You are not eligible")


# Multiple conditions using and

age = 25
has_id = True

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

# Output:
# Entry allowed


# Multiple conditions using or

temperature = 95

if temperature > 90 or temperature < 40:
    print("Extreme temperature")
else:
    print("Normal temperature")

# Output:
# Extreme temperature


# Membership condition

skills = ["Python", "SQL", "Git"]

if "Python" in skills:
    print("Python skill found")

# Output:
# Python skill found


# String condition

username = "Deepthi"

if username:
    print("Username is not empty")
else:
    print("Username is empty")

# Output:
# Username is not empty
