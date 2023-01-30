#standard method sort() - sort the list alphanumerically

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist2 = [100, 50, 65, 82, 23]
thislist2.sort()
print(thislist2)#sort in increasing  order

#sort descending 
thislist.sort(reverse = True)
print(thislist)
thislist2.sort(reverse = True)
print(thislist2)

#custom sort
def myfunc(n):
    return abs(n - 50)

thislist2.sort(key = myfunc)
print(thislist2)


#in defoult func. sort() capital letters being sorted before lower case letters
thislist3 = ["banana", "Orange", "Kiwi", "cherry"]
thislist3.sort()
print(thislist3)#unexpected result

#solution:
thislist3.sort(key = str.lower)
print(thislist3)

#revers order
thislist.reverse()
print(thislist)
