# What is Inheritance?
# Imagine you have a parent and a child. The child gets some qualities from the parent, like eye color, height, or habits. 
# Similarly, in programming, a child class gets properties and behaviors from a parent class.

# 🔹 Why Use Inheritance?
# Reuse code (No need to write the same code again and again).

# Save time (Use the existing class and just add new features).

# Make better programs (Organized and structured).

# 🔹 Example in Real Life
#  Father (Parent Class) → Has a surname and eye color.
#  Son (Child Class) → Automatically gets the surname and eye color from the father but can have his own hobbies.

# 🔹 Example in Python

# Parent class
class Animal:
    def sound(self):
        print("Animals make sounds")

# Child class (inherits from Animal)
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Creating an object of Dog
doggy = Dog()
doggy.sound()  # Comes from the Parent class
doggy.bark()   # Comes from the Child class
# ✅ Here, Dog gets the sound() function from Animal without writing it again!
