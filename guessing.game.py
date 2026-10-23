import random

def play_guessing_game():
    # 1. Generate a random secret number between 1 and 100
    secret_number = random.randint(1, 100)
    max_attempts = 7
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.\n")

    # 2. 'for' loop to limit the number of total attempts
    for attempt in range(1, max_attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{max_attempts} - Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer!")
            continue

        # 3. 'if-else' logic to check the user's guess
        if guess == secret_number:
            print(f"🎉 Congratulations! You guessed the correct number ({secret_number}) in {attempt} attempts!")
            break  # Exit the loop early since the player won
        elif guess < secret_number:
            print("Too low! Try a higher number.\n")
        else:
            print("Too high! Try a lower number.\n")
    else:
        # Executed only if the for loop finishes without reaching 'break'
        print(f"❌ Game Over! You've ran out of attempts. The secret number was {secret_number}.")

if __name__ == "__main__":
    play_guessing_game()