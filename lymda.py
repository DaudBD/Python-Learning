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

num = [1,2,4,5]

x= list(map(lambda x : x*2 ,num))

print (x)

num = [1,2,4,5]

x= list(filter(lambda x : x*2 ,num))

print (x)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)

words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)