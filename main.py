
# Import statements
import random
import item
import classes
#main game loop

import time, character, intro
import rng

def main():

    print("Intro")
    player = classes.Player(str(input("What is your name?")))
    print(player)
    # object = classes.Object(3, "ee")
    # object2 = classes.Object(4, "dd")
    dict = {}
    dict[1] = player
    print(dict)
    print(dict[1].attack)
    # dict[1] = object
    # dict[2] = object2
    # print(dict)
    # for i in dict.values():
    #     print(i.item)
    
    
if __name__ == "__main__":
    main()
import mud

import data

if __name__ == "__main__":
    game = mud.Game()
    mud.welcome()
    player = data.create_player()
    game.add_player(player)
    while not game.is_gameover():
        choices = game.get_options()
        choice = data.prompt_player_choice(choices)
        actions = game.get_actions(choice)
        game.execute(actions)
        data.display(game.status())
    mud.epilogue()

