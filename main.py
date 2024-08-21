
# Import statements
#main game loop

import time, character, intro, game, item
import rng

"""
def main():
    Board = game.Game("Jian Lin")
    Board.random_map()
    Board.printmap()
    while True:
        Board.player_input()
        Board.update_position()
        Board.printmap()
        Board.check_event()
if __name__ == "__main__":
    main()
"""

player = character.Player('Test')
print(player.mload)
player.unequip('weapon')