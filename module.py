
# Module
person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

import module

a = module.person1["age"]
print(a)

import module as mx

a = mx.person1["age"]
print(a)

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)