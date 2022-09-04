"""
Namespace: Namespace is an area where you create and store object/variable
- Class namespace
- Object/Instance namespace

Static variable
Class Variable : Class level scope (enginetype)
Instance Variable: Method level scope (mil, compname)

"""

class Car:
    enginetype = "Auto"

    def __init__(self):
        self.mil = 10
        self.compname = "BMW"


c1 = Car()
c2 = Car()

c1.mil = 8
Car.enginetype = "EV"
c1.enginetype = "Manual"

print(c1.compname, c1.mil, c1.enginetype)
print(c2.compname, c2.mil, c2.enginetype)

