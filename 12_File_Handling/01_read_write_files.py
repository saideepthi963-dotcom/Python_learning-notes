
# ================================================================================
# FILE HANDLING IN PYTHON
# ----------------------------------------
# File handling allows Python to work with files.
#
# Common file modes:
# r -> Read
# w -> Write (creates or overwrites)
# a -> Append (adds content at the end)
# x -> Create a new file (fails if it exists)
#
# The with statement closes files automatically.
# ================================================================================


# ---------------------------------------
# 1. Writing to a File
# ---------------------------------------
# w creates a file if it does not exist.
# If the file exists, its content is overwritten.

with open("sample.txt", "w", encoding="utf-8") as file:
    file.write("Hello Python\n")
    file.write("Learning file handling\n")

print("File created successfully")


# ---------------------------------------
# 2. Reading an Entire File
# ---------------------------------------
# read() returns all file contents as a string.

with open("sample.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)

# Output:
# Hello Python
# Learning file handling


# ---------------------------------------
# 3. Reading One Line
# ---------------------------------------
# readline() reads one line at a time.

with open("sample.txt", "r", encoding="utf-8") as file:
    first_line = file.readline()

print(first_line.strip())

# Output: Hello Python


# ---------------------------------------
# 4. Reading All Lines
# ---------------------------------------
# readlines() returns a list of lines.

with open("sample.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

print(lines)

# Output:
# ['Hello Python\n', 'Learning file handling\n']


# ---------------------------------------
# 5. Appending to a File
# ---------------------------------------
# a adds content without removing existing text.

with open("sample.txt", "a", encoding="utf-8") as file:
    file.write("This is a new line\n")

print("Content appended")


# ---------------------------------------
# 6. Reading Files Using a Loop
# ---------------------------------------
# A for loop reads one line at a time.

with open("sample.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

# Output:
# Hello Python
# Learning file handling
# This is a new line


# ---------------------------------------
# 7. Creating a New File Using x
# ---------------------------------------
# x fails if the file already exists.
# Change the filename to create another new file.

try:
    with open("new_file.txt", "x", encoding="utf-8") as file:
        file.write("New file created")

    print("New file created successfully")

except FileExistsError:
    print("File already exists")


# ---------------------------------------
# 8. Handling a Missing File
# ---------------------------------------
# FileNotFoundError occurs when reading
# a file that does not exist.

try:
    with open("missing_file.txt", "r", encoding="utf-8") as file:
        print(file.read())

except FileNotFoundError:
    print("File not found")


# ---------------------------------------
# 9. Checking Whether a File Exists
# ---------------------------------------
# pathlib provides tools for working with paths.

from pathlib import Path

file_path = Path("sample.txt")

print(file_path.exists())  # -> True


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. open() opens a file.
# 2. r reads file contents.
# 3. w creates or overwrites a file.
# 4. a appends content.
# 5. x creates a new file only if it does not exist.
# 6. read() returns the entire content.
# 7. readline() reads one line.
# 8. readlines() returns a list of lines.
# 9. with automatically closes the file.
# 10. File paths are relative to the working directory.

