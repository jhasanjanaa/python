'''
Create a class Calculator with a method subtract(a, b) that returns the difference of two numbers without creating an instance of the class.
'''
import math
class Calculator:
    @staticmethod
    def subtract(a,b):
        return a - b
print(Calculator.subtract(18,14))