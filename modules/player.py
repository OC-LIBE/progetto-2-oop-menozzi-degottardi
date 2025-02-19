import random
from modules.hand import Hand 

class Player:
    def __init__(self, name, avatar):
        self.name= name
        self.avatar= avatar
        self.hand= Hand
        self.chips = 100 #chips iniziali 

    