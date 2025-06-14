'''
➡ Ek Laptop class banao jisme brand ek class variable ho.
➡ Ek class method update_brand() likho jo brand update kare.
➡ Laptop ka brand update karo aur print karo.
'''
class Laptop:
    Brand = 'Lenovo'
    def update_brand(cls, new_brand):
        cls.Brand = new_brand

L1 = Laptop()
print(Laptop.Brand)
L1.update_brand('Dell')
print(L1.Brand)