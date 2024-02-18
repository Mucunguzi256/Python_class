from random import randint
import sys

answer = randint(1, 10)

while True:
    try:
        guess = int(input('Guess a number; 1 to 10  '))
        if 0 < guess < 11:
            if guess == answer:
                print("you're a genius")
                break
        else:
            print('I said 1 to 10')
    except ValueError:
        print('Please enter a number')
        continue
