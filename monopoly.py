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

    def buy_property(self, property):
        """Buys the property if the player has enough money."""
        if self.money >= property['price']:
            self.money -= property['price']
            self.properties.append(property)
            print(f"{self.name} buys {property['name']} for ${property['price']}")
        else:
            print(f"{self.name} cannot afford {property['name']}!")