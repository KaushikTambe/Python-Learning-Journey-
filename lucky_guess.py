# Number Guessing Game
# Learned: while loop, if/elif, user input, != condition
# Date: 09-06-2026

# Secret number set by the program
Secret_no = 10

# First guess before the loop starts
guess = int(input("Guess the number: "))

# Keep looping until user guesses correctly
while guess != Secret_no:
    if guess > Secret_no:
        print("Too high! Try lower.")
    elif guess < Secret_no:
        print("Too low! Try higher.")
    
    # Ask again after every wrong guess
    guess = int(input("Guess the number: "))

# Outside loop — runs only when guess is correct
print("Correct! Well done! 🎉")
