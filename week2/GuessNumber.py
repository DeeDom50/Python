from random import randint

print("devdom5222")

# Generate a random number between 1 and 9
num = randint(1, 9)
user_guess = 0
guess = 0

# Create a loop to check user guesses
while user_guess != num:
    # Get a guess from the user
    user_guess = int(input("Enter a guess from 1 to 9: "))
    guess += 1
     
    # Check if the guess is lower, higher, or correct
    if user_guess < num:
        print("Guess is low")
    elif user_guess > num:
        print("Guess is high")
    else:
        print(f"You guessed it! You won in {guess} guesses!")

# End of loop
print("Game Over")