# A scores prediction program 
print('Welcome to the prediction game.')
name = input('Enter your name: ')
print(f"Hello {name}, let's get started. Pick a game number from the list below....")

# the set of available games shown to the user
print("""
Here are the available games:
1. Chelsea VS Man U
2. Atalanta VS Napoli
3. Bayern VS Frankfurt
4. Barcelona VS Elche
      """)

# a dictionary containing the available games 
games: dict = {
    1 : 'Chelsea VS Man U',
    2 : "Atalanta VS Napoli",
    3 : 'Bayern VS Frankfurt',
    4 : 'Barcelona VS Elche'
}


choice = int(input('Enter the number of your preferred game: '))
print(f"You've picked '{games.get(choice)}'")

h_score = int(input('Enter your goals prediction for the home team: '))
a_score = int(input('Enter your goals prediction for the away team: '))
print(f"You've predicted ({h_score}, {a_score})")
pred = (h_score, a_score)

import random

class Score:
    def ft(self):
        home = random.randint(1,7)
        away = random.randint(1,7)
        return (home, away) # the least a team can score is 1, and the highest is 7 (to keep it realistic)


print('Here is the final score')
result = Score()
a = print(result.ft())

if a == pred:
    print("You're awesome, you've won $5000.00")
else:
    print("Sorry, you're wrong try again later")
