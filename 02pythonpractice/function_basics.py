
# Python Functions
# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.
# In Python a function is defined using the def keyword:



def sum_function(x,y):
  return x+y




print(sum_function(12,34))
print(sum_function(10,56))
print(sum_function(23,66))


# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

def func_one(*kids):
  print("The youngest child is " + kids[2])


func_one("Emil", "Tobias", "Linus")



# Keyword Arguments
# You can also send arguments with the key = value syntax.

def func_two(child3, child2, child1):
  print("The youngest child is " + child3)



func_two(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:


def func_3(**kid):
  print("His last name is " + kid["lname"])

func_3(fname = "Tobias", lname = "Refsnes")


def func_4(country = "Norway"):
  print("I am from " + country)


func_4("England")




# Passing a List as an Argument
def func_5(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

func_5(fruits)





# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.




def myfunction():
  pass




# Recursion
# Python also accepts function recursion, which means a defined function can call itself.


def func_recursion(k):
  if(k > 0):
    result = k + func_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result


print("\n\nRecursion Example Results")
func_recursion(6)



