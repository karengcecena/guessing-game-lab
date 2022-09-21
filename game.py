"""A number-guessing game."""

import random
import sys

def greeting():
    """Greets player with their name
    
    Greets the player as well as asks for name as input, and reponds with their name
    """
    
    # greet player
    print("hello!")

    # get player name
    name = input("What's your name?: ")
    print(f"Hi {name}, nice to meet you!")

    # choose random number between 1 and 100

def guess_num():
    """Game where user guesses number from set range
    
    Allows user to set their own range, and guess up to 10 times. 
    """

    a = int(input("Set bottom range: "))
    b = int(input("Set upper range: "))

    number = random.randrange(a,b+1)
    guess_count = 1
    scores = []

    computer_play(a,b+1)

    while True:
        # Sets the amount of times a user can guess a number. 
        if guess_count < 11:
            guess = input(f"Choose a number between {a}-{b}:")
            
            # Makes sure that the user is inputting a number. 
            if guess.isdigit():
                guess = int(guess)

                # Makes sure that the guess is in the range of numbers set previously. 
                if guess in range(a,b+1): 

                    # Let's user know if guess is incorrect and adds to the guess count. 
                    if guess > number:
                        print("Too high!")
                        guess_count += 1

                    elif guess < number:
                        print("Too low!")
                        guess_count += 1

                    # Let's user know they guessed correctly. 
                    else:
                        print(f"Congrats! {guess} is the correct number. You had {guess_count} attempts.")
                        # Adds guess amount to scores to keep track of lowest score. 
                        scores.append(guess_count)
                        
                        play_again()

                        # Sorts all scores to select the lowest number as lowest score. 
                        final_score = sorted(scores)
                        print(f"Your best score was {final_score[0]}")
                        break
                        
                else:
                    print(f"{guess} is out of range, please choose a number between {a}-{b}.")

            else:
                print(f"{guess} is out of range, please choose a number between {a}-{b}.")

        else:
            answer = input(f"Too many tries... Want to play again? ")
            if answer == "Y" or answer == "y":
                guess_num()

def play_again():
    """"Asks user if they want to play again"""

    answer = input("Do you want to play again? (Y or N): ")
    if answer == "Y" or answer == "y":
        guess_num()  

def computer_play(a,b):
    """Asks if the user wants the computer to guess
    
    Allows the computer to guess if answer is yes
    """

    # Asks user if they want to play or have the computer play
    user_answer = input("Do you want the computer to guess? Y or N: ")

    # Assign numbers to computer has bounds
    low_number = a
    high_number = b

    while True:
        # When user wants to play against computer, input yes
        if user_answer == "y" or user_answer == "Y":

            # Computer can randomly guess a number
            computer_guess = random.randrange(low_number, high_number)
            message = input(f"Computer guess = {computer_guess}. Please answer, 'too high', 'too low', or 'you won': ")

            # Lets computer know it is too high and guesses again with number dictating upper range
            if message.startswith("too high"):
                high_number = computer_guess
                new_computer_guess = random.randrange(low_number, high_number)

            # Lets computer know it is too low and guesses again with number dictating lower range
            elif message.startswith("too low"):
                low_number = computer_guess
                new_computer_guess = random.randrange(low_number, high_number)
            
            # if computer wins, let it print they one and exit the game completely
            else:
                print("I won")
                sys.exit()
        else:
            # If they want to guess, then continue with guess_num 
            break

### Run Program:

greeting()
guess_num()