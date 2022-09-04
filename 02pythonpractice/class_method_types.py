"""
Instance Methods
Class Methods
Static Methods

"""

class Student:

    school = "Imp London"

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3 )/3

    @classmethod
    def getSchool(cls):
        return cls.school

    @staticmethod
    def getInfo():
        print ("This is Class Object .. in abc module")



s1 = Student(23,21,40)
s2 = Student(22,45,67)

s1.m1 = 900
s2.m2 = 90000

print(s1.avg())
print(s2.avg())

print(s1.getSchool())
print(s2.getSchool())
print(Student.getSchool())

Student.getInfo()

