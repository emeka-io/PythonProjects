import random
print("Welcome to the password guessing game!")
# Generate a random password
def generate_password(length=8):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
password = generate_password()
max_attempts = 5
attempts = 0
print("A random password has been generated. Try to guess it!")
while attempts < max_attempts:
    guess = input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: ")
    attempts += 1
    if guess == password:
        print(f"Congratulations! You've guessed the password '{password}' correctly in {attempts} attempts.")
        break
    else:
        print("Incorrect guess. Try again.")
else:
    print(f"Sorry, you've used all your attempts. The correct password was '{password}'.")

    