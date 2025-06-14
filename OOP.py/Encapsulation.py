# Encapsulation (Hiding Data)
# Encapsulation means hiding data inside a class so it can’t be changed directly.
# ALL WE DO HERE IS ASSIGNING A VARIABLE WITH _.

# Why is it useful?
# It protects data from accidental changes.

# Only specific methods can access or modify data.

# 🔹 Example Without Encapsulation (BAD Approach)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age  # This can be changed directly

p = Person("Jake", 20)
p.age = 100  # OOPS! Anyone can change the age!
print(p.age)  # Output: 100 (wrong change)
# Problem: Anyone can change age directly, which is risky.

# 🔹 Example With Encapsulation (GOOD Approach)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # Private variable (hides age)

    def get_age(self):  # Getter method
        return self.__age

    def set_age(self, new_age):  # Setter method
        if new_age > 0:  # Allow only valid ages
            self.__age = new_age

p = Person("Jake", 20)
print(p.get_age())  # Output: 20

p.set_age(25)  # Correct way to update age
print(p.get_age())  # Output: 25

p.set_age(-5)  # This won't work (invalid age)
print(p.get_age())  # Output: 25 (unchanged)
# ✅ Now, the age cannot be modified directly, only through set_age().

# 🔹 Mini Topics in Encapsulation
# Private Variables: Use __ before a variable name to make it private. (e.g., self.__balance)

# Getter Methods: A function to return the value of a private variable.

# Setter Methods: A function to update the value of a private variable with conditions.