# Random Module

# The random module is used to generate random values.
# It is useful for games, simulations, random selections,
# test data, and simple practice programs.

import random


# random.random()
# Returns a random float between 0.0 and 1.0.

value = random.random()

print(value)

# Example Output:
# 0.573821


# random.randint()
# Returns a random integer between the given start and end values.
# Both values are included.

number = random.randint(1, 10)

print(number)

# Example Output:
# 7


# random.randrange()
# Returns a random number from a range.
# The stop value is not included.

number = random.randrange(1, 10)

print(number)

# Example Output:
# 6


# random.randrange() with step

number = random.randrange(0, 20, 2)

print(number)

# Example Output:
# 14


# random.uniform()
# Returns a random float between two values.

price = random.uniform(10, 20)

print(price)

# Example Output:
# 16.438291




# random.choice()
# Selects one random item from a sequence.

skills = ["Python", "SQL", "Git", "Power BI"]

selected_skill = random.choice(skills)

print(selected_skill)

# Example Output:
# SQL




# random.shuffle()
# Randomly changes the order of items in a list.
# It changes the original list.

numbers = [1, 2, 3, 4, 5]

random.shuffle(numbers)

print(numbers)

# Example Output:
# [3, 5, 1, 4, 2]


# Simple Dice Roll

dice = random.randint(1, 6)

print(dice)

# Example Output:
# 4



