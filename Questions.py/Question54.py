'''
Create a Parent class Vehicle with a method start_engine() that prints "Engine started".
Then, create a Child class Car that inherits from Vehicle and has its own method honk() that prints "Beep Beep!".
Finally, create an object of Car and call both methods.
'''
class Vehicle:
    def start_engine(self):
        print("Engine started!")
class Car(Vehicle):
    def honk(self):
        print("Beep Beep")
c = Car()
c.honk()
c.start_engine()
                