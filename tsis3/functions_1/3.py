def solve(numheads, numlegs):
    rabbits = int(numlegs/2 - numheads)
    chickens = int(numheads - rabbits)
    print("Number of rabbits:", rabbits)
    print("Number of chickens:", chickens)
    

heads = int(input("number of heads: "))
legs = int(input("number of legs: "))

solve(heads, legs)
