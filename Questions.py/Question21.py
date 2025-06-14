# WAP to find the sum of first n elements using while.

n = int(input("n: "))

def sum_of_numbers(n):
    i = 0
    total = 0
    while i < n:
        total += i + 1
        i += 1
    print(total)

sum_of_numbers(n)

'''
# Using Range:
def sum_of_numbers(n):
    while range[0:n+1]:   # WRONG CODE COZ RANGE CANNOT BE DIRECTLY USED IN WHILE!!!!!
        total = sum(range[0:n+1])
        print(total)
        return sum(range[0:n+1])


sum_of_numbers(n)   '
'''