# Duck Typing (If it acts like a duck, it's a duck!)
# In Python, we don’t care about the type of an object. If it has the required method, we can use it!
 
# Example in Python

class Dog:
    def speak(self):
        print("Woof! Woof!")

class Cat:
    def speak(self):
        print("Meow! Meow!")

def make_sound(animal):
    animal.speak()  # Doesn't matter if it's a Dog or Cat!

dog = Dog()
cat = Cat()

make_sound(dog)  # Output: Woof! Woof!
make_sound(cat)  # Output: Meow! Meow!
# ✅ Function works with different types of objects as long as they have the method!


