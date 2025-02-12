import random
from modules.card import Card 

class Hand:
    def __init__(self, cards, score):
        self.cards= []
        self.score= 0
    
    def add_card(self, card):
        self.cards.append(card)
    
    def calcola_score(self):
        total_score = 0
        aces = 0
        for card in self.cards: 
            total_score += card.card_scores[0] #prendo il primo valore, nel caso dell'asso considero l'1. 
            if card.rank == 1:
                aces += 1
        
        while total_score <= 11 and aces > 0:
            total_score += 10 
            aces -= 1
    
        self.score = total_score 

    def discard(self):
        self.cards = []
        self.score = 0
        
