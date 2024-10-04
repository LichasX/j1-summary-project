import random
import sys

import character
import item
import script


class Game:

    def __init__(self, name):
        self.n = 5  #length of sides of grid
        self.e = 12  #num of enemies
        self.map = [['.' for i in range(self.n)] for i in range(self.n)]
        self.player = character.Player(name)

    def printmap(self):
        print("\n-----\nMap\n\n")
        for i in range(self.n):
            output = ""
            for j in range(self.n):
                output += str(self.map[i][j]) + " "
            print(output)
        print(f"Current Event:{self.player.event_queue}",
              type(self.player.event_queue))
        print("-----\n")

    def random_map(self):  #randomise events in map
        #player spawn
        self.map[0][0] = self.player
        #boss spawn
        while True:
            coords = (random.randint(0, self.n - 1),
                      random.randint(0, self.n - 1))
            if self.map[coords[0]][coords[1]] == ".":
                self.map[coords[0]][coords[1]] = character.Boss(
                    ["Overlord", 50, 3, 5, 0.5])  #change values as needed
                break
        #enemies spawn
        for i in range(self.e):
            while True:
                coords = (random.randint(0, self.n - 1),
                          random.randint(0, self.n - 1))
                if self.map[coords[0]][coords[1]] == ".":
                    self.map[coords[0]][coords[1]] = character.Enemy([
                        "Enemy",
                        random.randint(3, 10),
                        random.randint(1, 2),
                        random.randint(1, 3), 1
                    ])
                    break

    def help_cmds(self):
        return script.help

    def player_input(self):
        while True:
            move = input(script.prompt_move)
            if move == "help":
                print(self.help_cmds())
            elif move == "inventory":
                self.player.display_inv()
            elif move == "gears":
                self.player.display_gears()
            elif move == "equip":
                if len(self.player.items.keys()) > 0:
                    self.player.display_inv()
                    move2 = input(script.prompt_equip)
                    while move2 not in self.player.items.keys():
                        move2 = input(script.prompt_item)
                    self.player.equip(self.player.items[move2])
                else:
                    print(script.invalid_equip)
            elif move == "unequip":
                self.player.display_gears()
                move2 = input(script.prompt_equip)
                while move2 not in [
                        "helm", "chest", "legs", "boots", "weapon"
                ]:
                    move2 = input(script.invalid_unequip)
                self.player.unequip(move2)
            elif move == "trash":
                if len(self.player.items.keys()) > 0:
                    self.player.display_inv()
                    move2 = input(script.prompt_trash)
                    while move2 not in self.player.items.keys():
                        move2 = input(script.invalid_item)
                    self.player.trash(self.player.items[move2])
                else:
                    print(script.invalid_trash)
            elif move == 'w' and self.player.coords[0] > 0:
                self.player.event_queue = self.map[self.player.coords[0] -
                                                   1][self.player.coords[1]]
                self.player.last_move = self.player.coords
                self.player.coords = (self.player.coords[0] - 1,
                                      self.player.coords[1])
                break
            elif move == 'a' and self.player.coords[1] > 0:
                self.player.event_queue = self.map[self.player.coords[0]][
                    self.player.coords[1] - 1]
                self.player.last_move = self.player.coords
                self.player.coords = (self.player.coords[0],
                                      self.player.coords[1] - 1)
                break
            elif move == 's' and self.player.coords[0] < self.n - 1:
                self.player.event_queue = self.map[self.player.coords[0] +
                                                   1][self.player.coords[1]]
                self.player.last_move = self.player.coords
                self.player.coords = (self.player.coords[0] + 1,
                                      self.player.coords[1])
                break
            elif move == 'd' and self.player.coords[1] < self.n - 1:
                self.player.event_queue = self.map[self.player.coords[0]][
                    self.player.coords[1] + 1]
                self.player.last_move = self.player.coords
                self.player.coords = (self.player.coords[0],
                                      self.player.coords[1] + 1)
                break
            else:
                print(script.invalid_move)

    def update_position(self):
        self.map[self.player.coords[0]][self.player.coords[1]] = self.player
        self.map[self.player.last_move[0]][self.player.last_move[1]] = "X"

    def check_event(self):
        if isinstance(self.player.event_queue, character.Enemy):
            print(script.event_encounter)
            self.event_fight(self.player, self.player.event_queue)
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
            self.player.store(reward)
