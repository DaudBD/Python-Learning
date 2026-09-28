fruits = ["apple", "banana", "cherry"]

my_iterator = iter(fruits)

print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)


  class MyNumbers:
   def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))