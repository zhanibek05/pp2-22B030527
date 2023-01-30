#Print all key names in the dictionary, one by one
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)

#print values
for x in thisdict:
    print(thisdict[x])

#or

for x in thisdict.values():
    print(x)

#Loop through both keys and values, by using the items() method
for x in thisdict.keys():
    print(x)

#Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
    print(x, y) 