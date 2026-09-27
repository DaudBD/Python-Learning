def my_function(*args):

    print(args)

    print("Type:", type(args))

    print("First Argument:", args[0])
    print("2nd Argument:", args[1])
    print("3rd Argument:", args[2])


my_function("Emil", "Tobias", "Linus")

def my_function(**kids):

    print(kids)

    print("Type:", type(kids))

    print("First Argument:", kids["child1"])

    print("2nd Argument:", kids["child2"])

    print("3rd Argument:", kids["child3"])
my_function(child1="Emil", child2="Tobias", child3="Linus")


def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")


# Expample 

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))



def my_function(**kwargs):
    print(kwargs)

def my_function(**kid):
    print("His first name is " + kid["fname"])
    print("His last name is " + kid["lname"])

my_function(fname="Tobias", lname="Refsnes")


def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")


def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print("  ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")


def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")


def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers)
print(result)


def my(a,b,c):
   return a+b+c
numbers=[1,4,3]
result=my(*numbers)
print(result)


def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person)