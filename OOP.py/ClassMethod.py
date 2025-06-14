# Ye pura class ke liye hota hai, kisi ek object ke liye nahi.

# cls ka use hota hai (self nahi).

# Class variables ko modify kar sakta hai.

# @classmethod decorator lagta hai.

# ✅ Example - Class Method

class Student:
    school = "DPS"  # Class variable

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school  # Class variable change ho raha hai

s1 = Student()
print(Student.school)  # DPS

Student.change_school("KV")            # KYUKI HAM STUDENT KO UPDATE KAR RAE HAI IE CLASS VARIABLE KO.
print(Student.school)  # KV
# 👉 change_school() ek class method hai jo pura class ka variable change kar raha hai.

