def number_generator(n):
    for i in range(n + 1):
        if(i%12 == 0):
            yield i
            
N = int(input())

for x in number_generator(N):
    print(x)

