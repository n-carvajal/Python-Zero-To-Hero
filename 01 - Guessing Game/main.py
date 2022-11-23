"""01 - Number Guessing Game"""

# Imports
from random import randint

# Game intro:
print("Welcome to GUESS THE NUMBER!")
print("The aim of the game is to guess the number I am thinking of in as few "
      "tries as possible.\n")
print("Would you like to play?")

# While loop for game starting:
start_prompts = 0
number = randint(1, 100)
guesses = []
attempts = 0
game_not_starting = True
while game_not_starting:
    start = input("Type 'Yes' or 'No': ")
    start_prompts += 1

    # if player types random word:
    if start.lower() != "yes" and start.lower() != "no":
        print("Sorry that input isn't valid.")
        print("Let's try again.")
        continue

    # else if player types no for first time:
    elif start.lower() == "no" and start_prompts == 1:
        print("Are you sure you don't want to play?")
        print("It's a lot fun...")
        continue

    # else if player types no more than once:
    elif start.lower() == "no":
        print("OK. Maybe some other time...")
        print("Bye.")
        break

    # else continue with game:
    else:
        game_not_starting = False
        print("Great!")
        print("Let's start...")
        print("I'm thinking of a number between 1 - 100: ")
        print(f"For testing the number is {number}")

# While loop for game play:
while True:
    guess = int(input("Guess the number: "))
    guesses.append(guess)
    attempts += 1

    # if guess falls out of bounds:
    if guess < 1 or guess > 100:
        print("That number is out of bounds.")
        print("Try again.")
        continue

    # if guess is repeated:
    if guesses.count(guess) > 1:
        print("You have already tried that number.")
        print("Try again.")
        continue

    # if guess is correct:
    if guess == number:
        print(f"Congratulations! You were right in {attempts} guesses.")
        print("You win.")
        break

        # if on first attempt:
    if attempts == 1:
        # Guess is within 10 of number:
        if abs(number - guess) <= 10:
            print("WARM! You are only 10 away from the right answer.")
            print("Try again.")
            continue
        # else guess more than 10 away:
        else:
            print("COLD! You are more than 10 away from the right answer.")
            print("Try again.")
            continue

    # if on subsequent attempts:
    if attempts > 1:
        # Guess is closer than previous:
        if abs(number - guesses[attempts - 1]) \
               < abs(number - guesses[attempts - 2]):
            print("WARMER! Your previous attempt is even closer than the "
                  "last.")
            print("Try again.")
            continue
        # else if on subsequent attempts guess is further away than previous:
        else:
            print("COLDER! Your previous attempt is further away than the "
                  "last.")
            print("Try again.")
            continue
