print (10>5)
print (10 ==5)
print (10<5)
a =10 
b =5 

a = 15
b = 5

if a > b:
    print("a is larger")
elif a < b:
    print("b is smaller")
else:
    print("a and b are equal")

print(bool("hello"))   
print (bool(15))

x = 15 
y = "hello"

print(bool(x))
print (bool(y))

print(bool(""))
print (bool(0))

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

def myFunction() :
      return True

print(myFunction())

def myFunction() :
  return False # Dcelar True Or False 

if myFunction():
  print("YES!")
else:
  print("NO!")

  x = 200
print(isinstance(x, int))
