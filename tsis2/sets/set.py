#A set is a collection which is unordered, unchangeable*, and unindexed.
#Set items are unchangeable, but you can remove items and add new items.

thisset = {"apple", "banana", "cherry"}
print(thisset)
#Sets are unordered, so you cannot be sure in which order the items will appear.

#Duplicate values will be ignored
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False} 

set1 = {"abc", 34, True, 40, "male"} 

#type of set is "<class 'set'>"

#the set() constr.
thisset = set(("apple", "banana", "cherry"))