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
    a = int(input("Set bottom range: "))
    b = int(input("Set upper range: "))

    number = random.randrange(a,b+1)
    guess_count = 1
    scores = []

    while True:
        if guess_count < 4:
            guess = input(f"Choose a number between {a}-{b}:")
            
            if guess.isdigit():
                guess = int(guess)

                if guess in range(a,b+1): 
            #     if guess is incorrect:
                    if guess > number:
                        print("Too high!")
                        guess_count += 1
                    elif guess < number:
                        print("Too low!")
                        guess_count += 1
                    else:
                        print(f"Congrats! {guess} is the correct number. You had {guess_count} attempts.")
                        scores.append(guess_count)
                        
                        play_again()
                        final_score = sorted(scores)
                        print(f"Your best score was {final_score[0]}")
                        
                else:
                    print(f"{guess} is out of range, please choose a number between {a}-{b}.")

            else:
                print(f"{guess} is out of range, please choose a number between {a}-{b}.")

        else:
            answer = input(f"Too many tries... Want to play again? ")
            if answer == "Y" or answer == "y":
                guess_num()

def play_again():
    answer = input("Do you want to play again? (Y or N): ")
    if answer == "Y" or answer == "y":
        guess_num()   

### Run Program:

greeting()
guess_num()