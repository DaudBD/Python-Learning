# AirthMethic Operators 
print(10+10)
sum1 = 100+ 100

print(sum1)

x = 5
y = 3

print(x - y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)  # Expontation Square
print(x//y) # Floor Divison 

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

    num = 6

x = "WEEKEND!" if num > 5 else "Workday"

print(x)

num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)