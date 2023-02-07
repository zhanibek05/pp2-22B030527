import random
name = input("Hello! What is your name?")
print(f"Well, {name}, I am thinking of a number between 1 and 20.")
number = random.randint(1, 20)
cnt = 0
while True:
    guess = int(input("Take a guess."))
    cnt += 1
    if(guess == number):
        print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
        break
    if(guess < number):
        print("Your guess is too low")
    else:
        print("Your guess is too high")


