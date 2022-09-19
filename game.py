"""A number-guessing game."""

import random

def greeting():
    # greet player
    print("hello!")

    # get player name
    name = input("What's your name?: ")
    print(f"Hi {name}, nice to meet you!")

    # choose random number between 1 and 100

def guess_num():
    number = random.randrange(1,101)
    guess_count = 0
    # repeat forever:
    while True:
        guess = input("Choose a number between 1-100:")
        
        if guess.isdigit():
            guess = int(guess)

            if guess in range(1,101): 
        #     if guess is incorrect:
                if guess > number:
                    print("Too high!")
                    guess_count += 1
                elif guess < number:
                    print("Too low!")
                    guess_count += 1
                else:
                    print(f"Congrats! {guess} is the correct number. You had {guess_count} attempts.")
            else:
                print(f"{guess} is out of range, please choose a number between 1-100.")

        else:
            print(f"{guess} is out of range, please choose a number between 1-100.")

def play_again()
    answer = input("Do you want to play again? (Y or N): ")
    if answer == "Y":
        guess_num()
    else:
        print("ok bye")

### Run Program:

greeting()
guess_num()
play_again()