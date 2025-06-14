# Ye kisi object ya class variable ko modify nahi karta.

# self ya cls nahi hota isme.

# Independent function ki tarah kaam karta hai.

# @staticmethod decorator lagta hai.

# ✅ Example - Static Method

class MathUtils:
    @staticmethod
    def add(a, b):  # No self, No cls
        return a + b  

print(MathUtils.add(5, 3))  # 8
# 👉 add() ek static method hai, jo sirf calculation kar raha hai, class ke kisi bhi data se related nahi hai.