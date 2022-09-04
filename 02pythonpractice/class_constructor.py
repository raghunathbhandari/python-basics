"""
Constructor in Inheritance
Method Resulotion Order : it will go left to right

"""

class A:

    def __init__(self):
        print("This is A Constructor")

    def featur1(self):
        print("This is Feature A-1 ")

    def featur2(self):
        print("This is Feature A-2 ")

class B:

    def __init__(self):
        print("This is B Constructor")

    def featur1(self):
        print("This is Feature B-1 ")
        
    def featur3(self):
        print("This is Feature B-3 ")

    def featur4(self):
        print("This is Feature B-4 ")

class C(A,B):
    def __init__(self):
        print("This is C Constructor")
        super().__init__()
        

    def featur5(self):
        print("This is Feature B-5 ")

    def featur6(self):
        print("This is Feature B-6 ")


ob = C()
ob.featur1() # While doing inheritance I have used(A,B) so it will access left class feature1 first which is A class

