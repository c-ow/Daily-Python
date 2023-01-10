import random

print('Welcome to Rock, Paper, Scissors. ')
rps = ['Rock', 'Paper', 'Scissors']
games_played = 0
player_wins = 0
computer_wins = 0

def compare(choice1, choice2):
    if choice1 == 'rock' and choice2 == 'scissors' or choice1 == 'scissors' and choice2 == 'paper' or choice1 == 'paper' and choice2 == 'rock':
        return 'Win'
    elif choice1 == choice2:
        return 'Tie'
    else:
        return 'Lose'

playing = True
while playing:
    player_choice = input('Choose Rock, Paper, or Scissors.\n')
    computer_choice = random.choice(rps)
    if player_choice.lower() == 'rock' or player_choice.lower() == 'paper' or player_choice.lower() == 'scissors':
        result = compare(player_choice.lower(), computer_choice.lower())
        print('You chose %s, your opponent chose %s. ' %(player_choice, computer_choice))
        games_played += 1
        if result == 'Win':
            player_wins += 1
            print('You won the round!')
        elif result == 'Lose':
            computer_wins += 1
            print('You lost the round!')
        elif result == 'Tie':
            print('You tied!')
        while True:
            play_again = input('Play again? ')
            if play_again.lower() == 'yes':
                break
            elif play_again.lower() == 'no':
                print('You played %s game(s) and won %s of them' %(games_played, player_wins))
                playing = False
                break
            else: 
                print('Could not read input.')
    else:
        print('Could not read input.')