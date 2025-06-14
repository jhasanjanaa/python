'''
Practice Question 2:
➡ Ek Student class banao jisme name aur age store ho.
➡ Jab bhi object bane, constructor (__init__) use hoke name aur age set kare.
➡ Ek object banao aur uska name aur age print karo.
'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

S1 = Student('Sanjana', '19')
print(S1.name)
print(S1.age)
