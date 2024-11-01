import random

def guessing_game():
    """A number guessing game where the player has 5 attempts to guess a random number between 1 and 100."""
    lives = 5
    target_number = random.randint(1, 100)

    while lives > 0:
        try:
            guess = int(input("Guess a number between 1-100: "))
            print(f"You entered: {guess}")
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue  # Skip to the next iteration if input is invalid

        if guess < target_number:
            print("Too low")
        elif guess > target_number:
            print("Too high")
        else:
            print(f"Correct - Game Over - Number is: {target_number}")
            break  # Exit the loop if the guess is correct

        lives -= 1
        print(f"Lives remaining: {lives}")

    if lives == 0:
        print(f"You Lose - Game Over - Number was: {target_number}")

# Run the game
guessing_game()
