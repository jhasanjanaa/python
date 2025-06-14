# WAP to print the elements of list in single line.

list = input("Enter elements by spaces: ").split()  # Split will make list of all elements.

print(' '.join(list))

for item in list:
    print(item, end = " ")
