import json
import random


# Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.position = 0
        self.money = 16  # Starting money
        self.properties = []  # Properties owned by the player
    
    def move(self, steps, board_size):
        """Moves the player around the board, wrapping around if necessary."""
        self.position = (self.position + steps) % board_size

    def buy_property(self, property):
        """Buys the property if the player has enough money."""
        if self.money >= property['price']:
            self.money -= property['price']
            self.properties.append(property)
            print(f"{self.name} buys {property['name']} for ${property['price']}")
        else:
            print(f"{self.name} cannot afford {property['name']}!")

    def collect_money(self, amount):
        """Collects money (e.g., passing GO)."""
        self.money += amount
        print(f"{self.name} collects ${amount}.")

# Load board from JSON
def load_board(filename='board.json'):
    with open(filename, 'r') as file:
        return json.load(file)

# Game class
class MonopolyGame:
    def __init__(self, board):
        self.board = board
        self.players = []
        self.turn_order = ["Peter", "Billy", "Charlotte", "Sweedal"]
        self.current_turn = 0

    def add_player(self, player_name):
        """Add players to the game."""
        player = Player(player_name)
        self.players.append(player)
        print(f"Player {player_name} has joined the game.")

    def roll_dice(self):
        """Simulate dice rolls."""
        return random.randint(1, 6), random.randint(1, 6)

    def play_turn(self, player):
        """Handle a player's turn: roll dice, move, and possibly buy a property."""
        dice_roll = self.roll_dice()
        print(f"{player.name} rolls {dice_roll[0]} and {dice_roll[1]}.")
        steps = sum(dice_roll)
        player.move(steps, len(self.board))

        # Handle passing GO
        if player.position == 0:
            player.collect_money(1)  # Collect $1 for passing GO
        
        # Land on the current board space
        current_space = self.board[player.position]
        print(f"{player.name} moves {steps} steps to {current_space['name']}.")

        if current_space['type'] == 'property':
            # If property is not owned, player can buy it
            if current_space not in [p['name'] for p in player.properties]:
                player.buy_property(current_space)

    def check_winner(self):
        """Check the winner based on who has the most money."""
        winner = max(self.players, key=lambda p: p.money)
        return winner

    def start_game(self):
        """Start the game, simulate turns, and display results."""
        print("Starting the game!\n")

        while True:
            print(f"\n--- Round {self.current_turn + 1} ---")
            player = self.players[self.current_turn % len(self.players)]
            print(f"{player.name}'s turn:")
            self.play_turn(player)
            
            # Move to next round
            self.current_turn += 1

            # End condition: Can stop based on your own logic (e.g., rounds or when only one player has money left)
            if self.current_turn == 10:  # Just as an example, end the game after 10 rounds
                break
        
        # Determine the winner after 10 rounds
        winner = self.check_winner()
        print(f"\nGame Over! The winner is {winner.name} with ${winner.money}.")
        print(f"Properties owned by {winner.name}: {[p['name'] for p in winner.properties]}")

# Main execution
if __name__ == '__main__':
    # Load the board from the provided JSON file
    board = load_board()

    # Create the game
    game = MonopolyGame(board)

    # Add players
    game.add_player("Peter")
    game.add_player("Billy")
    game.add_player("Charlotte")
    game.add_player("Sweedal")

    # Start the game
    game.start_game()