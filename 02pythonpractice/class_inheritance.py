"""
Python - Class Inheritance

> Single Level Inheritance
> Multiple Inheritance
> Multi level Inheriance

"""


class A:
    
    def feature1(self):
        print ("This is Feature 1")

    def feature2(self):
        print ("This is Feature 2")


class B:

    def feature3(self):
        print ("This is Feature 3")

    def feature4(self):
        print ("This is Feature 4")

# Multiple Class Inritance
class C(A, B):
    
    def feature5(self):
        print ("This is Feature 5")

    def feature6(self):
        print ("This is Feature 6")

# Multi Level Class Inritance
class D(C):
    
    def feature7(self):
        print ("This is Feature 6")

    def feature8(self):
        print ("This is Feature 7")

# Single Level Class Inritance
class E(A):
    
    def feature9(self):
        print ("This is Feature 6")



a1 = A()
b1 = B()
c1 = C()
d1 = D()
e1 = E()

# a1.feature1()
# b1.feature3()
# c1.feature1()


d1.feature1()
d1.feature3()
d1.feature5()

