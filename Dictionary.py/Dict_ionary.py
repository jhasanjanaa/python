# Dictionary in Python : Dictionaries are used to store values in key:value pairs.
# They are unordered, mutable (changable) and doesn't allow duplicate key.
# There is no indexing.
'''
Word : Meaning
Key  : Value

'''

dict = {
    "Name" : "Sanjana Jha",
    "Age" : 18
}

'''
To change the value aka meaning.
dict("Name") = "Sanjana"
'''

print(dict)


'''
For Accessing use square brackets.
'''

dict["Name"]
dict["Age"]

#For printing:
print(dict["Name"])

# Can create empty dictionary aswell. null_dict = {}
null_dictionary = {}
print(null_dictionary)

# To add elements:
null_dictionary["Favourite Subject"] = "Python Programming"

print(null_dictionary)


# Nested Dictionary: Dictionary inside Dictionary.
Singers = {
    "Favourite Artist" : {
        1 : "Jungwon",
        2 : "Heeseung",
        3 : "Jay",
        4 : "Jake",
        5 : "Sunghoon",
        6 : "Sunoo",
        7 : "Niki"
    }
    }

print(Singers)
print(Singers["Favourite Artist"])
print(Singers["Favourite Artist"][4])


'''
DICTIONARY METHODS:

1. myDict.keys()              = Return all Keys.

2. myDict.values()            = Return all Values.

3. myDict.items()             = Return all key : value pairs as tuples.

4. myDict.get("Key"")         = Return the key according to the value.

5. myDict.update(newDict)     = Inserts the specified items to the dictionary.

'''




