#The pop() method removes the item with the specified key name:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict) 

#The popitem() method removes the last inserted item
thisdict.popitem()

#The del keyword removes the item with the specified key name:
del thisdict["model"]

