# Write a recursive function to calculate the sum of n natural numbers.

def sum(n):
    if n == 1:          # Natural Numbers
        return 1
    else:
        plus = n + sum(n-1)     # Called our function again.
        return plus
    
print(sum(100))


# Very Very Good.