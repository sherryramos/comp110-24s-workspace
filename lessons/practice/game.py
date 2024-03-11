""""Number guessing game."""
from random import randint

SECRET: int = randint(1,10)
# SECRET is outside the loop so it stays constant
correct: bool = False

while not correct: # correct == False
    guess: int = int(input("Guess a number: "))
    if guess == SECRET:
        print(f"You go it right! {guess} is the secret number!")
        correct = True
    elif guess < 1:
        print(f"Error! {guess} is too low!")
    elif guess > 10:
        print(f"Error! {guess} is too high!")
    else:
        print("Try again!")