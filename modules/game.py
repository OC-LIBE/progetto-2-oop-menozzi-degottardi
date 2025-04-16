import random
from modules.deck import Deck
from modules.player import Player
from modules.human_player import HumanPlayer
from modules.dealer_player import Dealerplayer
from modules.hand import Hand

class Game:
    def __init__(self, number_of_decks):
        self.deck = Deck(number_of_decks = number_of_decks)
        self.deck.shuffle()
        self.player = HumanPlayer(chips=100, last_score = 0)
        self.dealer = Dealerplayer(dealer_score=0)
        self.player.hand = Hand([], 0)
        self.dealer.hand = Hand([], 0)
        
    def reset_game(self):
        self.deck.reset() 
        self.deck.shuffle()
        self.player.hand.discard()
        self.dealer.hand.discard()
        self.phase= "Puntata iniziale"
