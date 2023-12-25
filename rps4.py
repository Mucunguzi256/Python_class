

import random
import sys
from enum import Enum

game_count = 0


def play_rsp():
    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerChoice = input(
        '\nEnter... \n1 for Rock,\n2 for Paper, or\n3 for Scissors:\n\n')
    if playerChoice not in ['1', '2', '3']:
        print('You must enter 1, 2, or 3.')
        return play_rsp()

    player = int(playerChoice)

    computerChoice = random.choice('123')
    computer = int(computerChoice)

    print('\nYou chose ' + str(RPS(player)).replace('RPS.', '') + '.')
    print('Python chose ' + str(RPS(computer)).replace('RPS.', '') + '.\n')

    def decide_winner(player, computer):
        if player == 1 and computer == 3:
            return '🎉 You Win!'
        elif player == 2 and computer == 1:
            return '🎉 You Win!'
        elif player == 3 and computer == 2:
            return '🎉 You Win!'
        elif player == computer:
            return '🙀 Tie Game!'
        else:
            return '🐍 Python Wins!'
    game_result = decide_winner(player, computer)
    print(game_result)

    global game_count
    game_count += 1
    print('\nGame Count: ' + str(game_count))

    print('\nPlay again?')
    while True:
        playagain = input(' \nY for yes or \nQ to quit \n\n')
        if playagain.lower() not in ['y', 'q']:
            continue
        else:
            break
    if playagain.lower() == 'y':
        return play_rsp
    else:
        print('\n🎉🎉🎉🥳')
        print('Thank you for playing!\n')
        sys.exit('Bye! 👋🏾')


play_rsp()

# break could have also worked!!


play_rsp()
