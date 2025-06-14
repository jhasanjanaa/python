'''
Search for a number x in this tuple using loop:
[1, 4, 9, 16, 25, 36, 49, 64, 81,100]
'''
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

Number = int(input("Enter the number searching for: "))

for x in tup:
    if (x == Number):
        print("Yes, the number is present.")
    

# GOOD    