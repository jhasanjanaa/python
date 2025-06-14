'''
Create two parent classes:

Chef with method cook() → prints "I can cook"

Singer with method sing() → prints "I can sing"

Then, create a Child class Person that inherits from both Chef and Singer.
Create an object of Person and call both methods.
'''
class Chef:
    def cook(self):
        print("I can cook.")
class Singer:
    def sing(self):
        print("I can sing.")
class Person(Chef, Singer):
    def hobbies(self):
        print("I can cook and sing.")
P1 = Person()
P1.cook()
P1.sing()
P1.hobbies()

                 