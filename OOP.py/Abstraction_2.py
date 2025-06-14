'''
Create an abstract class Vehicle with an abstract method start(). Create Car and Bike classes that implement it differently.
'''
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car starts with a button.")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a key.")

C = Car()
C.start() 

B = Bike()
B.start()

'''
The abstract class hides unnecessary details and only provides a necessary function (start()).

The child classes (Car, Bike) handle different implementations without exposing them directly.

The user only sees the important part: every vehicle must have a way to start.
'''