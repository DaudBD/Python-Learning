fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "b" in x]

print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]

print(newlist)

fruits.sort()
print(fruits)
thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.reverse()

print(thislist) 

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
# Join List 
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Create a list
colors = ["red", "green", "blue"]

# Print the first item
print(colors[0])

# Change the second item to "yellow"
colors[1] = "yellow"

# Add "purple" to the end
colors.append("purple")

# Remove "red"
colors.remove("red")

# Print the list
print(colors)