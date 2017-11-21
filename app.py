#!/user/bin/env python3
"""Rock, paper, scissors

Simple implementation of rock, paper, scissors in Python

Rules of the game:
    1. Rock beats scissors
    2. Scissors beats paper
    3. Paper beats rock

"""
from getpass import getpass as maskinput

class JanKenPo:
    
    def __init__(self, name, choice):
        self.name = name        

    def get_player_name(self):
        return self.name

    # def get_player_two_name(self):
    #     return self.player_two

    # SELECTION = [select for select in ["rock", "paper", "scissors"]]
    # PLAYER1_NAME = input("Player ONE, enter your name. 'q' to quit: ").title()
    # PLAYER2_NAME = input("Player TWO, enter your name. 'q' to quit: ").title()
    # COUNTER = int(input("Enter number of games to play. 0 to quit: "))

    # while COUNTER != 0:
    #     print("Enter rock, paper, or scissors as choices. 'q' to quit")
    #     PLAYER1_CHOICE = maskinput(("{}, your choice: ").format(PLAYER1_NAME)).lower()
    #     PLAYER2_CHOICE = maskinput(("{}, your choice: ").format(PLAYER2_NAME)).lower()

    #     if PLAYER1_CHOICE == 'q' or PLAYER2_CHOICE == 'q':
    #         print('Goodbye!')
    #         break
        
    #     if PLAYER1_CHOICE == PLAYER2_CHOICE:
    #         print("It's a tie! Play again.")
        
    #     else:
    #         print("{} chose {}".format(PLAYER1_NAME, PLAYER1_CHOICE))
    #         print("{} chose {}".format(PLAYER2_NAME, PLAYER2_CHOICE))

    #     COUNTER -= 1

if __name__ == "__main__":
    frank = JanKenPo("Frank", "rock")
    tammy = JanKenPo("Tammy", "paper")

    print(frank.get_player_name(), tammy.get_player_name())
