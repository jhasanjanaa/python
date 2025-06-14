# WAP to find the greatest of three numbers entered by the user.

A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))

if A > B and A > C:
    print("A is the greatest of all the given numbers.")

elif B > A and B > C:
    print("B is the greatest of all the given numbers.")

elif C > A and C > B:
    print("C is the greatest of all the given numbers.")

else:
    print("There's and error")    
