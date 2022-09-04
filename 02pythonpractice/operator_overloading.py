"""
Polymorphism:
Operator Overloading

# print(int.__add__(12,12))

"""


from operator import truediv


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + self.m2
        m2 = other.m1 + other.m2
        s3 = Student(m1, m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 = self.m2
        r2 = other.m1 = other.m2

        if r1 > r2:
            return True
        else:
            return False
        
    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)



s1 = Student(50, 12)
s2 = Student(5, 20)
s3 = s1 + s2

print(s1)


if s1 > s2:
    print ("Student 1 wins")
else:
    print("Student 2 wins")
