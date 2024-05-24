# function

x = "awesome"


def local_func():
  x = "fantastic"
  print("Python is " + x)

local_func()
print("Python is " + x)

def global_func():
  global x 
  x = "fantastic"
  print("Python is " + x)

global_func()
print("Python is " + x)

# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

def my_function(fname, lname):
  print(f"First name is {fname} and Last name is {lname}")

my_function("Yap", "Zhen Hao")
my_function("Kenyon","Yi")

# To let a function return a value, use the return statement:
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:

def my_function(**kid):
  print("His first name is " + kid["fname"])
  print("His last name is " + kid["lname"])

my_function(fname = "Yap", lname = "Zhen Hao")
my_function(fname = "Kenyon", lname = "Yi")