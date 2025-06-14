# When a function calls itself repeatedly.

# Print numbers from 1 to 7.
'''
def show(n):
    if ( n == 0):      # Base case: Batayega yahan recursion rukna chahiye ya nahi rukna chahiye.
        return         # Khali return likhna matlab koi value return nahi hoyegi, bas control return kar rae hai, aage na badhega.
    print(n)
    show(n-1)          # Function call hogaya na.

show(7)

'''# For Factorial:
def fact(n):
    if (n==0 or n==1):
        return 1
    else:
        return (n * fact(n-1))    # Ab factorial of n-1 ko call lagaya.
        
print(fact(9))


#Good