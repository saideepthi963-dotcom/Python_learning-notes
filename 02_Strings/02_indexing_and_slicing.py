""" STRING INDEXING AND SLICING
Indexing lets us access individual characters in a string.
Slicing lets us access a part of a string.

1. POSITIVE INDEXING
#
Positive indexing starts from 0.

P  y  t  h  o  n
0  1  2  3  4  5 """

language = "Python"
print(language[0])    # P
print(language[1])    # y
print(language[2])    # t
print(language[5])    # n

"""
2. NEGATIVE INDEXING

Negative indexing starts from -1 at the end of the string.
P   y   t   h   o   n
-6 -5  -4  -3  -2  -1   """
print(language[-1])   # n
print(language[-2])   # o
print(language[-3])   # h

"""
3. STRING SLICING

Syntax:
string[start]

start is included
stop is excluded """
language = "Python"

print(language[0:3])    # Pyt
print(language[1:4])    # yth
print(language[2:6])    # thon


#4. OMITTING START OR STOP

#If start is missing, slicing starts from the beginning.
print(language[:3])     # Pyt

#If stop is missing, slicing continues to the end.
print(language[2:])     # thon

#If both are missing, the whole string is returned.
print(language[:])      # Python


#5. SLICING WITH STEP

#Syntax:
#string[start:stop]

# step decides how many positions to move each time.
text = "abcdefghij"

print(text[::2])        # acegi [start: end : step]
print(text[1::2])       # bdfhj


# 6. REVERSE A STRING

word = "Python"

reversed_word = word[::-1]

print(reversed_word)     # nohtyP


# 7. NEGATIVE SLICING

text = "Programming"

print(text[-4:])         # ming
print(text[:-4])         # Program


# 8. ACCESSING FIRST AND LAST CHARACTERS

name = "Deepthi"

print(name[0])           # D
print(name[-1])          # i


# 9. USING len() WITH INDEXING

word = "HackerRank"

last_index = len(word) - 1

print(last_index) #9
print(word[last_index]) #k


#10. INDEX ERROR

word = "Python"

#Python has indexes from 0 to 5.
#Accessing an index that does not exist causes IndexError.
print(word[10])   # IndexError

#11. SLICING DOES NOT USUALLY GIVE INDEXERROR

#Slicing safely stops at the end of the string.
word = "Python"

print(word[0:100])      # Python

""" 12. STRINGS ARE IMMUTABLE

Individual string characters cannot be changed directly. """

language = "Python"  

#Invalid:
language[0] = "J"
#Instead, create a new string.
new_language = "J" + language[1:]

print(new_language)     # Jython