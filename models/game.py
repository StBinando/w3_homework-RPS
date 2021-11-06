from models.player import Player
from random import randint

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

# method to assign values of name and choice for Player 1 only
    def get_input_player1(self, name1, choice1):
        self.player1.name = name1
        self.player1.choice = choice1

# method to assign values of name and choice for Player 2 only
    def get_input_player2(self, name2, choice2):
        self.player2.name = name2
        self.player2.choice = choice2

# method to assign values of name and choice for Computer only (as Player 2)
    def get_computer_choices(self,):

        # assigns the computer name to Player 2
        self.player2.name = "HAL 9000"

        # local variable of LIST type with the possible choices
        choices = ["scissors", "rock", "paper"]

        # assigns the choice to Player 2, picking an element from the list,
        # based on the index, generated at random by "randint"
        self.player2.choice = choices[randint(0, 2)] #

# method to check which player won
    def get_winner(self):
        
        # there are only 3 winning combinations of choices:
        # scissors against paper
        # rock against scissors
        # paper against rock

        # if one of the 3 wiining combinations occurred
        # in favour of Player 1, Player one is the winner
        winner = self.player1 if (
            (self.player1.choice[0] == "s" and self.player2.choice[0] == "p") or
            (self.player1.choice[0] == "r" and self.player2.choice[0] == "s") or
            (self.player1.choice[0] == "p" and self.player2.choice[0] == 'r')

        # else, if one of the 3 winning combinations occurred
        # in favour of Player 2, Player 2 is the winner
        ) else self.player2 if (
            (self.player1.choice[0] == "s" and self.player2.choice[0] == "r") or
            (self.player1.choice[0] == "r" and self.player2.choice[0] == "p") or
            (self.player1.choice[0] == "p" and self.player2.choice[0] == 's')
        
        # else, it is a draw
            ) else None
        

#  ALTERNATIVE SOLUTION - for every possible choice of Player 1 compares the choice of Player 2

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

            