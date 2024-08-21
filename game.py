import random
import character, sys, item
class Game:
    def __init__(self, name):
        self.n = 5 #length of sides of grid
        self.e = 12 #num of enemies
        self.map = [['.' for i in range(self.n)] for i in range(self.n)]
        self.player = character.Player(name)

    def printmap(self):
        for i in range(self.n):
            output = ""
            for j in range(self.n):
                output += str(self.map[i][j])+" "
            print(output)
        print("\n")
        print(f"Current Event:{self.player.event_queue}", type(self.player.event_queue))

    def random_map(self): #randomise events in map
        #player spawn
        self.map[0][0] = self.player
        #boss spawn
        while True:
            coords = (random.randint(0, self.n-1), random.randint(0, self.n-1))
            if self.map[coords[0]][coords[1]] == ".":
                self.map[coords[0]][coords[1]] = character.Boss(["Overlord", 50, 3, 5, 0.5]) #change values as needed
                break
        #enemies spawn
        for i in range(self.e):
            while True:
                coords = (random.randint(0, self.n-1), random.randint(0, self.n-1))
                if self.map[coords[0]][coords[1]] == ".":
                    self.map[coords[0]][coords[1]] = character.Enemy(["Enemy", random.randint(3, 10), random.randint(1, 2), random.randint(1, 3), 1])
                    break

    def help_cmds(self):
        return "-----\nMovement\n\n'w'\n'a'\n's'\n'd'\n-----\nActions\n\n'trash' (remove item from inventory)\n'equip'\n'unequip'\n-----\nInfo\n\n'inventory'\n'gears'"
        
    def player_input(self):
        while True:
            move = input("Enter move or 'help' to view all commands: ")
            if move=="help":
                print(self.help_cmds())
            elif move=="inventory":
                self.player.display_inv()
            elif move=="gears":
                self.player.display_gears()
            elif move=="equip":
                if len(self.player.items.keys()) > 0:
                    self.player.display_inv()
                    move2=input("Enter what to equip: ")
                    while not move2 in self.player.items.keys():
                        move2=input("Enter valid item: ")
                    self.player.equip(self.player.items[move2])
                else:
                    print("got nothing to equip lah")
            elif move=="unequip":
                self.player.display_gears()
                move2=input("Enter what section to unequip (e.g. helm, chest etc AND NOT THE NAME OF THE ITEM): ")
                while not move2 in ["helm", "chest", "legs", "boots", "weapon"]:
                    move2=input("Enter valid section: ")
                self.player.unequip(move2)
            elif move=="trash":
                if len(self.player.items.keys()) > 0:
                    self.player.display_inv()
                    move2=input("Enter what to trash: ")
                    while not move2 in self.player.items.keys():
                        move2=input("Enter valid item: ")
                    self.player.trash(self.player.items[move2])
                else:
                    print("got nothing to trash lah")
            elif move=='w' and self.player.coords[0] > 0:
                self.player.event_queue = self.map[self.player.coords[0] - 1][self.player.coords[1]]
                self.player.last_move = self.player.coords
                self.player.coords =(self.player.coords[0] - 1, self.player.coords[1])
                break
            elif move=='a' and self.player.coords[1] > 0:
                self.player.event_queue = self.map[self.player.coords[0]][self.player.coords[1] - 1]
                self.player.last_move = self.player.coords
                self.player.coords =(self.player.coords[0], self.player.coords[1] - 1)
                break
            elif move=='s' and self.player.coords[0] < self.n - 1:
                self.player.event_queue = self.map[self.player.coords[0] + 1][self.player.coords[1]]
                self.player.last_move = self.player.coords
                self.player.coords =(self.player.coords[0] + 1, self.player.coords[1])
                break
            elif move=='d' and self.player.coords[1] < self.n - 1:
                self.player.event_queue = self.map[self.player.coords[0]][self.player.coords[1] + 1]
                self.player.last_move = self.player.coords
                self.player.coords =(self.player.coords[0], self.player.coords[1] + 1)
                break
            else:
                print("Invalid move")


    def update_position(self):
        self.map[self.player.coords[0]][self.player.coords[1]] = self.player
        self.map[self.player.last_move[0]][self.player.last_move[1]] = "X"

    def check_event(self):
        if isinstance(self.player.event_queue, character.Enemy):
            print("You have encountered an enemy.")
            self.event_fight(self.player, self.player.event_queue)
        else:
            print("nothing")

    def event_fight(self, player, enemy):
        result = False
        turn_order = [player, enemy]
        if player.speed >= enemy.speed:
            i = 0
        else:
            i = 1
        while not result:
            result = turn_order[i].combat(turn_order[i - 1]) #if i = 0 i.e. player, i - 1 will become -1 which points to enemy as intended
            if i == 1:
                i = 0
            else:
                i += 1
        if result == -1: #defeat against normal enemy
            sys.exit()
        elif result == -666: #defeat against boss
            print("The final boss has killed you...")
            sys.exit()
        elif result == -888: #win against boss
            print("You have defeated the final boss")
            sys.exit()
        elif result == True: #win against normal enemy
            self.player.health = self.player.max_health
            reward = random.choice(item.loot_table)
            print(f"You have obtained {reward}")
            self.player.store(reward)
