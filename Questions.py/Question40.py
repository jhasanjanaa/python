'''
Ek Employee class banao jisme ek class variable company ho jo "Google" ho.
➡ Ek class method change_company() likho jo company ka naam update kare.
➡ Ek Employee object banao, company update karo aur dono values print karo.
'''
class Employee:
    Company = "Google"   # Class Variable isi ko ham change karte hai.
    @classmethod
    def change_company(cls, new_company):
        cls.Company = new_company
E1 = Employee()
print(E1.Company)
Employee.change_company('Microsoft')       # Yaha hamne uski andar ki value change ki.
print(E1.Company)
