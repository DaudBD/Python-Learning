

x = "Hello6 World!"

print(len(x))

mytuple = ("apple", "banana", "cherry")

print(len(mytuple))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))

# Polymorphism 

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def movie(self):
        print("Drive")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def movie(self):
        print("Sail")    

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def movie(self):
        print("Fly")  
car1 = Car("Ford", "Mustang")
boat1 = Boat("Yamaha", "242X")
plane1 = Plane("Boeing", "747")

for vehicle in (car1, boat1, plane1):
    vehicle.movie()
    


    # Create the Cat class
class Cat:
  def sound(self):
    print("Meow")

class Fox :
      def sound(self):
       print("Wa-pa-pa-pa-pa-pow!")
# Create the Fox class
c1 =Cat()
f1 = Fox()

# Create objects and loop
for x in [c1, f1]:
      x.sound()

class Person:
    def __init__(self):
        self.__age = 25

    def get_age(self):
        return self.__age


p1 = Person()

print(p1.get_age())