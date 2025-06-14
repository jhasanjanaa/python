# Abstraction (Hiding Complexity)
# Abstraction means hiding complex details and showing only what is necessary.
# Abstract classes act as blueprints for other classes.


# Why is it useful?
# Users don’t need to know how things work internally.

# Helps to keep code clean and easy to use.

# 🔹 Example Without Abstraction (BAD Approach)

class Car:
    def __init__(self):
        self.engine_status = False

    def start_engine(self):
        print("Turning on fuel pump...")
        print("Injecting fuel...")
        print("Starting engine...")
        self.engine_status = True
        print("Engine started!")

c = Car()
c.start_engine()
# Problem: The user sees all unnecessary steps.

# 🔹 Example With Abstraction (GOOD Approach)

from abc import ABC, abstractmethod

class Vehicle(ABC):  # Abstract class
    @abstractmethod
    def start(self):  # Abstract method (no details)
        pass  

class Car(Vehicle):
    def start(self):
        print("Car started with a key!")

class Bike(Vehicle):
    def start(self):
        print("Bike started with a button!")

c = Car()
c.start()  # Output: Car started with a key!
# ✅ The user only sees start() instead of complex internal processes.

# 🔹 Mini Topics in Abstraction
# Abstract Classes: Classes that cannot be used directly.

# Abstract Methods: Methods that must be defined in child classes.

# Hiding Complexity: Only showing essential parts to the user.

