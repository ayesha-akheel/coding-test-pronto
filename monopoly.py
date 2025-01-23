import json
import random

# Player class

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.money = 16 # starting money
        self.properties = [] #properties owned by player
    
    def move(self, steps, board_size):
        """Move the layer around the board, wrapping around if necessary."""
        self.position = (self.position + steps) % board_size