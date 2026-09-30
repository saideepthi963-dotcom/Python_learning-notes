# first code every python learner start with on the day one of coding.
print("Hello World")

# --------------- PRINT() --------------------------------------
# The `print()` built-in Python function is used to display text
# on the screen. It’s your main way to *communicate* with users
# and check what your code is doing.
# You’ll use it in almost every Python program!


# ------------- ESCAPE SEQUENCES----------------------------------

# \" and \' - Print quotes inside strings -- for multi line comments

"""In Python and other programming languages \ followed by a character is an escape sequence. Let us see the most common escape characters:

\n: new line
\t: Tab means(8 spaces)
\\: Back slash
\': Single quote (')
\": Double quote (") """


# print("Hi "Python"") #Invalid: Double quotes inside Double quotes
print("Hi \"Python\"") # Use escape character (backslash)
print('Hi "Python"') # Fix2: Mix single and double quotes
# print('Hi 'Python'') #Invalid: Single quote inside Single quotes
print('Hi \'Python\'') # Fix1: Use escape character (backslash)
print("Hi 'Python'") # Fix2: Mix single and double quotes

# \\ - Backslash - Python interprets the backslash sequence as a formatting instruction instead of normal text
print("Path: C:\Users\sai") #Invalid
print("Path: C:\\Users\\sai") # if we need backslash in the output we must give two backslashes, 

# \n - New Line
print("Message1")
print()  # Blank Line
print("Message2")

print("Message1\n") # Adds one new line
print("Message2")

print("Message1\n\n\nMessage2")  # Adds three new lines
print("Message1\nMessage2") # One new line between

# \t - Tab
print("Message1\tMessage2")


# -------------------- input -----------------------------------------------------
# A built-in python function that stops your program to get the user input, basically we're requesting input from the user
# using input() alone reads the user's response. but it doesn't store anywhere. to keep the value we need to assign it to a variable.

# Dynamic Value: data entered by the user that can vary each time the program runs
name = input("Enter Your Name:")

# Hardcoded value: fixed piece of data written directly into your code that never changes at runtime
country = "India"

# Combine both variables
print(name, "comes from", country)
 
