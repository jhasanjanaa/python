'''                                            
Types of String Functions:

str = "Sanjana is the best."
1. str.endswith("best")         = Return with True or False Value.

2. str.capitalize()             = Capitalizes first character.

3. str.replace(old, new)        = Replaces all occurances of old.

4. str.find(word)               = Returns first index of first occurrer.

5. str.count("is")              = Counts the number of time a word appeared.

'''
# EXAMPLES :

str = "well, i really don't know what should i write."

print(str.endswith("ite."))
print(str.capitalize())
print(str.replace("i", "we"))
print(str.find("well"))
print(str.count("i"))