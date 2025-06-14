'''
WAP to enter marks of 3 subjects from the user and store them in a dictionary.
Start with an empty dictionary & add one by one. Use subject name as key & marks as value.
'''

Marks_1 = input("Marks: ")
Marks_2 = input("Marks: ")
Marks_3 = input("Marks: ")
dictionary = {}

dictionary["Science"] = Marks_1
dictionary["Sanskrit"] = Marks_2
dictionary["English"] = Marks_3
print(dictionary)

