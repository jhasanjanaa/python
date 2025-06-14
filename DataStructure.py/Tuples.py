    # Tuples: A built in data type that let us create immutable sequences of values.
# Lists are mutable i.e values can be changed, but tuples and strings are immutable, once a value is given it cannot be changed.
# In tuples we use parenthesis i.e () brackets.

# There can exist empty tuple aswell. Just have it as ().
# For python to understand that it is tuple, we need to add comma if one element is there.
# Slicing is same as other cases.

'''
TUPLE METHODS:

1. tup.index(el) = returns index of first occurance.

2. tup.count(el) = counts total occurances.

'''

tuple = (1,3,7,50)
print(type(tuple))

print(tuple[1:3])