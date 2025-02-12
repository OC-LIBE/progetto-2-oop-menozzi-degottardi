import random
from modules.py import Player

class Dealerplayer(Player):

    def __init__(self, dealer_score):
        self.dealer_score= dealer_score 

    def ritira_puntate(self, total_score):
        total_score = 0 


