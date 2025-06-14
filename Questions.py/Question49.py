'''
Create a class Employee with a class attribute company_name = "TechCorp". 
Add a method to change the company name and update it to "Innovate Ltd.".
'''
class Employee:
    company_name = "TechCorp"    # Class Attribute
    @classmethod
    def update(cls, name):
        cls.company_name = name
Object = Employee()
print(Object.company_name)    
Object.update("Innovate Ltd.") 
print(Object.company_name)   