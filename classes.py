class Gears:
    def __init__(self):
        self.helmet = (None)
        self.chestplate = (None)
        self.leggings = (None)
        self.boots = (None)
        self.accessories = (None)
        pass
        
class Backpack: #store, display, check, destroy
    def __init__(self, slots):
        self.items = {}
        self.backpack_size = slots

    def store(self, name, object):
        if name in self.items:
            self.items[name].num += object.num
            print(f'{name} * {object.num} has been stored')
            return
            
        if len(self.items) >= self.backpack_size:
            print("Backpack is full!")
            return
        self.items[name] = object
        print(f'{name} * {object.num} has been stored.')
        return
        
    def display(self):
        lst = [i for i in self.items.keys()]
        disp = ', '.join(lst)
        return disp

    def check(self, item):
        pass

class Player:
    def __init__(self, name):
        self.name = str(name)
        self.health = 10
        self.defense = 0
        self.attack = 1
        self.dodge = 0.05 #5%
        self.speed = 1
        self.crit_chance = 0.05 
        self.crit_dmg = 2 #200%
        
    def __repr__(self):
        return f"Name: {self.name}"

class Backpack:
    pass
        

class Object:
    def __init__(self, num, desc):
        self.num = num
        self.desc = desc


class Enemy:
    def __init__(self, type):
        if type:
            self.health, self.attack, self.defense = 10, 2, 1
        else:  
            self.health, self.attack, self.defense = 5, 1, 0
    def attack(self, player_obj):
        pass


