# Number Guessing Game
# Created by Jakob

import random

def intro():
    print("Welcome to my Number Guessing Game!")
    print("Try to guess the number from 1 to 20.\n")

def player_guess():
    return int(input("Guess a number: "))

def compare(answer, guess):
    if guess < answer:
        print("Too low!\n")
        return False
    elif guess > answer:
        print("Too high!\n")
        return False
    else:
        print("You got it!")
        return True

intro()
 
answer = random.randint(1, 20)
tries = 0
win = False

while win == False:
    guess = player_guess()
    tries += 1
    win = compare(answer, guess)

print(f"It took you {tries} guesses.")