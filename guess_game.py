import random
def guessing_game():
    # generate a random secret number
    secret_number = random.randint(1,20)
    max_trials = 5
    attempts = 0

    print('NUMBER GUESSING GAME')
    print("Guess the secret number. (Hint: It's between 1 and 20)")
    print(f'You have {max_trials} attempts, Good luck.')

    # game loop
    while attempts < max_trials:
        try:
            guess = int(input(f'Enter Guess #{attempts + 1}: '))
        except ValueError:
            print('Invalid Input! Please enter a whole number.')
            continue

        attempts += 1

        # if user is correct
        if guess == secret_number:
            print(f"\nYou're CORRECT! The number was {secret_number}.")
            print(f'You guessed it in {attempts} attempt(s).')


            # scoring system
            score = (max_trials - attempts + 1) * 20
            print(f'Final score: {score} points.')
            return
        
        #hints
        if guess < secret_number:
            print("Nope, The number is HIGHER")
        else:
            print('Nope, The number is LOWER')

    # out of attempts
    print("Game Over! You've used up all attempts")
    print(f"The number was {secret_number}. Better luck next time.")

guessing_game()