#remove
thislist = ['apple', 'banana', 'cherry']
thislist.remove('banana')
print(thislist)

#pop
thislist.pop()#removed the last item
thislist.pop(1)#removed item with index 1(second item)

#del
thislist = ["apple", "banana", "cherry"]
del thislist[0]#remove the first item
del thislist#delete the list completely


#clear
#The clear() method empties the list.
#The list still remains, but it has no content.

thislist.clear()
print(thislist)# []

