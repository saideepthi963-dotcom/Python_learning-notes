"""
----------------------  EXPRESSIONS AND OPERATORS  -----------------------------------
An expression is a combination of values, variables, and operators that Python evaluates to produce a result.

Example:
result = 10 + 5

Operators are symbols or keywords used to perform operations on values.

Arithmetic Operators:
- Addition(+): a + b
- Subtraction(-): a - b
- Multiplication(*): a * b
- Division(/): a / b
- Modulus(%): a % b
- Floor division(//): a // b
- Exponentiation(**): a ** b

"""

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)
print("Exponent:", a ** b)

"""ASSIGNMENT OPERATORS

=     Assign value
+=    Add and assign
-=    Subtract and assign
*=    Multiply and assign
/=    Divide and assign
//=   Floor divide and assign
%=    Modulus and assign
**=   Power and assign       """

score = 10
score += 5
print(score)        # 15

score -= 3
print(score)        # 12

score *= 2
print(score)        # 24

score /= 4
print(score)        # 6.0

""" COMPARISON OPERATORS

Comparison operators compare two values.
The result is always True or False.

==   Equal to
!=   Not equal to
>    Greater than
<    Less than
>=   Greater than or equal to
<=   Less than or equal to
a = 10
b = 5  """

print(a == b)       # False
print(a != b)       # True
print(a > b)        # True
print(a < b)        # False
print(a >= b)       # True
print(a <= b)       # False

#Comparing string lengths
word_one = "Python"
word_two = "SQL"

print(len(word_one) > len(word_two))     # True


"""LOGICAL OPERATORS
Logical operators combine Boolean expressions. 

and -> True when BOTH conditions are True
or  -> True when AT LEAST ONE condition is True
not -> reverses True and False  """

age = 25
has_id = True

print(age >= 18 and has_id)      # True
print(age < 18 or has_id)        # True
print(not has_id)                # False 

#Another example
temperature = 75

print(temperature > 60 and temperature < 90)


""" MEMBERSHIP OPERATORS

in
not in

Membership operators check whether a value exists inside another object. """

language = "Python" 

print("Py" in language)          # True
print("Java" in language)        # False
print("Java" not in language)    # True

skills = ["Python", "SQL", "Git"]

print("SQL" in skills)           # True


""" IDENTITY OPERATORS

is
is not

Identity operators check whether two variables refer to the SAME object.

Do not use "is" when you simply want to compare values. 
Use == for value comparison. """

list_one = [1, 2, 3]
list_two = [1, 2, 3]
list_three = list_one

print(list_one == list_two)       # True - values are equal
print(list_one is list_two)       # False - different objects
print(list_one is list_three)     # True - same object

# A common correct use of "is"
value = None

print(value is None)              # True


""" OPERATOR PRECEDENCE

Python follows an order when evaluating expressions.

Basic order:

1. ()
2. **
3. *, /, //, %
4. +, -
5. comparison operators
6. not
7. and
8. or  """

result = 5 + 3 * 2

print(result)             # 11

result = (5 + 3) * 2

print(result)             # 16