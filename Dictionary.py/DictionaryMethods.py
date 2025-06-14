'''
DICTIONARY METHODS:

1. myDict.keys()              = Return all Keys.

2. myDict.values()            = Return all Values.

3. myDict.items()             = Return all key : value pairs as tuples.

4. myDict.get("Key"")         = Return the key according to the value.

5. myDict.update(newDict)     = Inserts the specified items to the dictionary.

'''

Top2 = {
    "Songs" : {
        1 : "Moonstruck",
        2 : "Paranormal"

    },
    "Singers" : {
        1 : "Enhypen",
        2 : "The Weeknd"
    }
}


#EXAMPLE:
print(Top2.keys())
print(Top2.values())
print(Top2.items())
print(Top2.get("Songs"))

Top_2 = {
    "Songs" : {
        1 : "Moonstruck",
        2 : "XO"

    },
    "Singers" : {
        1 : "Enhypen",
        2 : "The Weeknd"
    }
}

Top2.update(Top_2)
print(Top2)
# Old dictionary got updated.
# We can use this method to update the values for old dictionary aswell.
