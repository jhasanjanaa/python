'''
Create a class User with a private attribute _password. 
Add methods to set and get the password. Ensure the password cannot be accessed directly.
'''
# INCAPSULATION:
class User:
    def __init__(self, _password):
        self._password = _password
Object = User(456897)
print(Object._password)        