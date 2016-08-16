import random

number = random.randint(0, 10)
guess = int(input("A number between 0 and 10, inclusive, has been selected. Guess the number.\n"))

while guess != number:
    if guess > number:
        print("Your guess is too high.\n")
    else:
        print("Your guess is too low.\n")
    guess = int(input("Guess again.\n"))

print("You guessed correctly.\n")
