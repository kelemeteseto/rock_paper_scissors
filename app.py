#!/user/bin/env python3
"""Rock, paper, scissors

Simple implementation of rock, paper, scissors in Python

Rules of the game:
    1. Rock beats scissors
    2. Scissors beats paper
    3. Paper beats rock

"""
from getpass import getpass as maskinput

class JanKenPo(object):
    
    print('*********************************************')
    # SELECTION = [select for select in ["rock", "paper", "scissors"]]
    COUNTER = int(input("\t\n Enter number of games to play. 0 to quit: "))

    def __init__(self, name, choice):
        self.name = name
        self.choice = choice

    def get_name(self):
        return self.name

    def get_choice(self):
        return self.choice

    @classmethod
    def from_input(cls):
        return cls(
            raw_input('\t Name: ').title(),
            maskinput('\t Choice: ').lower()
        )


if __name__ == "__main__":
    rounds = JanKenPo.COUNTER
    player_one = JanKenPo.from_input()
    player_two = JanKenPo.from_input()

    while rounds != 0:
        if player_one.get_choice() == 'q' or player_two.get_choice() == 'q':
            print('Goodbye!')
            break
        
        if player_one.get_choice() == player_two.get_choice():
            print("")
            print("\t It's a tie! Play again.")
        
        else:
            print("")
            print("\t {} chose {}".format(player_one.get_name(), player_one.get_choice()))
            print("\t {} chose {}".format(player_two.get_name(), player_two.get_choice()))

        rounds -= 1
    print('*********************************************')
