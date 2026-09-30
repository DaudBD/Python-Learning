class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

# Accese Propertise
class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age 
  def get_into(self):
     self.age = 27
     self.name = "Arif"
     return (f"{self.name} is {self.age} Years Old")
p1 =Person("Rahim",31)  

print(p1.get_into())



class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()