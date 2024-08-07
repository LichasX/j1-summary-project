from item import Item
class Player:
    def __init__(self, name, max_load):
        self.name = str(name)
        self.health = 10
        self.defense = 0
        self.attack = 1
        self.speed = 1

        self.items = {}
        self.mload = max_load

        self.gears = {'helm': None, 'chest': None, 'legs': None, 'boots': None, 'accessories': None}

    def __repr__(self):
        return f"Name: {self.name}"

    def backpack_isFull(self):
        total = 0
        for item in self.items.values():
            total += item.weight
        print(total)
        return total >= self.mload

    def store(self, object):
        if not self.backpack_isFull:
            if object.name in self.items: #item present
                self.items[object.name].num += object.num
                
                total = 0
                for item in self.items.values():
                    total += item.weight
                if total > self.mload:
                    print("That's too much for your bag to handle!")
                    self.items[object.name].num -= object.num
                    return
                    
                print(f'{object.num} {object.name} has been stored')
            
            else: #new item
                self.items[object.name] = object
                
                total = 0
                for item in self.items.values():
                    total += item.weight
                if total > self.mload:
                    print("That's too much for your bag to handle!")
                    del self.items[object.name]
                    return
                    
                print(f'{object.num} {object.name} has been stored.')t
                
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
    def equip(self, gear: 'Item'):
        if gear.name not in self.items:
            print("You don't have that gear!")
            return False
        #if that section is full, say you have it on
        pass

    def unequip(self, section):
        if self.gears[section] is None:
            print('Nothing is equipped there.')
            return False
            
        if self.store(self.gears[section]) is False:
            print(f'Backpack Full! {section} cannot be unequipped!')
            return False 
        self.store(self.gears[section])
        self.gears[section] = None
        print(f'{self.gears[section].name} unequipped')
        return True
        

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
object1 = Item("Object1", 7, "Object1 desc", 10)
player.store(object1)
print(player.backpack_isFull())

