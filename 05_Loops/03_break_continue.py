
# ================================================================================
# BREAK, CONTINUE, AND PASS IN PYTHON
# ----------------------------------------
# These statements control how loops execute.
#
# break    -> Stops the loop completely.
# continue -> Skips the current iteration.
# pass     -> Does nothing (placeholder).
# ================================================================================


# ---------------------------------------
# 1. BREAK Statement
# ---------------------------------------
# break stops the loop when a condition is met.

for number in range(1, 6):
    if number == 4:
        break
    print(number)

# Output:
# 1
# 2
# 3

# The loop stops when number becomes 4.


# ---------------------------------------
# 2. CONTINUE Statement
# ---------------------------------------
# continue skips the current iteration
# and moves to the next iteration.

for number in range(1, 6):
    if number == 3:
        continue
    print(number)

# Output:
# 1
# 2
# 4
# 5

# Number 3 is skipped.


# ---------------------------------------
# 3. PASS Statement
# ---------------------------------------
# pass is a placeholder that does nothing.
# It is useful when code is not yet written.

for number in range(1, 4):
    if number == 2:
        pass
    print(number)

# Output:
# 1
# 2
# 3

# pass does not stop or skip the iteration.


# ---------------------------------------
# 4. BREAK with While Loop
# ---------------------------------------
number = 1

while number <= 5:
    if number == 4:
        break
    print(number)
    number += 1

# Output:
# 1
# 2
# 3


# ---------------------------------------
# 5. CONTINUE with While Loop
# ---------------------------------------
number = 0

while number < 5:
    number += 1

    if number == 3:
        continue

    print(number)

# Output:
# 1
# 2
# 4
# 5

# Update the counter before continue
# to avoid an infinite loop.


# ---------------------------------------
# 6. BREAK with Loop ELSE
# ---------------------------------------
# The else block does not run if break executes.

for number in range(1, 6):
    if number == 3:
        break
    print(number)
else:
    print("Loop completed")

# Output:
# 1
# 2


# ---------------------------------------
# 7. BREAK vs CONTINUE
# ---------------------------------------
# break stops the entire loop.
# continue skips only the current iteration.

for number in range(1, 6):
    if number == 2:
        continue
    if number == 5:
        break
    print(number)

# Output:
# 1
# 3
# 4


# ---------------------------------------
# Important Points
# ---------------------------------------
# 1. break exits the nearest enclosing loop.
# 2. continue skips to the next iteration.
# 3. pass does nothing and is a placeholder.
# 4. break and continue work with for and while.
# 5. Loop else does not execute if break stops the loop.
# 6. Be careful using continue in while loops.
