import random
from modules.hand import Hand 

class Player:
    def __init__(self, name, Avatar):
        self.name= name
        self.avatar= Avatar
        self.hand= Hand
        self.chips = 100 #chips iniziali 

    