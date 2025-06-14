'''
Create a class Mobile with a method brand_name() that prints "Apple". 
Create an object and call the method.
'''
class Mobile:
    brand_name = "Apple"
    def print(self):
        print(f"Phone's brand is {self.brand_name}")    
Phone = Mobile()
Phone.print()        