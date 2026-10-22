
# ================================================================================
# FOR LOOPS IN PYTHON
# ----------------------------------------
# A for loop repeats a block of code for each item in a sequence.
# It is commonly used with range(), strings, lists, and other collections.
# ================================================================================


# ---------------------------------------
# 1. Basic For Loop
# ---------------------------------------
# range(5) produces numbers from 0 to 4.
# The stop value is excluded.

for number in range(5):
    print(number)

# Output:
# 0
# 1
# 2
# 3
# 4


# ---------------------------------------
# 2. range(start, stop)
# ---------------------------------------
# Start is included, stop is excluded.

for number in range(1, 6):
    print(number)

# Output: 1 2 3 4 5 (on separate lines)


# ---------------------------------------
# 3. range(start, stop, step)
# ---------------------------------------
# Step controls how much the number changes.

for number in range(2, 11, 2):
    print(number)

# Output: 2 4 6 8 10


# ---------------------------------------
# 4. Reverse For Loop
# ---------------------------------------
# Negative step counts backward.

for number in range(5, 0, -1):
    print(number)

# Output: 5 4 3 2 1


# ---------------------------------------
# 5. Loop Through a String
# ---------------------------------------
language = "Python"

for letter in language:
    print(letter)

# Output: P y t h o n (on separate lines)


# ---------------------------------------
# 6. Loop Through a List
# ---------------------------------------
fruits = ["Apple", "Banana", "Mango"]

for fruit in fruits:
    print(fruit)

# Output:
# Apple
# Banana
# Mango


# ---------------------------------------
# 7. Using Conditions Inside a Loop
# ---------------------------------------
for number in range(1, 6):
    if number % 2 == 0:
        print(number, "is even")
    else:
        print(number, "is odd")


# ---------------------------------------
# 8. Calculate Total Using a Loop
# ---------------------------------------
total = 0

for number in range(1, 6):
    total += number

print("Total:", total)

# Output: Total: 15


# ---------------------------------------
# 9. Loop with else
# ---------------------------------------
# The else block runs if the loop finishes normally.
# It does not run if the loop is stopped using break.

for number in range(1, 4):
    print(number)
else:
    print("Loop completed")

# Output:
# 1
# 2
# 3
# Loop completed


# ---------------------------------------
# 10. Nested For Loops
# ---------------------------------------
# A nested loop is a loop inside another loop.
# The inner loop runs completely for each outer iteration.

for i in range(1, 3):
    for j in range(1, 4):
        print(i, j)

# Output:
# 1 1
# 1 2
# 1 3
# 2 1
# 2 2
# 2 3


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. for loops repeat code for each item.
# 2. range(stop) starts at 0 by default.
# 3. The stop value in range() is excluded.
# 4. Negative steps allow backward counting.
# 5. for loops can iterate over strings and lists.
# 6. Nested loops are loops inside other loops.
# 7. Loop indentation is important.
