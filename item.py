import random

import gamedata


class Item:

    def __init__(self, name: str, desc: str, weight: int):
        self.name = name
        self.desc = desc
        self.weight = weight


class Armor(Item):

    def __init__(self, section, name: str, desc: str, defense: int, weight: float):
        super().__init__(name, desc, weight)
        self.section = section  #helm, chest, leg, boots
        self.defense = defense

    def __repr__(self):
        return f"{self.name}"

    def get_stats(self):
        return f"Item Description\n-----\nName: {self.name}\nDefense: {self.defense}\nItem Stack: {self.num}\nTotal Weight: {self.weight}\n-----"


class Weapon(Item):

    def __init__(self, attack: int, critc: int, name: str, desc: str, weight: int):
        super().__init__(name, desc, weight)
        self.section = 'weapon'
        self.attack = attack
        self.critc = critc

    def __repr__(self):
        return f"{self.name}"

    def get_stats(self):
        return f"Item Description\n-----\nName: {self.name}\nAttack: {self.attack}\nCrit Chance: {self.critc}\nItem Stack: {self.num}\nTotal Weight: {self.weight}\n-----"

    def crit(self):
        x = random.randint(1, 100)
        if x <= self.critc:
            return True
        return False


class Potion(Item):

    def __init__(self, name: str, desc: str, buff: int, weight: int):
        super().__init__(name, desc, weight)
        self.buff = buff

    def __repr__(self):
        return self.desc

    def potion_buff(self, player):
        pass


def create_weapon(jsondata: dict) -> Weapon:
    return Weapon(**jsondata)

def create_armor(jsondata: dict) -> Armor:
    return Armor(**jsondata)

def create_potion(jsondata: dict) -> Potion:
    return Potion(**jsondata)

def create_item(name: str) -> Weapon | Armor | Potion:
    if name in gamedata.weapons:
        return create_weapon(gamedata.weapons[name])
    elif name in gamedata.armor:
        return create_armor(gamedata.armor[name])
    elif name in gamedata.potions:
        return create_potion(gamedata.potions[name])
    else:
        raise ValueError(f"Invalid item name: {name}")


loot_table = [
    "wooden_sword", "stone_sword", "iron_sword", "steel_sword", "fire_blade",
    "ice_blade", "diamond_sword", "forty_metre_long_sword", "iron_helmet",
    "iron_chestplate", "iron_leggings", "iron_boots", "diamond_helmet",
    "diamond_chestplate", "diamond_leggings", "diamond_boots"
]
