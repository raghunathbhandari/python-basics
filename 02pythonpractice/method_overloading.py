"""

Polymorphism:
Method Overloading
Function Overloading

"""

class A:
    
    def show(self):
        print ("This is Class A")



class B(A):
    def show(self):
        print ("This is Class B")


a1= B()
a1.show()

