'''
Figure out a way to store 9 & 9.0 as separate values in the set.
(You can take help of built-in data types.)
'''

'''
x = int("9")
y = float("9")
print(y) 

list = []
list.append(x)

list.append(y)
print(list)
But you did all this for list not set.'''


# Now for set
x = (9, "int")    # 9 ko ek tuple me store kiya, jisme type ka bhi mention kiya
y = (9.0, "float")

set = set()
set.add(x)
set.add(y)
print(set)

