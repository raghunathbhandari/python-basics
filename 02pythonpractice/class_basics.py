
class Person:
    def __init__(self):
        self.name = "Raghu"
        self.age = 30
        self.hdd = "1TB"


    def update(self):
        self.age = 30

    def compare (self,other):
        if self.age == other.age:
            return True
        else:
            return False


# Create or Construct Methods
p1 = Person()
p2 = Person()

# Modify Value
p1.name = "Shaivi"
p1.age = 30

# Print Value
print(p1.name, p1.age, p2.hdd)
print(p2.name, p2.age, p2.hdd)


if p1.compare(p2):
    print ("Both are same age")
else:
    print("Both are not same")


