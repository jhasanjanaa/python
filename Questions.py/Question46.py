'''
Create a class BankAccount that follows these rules:
It should have a hidden attribute _balance that should not be accessible directly.    
Include a method deposit(amount) to add money to the account.
Include a method withdraw(amount) that subtracts money, ensuring the balance doesn’t go below a minimum limit.
Create another method to update the bank’s name for all accounts.
Add a function that prints "Banking rules: Maintain minimum balance of $500.", which should work without creating an account.
Ensure withdraw(amount) is not defined directly in BankAccount but must be implemented in subclasses.
Create a subclass SavingsAccount that allows withdrawal only if the balance remains above $500.
'''
class BankAccount:
    
