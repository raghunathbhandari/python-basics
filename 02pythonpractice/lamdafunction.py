

# Python Lambda

# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.


var1 = lambda a : a + 10
var2 = lambda a, b : a * b



print(var1(5))
print(var2(5, 6))




# Why Use Lambda Functions?
# The power of lambda is better shown when you use them as an anonymous function inside another function.



def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(5)
print(mytripler(11))



# Multiple call from same lamda function

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))






