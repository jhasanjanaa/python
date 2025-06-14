'''
Practice Question 4:
➡ Ek Mobile class banao jisme brand aur price ho.
➡ Ek method show_details() banao jo brand aur price print kare.
➡ Ek Mobile object banao aur show_details() call karo.
'''

class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def show_details(self):
        print(f"The brand of the mobile is {self.brand} and price is {self.price}")

MobilePhone = Mobile('Google Pixel', '70K')
MobilePhone.show_details()
