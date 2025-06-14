# Ye object ke data ko access karta hai.

# self ka use hota hai (kyunki ye object se linked hota hai).

# ✅ Example - Instance Method

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks  

    def show_details(self):  # Instance method
        print(f"Name: {self.name}, Marks: {self.marks}")

s1 = Student("Sanjana", 95)
s1.show_details()  # Name: Sanjana, Marks: 95
# 👉 show_details() ek instance method hai kyunki ye self ka use kar raha hai.