import time

import item


class Slot:
    """A slot in inventory stores one item type alongside a count"""
    def __init__(self, item, limit: int | None = None, count: int = 0):
        self.item = item
        self.count = count
        self.limit = limit

    def __str__(self) -> str:
        """Name of item"""
        return f"{self.item.name} ({self.count})"

    def is_empty(self) -> bool:
        return self.count == 0

    def add(self, count: int = 1) -> bool:
        """Adds count to slot.
        Returns True if successful, otherwise False.
        """
        if self.limit is not None and self.count + count > self.limit:
            return False
        self.count += count
        return True

    def remove(self, count: int = 1) -> bool:
        """Removes count from slot.
        Returns True if successful, otherwise False.
        """
        if self.count < count:
            return False
        self.count -= count
        return True

    def gross_weight(self) -> int:
        """Gross weight of slot"""
        return self.item.weight * self.count



class Inventory:
    def __init__(self, weight_limit: int):
        self.slots = {}
        self.weight_limit = weight_limit

    def gross_weight(self) -> int:
        """Gross weight of inventory"""
        return sum(slot.gross_weight() for slot in self.slots.values())

    def has(self, object) -> bool:
        """Returns True if inventory contains object, otherwise False"""
        return object.name in self.slots and not self.slots[object.name].is_empty()

    def store(self, object) -> bool:
        """Add object to inventory.
        Returns True if successful, otherwise False.
        """
        if object.weight + self.gross_weight > self.weight_limit:
            return False
        if object.name not in self.slots.keys():
            self.slots[object.name] = Slot(object)
        if not self.slots[object.name].add(1):
            return False
        return True

    def trash(self, object) -> bool:
        """Remove object from inventory"""
        if not self.has(object).name not in self.slots.keys():
            return False
        if not self.slots[object.name].remove(1):
            return False
        if self.slots[object.name].is_empty():
            del self.slots[object.name]
        return True


class Player:

    def __init__(self, name):
        self.name = str(name)
        self.health = 10
        self.max_health = self.health
        self.defense = 0
        self.attack = 1
        self.speed = 1
        self.coords = (0, 0)
        self.last_move = (0, 0)  #tracks the player's position last turn
        self.event_queue = None  #stores the event that the player is moving to (e.g. enemy fight)
        self.items = {}
        self.mload = 10000000000000000000000  #fuck it who cares
        self.gears = {
            'helm': Slot(None, limit=1),
            'chest': Slot(None, limit=1),
            'leg': Slot(None, limit=1),
            'boots': Slot(None, limit=1),
            'weapon': Slot(item.create_item("wooden_sword"), limit=1)
        }

    def __repr__(self):
        return "P"

    def backpack_isFull(self):
        total = 0
        for itm in self.items.values():
            total += itm.weight
        return total >= self.mload

    def store(self, object):
        if not self.backpack_isFull():
            if object.name in self.items:  #item present
                self.items[object.name].num += 1
                weight = 0
                for item in self.items.values():
                    weight += item.weight
                if weight > self.mload:
                    print("That's too much for your bag to handle!")
                    self.items[object.name].num -= object.num  #Take back item
                    return False

                print(f'1 {object.name} has been stored')
                return True

            else:  #new item
                self.items[object.name] = object

                total = 0
                for item in self.items.values():
                    total += item.weight
                if total > self.mload:
                    print("That's too much for your bag to handle!")
                    del self.items[object.name]
                    return False

                print(f'{object.num} {object.name} has been stored.')
                return True

        else:
            print("Unable to store. Backpack is full.")

    def display_inv(self):
        print("-----\nInventory\n")
        for i in self.items.keys():
            print(i, self.items[i].num)
        print("-----\n")

    def display_gears(self):
        print("-----\nGears\n")
        for i in self.gears.keys():
            print(f"{i}: {self.gears[i]}")
        print("-----\n")

    def check(self, object):
        if item in self.items.keys():
            print(f'Name: {item}')
            print(f'Amount:{self.items[item].num}')
            print(f'Description:{self.items[item].desc}')
            return True
        print('Item not in Backpack')
        return False

    def trash(self, object):
        if object.name not in self.items:
            print("Invalid object entered")
        else:
            self.items[object.name].num -= 1
            if self.items[object.name].num <= 0:
                del self.items[object.name]

    #Gears
    def equip(self, gear) -> bool:  #accepts object class
        if gear.name not in self.items:
            print("You don't have that gear!")
            return False
        #if that section is full, say you have it on

        if not self.gears[gear.section].is_empty():
            print(f'You already have a {gear.section} equipped.')
            return False
        self.gears[gear.section].item = gear
        self.gears[gear.section].add(1)
        print(f'{gear.name} is equipped')
        self.trash(gear)
        return True

    def unequip(self, section: str) -> bool:  #accepts string of equipment type
        if self.gears[section].is_empty():
            print('Nothing is equipped there.')
            return False
        if self.backpack_isFull():
            print(f'Backpack Full! {section} cannot be unequipped!')
            return False
        gear = self.gears[section].item
        self.store(gear)
        print(f'{gear.name} unequipped')
        self.gears[section].remove(1)
        return True

    def combat(self, enemy: "Enemy"):
        print("\n")
        time.sleep(0.5)
        crit = 1  #if there is no crit does not change

        if self.gears["weapon"].crit():
            crit = 2  # double the damage when it crits

        damage = (self.gears['weapon'].attack + self.attack -
                  enemy.defense) * crit

        if damage <= 0:
            damage = 1

        enemy.health -= damage

        print(f"You dealt {damage} damage to the {enemy.name}.")

        print(f"{enemy.name} current health:{enemy.health}")

        if enemy.health <= 0:
            enemy.health = 0
            print(f"{enemy} fainted.")
            if isinstance(enemy, Boss):
                return -888
            return True
        else:
            return False


class Enemy:

    def __init__(
            self,
            name: str,
            health: int,
            defense: int, 
            attack: int,
            speed: int
    ):
        self.name = name
        self.health = health
        self.defense = defense
        self.attack = attack
        self.speed = speed

    def __repr__(self):
        return "E"

    def combat(self, player: "Player"):

        print("\n")
        time.sleep(0.5)
        damage = (self.attack - player.defense)  #enemy doesn't crit

        if damage < 0:
            damage = 1

        player.health -= damage  #lose health

        print(f"You received {damage} damage from the {self.name}."
              )  #print damage to player

        print(f"{player.name} current health:{player.health}")  #print hp left

        if player.health <= 0:
            player.health = 0
            print("You fainted. Skill Issue.")
            return -1
        else:
            return False


class Boss(Enemy):

    def __repr__(self):
        return "B"

    def combat(self, player: "Player"):
        print("\n")
        time.sleep(0.5)
        damage = (self.attack - player.defense)  #enemy doesn't crit

        if damage < 0:
            damage = 1

        player.health -= damage  #lose health

        print(f"You received {damage} damage from the {self.name}."
              )  #print damage to player

        print(f"{player.name} current health:{player.health}")  #print hp left

        if player.health <= 0:
            player.health = 0
            print("You fainted. Skill Issue.")
            return -666
        else:
            return False
