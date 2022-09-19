"""A number-guessing game."""

# greet player
print("hello!")

# get player name
name = input("What's your name?: ")
print(f"Hi {name}, nice to meet you!")

# choose random number between 1 and 100
number = 30

# repeat forever:
while True:
    guess = int(input("Choose a number between 1-100:"))
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