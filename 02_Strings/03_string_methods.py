# String Methods

# Python provides many built-in methods for working with strings.
# String methods usually do not change the original string.
# Instead, they return a new string or another value.


# upper()
# Converts all alphabetic characters to uppercase.

text = "python programming"

print(text.upper())      # PYTHON PROGRAMMING


# lower()
# Converts all alphabetic characters to lowercase.

text = "PYTHON PROGRAMMING"

print(text.lower())      # python programming


# capitalize()
# Converts the first character of the string to uppercase.
# Remaining characters are converted to lowercase.

text = "python programming"

print(text.capitalize())     # Python programming


# title()
# Converts the first letter of each word to uppercase.

text = "python programming"

print(text.title())      # Python Programming


# swapcase()
# Converts uppercase letters to lowercase.
# Converts lowercase letters to uppercase.

text = "Python Programming"

print(text.swapcase())       # pYTHON pROGRAMMING


# count()
# Counts how many times a character or substring appears.

text = "banana"

print(text.count("a"))       # 3
print(text.count("an"))      # 2


# count() can also search within a specific range.

text = "banana"

print(text.count("a", 0, 4))     # 2


# find()
# Returns the index of the first occurrence of a substring.
# If the substring is not found, it returns -1.

text = "Python Programming"

print(text.find("Python"))       # 0
print(text.find("Program"))      # 7
print(text.find("Java"))         # -1


# rfind()
# Searches from the right side.
# Returns the index of the last occurrence.
# Returns -1 if the substring is not found.

challenge = 'thirty days of python'
print(challenge.rfind('y'))  # 16
print(challenge.rfind('th')) # 17

# index()
# Similar to find().
# The difference is that index() raises ValueError
# if the substring is not found.

text = "Python Programming"

print(text.index("Python"))      # 0

# This would cause ValueError:
# print(text.index("Java"))


# rindex()
# Returns the index of the last occurrence.
# Raises ValueError if the substring is not found.

challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 7
print(challenge.rindex(sub_string, 9)) # error
print(challenge.rindex('on', 8)) # 19

# format(): formats string into a nicer output
first_name = 'Asabeneh'
last_name = 'Yetayeh'
age = 250
job = 'teacher'
country = 'Finland'
sentence = 'I am {} {}. I am a {}. I am {} years old. I live in {}.'.format(first_name, last_name, age, job, country)
print(sentence) # I am Asabeneh Yetayeh. I am 250 years old. I am a teacher. I live in Finland.

radius = 10
pi = 3.14
area = pi * radius ** 2
result = 'The area of a circle with radius {} is {}'.format(str(radius), str(area))
print(result) # The area of a circle with radius 10 is 314


# replace()
# Replaces a substring with another substring.

text = "I am learning SQL"

new_text = text.replace("SQL", "Python")

print(new_text)      # I am learning Python


# strip()
# Removes whitespace from both the beginning and end.

name = "   Deepthi   "

print(name.strip())      # Deepthi


# lstrip()
# Removes whitespace from the left side.

name = "   Deepthi"

print(name.lstrip())     # Deepthi


# rstrip()
# Removes whitespace from the right side.

name = "Deepthi   "

print(name.rstrip())     # Deepthi


# startswith()
# Checks whether a string starts with a specific value.
# Returns True or False.

filename = "python_notes.py"

print(filename.startswith("python"))     # True
print(filename.startswith("java"))       # False


# endswith()
# Checks whether a string ends with a specific value.
# Returns True or False.

filename = "python_notes.py"

print(filename.endswith(".py"))      # True
print(filename.endswith(".txt"))     # False


# isalpha()
# Returns True if all characters are alphabetic letters.
# Spaces and numbers cause it to return False.

word = "Python"

print(word.isalpha())        # True

word = "Python123"

print(word.isalpha())        # False


# isdigit()
# Returns True if all characters are digits.

number = "12345"

print(number.isdigit())      # True

number = "123A"

print(number.isdigit())      # False




# isalnum()
# Returns True when the string contains only letters and numbers.
# Spaces and special characters return False.

value = "Python123"

print(value.isalnum())       # True

value = "Python 123"

print(value.isalnum())       # False


# islower()
# Returns True if all alphabetic characters are lowercase.

text = "python programming"

print(text.islower())        # True


# isupper()
# Returns True if all alphabetic characters are uppercase.

text = "PYTHON PROGRAMMING"

print(text.isupper())        # True



# split()
# Splits a string into multiple parts.
# It returns a list.

skills = "Python,SQL,Git"

skills_list = skills.split(",")

print(skills_list)
# ['Python', 'SQL', 'Git']


# split() without an argument
# Splits the string using whitespace.

sentence = "Python is easy to learn"

words = sentence.split()

print(words)
# ['Python', 'is', 'easy', 'to', 'learn']


# join()
# Combines multiple strings into one string.
# The value before .join() is used as the separator.

skills = ["Python", "SQL", "Git"]

result = ", ".join(skills)

print(result)
# Python, SQL, Git


# Another join() example

words = ["I", "am", "learning", "Python"]

sentence = " ".join(words)

print(sentence)
# I am learning Python



