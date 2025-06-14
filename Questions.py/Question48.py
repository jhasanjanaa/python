'''
Create an abstract class BankAccount with an abstract method get_balance().

Create SavingsAccount and CurrentAccount classes that provide different ways to display balance.

Implement a constructor (__init__) to set the initial balance in both subclasses.
'''
# from abc import ABC, abstractmethod
# class BankAccount(ABC):
#     def __init__(self, balance):
#         self.balance = balance
        
#     @abstractmethod
#     def get_balance(self):
#         pass
# class SavingsAccount(BankAccount):
#     def get_balance(self, saving):
#         self.saving = saving
# class CurrentAccount(BankAccount):
#     def get_balance(self, current):
#         self.current = current

# Person = BankAccount(100000)
# print(Person.saving(222222222222222222))
# print(Person.current(11111111111111111111111))        
        
from abc import ABC, abstractmethod

class BankAccount(ABC):  
    def __init__(self, balance):
        self.balance = balance  

    @abstractmethod
    def get_balance(self):
        pass  

class SavingsAccount(BankAccount):
    def get_balance(self):
        print("Savings Account Balance: ₹", self.balance)

class CurrentAccount(BankAccount):
    def get_balance(self):
        print("Current Account Balance: ₹", self.balance)

# Creating objects
s = SavingsAccount(5000)
c = CurrentAccount(20000)

s.get_balance()  # Output: Savings Account Balance: ₹ 5000
c.get_balance()  # Output: Current Account Balance: ₹ 20000
    