#!/user/bin/env python3
"""Rock, paper, scissors

Simple implementation of rock, paper, scissors in Python

Rules of the game:
    1. Rock beats scissors
    2. Scissors beats paper
    3. Paper beats rock

"""
from getpass import getpass as maskinput

SELECTION = [select for select in ["rock", "paper", "scissors"]]
PLAYER_ONE_NAME = input("Player ONE, enter your name. 'q' to quit: ").title()
PLAYER_TWO_NAME = input("Player TWO, enter your name. 'q' to quit: ").title()
COUNTER = int(input("Enter number of games to play. 'q' to quit: "))

while COUNTER != 0:
    print("Enter rock, paper, scissors")
    PLAYER_ONE_CHOICE = maskinput(("{}, your choice. 'q' to quit: ").format(PLAYER_ONE_NAME)).lower()
    PLAYER_TWO_CHOICE = maskinput(("{}, your choice. 'q' to quit: ").format(PLAYER_TWO_NAME)).lower()

    if PLAYER_ONE_CHOICE == 'q' or PLAYER_TWO_CHOICE == 'q':
        print('Goodbye!')
        break
    
    if PLAYER_ONE_CHOICE == PLAYER_TWO_CHOICE:
        print("It's a tie! Play again.")
    
    else:
        print("{} chose {}".format(PLAYER_ONE_NAME, PLAYER_ONE_CHOICE))
        print("{} chose {}".format(PLAYER_TWO_NAME, PLAYER_TWO_CHOICE))

    COUNTER -= 1
