'''
Create a BankAccount class where:

Balance is private.

You can deposit money using deposit().

You can check balance using get_balance().
'''

class BankAccount:
    def __init__(self, deposit):
        self.deposit = deposit
    def get_balance(self):
        return self.deposit
    def change_deposit(self, new):
        self.deposit = new

Acc = BankAccount(1000)
print(Acc.get_balance())
Acc.change_deposit(5000)
print(Acc.get_balance())

