import random
import sys

import character
import display
import gamedata
import item
import script

def random_coord(max_x: int, max_y: int) -> tuple[int, int]:
    return random.randint(0, max_x), random.randint(0, max_y)

def create_boss() -> character.Boss:
    return character.Boss(
        name=gamedata.boss["name"],
        health=gamedata.boss["health"],
        attack=gamedata.boss["attack"],
        defense=gamedata.boss["defense"],
        speed=gamedata.boss["speed"]
    )

def create_enemy() -> character.Enemy:
    min_health, max_health = gamedata.enemy["health"]
    min_attack, max_attack = gamedata.enemy["attack"]
    min_defense, max_defense = gamedata.enemy["defense"]
    return character.Enemy(
        name=gamedata.enemy["name"],
        health=random.randint(min_health, max_health),
        attack=random.randint(min_attack, max_attack),
        defense=random.randint(min_defense, max_defense),
        speed=gamedata.enemy["speed"]
    )


class Map:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.map = [['.' for i in range(self.width)]
                    for i in range(self.height)]

    def get_coord(self, x: int, y: int) -> str:
        return self.map[y][x]

    def set_coord(self, x: int, y: int, value) -> None:
        self.map[y][x] = value

    def random_empty_coord(self, max_tries: int = 20) -> tuple[int, int]:
        """Return any random coord that is empty."""
        x, y = random_coord(self.width - 1, self.height - 1)
        tries = 1
        while self.get_coord(x, y) != '.' and tries < max_tries:
            x, y = random_coord(self.width - 1, self.height - 1)
            tries += 1
        if tries >= max_tries:
            return None
        return x, y


class Game:

    def __init__(self, name):
        self.n = 5  #length of sides of grid
        self.e = 12  #num of enemies
        self.map = Map(self.n, self.n)
        self.player = character.Player(name)
        self.player_coord = (0, 0)
        self.player_last_move = None
        self.player_next_encounter = None
        self.moveset = ["help", "gears", "equip", "unequip", "inventory", "trash"]
        self.directions = ["w", "a", "s", "d"]

    def printmap(self):
        print("\n-----\nMap\n\n")
        for i in range(self.n):
            output = ""
            for j in range(self.n):
                output += str(self.map.get_coord(i, j)) + " "
            print(output)
        print(f"Current Event:{self.player.event_queue}",
              type(self.player.event_queue))
        print("-----\n")

    def random_map(self):  #randomise events in map
        #player spawn
        self.map.set_coord(0, 0, self.player)
        self.player_coord = (0, 0)
        self.player_last_move = None
        self.player_next_encounter = None
        #boss spawn
        coord = self.map.random_empty_coord()
        if not coord:
            raise ValueError("No empty coords")
        x, y = coord
        self.map.set_coord(x, y, create_boss())
        #enemies spawn
        for i in range(self.e):
            coord = self.map.random_empty_coord()
            if not coord:
                raise ValueError("No empty coords")
            x, y = coord
            self.map.set_coord(x, y, create_enemy())

    def help_cmds(self):
        return script.help

    def prompt_player(self) -> str:
        move = input(script.prompt_move)
        if move not in self.moveset and move not in self.directions:
            print(script.invalid_move)
            move = input(script.prompt_move)
        return move

    def player_action(self, move: str):
        if move == "help":
            print(self.help_cmds())
        elif move == "inventory":
            display.inventory(
                self.player.json_inventory()
            )
        elif move == "gears":
            display.gear(
                self.player.json_gear()
            )
        elif move == "equip":
            self.player_equip()
        elif move == "unequip":
            self.player_unequip()
        elif move == "trash":
            self.player_trash()
        else:  # assumed to be "w", "a", "s", "d"
            self.player_move(move)

    def player_equip(self) -> None:
        """Equipping submenu"""
        if self.player.items.is_empty():
            print(script.invalid_equip)
            return
        display.inventory(
            self.player.json_inventory()
        )
        choice = self.player.get_item(
            input(script.prompt_equip)
        )
        while not choice or not isinstance(choice, (item.Weapon, item.Armor)):
            choice = self.player.get_item(
                input(script.prompt_item)
            )
        self.player.equip(choice)

    def player_unequip(self) -> None:
        """Unequipping submenu"""
        display.gear(
            self.player.json_gear()
        )
        choice = input(script.prompt_unequip)
        while not self.player.get_gear(choice):
            choice = input(script.invalid_equip)
        self.player.unequip(choice)

    def player_trash(self) -> None:
        """Trashing submenu"""
        if self.player.items.is_empty():
            print(script.invalid_equip)
            return
        item = self.player.get_item(
            input(script.prompt_trash)
        )
        while not item:
            item = self.player.get_item(
                input(script.invalid_item)
            )
        self.player.trash(item)

    def player_move(self, move: str) -> None:
        x, y = self.player_coord
        if move == 'w' and x > 0:
            self.move_player(x - 1, y)
        elif move == 'a' and y > 0:
            self.move_player(x, y - 1)
        elif move == 's' and x < self.n - 1:
            self.move_player(x + 1, y)
        elif move == 'd' and y < self.n - 1:
            self.move_player(x, y + 1)

    def move_player(self, x: int, y: int):
        prev_x, prev_y = self.player_coord
        self.player_next_encounter = self.map.get_coord(x, y)
        self.player_last_move = self.player_coord
        self.player_coord = (x, y)
        self.map.set_coord(x, y, self.player)
        self.map.set_coord(prev_x, prev_y, "X")

    def check_event(self):
        if isinstance(self.player_next_encounter, character.Enemy):
            print(script.event_encounter)
            self.event_fight(self.player, self.player_next_encounter)
        else:
            print(script.event_nothing)

    def event_fight(self, player, enemy):
        result = False
        turn_order = [player, enemy]
        if player.speed >= enemy.speed:
            i = 0
        else:
            i = 1
        while not result:
            result = turn_order[i].combat(
                turn_order[i - 1]
            )  #if i = 0 i.e. player, i - 1 will become -1 which points to enemy as intended
            if i == 1:
                i = 0
            else:
                i += 1
        if result == -1:  #defeat against normal enemy
            sys.exit()
        elif result == -666:  #defeat against boss
            print(script.boss_won)
            sys.exit()
        elif result == -888:  #win against boss
            print(script.boss_defeated)
            sys.exit()
        elif result == True:  #win against normal enemy
            print("\n")
            self.player.health = self.player.max_health
            reward = random.choice(item.loot_table)
            print(script.get_reward.replace("$$reward$$", reward))
            self.player.store(item.create_item(reward))
