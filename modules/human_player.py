import random
from modules.player import Player 

class HumanPlayer(Player):

    def __init__(self, chips, last_score):
        self.chips= chips
        self.last_score= last_score

    def place_bet(self, scommessa):
        if amount <= self.chips:
            self.chips -= amount 
            return amount 
        else:
            return 0
