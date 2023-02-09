#Get the value of the "model" key:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

#get() method
x = thisdict.get("model")

## get keys
#The keys() method will return a list of all the keys in the dictionary.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)

#Add a new item to the original dictionary, and see that the keys list gets updated as well
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()
print(x) #before the change
car["color"] = "white"
print(x) #after the change 

## get values
x = thisdict.values()

car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.values()
print(x) #before the change
car["year"] = 2020
print(x) #after the change 

# get items
x = thisdict.items()
print(x)

# check if key exists
if "model" in thisdict:
    print("yes, 'model' is one of the keys")

