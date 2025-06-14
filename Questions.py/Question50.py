'''
Create an abstract class Shape with an abstract method area(). 
Create two subclasses, Circle and Square, and implement the area() method in both.
'''
from abc import ABC, abstractmethod
import math
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

class square(shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2

Object1 = circle(5)
print(Object1.area())       

Object2 = square(8)
print(Object2.area())


    