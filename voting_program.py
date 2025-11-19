# VOTING PROGRAM WITH PYTHON
first_name = input('Enter your name: ')
while True:
    try:
        age = int(input('Enter your age: '))
        break
    except ValueError:
        print('Enter a whole number.')
    continue


def voting_system():
    candidates = {
        1: "PDP - 'Amos Jacobs'",
        2: "APC - 'Ola David'",
        3: "SDP - 'Daniel Benson'",
        4: "NRDP - 'Marvin Kilolo'",
        5: "ZTW - 'Divine Ikubor'"
    }

    print('Here are the available candiates to be voted for in this election.')
    print("""
    1: "PDP - 'Amos Pikins',
    2: "APC - 'Ola David',
    3: "SDP - 'Daniel Benson',
    4: "NRDP - 'Marvin Ukanigbe',
    5: "ZTW - 'Divine Ikubor'
    """)

    vote = int(input('Enter the ID/No. of your preferred candidate: '))
    print(f"Are you sure you want to vote for {candidates.get(vote)}")
    ans = input('Yes/No:').lower()
    if ans == 'yes':
        print(f'You have successfully voted for {candidates.get(vote)}. The election results would be released in 14 days time. ')
    else:
        print("Your vote has been cancelled.")



if age > 18:
    print(f"Hello {first_name}, welcome to the Voter's registration site.")
    voting_system()
else:
    print(f"Sorry {first_name}, you're too young to vote.")

