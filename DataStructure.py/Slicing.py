#Accessing parts of a string.

str = "Bro I really don't know what to write."

print(len(str))
print(str[20:30])

# S A N J A N A
# 0 1 2 3 4 5 6      Always these strings are starting with 0.
'''
Negative Index
Backward Counting

S  A  N
-3 -2 -1

In backward slicing we use two colons, one for start end and other for stepping.
A[::-1]
'''
#We can access our range with backward counting aswell.