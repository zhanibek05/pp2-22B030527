def filter_prime(numbers):
    for x in numbers:
        y = int(x)
        for i in range(2,y):
            if y%i == 0:
                numbers.remove(x)
                break
    return numbers


numbers = input().split()
print(filter_prime(numbers))