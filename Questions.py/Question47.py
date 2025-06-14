'''
Create an abstract class Appliance with an abstract method turn_on().

Create Fan and WashingMachine classes that implement turn_on() differently.

Try to create an object of Appliance and see what happens!
'''
from abc import ABC, abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass
class Washing_Machine(Appliance):
    def turn_on(self):
        print("Turn on the requirements as per your need. It is displayed in the contriol terminal of the machine.") 
class Fan(Appliance):
    def turn_on(self):
        print("Turn on the switch, or use remote.")

# Creating instances
wm = Washing_Machine()  
fan = Fan()

# Calling methods on instances
wm.turn_on()        
fan.turn_on()

