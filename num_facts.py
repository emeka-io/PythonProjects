print('WELCOME TO THE NUMBER FACTS PROGRAM.')

while True:    
    num = int(input('Enter a whole number: '))

    if num % 2 == 0:
        print(f'{num} is even.')

    if num % 2 == 1:
        print(f'{num} is odd.')

    if num > 0:
        print(f'{num} is positive.')

    if num < 0:
        print(f'{num} is negative.')

    if num == 0:
        print('The number is zero.')

    print(f'The square of {num} is {num * num}')

    try_again = input('Do you want to try again? (yes/no): ').lower()

    if try_again == 'no':
        print('Goodbye!')
        break  
    elif try_again != 'yes':
        print("Invalid input. Exiting program.")
        break
