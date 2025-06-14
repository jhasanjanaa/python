'''
You are given a list of numbers.
Write a Python program that finds the first even number in the list and stops checking further using the break statement.
If no even number is found, print "No even number found.
'''

Numbers = list(map(int, input("Enter the numbers seperated by space: ").split()))
print(Numbers)

i = 1
for num in Numbers:
    print("Number",i, ": ", num)
    i += 1

for num in Numbers:
    if num % 2 == 0:

        print("First Even Number in the list is:", num)
        break
print("Command Ended.")


# Good Girl
