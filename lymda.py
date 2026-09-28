# 
# lambda arguments : expression
x =lambda a: a + 10 + 16
print(x(5))

x =lambda a,b : a * b 

print (x(5,6))

x =lambda a,b : a - b 

print (x(5,6))


x =lambda a,b : a / b 

print (x(5,6))

x =lambda a,b : a % b 

print (x(5,6))

x = lambda a,b,c : a + b + c
print(x(6,6,7))


# Lambda Function
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def ab(n):
  return lambda c : c * n
mybd = ab(3)
print(mybd(33))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))