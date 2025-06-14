'''
📝 Practice Question 1:
➡ Ek Laptop naam ki class banao.
➡ Uske andar ek brand naam ka variable rakho.
➡ Laptop ka ek object banao aur uska brand print karo.
'''
class Laptop:
    def __init__(self, brand):
        self.brand = brand

Laptop1 = Laptop('Lenovo')
print(Laptop1.brand)     