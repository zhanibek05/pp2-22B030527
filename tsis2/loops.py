#while
i = 0
while i < 5:
    print(i)
    i += 1

#break
i = 0
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1
    

#continue
i = 0
while i < 5:
    if i == 3:
        continue # continue to next iteration
    print(i)
    i +=1

#else
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#exercise
i = 1
while i < 6:
    print(i)
    i += 1


## For loop
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)#

#Loop through the letters in the word "banana"
for x in "banana":
    print(x)

#break
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break

#the range funcion
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
    print(x)#print numbers from 0 to 6(exclus.)
#range second parameter
for x in range(2, 6):
    print(x)# from 2 to 6(ex)

#range third parameter
for x in range(1,100,2):
    print(x)#1, 3, 5, 7, ...

#else in for loop will be executed when the loop is finished
for i in range(6):
    print(i)
else:
    print("Finally finshed")

#else will not be executed if the loop is stopped by a "break"

#nested loops
adjectives = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adjectives:
    for y in fruits:
        print(x, y)

#pass statement
for x in [1, 2, 3]:
    pass #if you do not know what write, just put pass
    

