def has_33(numbers):
    for i in range(0, len(numbers) - 1):
        if(numbers[i] == '3' and numbers[i + 1] == '3'):
            return True
    return False

numbers = input().split()
print(has_33(numbers))