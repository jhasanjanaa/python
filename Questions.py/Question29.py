# Write a recursive function to print all elements in a list.

list1 = list(input("Enter the elements of your list:").split())

def print_list(list):
    if list == []:
        return 0
    else:
        return list
    
print(print_list(list1))    

# Very Very Good.
