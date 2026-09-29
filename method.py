class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Arif", 31)

print(p.name)
print(p.age)

class Person:
  pass

p1 = Person()
p1.name = "Tobias"
p1.age = 25

print(p1.name)
print(p1.age)


# Defualt Self Parameter 

class Person:
  def __init__(self, name, age=18):
    self.name = name
    self.age = age

p1 = Person("Emil")
p2 = Person("Tobias", 25)

print(p1.name, p1.age)
print(p2.name, p2.age)

# Multple Parameter 
class Person:
  def __init__(self, name, age, city, country):
    self.name = name
    self.age = age
    self.city = city
    self.country = country

p1 = Person("Linus", 30, "Oslo", "Norway")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)



# Multiple Parameters
class Person:                              # ← CLASS
    def __init__(self, name, age, city, country):  # ← METHOD
        self.name = name                   # name → PARAMETER
        self.age = age                     # age → PARAMETER
        self.city = city                   # city → PARAMETER
        self.country = country             # country → PARAMETER

p1 = Person("Linus", 30, "Oslo", "Norway") # ← OBJECT
#             ↑       ↑    ↑       ↑
#           ARGUMENTS (actual values)

print(p1.name)                             # ← ATTRIBUTE
print(p1.age)                              # ← ATTRIBUTE
print(p1.city)                             # ← ATTRIBUTE
print(p1.country)                          # ← ATTRIBUTE


# Self parameter 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def greet(self):
    print("Hello, my name is " + self.name)

p1 = Person("Emil", 25)
p1.greet()


class Person:
  def __init__(self, name):
    self.name = name

  def printname(self):
    print(self.name)

p1 = Person("Tobias")
p2 = Person("Linus")

p1.printname()
p2.printname()