import random

import gamedata


class Item:

    def __init__(self, name: str, num: int, desc: str, spec_weight: float):
        self.name = name
        self.num = num
        self.desc = desc
        self.weight = spec_weight * self.num


class Armor:

    def __init__(self, section, name: str, defense: int, num: int,
                 spec_weight: float):  #name, defense, num, spec_weight
        self.section = section  #helm, chest, leg, boots
        self.name = name
        self.defense = defense
        self.num = num
        self.weight = spec_weight * self.num

    def __repr__(self):
        return f"{self.name}"

    def get_stats(self):
        return f"Item Description\n-----\nName: {self.name}\nDefense: {self.defense}\nItem Stack: {self.num}\nTotal Weight: {self.weight}\n-----"


class Weapon:

    def __init__(self, attack: int, critc: int, name: str, num: int,
                 weight: int):
        self.section = 'weapon'
        self.attack = attack
        self.critc = critc
        self.name = name
        self.num = num
        self.weight = weight * self.num

    def __repr__(self):
        return f"{self.name}"

    def get_stats(self):
        return f"Item Description\n-----\nName: {self.name}\nAttack: {self.attack}\nCrit Chance: {self.critc}\nItem Stack: {self.num}\nTotal Weight: {self.weight}\n-----"

    def crit(self):
        x = random.randint(1, 100)
        if x <= self.critc:
            return True
        return False


class Potion:

    def __init__(self, name: str, desc: str, buff: int):
        self.name = name
        self.desc = desc
        self.buff = buff

    def __repr__(self):
        return self.desc

    def potion_buff(self, player):
        pass


def create_weapon(jsondata: dict) -> Weapon:
    return Weapon(jsondata["attack"], jsondata["critc"], jsondata["name"],
                  jsondata["num"], jsondata["weight"])

def create_armor(jsondata: dict) -> Armor:
    return Armor(jsondata["section"], jsondata["name"], jsondata["defense"], jsondata["num"], jsondata["weight"])

def create_potion(jsondata: dict) -> Potion:
    return Potion(jsondata["name"], jsondata["desc"], jsondata["buff"])

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
