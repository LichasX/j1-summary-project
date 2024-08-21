
# Import statements
#main game loop

import time, character, intro, game, item
import rng


def main():
    # Board = game.Game("Jian Lin")
    # Board.random_map()
    # Board.printmap()
    # while True:
    #     Board.player_input()
    #     Board.update_position()
    #     Board.printmap()
    #     Board.check_event()
    player = character.Player("Test")
    print(player.gears)
    print(player.items)
    print(not player.backpack_isFull())
    player.store(item.stone_sword)
    print(player.items)
    player.unequip("weapon")
    print(player.items)

if __name__ == "__main__":
    main()

