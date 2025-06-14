# WAP to find the factorial of first n numbers using for.
n = int(input("n: "))
def factorial(n):
    result = 1
    for i in range(1,n+1):              # Semi Colon nahi comma hota hai range mein.
        result *= i
        print(f"Factorial of {i} is {result}")      # f is important for formatting purposes here. 
    return result                       # Return hamesha loop ke niche aayega.
factorial(n)    
           