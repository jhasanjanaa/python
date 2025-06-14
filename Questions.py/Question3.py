# WAP to check if number entered by user is odd or even.

N = int(input("N: "))

if N % 2 == 0:
    print("The number is even.")

elif N % 2 != 0:
    print("The number is odd.")

else:
    print("The number is not defined.")    