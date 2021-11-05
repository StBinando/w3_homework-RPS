from models.player import Player
from random import randint

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def get_input_player1(self, name1, choice1):
        self.player1.name = name1
        self.player1.choice = choice1

    def get_input_player2(self, name2, choice2):
        self.player2.name = name2
        self.player2.choice = choice2

    def get_computer_choices(self,):
        self.player2.name = "HAL 9000"
        choices = ["scissors", "rock", "paper"]
        self.player2.choice = choices[randint(0, 2)]

    def get_winner(self):
        winner = None
        winner = self.player1 if (
            (self.player1.choice[0] == "s" and self.player2.choice[0] == "p") or
            (self.player1.choice[0] == "r" and self.player2.choice[0] == "s") or
            (self.player1.choice[0] == "p" and self.player2.choice[0] == 'r')
        ) else self.player2 if (
            (self.player1.choice[0] == "s" and self.player2.choice[0] == "r") or
            (self.player1.choice[0] == "r" and self.player2.choice[0] == "p") or
            (self.player1.choice[0] == "p" and self.player2.choice[0] == 's')
            ) else None
        

#  alternative solution

        # if self.player1.choice[0] == "s":
        #     if self.player2.choice[0] == "p":
        #         winner = self.player1
        #     elif self.player2.choice[0] == "r":
        #         winner = self.player2

        # elif self.player1.choice[0] == "r":
        #     if self.player2.choice[0] == "s":
        #         winner = self.player1
        #     elif self.player2.choice[0] == "p":
        #         winner = self.player2

        # elif self.player1.choice[0] == "p":
        #     if self.player2.choice[0] == "r":
        #         winner = self.player1
        #     elif self.player2.choice[0] == "s":
        #         winner = self.player2

        return winner

            