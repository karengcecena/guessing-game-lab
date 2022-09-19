"""A number-guessing game."""

import random

# greet player
print("hello!")

# get player name
name = input("What's your name?: ")
print(f"Hi {name}, nice to meet you!")

# choose random number between 1 and 100
number = random.randrange(1,101)

# repeat forever:
while True:
    guess = int(input("Choose a number between 1-100:"))
    


#### still needs to scold them if they do not put in an integer
    if guess.isint():
        guess = int(guess)
        guess_count = 0
    #     if guess is incorrect:
        if guess > number:
            print("Too high!")
            guess_count += 1
        elif guess < number:
            print("Too low!")
            guess_count += 1
        else:
            print(f"Congrats! {guess} is the correct number")
            
    else:
        print("Sorry, I don't play with people who don't follow rules.")