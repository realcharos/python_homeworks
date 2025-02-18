import random

number = random.randint(1, 100)
attempts = 10

for _ in range(attempts):
    guess = int(input("Guess the number: "))
    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print("You guessed it!")
        break
else:
    print("You lost.")
