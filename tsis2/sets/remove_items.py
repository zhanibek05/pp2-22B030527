#Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

#if item does not exist remove will give error
#discard will NOT raise an error

thisset.discard("banana")

#pop - remove a random item
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset) 

#The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset) 

#del will delete the set completly
del thisset
print(thisset)#error
