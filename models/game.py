from os import name
from models.player import Player

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def get_input_2_players(self, name1, choice1, name2, choice2):
        self.player1.name = name1
        self.player1.choice = choice1
        self.player2.name = name2
        self.player2.choice = choice2

    def get_winner(self):
        pass