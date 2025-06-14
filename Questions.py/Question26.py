# WAP to find the factorial of n.

# How about doing this code with so called recursion <3

def fac(n):
    if n == 0 or n == 1:
        return 1                     #Print ham jo return kar rae hai vahi print karayenge na aur print toh is function ko jabtak call nahi karenge tab tak hone bhi wala nahi.
    else:
        n = n * fac(n-1)
        return n
    
print(fac(7))    
    

# Very Very Good
    