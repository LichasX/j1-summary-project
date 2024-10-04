import time

import game


def main():
    print(
        "Myserious voice: 'I don't care! I seriously DON'T CARE! I have locked you up in my dungeon and you will never ever have the slightest of slimmer of hope in having the ability to even attempt to escape from this hell of mine!"
    )
    time.sleep(2)
    print("You wake up, dazed, who are you again?")
    name = input("\nWhat is your name?")
    time.sleep(1)
    print("\nwell, i dont care what your name is")
    time.sleep(2)
    board = game.Game("Jian Lin")
    board.random_map()
    board.printmap()
    while True:
        move = board.prompt_player()
        board.player_action(move)
        board.update_position()
        board.printmap()
        board.check_event()


if __name__ == "__main__":
    main()
