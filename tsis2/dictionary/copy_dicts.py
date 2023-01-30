#copy() method
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#make a copy with the 'dict()' funct.
mydict = dict(thisdict)
print(mydict)