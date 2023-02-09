def is_it_prime(x):
    for i in range(2, x - 1):
        if x%i == 0:
            return False
    return True

def filter_prime(numbers):
    primes = []
    for x in numbers:
        if is_it_prime(int(x)):
            primes.append(x)
    return primes
        


numbers = input().split()
print(filter_prime(numbers))