"""
Polymorphism
Duck Typing - Polymorphism (It is similar with Interface)

"""

class Book1:
    
    def info(self):
        print("Basics")
        print("Example Codes")

class Book2:
    
    def info(self):
        print("Advance")
        print("Online videos")
        print("Sample Codes")


class Student:
    
    def code(self, book):
        book.info()


b1 = Book1()
b2 = Book2()
st = Student()
st.code(b2)

