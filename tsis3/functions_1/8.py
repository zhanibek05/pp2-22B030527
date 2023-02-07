def spy_game(numbers):
    for i in range(len(numbers)):
        if(numbers[i] == 7 and numbers[i - 1] == 0 and numbers[i - 2] == 0):
            return True
    return False

print(spy_game([0, 12, 7, 0, 0, 7]))