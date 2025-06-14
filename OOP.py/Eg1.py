class Pizza:
    def __init__(self, size, topping):  # Jab object banega, ye function chalega
        self.size = size  
        self.topping = topping  

pizza1 = Pizza("Large", "Cheese")  
pizza2 = Pizza("Small", "Veggies")  

print(pizza1.size)  # Large
print(pizza2.topping)  # Veggies
