# Hierarchical Inheritance (One Parent, Many Children)
# One parent, multiple child classes.

# Like a father having many kids, and each kid having their own talent.

# Example:

class Dad:  
    def house(self):  
        print("Dad owns a house")  

class Son(Dad):  
    def football(self):  
        print("Son plays football")  

class Daughter(Dad):  
    def dance(self):  
        print("Daughter loves dancing")  

s = Son()  
s.house()   # Inherited from Dad  
s.football()  

d = Daughter()  
d.house()   # Inherited from Dad  
d.dance()  
# ✅ Son and Daughter both inherit from Dad, but have different skills!



'''
Hybrid Inheritance (Mix of Everything 😵‍💫)
A mix of two or more types of inheritance together.

Just like a family tree with lots of connections!

Since it's a complex mix, we use it rarely!
'''