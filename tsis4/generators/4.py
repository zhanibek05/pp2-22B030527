def squares(a, b):
    for i in range(a, b + 1):
        yield i*i


a = int(input("введите 'a' :"))
b = int(input("введите 'b' :"))

for x in squares(a, b):
    print(x)
