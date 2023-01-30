#loop through the list

#print all items in the list, one by one
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#Print all items by referring to their index number
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#using whilel loop
i = 0
while i < len(thislist):
    print(thislist[i])
    i += 1

#short hand for loop that will print all items in a list
[print(x) for x in thislist]