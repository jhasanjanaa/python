'''
Create a parent class Bird with a method speak() that prints "Chirp Chirp!".
Then, create two child classes Parrot and Crow that override speak() to print:
"I can mimic human speech!" for Parrot
"Caw Caw!" for Crow
'''
class Bird:
    def speak(self):
        print("Chirp Chirp!")  # Default bird sound

class Parrot(Bird):
    def speak(self):  # Overriding speak() method
        print("I can mimic human speech!")

class Crow(Bird):
    def speak(self):  # Overriding speak() method
        print("Caw Caw!")

# Creating objects
p = Parrot()
c = Crow()

p.speak()  # Output: I can mimic human speech!
c.speak()  # Output: Caw Caw!
 
