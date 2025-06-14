# SET: Set is the collection of unordered items.
# Each iteam in a set must be unique and immutabble.

A = {"ENHYPEN", "ENHYPEN", "DAY", 1, 2, 2.8}
print(A)
print(type(A))

# The order we wrote is not printed i.e unordered set.
# For empty set we can't do set = {} cuz this is the notation for empty dictionary.
empty_set = set() # For empty set.
print(type(empty_set))

'''
SET METHODS:

1. set.add(el)           = Adds an element.

2. set.remove(el)        = Removes an element.

3. set.clear()           = Empties the set.

4. set.pop()             = Removes a random value.

5. set.union(set2)       = Combines both value and returns new.

6.set.intersection(set2) = Combines common values and returns new.

'''

A = {"ENHYPEN", "ENHYPEN", "DAY", 1, 2, 2.8}

A.add("BEST")
print(A)

A.remove(2.8)
print(A)

A.pop()
print(A)

A2 = {"ENHYPEN", 3, 1}

A.union(A2)
print(A.union(A2))

print(A.intersection(A2))