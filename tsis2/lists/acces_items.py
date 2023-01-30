thislist = ["apple", "banana", "cherry"]
print(thislist[1])# "banana"

print(thislist[1])# "cherry"

thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist2[2:5])#This will return the items from position 2 to 5.

#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included

print(thislist[:4])
#This will return the items from index 0 to index 4.

print(thislist[2:])
#This will return the items from index 2 to the end.

##checking is item exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

