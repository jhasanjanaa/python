'''
Create a class Student with a private variable _marks and two methods:

get_marks(): Returns the marks.

set_marks(): Updates marks only if the value is between 0-100.

'''
class Student:
    _marks = 98
    def get_marks(self):
        return self._marks
    def set_marks(self, new_marks):
        if new_marks >= 0 or new_marks <= 100:
            self._marks = new_marks
        else:
            print("Marks should be between 0 to 100.")

S1 = Student()
print(S1.get_marks())      

S1.set_marks(100)
print(S1.get_marks())

    