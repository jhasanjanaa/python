'''
➡ Ek Library class banao jisme ek class variable total_books ho jo initially 100 ho.
➡ Ek class method update_books() likho jo total_books ko update kare.
➡ Ek Library object banao, total books update karo aur print karo.
'''
class Library:
    total_books = 100
    @classmethod
    def update_books(cls, new):
        cls.total_books = new
            
L1 =Library()
print(L1.total_books)            
Library.update_books(250)                     # Kyuki ham prev lib ko update kar rae haina.
print(L1.total_books)
