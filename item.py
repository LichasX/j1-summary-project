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



class Potions:
    def __init__(self, data):
        self.desc = data[0]
        self.buff = data[1]
        
    def __repr__(self):
        return self.desc 

    def potion_buff(self, player):
        pass
