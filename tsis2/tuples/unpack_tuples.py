#packing a tuple
fruits = ("apple", "banana", "cherry")

#unpucking a tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)# apple
print(yellow)# banana
print(red)# cherry

#Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

