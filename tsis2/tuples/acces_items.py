#доступ к элементам

#print the second item in the tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#or
print(thistuple[-2])

#range of indexes
#Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#This example returns the items from the beginning to, but NOT included, "kiwi":
print(thistuple[:4])

#check if item exists
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in fruits tuple")


