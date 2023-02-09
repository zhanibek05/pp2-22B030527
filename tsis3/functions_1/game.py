import random
def main():
    
    name = input("\nHello! What is your name?\n")
    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    number = random.randint(1, 20)
    cnt = 0
    while True:
        guess = int(input("Take a guess.\n"))
        cnt += 1
        if(guess == number):
            print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
            break
        if(guess < number):
            print("\nYour guess is too low")
        else:
            print("\nYour guess is too high")


