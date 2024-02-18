#Creating Variables
x = 5
y = "John"
print(x)
print(y)

#2
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

#Casting  INT-->FLOAT-->COMPLEX
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Get the type
x = 5
y = "John"
print(type(x))
print(type(y))

#Single or double quotes?
x = "John"
# is the same as
x = 'John'

#Case Sensitive
a = 4
A = "Sally"
#A will not overwrite a

#VARIABLE NAMES
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

#Camel Case
myVariableName = "John"

#Pascal Case
MyVariableName = "John"

#Snake Case
my_variable_name = "John"

#MultiValues
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#Assign same datatype
x = y = z = "Orange"
print(x)
print(y)
print(z)

#Unpake a collection(tuples, list etc)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Output Variables
x = "Python is awesome"
print(x)

#Separated by comma
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

#Separated by +, without space
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

#For numbers +, will be as math.operator
x = 5
y = 10
print(x + y)

#Error
x = 5
y = "John"
print(x + y)

#For different datatypes use ,
x = 5
y = "John"
print(x, y)

#Create a variable outside of a function, and use it inside the function
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#The global variable with the same name will remain as it was, global and with the original value.
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#global Keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#To change the value of a global variable inside a function, refer to the variable by using the global keyword
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#