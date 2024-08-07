import random

class Weapon:
    def __init__(self, data: list):
        self.attack = data[0]
        self.critc = data[1]
        self.name = data[2]

    def __repr__(self):
        return f"Att:{self.attack} Crit:{self.critc}% Name:{self.name}"

    def crit(self):
        x = random.randint(1, 100)
        if x <= self.critc:
            return True
        return False

    def combat(self, enemy, Player):
        crit = 1  #if there is no crit does not change
        if self.crit():
            crit = 2  # double the damage when it crits
        damage = (self.attack + Player.attack - enemy.defense) * crit
        if damage < 0:
            damage = 1
        enemy.health -= damage
        print(f"You dealt {damage} damage to the {enemy.name}.")
        print(f"{enemy.name} current health:{enemy.health}")
        if enemy.health <= 0:
            enemy.health = 0
            print(f"{enemy} fainted.")


#Weapon list
#format   att, critc
Wooden_sword = Weapon([3, 5, "Wooden Sword"])
Stone_sword = Weapon([5, 5, "Stone Sword"])
Iron_sword = Weapon([8, 10, "Iron Sword"])

Steel_sword = Weapon([12, 8, "Steel Sword"])

Fire_blade = Weapon([20, 5, "Fire Blade"])
Ice_blade = Weapon([12, 50, "Ice Blade"])

Diamond_sword = Weapon([25, 12, "Diamond Sword"])
Forty_metre_long_sword = Weapon([40, 40, "40m-long-sword"])

Soul_stealer = Weapon(
    [5, 5, "Soul Stealer"])  #steal the attack of enemy and add it to weapon's attack.

#fire blade does half of the damage dealt to the enemy, last 2 turns

#dev weapon
Ulti_blade = Weapon([100000000000000, 0, "Ulti-Blade"])



class Potions:
    def __init__(self, data):
        self.desc = data[0]
        self.buff = data[1]
        
    def __repr__(self):
        return self.desc 

    def potion_buff(self, player):
        pass

#Potion list
lesser_healing_potion = Potions(["Heals 2 hp to the player", 2])
normal_healing_potion = ["Heals 5 hp to the player", 5]
greater_healing_potion = ["Heals 10 hp to the player ", 10]
supreme_healing_potion = ["Heals 20 hp to the player", 20]

strength_potion = Potions(["Add 10 att to the player's strength stats", 10])
speed_potion = Potions(["Add 5 speed to the player's speed stats", 5])
almond_potion = Potions(["Add 2 to each of the player's stat"])

bleach = Potions(["Kills you instantly, toddler approved!", -9999999999999])

class Item:
    def __init__(self, num, desc, name, weight):
        self.name = name
        self.num = num
        self.desc = desc
        self.weight = weight