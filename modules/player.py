import random
from modules.card import Card


class Player:
    def __init__(self, hand_value, money):
        self.hand_value = hand_value
        self.money= money

    def draw(self):
        if len(self.cards) == 0:
            return False
        drawn_card = self.cards[0]
        self.cards.remove(self.cards[0])
        print(len(self.cards))
        return drawn_card

    def aggiorna_mano(self):
        mano = 0 
        mano =+  self.cards_scores 
