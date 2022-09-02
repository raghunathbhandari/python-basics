##Python Variables Example -1 
# Python has no command for declaring a variable.A variable is created the moment you first assign a value to it.
## 



a=5 
b="Raghu"

# print(a)
# print(b)
# print(b[1])
# print(b[1:2])
# print(b[-1])


##Python Variables Example -2  Variable type can even change type after they have been set.
x = 5       
x = "Raghu"


## It supports Camel Case, Pascal Case, Snake Case
firstVar=99
SecondVar="test"
third_var =20.22



# List:
# Lists are used to store multiple items in a single variable.

first_list = ["apple", "banana", "orange"]
second_list = [2,3,4,5,8,9,7,6,3,8]

first_list[1]="apple"
first_list.append("mango")


# first_list.remove("banana")
first_list.pop(1)
first_list.insert(1,"watermelon")
first_list.sort()
second_list.sort(reverse = True)
mylist = first_list.copy()


# print(first_list[0])
# print(first_list)
# print(second_list)
# print(type(first_list))



# Join list
th_list = first_list + second_list
print(th_list)


# For Loop
for x in first_list:
  print(x)



# While Loop
i = 0
while i < len(first_list):
  print(first_list[i])
  i = i + 1





# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType
#



x = 5   # int
y = 28  # float
z = 1j    # complex


# print(type(x))
# print(type(y))
# print(type(z))



# Tuple
# Tuples are used to store multiple items in a single variable.


var_tup = ("apple", "banana", "cherry")
print(var_tup)



# Dictionary:
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.




# Set
# Sets are used to store multiple items in a single variable.


var1_set = {"apple", "banana", "cherry"}
var3_set = {1, 5, 7, 9, 3}
var4_set = {True, False, False}
var5_set = {"abc", 34, True, 40, "male"}

var1_set.add("orange")
var1_set.update(var5_set)
var1_set.remove("banana")
var1_set.discard("banana")
var1_set.clear()
del var3_set

set3 = var1_set.union(var5_set)


for x in var5_set:
  print(x)



print (type(var5_set))
print (set3)




# Dictionary
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

var_dis1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}


var_dis2 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

var_dis1["color"] = "red"
var_dis1.update({"year": 2020})
var_dis1.pop("model")
var_dis1.popitem()
del var_dis2["electric"]
var_dis1.clear()
mydict = var_dis2.copy()



varDictFamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}




print(varDictFamily)





# Python Conditions and If .. Eleif statements
# Python supports the usual logical conditions from mathematics:

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")



# Python Array?
# An array is a special variable, which can hold more than one value at a time.

var_array1 = ["Ford", "Volvo", "BMW"]
var_array1.pop(1)
var_array1.remove("Volvo")


print(var_array1)













