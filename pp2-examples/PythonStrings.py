print("Hello")
print('Hello')

#Assign String to a variable
a = "Hello"
print(a)

#Multiline strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings as arrays
a = "Hello, World!"
print(a[1]) #e

#Looping through string
for x in "banana":
  print(x)
  
#String Length
a = "Hello, World!"
print(len(a))

#Check String
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
  
#Check if NOT
txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
  
#SLICING
b = "Hello, World!"
print(b[2:5]) #llo

#Slice from Start
b = "Hello, World!"
print(b[:5])

#Slice to End
b = "Hello, World!"
print(b[2:])

#Negative Indexing
b = "Hello, World!"
print(b[-5:-2]) #orl

#Upper Case
a = "Hello, World!"
print(a.upper())

#Lower case
a = "Hello, World!"
print(a.lower())

#remove Whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

#Replace
a = "Hello, World!"
print(a.replace("H", "J"))

#Split String
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

#Merging Variables
a = "Hello"
b = "World"
c = a + b
print(c) #HelloWorld

a = "Hello"
b = "World"
c = a + " " + b
print(c) #Hello World

#ERROR
age = 36
txt = "My name is John, I am " + age
print(txt)

#CORRECT
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#ordering
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

#ERROR
#txt = "We are the so-called "Vikings" from the north."
#CORRECT
txt = "We are the so-called \"Vikings\" from the north."





