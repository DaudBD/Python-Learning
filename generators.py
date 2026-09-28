#  Genrators
def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)


def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)



def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

# Range Function
x = range(3, 10)

#display x:
print(x)

#convert to list to display the content of x:
print(list(x))

x = range(3, 10, 2)

#display x:
print(x)

#convert to list to display the content of x:
print(list(x))