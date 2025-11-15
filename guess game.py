import random

def guessing_game():
    # Step 1: Generate a random secret number
    SECRET_NUMBER = random.randint(1, 20)
    MAX_TRIALS = 5
    attempts = 0

    print("--- Number Guessing Game ---")
    print("Guess the secret number (Hint: It's between 1 and 20)")
    print(f"You have {MAX_TRIALS} attempts. Good luck!")

    # Step 2: Game loop
    while attempts < MAX_TRIALS:
        try:
            guess = int(input(f"Enter Guess #{attempts + 1}: ")) #\n
        except ValueError:
            print("Invalid input! Please enter a whole number.")
            continue

        attempts += 1

        # Correct guess
        if guess == SECRET_NUMBER:
            print(f"\nYou're CORRECT! The number was {SECRET_NUMBER}.") #\n
            print(f"You guessed it in {attempts} attempt(s).")

            # Simple scoring system
            score = (MAX_TRIALS - attempts + 1) * 20
            print(f"Final Score: {score} points")
            return
        
        # Give hints
        if guess < SECRET_NUMBER:
            print("Nope! The number is HIGHER.")
        else:
            print("Nope! The number is LOWER.")

    # Out of attempts
    print("Game Over! You've used all attempts.")
    print(f"The number was {SECRET_NUMBER}. Better luck next time!")

guessing_game()