N = int(input())

even_generator = (i for i in range(N+1) if i%2 == 0)

print(",".join(str(x) for x in even_generator))