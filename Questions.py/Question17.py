# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 61, 81,100]

tuple = (1, 4, 9, 16, 25, 36, 49, 61, 81,100)
# We can see tuple have 10 elements.

# WAY 1:
'''
print("The tuple have 10 elements. Choose any number btw 0 to 9.")
Count = int(input("Count: "))
while Count <= 9:
    print(tuple[Count])
    break
'''

# WAY 2:
'''
print(36 in tuple)    # True
print(102 in tuple)   # False
'''

# WAY 3 [NOW BY LOOP]

tuple = (1, 4, 9, 16, 25, 36, 49, 61, 81,100)

'''
Number = int(input("Number: "))
while Number in tuple:
    print("Found!")           # But this will give you an infinite loop.><
'''

tuple = (1, 4, 9, 16, 25, 36, 49, 61, 81,100)
X = int(input("X: "))
Y = tuple()