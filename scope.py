# Inside Function 
def myfunc():
  x = 300
  print(x)

myfunc()
# Inner Function The local variable can be accessed from a function within the function:

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

#  GLobal Scope : A variable created outside of a function is global and can be used by anyone:

x = 30

def myfunc():
  print(x)

myfunc()

print(x)

#  Naming Variable :The function will print the local x, and then the code will print the global x:
x = 15

def myfunc():
  x = 20
  print(x)

myfunc()

print(x)


# Global Keyword :If you use the global keyword, the variable belongs to the global scope:
# x = 15

def myfunc():
    global x
    x = 20

myfunc()

print(x)

# NonLocal Keyword FUnction :If you use the nonlocal keyword, the variable will belong to the outer function:

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

# LEGB Rule :Understanding the LEGB rule:
x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print("Inner:", x)

    inner()
    print("Outer:", x)

outer()
print("Global:", x)


# Python Scope — Short Summary

# Scope = কোন জায়গা থেকে variable ব্যবহার করা যাবে।

# Local → function-এর ভিতরের variable
# Enclosing → nested function-এর বাইরের function-এর variable
# Global → পুরো program-এ ব্যবহারযোগ্য variable
# Built-in → Python-এর built-in names যেমন print(), len()

