
# ================================================================================
# WHILE LOOPS IN PYTHON
# ----------------------------------------
# A while loop repeats a block of code as long as a condition is True.
# It stops when the condition becomes False.
# ================================================================================


# ---------------------------------------
# 1. Basic While Loop
# ---------------------------------------
# Print numbers from 1 to 5.

number = 1

while number <= 5:
    print(number)
    number += 1

# Output:
# 1
# 2
# 3
# 4
# 5


# ---------------------------------------
# 2. While Loop with Decrement
# ---------------------------------------
# Count backward from 5 to 1.

number = 5

while number >= 1:
    print(number)
    number -= 1

# Output: 5 4 3 2 1


# ---------------------------------------
# 3. While Loop with a Condition
# ---------------------------------------
# The loop stops when the condition becomes False.

temperature = 30

while temperature > 25:
    print("Temperature:", temperature)
    temperature -= 1

print("Temperature is now 25 or below")

# Output:
# Temperature: 30
# Temperature: 29
# Temperature: 28
# Temperature: 27
# Temperature: 26
# Temperature is now 25 or below


# ---------------------------------------
# 4. While Loop with User Input
# ---------------------------------------
# Keep asking until the user enters "quit".
# Uncomment this example to run it.

# command = ""
#
# while command != "quit":
#     command = input("Enter command (quit to stop): ")
#     print("You entered:", command)


# ---------------------------------------
# 5. While Loop with else
# ---------------------------------------
# The else block executes when the loop
# finishes normally without a break.

number = 1

while number <= 3:
    print(number)
    number += 1
else:
    print("Loop completed")

# Output:
# 1
# 2
# 3
# Loop completed


# ---------------------------------------
# 6. Infinite While Loop
# ---------------------------------------
# An infinite loop runs continuously
# when its condition never becomes False.
#
# Example (DO NOT RUN without a stopping condition):
#
# while True:
#     print("Hello")
#
# To avoid infinite loops, ensure there is
# a way to stop the loop.


# ---------------------------------------
# 7. For Loop vs While Loop
# ---------------------------------------
# for loop:
# Used to iterate over a sequence or range.

for number in range(1, 4):
    print(number)

# while loop:
# Used to repeat code while a condition is True.

number = 1

while number < 4:
    print(number)
    number += 1

# Both print 1, 2, 3.


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. while loops repeat while a condition is True.
# 2. The condition is checked before each iteration.
# 3. Update variables to avoid accidental infinite loops.
# 4. A while loop may execute zero times.
# 5. while loops are useful when repetition depends
#    on a condition instead of a fixed sequence.
# 6. The else block runs when the loop ends normally.


