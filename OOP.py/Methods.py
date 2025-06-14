# Methods - (Class ke Andar Functions)
# Methods kya hote hain?
# Methods functions hote hain jo kisi object pe kaam karte hain.
# Matlab object ka kaam karne ka tareeka hote hain!
# METHOD OBJECT SE KAAM KARANE KE LIYE USE HOTE HAI!
# ✅ Example - Car ka method (function)

class Car:
    def __init__(self, brand):
        self.brand = brand  

    def honk(self):  # Ye method hai
        print(f"{self.brand} is honking! 🚗📢")

car1 = Car("BMW")
car1.honk()  # BMW is honking! 🚗📢


# def honk(self) → Ye ek method hai jo self.brand ka use karega.

# car1.honk() → BMW horn bajayega!


# There are three types of methods. In seperate parts.
