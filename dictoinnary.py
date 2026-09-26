

person = {
    "name": "Ariful",
    "age": 25,
    "city": "Dhaka"
}
print(person)
print(person["name"])

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 2020,
    "color": ["red", "blue", "yellow"]
}

print(thisdict)
print(len(thisdict))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
# x = thisdict["model"]
x = thisdict.get("model")

x = thisdict.keys("model")

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

  thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")