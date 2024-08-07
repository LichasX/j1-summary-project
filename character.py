class Player:
    def __init__(self, name, slots):
        self.name = str(name)
        self.health = 10
        self.defense = 0
        self.attack = 1
        self.speed = 1
        self.items = {}
        self.backpack_size = slots

    def __repr__(self):
        return f"Name: {self.name}"

    def backpack_isFull(self):
        total = 0
        for item in self.items.values():
            total += item.num
        print(total)
        return total >= self.backpack_size

    def store(self, object):
        if not self.backpack_isFull:
            if object.name in self.items: #item present
                self.items[object.name].num += object.num
                print(f'{object.num} {object.name} has been stored')
            else: #new item
                self.items[object.name] = object
                print(f'{object.num} {object.name} has been stored.')
        else:
            print("Unable to store. Backpack is full.")


    def display(self):
        lst = [i for i in self.items.keys()]
        disp = ', '.join(lst) #all items in backpack
        return disp

    def check(self, item):
        if item in self.items.keys():
            print(f'Name: {item}')
            print(f'Amount:{self.items[item].num}')
            print(f'Description:{self.items[item].desc}')
            return
        print('Item not in Backpack')
        return
    #Gears
    def equip(self, gear):
        if gear not in self.items:
            print("You don't have that gear!")

class Object:
    def __init__(self, name, num, description):
        self.name = name
        self.num = num
        self.description = description


class Enemy:
    def __init__(self, type):
        if type == "Brute":
            self.name = "Brute"
            self.health, self.attack, self.defense = 10, 2, 1
        elif type == "Armored Gorilla":
            self.name = "Armored Gorilla"
            self.health, self.attack, self.defense = 10, 0, 1000
        else:
            self.health, self.attack, self.defense = 5, 1, 0

player = Player("NaMe", 20)
object1 = Object("Object1", 7, "Object1 desc")
player.store(object1)
print(player.backpack_isFull())
