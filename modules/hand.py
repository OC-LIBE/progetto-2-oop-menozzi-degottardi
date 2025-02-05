import random
from modules.card import Card 

class Hand:
    def __init__(self, cards, score):
        self.cards= []
        self.score= 0
    
    def add_card(self, card):
        self.cards.append(card)
    
    def calcola_score(self, score):
        scores= 0
        for card in self.hand:
            new_scores= []

    def discard(self):
        self.cards.clear()
        self.score = 0
        
