import json
import random

# Player class

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.money = 16 # starting money
        self.properties = [] #properties owned by player
        