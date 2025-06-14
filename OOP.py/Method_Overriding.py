# Method Overriding (Same function, different behavior in child class)
# Example: A parent and child both have a function with the same name, but the child changes how it works.

# Example in Python

class Parent:
    def speak(self):
        print("I speak normally.")

class Child(Parent):
    def speak(self):  # Overriding the parent method
        print("I speak loudly!")

obj1 = Parent()
obj2 = Child()

obj1.speak()  # Parent's version
obj2.speak()  # Child's version (Overridden)
# ✅ Child changes the behavior of the function!

