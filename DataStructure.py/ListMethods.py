
'''
1. list.append(No.)            = Adds a number at the end.

2. list.sort()                 = Sorts in ascending order.

3. list.sort( reverse = True)  = Arranges in descending order.

4. list.reverse()              = Reverses List.

5. list.insert(index, element) = Insert Element at index.

6. list.pop(index)             = Removes element at index.

7. list.remove(No.)            = Removes first occurance of the number. Jab pehli baar vo number aaya list mein.

'''
#EXAMPLE SECTION:

list = [ 7, 9, 5]

list.append(4)
print(list)

list.sort()
print(list)

list.sort( reverse = True)
print(list)

list.reverse()
print(list)

list.insert(1, 12)
print(list)

# print(list.sort()) or any other function will return none.

list.pop(2)
print(list)


'''
list = input("Enter elements by spaces: ").split()  # Split will make list of all elements.
'''