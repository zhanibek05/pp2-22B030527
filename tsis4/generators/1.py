def my_generator(n):
    i = 1
    while i <= n:
        yield i*i #key word
        i += 1
         
N = int(input())

squares_1 = my_generator(N)

for x in squares_1:
    print(x)

# or

print("another expression")

squares_2 = (i*i for i in range(N + 1))
 
for x in squares_2:
    print(x)