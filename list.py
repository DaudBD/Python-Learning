list = ["apple","Banna","chery","apple","Banna","chery"]
print(list)
print(len(list))
print(type(list))
print (list[3])
print (list[-4])
print (list[2:5])
print (list[:5])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


my = ["apple", "banana", "cherry"]
my[1] = "blackcurrant"

my.append("Lemon")
print(my)
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)