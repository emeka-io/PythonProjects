import random
import string

def generate_password(length=12):
    # Characters to choose from
    letters = string.ascii_letters      # a-z + A-Z
    digits = string.digits              # 0-9
    symbols = string.punctuation        # ! @ # $ % & *

    # Combine all characters
    all_chars = letters + digits + symbols

    # Ensure at least one of each (optional but good practice)
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols),
    ]

    # Fill the remaining characters randomly
    for _ in range(length - 3):
        password.append(random.choice(all_chars))

    # Shuffle so the password isn’t predictable
    random.shuffle(password)

    return "".join(password)

def main():
    print("=== Random Password Generator ===")
    length = int(input("Enter password length: "))
    result = generate_password(length)
    print(f"\nYour generated password is:\n{result}")

if __name__ == "__main__":
    main()
