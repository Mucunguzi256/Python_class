import random
import sys
from enum import Enum


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

    if player == 1 and computer == 3:
        print('🎉 You Win!')
    elif player == 2 and computer == 1:
        print('🎉 You Win!')
    elif player == 3 and computer == 2:
        print('🎉 You Win!')
    elif player == computer:
        print('🙀 Tie Game!')
    else:
        print('🐍 Python Wins!')

    print('\nPlay again?')
    while True:
        playagain = input(' \ny for yes or \nq to quit \n\n')
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

        # break could have also worked!!


play_rsp()
