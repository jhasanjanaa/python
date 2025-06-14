'''
Ek Car class banao jisme brand aur model ho.
➡ Ek instance method display_info() likho jo brand aur model print kare.
➡ Ek object banao aur display_info() call karo.
'''

class Car:
   
    def __init__(self, Brand, Model):
        self.Brand = Brand
        self.Model = Model

        
    def display_info(self):
        print(f"The Brand of our car is {self.Brand} and the model is {self.Model}.")


Car1 = Car('Mahindra', 'XUV700')
print(Car1.Brand)
print(Car1.Model)

Car1.display_info()
