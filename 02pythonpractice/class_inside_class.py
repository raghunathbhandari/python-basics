"""
Call inside the class and Object access from outside and from upper call inside the main class

"""

class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()

    def show(self):
        print("Details about Student")
        print(self.name, self.rollno)

        print("Details about Laptop from Inside Class object")
        self.lap.show()
        # self.Laptop().show()
        # print(self.Laptop().brand, self.Laptop().cpu, self.Laptop().ram)

    class Laptop:

        def __init__(self):
            self.brand = "HP"
            self.cpu = "i5"
            self.ram = "8GB"

        def show(self):
            print(self.brand, self.cpu, self.ram)

        

s1 = Student("Raghu", 20)
s2 = Student("Shaivi", 34)
lap = Student.Laptop()

s1.name= "Jayanti"
lap.brand = "Lenove"


# s1.show()
lap.show()

s2.show()
