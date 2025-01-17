import random
from modules.card import Card

class Player:
    def __init__(self, name):
        self.name = name #nome esterno o il banco
        self.hand = [] #lista carte in mano
        self.scores= [] #lista  punteggi  

    def aggiungi_carta(self, card):
        self.hand.append(card) #aggiungo la carta alla mnao
        self.scores= self.calcolo_punteggi() #per calcolare i nuovi punteggi

    def calcolo_punteggi(self): #da rivedere come  salvare tutti i risultati possibili
        scores = [0]
        for card in self.hand:
            new_scores = []
            for score in scores:
                for card_score in card.cards_scores: #devo valutare anche le varie possibilita ddell'asse 
                    new_scores.append(score + card_score)
            scores = #new scores in una lista, come??

    #mancano funzioni per vedere se hai perso o hai vinto (< o > 21)

    def draw(self):
        if len(self.cards) == 0:
            return False
        drawn_card = self.cards[0]
        self.cards.remove(self.cards[0])
        print(len(self.cards))
        return drawn_card
