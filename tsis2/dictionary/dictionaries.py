#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
 
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

#print the "brand" value of the dict.
print(thisdict["brand"])

#Dictionaries cannot have two items with the same key:
#Duplicate values will overwrite existing values

#Using the dict() method to make a dictionary:
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)