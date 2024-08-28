import random


class Item:

    def __init__(self, data: list):  # name, num, desc, spec_weight
        self.name = data[0]
        self.num = data[1]
        self.desc = data[2]
        self.weight = data[3] * self.num


class Armor:

    def __init__(self, section, data: list):  #name, defense, num, spec_weight
        self.section = section  #helm, chest, leg, boots
        self.name = data[0]
        self.defense = data[1]
        self.num = data[2]
        self.weight = data[3] * self.num

    def __repr__(self):
        return f"{self.name}"

    def get_stats(self):
        return f"Item Description\n-----\nName: {self.name}\nDefense: {self.defense}\nItem Stack: {self.num}\nTotal Weight: {self.weight}\n-----"


class Weapon:

    def __init__(self, data: list):  #attack, critc, name, num, spec_weight
        self.section = 'weapon'
        self.attack = data[0]
        self.critc = data[1]
        self.name = data[2]
        self.num = data[3]
        self.weight = data[4] * self.num

    def __repr__(self):
        return f"{self.name}"

    def get_stats(self):
        return f"Item Description\n-----\nName: {self.name}\nAttack: {self.attack}\nCrit Chance: {self.critc}\nItem Stack: {self.num}\nTotal Weight: {self.weight}\n-----"

    def crit(self):
        x = random.randint(1, 100)
        if x <= self.critc:
            return True
        return False


#Weapon list
#format   att, critc
wooden_sword = Weapon([3, 5, "Wooden Sword", 1, 2])
stone_sword = Weapon([5, 5, "Stone Sword", 1, 3])
iron_sword = Weapon([8, 10, "Iron Sword", 1, 4])

steel_sword = Weapon([12, 8, "Steel Sword", 1, 5])

fire_blade = Weapon([20, 5, "Fire Blade", 1, 0])
ice_blade = Weapon([12, 50, "Ice Blade", 1, 2])

diamond_sword = Weapon([25, 12, "Diamond Sword", 1, 2])
forty_metre_long_sword = Weapon([40, 40, "40m-long-sword", 1, 40])

soul_stealer = Weapon(
    [5, 5, "Soul Stealer", 1,
     0])  #steal the attack of enemy and add it to weapon's attack.

#fire blade does half of the damage dealt to the enemy, last 2 turns

#dev weapon
ulti_blade = Weapon([100000000000000, 0, "Ulti-Blade", 1, 0])

#Armors #wood 1, iron 2, diamond 3
#helm, boots 1, legs 2, chest 3

iron_helmet = Armor('helm', ['Iron Helmet', 2, 1, 10])
iron_chestplate = Armor('chest', ['Iron Chestplate', 6, 1, 16])
iron_leggings = Armor('leg', ['Iron Leggings', 4, 1, 14])
iron_boots = Armor('boots', ['Iron Boots', 2, 1, 8])

diamond_helmet = Armor('helm', ['Diamond Helmet', 3, 1, 5])
diamond_chestplate = Armor('chest', ['Diamond Chestplate', 9, 1, 8])
diamond_leggings = Armor('leg', ['Diamond Leggings', 6, 1, 7])
diamond_boots = Armor('boots', ['Diamond Boots', 3, 1, 4])


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
almond_potion = Potions(["Add 2 to each of the player's stat", -0])

bleach = Potions(["Kills you instantly, toddler approved!", -9999999999999])

loot_table = [
    wooden_sword, stone_sword, iron_sword, steel_sword, fire_blade, ice_blade,
    diamond_sword, forty_metre_long_sword, iron_helmet, iron_chestplate,
    iron_leggings, iron_boots, diamond_helmet, diamond_chestplate,
    diamond_leggings, diamond_boots
]
