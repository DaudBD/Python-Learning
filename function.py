def function():
    print("This is My First Function")


function()

def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))

def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

def my_function(fname,lname):
    print(fname + " " + lname)

my_function("MD Adiyan", "Islam")

def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

def my_function(country = "Norway"):
  
  print("I am from", country)

my_function("Sweden")
my_function("india")
my_function("Bangladesh")

def my_function(animal, name):
  print("I have a", animal)

  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)


def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")