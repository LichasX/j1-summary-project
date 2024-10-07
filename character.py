import time

import item

Status = int
OK = 1
ERROR = 0

Result = tuple[Status, str]


class Slot:
    """A slot in inventory stores one item type alongside a count"""

    def __init__(self,
                 item: item.Item,
                 limit: int | None = None,
                 count: int = 0):
        self.item = item
        self.count = count
        self.limit = limit

    def __str__(self) -> str:
        """Name of item"""
        return f"{self.item.name} ({self.count})"

    def is_empty(self) -> bool:
        return self.count == 0

    def add(self, count: int = 1) -> Result:
        """Adds count to slot.
        Returns True if successful, otherwise False.
        """
        status, msg = self.can_add(count)
        if status == ERROR:
            return status, msg
        self.count += count
        return (OK, f"{count} {self.item.name} added.")

    def can_add(self, count: int = 1) -> Result:
        """Returns True if there is space in the slot for count items"""
        if self.limit is None:
            return (OK, "Item can be added")
        if self.count + count > self.limit:
            return (ERROR, f"Cannot hold more than {self.limit} item(s)")
        return (OK, "Item can be added")

    def remove(self, count: int = 1) -> Result:
        """Removes count from slot.
        Returns True if successful, otherwise False.
        """
        if self.count < count:
            return (ERROR, f"There are fewer than {count} item(s)")
        self.count -= count
        return (OK, f"{count} {self.item.name} removed.")

    def gross_weight(self) -> int:
        """Gross weight of slot"""
        return self.item.weight * self.count

    def json(self) -> dict:
        """Returns a JSON-serializable dict"""
        return {"name": self.item.name, "count": self.count}


class GearSlot(Slot):

    def __init__(self, item: item.Item, limit: int = 1, count: int = 0):
        super().__init__(item, limit, count)

    def json(self) -> dict:
        """Returns a JSON-serializable dict"""
        return {"name": self.item.name, "desc": self.item.desc}


class Inventory:

    def __init__(self, weight_limit: int):
        self.slots = {}
        self.weight_limit = weight_limit

    def __getitem__(self, name: str) -> Slot:
        return self.slots[name]

    def get(self, name: str, default=None) -> item.Item:
        return self.slots.get(name, default)

    def items(self):
        return self.slots.items()

    def keys(self):
        return self.slots.keys()

    def values(self):
        return self.slots.values()

    def gross_weight(self) -> int:
        """Gross weight of inventory"""
        return sum(slot.gross_weight() for slot in self.slots.values())

    def can_store(self, item: item.Item, count: int = 1) -> Result:
        """Returns True if inventory can store item with count"""
        if self.gross_weight() + item.weight * count > self.weight_limit:
            return (ERROR, "Will exceed backpack capacity")
        if item.name not in self.slots:
            return (OK, "Item can be stored")
        return self.slots[item.name].can_add(count)

    def has(self, item: item.Item) -> bool:
        """Returns True if inventory contains item, otherwise False"""
        return item.name in self.slots and not self.slots[item.name].is_empty()

    def is_empty(self) -> bool:
        """Returns True if inventory is empty, otherwise False"""
        return len(self.slots) == 0

    def is_full(self) -> bool:
        """Returns True if inventory is full, otherwise False"""
        return self.gross_weight() >= self.weight_limit

    def store(self, item: item.Item) -> Result:
        """Add item to inventory.
        Returns True if successful, otherwise False.
        """
        if item.name not in self.slots.keys():
            self.slots[item.name] = Slot(item)
        status, msg = self.slots[item.name].add(1)
        if status == ERROR:
            if self.slots[item.name].is_empty():
                del self.slots[item.name]
        return status, msg

    def trash(self, item: item.Item) -> Result:
        """Remove item from inventory"""
        if not self.has(item):
            return (ERROR, f"No {item.name} in backpack")
        status, msg = self.slots[item.name].remove(1)
        if status == OK and self.slots[item.name].is_empty():
            del self.slots[item.name]
        return status, msg

    def json(self) -> list[dict]:
        """Returns a JSON-serializable list of dicts"""
        return [slot.json() for slot in self.slots.values()]


class Combatant:
    """Base class for all characters that can engage in combat."""
    attack: int
    defense: int
    speed: int

    def __init__(self, name: str, attack: int, defense: int, health: int,
                 speed: int):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.health = health
        self.speed = speed

    def get_crit_chance(self) -> int:
        """Combatant's chance to crit; default 0."""
        return 0

    def get_weapon_attack(self) -> int:
        """Get attack of equipped weapon; 0 if no weapon"""
        return 0

    def is_dead(self) -> bool:
        return self.health <= 0

    def take_damage(self, damage: int) -> None:
        """Subtracts damage from health.
        Health cannot go below 0.
        """
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def json(self) -> dict:
        """Returns a JSON-serializable dict"""
        return {
            "name": self.name,
            "attack": self.attack,
            "defense": self.defense,
            "health": self.health,
            "speed": self.speed
        }


class Player(Combatant):

    def __init__(self, name: str, attack: int, defense: int, health: int, speed: int, max_load: int):
        super().__init__(name, attack=1, defense=0, health=10, speed=1)
        self.max_health = self.health
        max_load = max_load
        self.items = Inventory(weight_limit=max_load)
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
        return self.items.is_full()

    def store(self, object):
        status, msg = self.items.store(object)
        print(msg)
        return (status == OK)

    def json_inventory(self):
        return self.items.json()

    def json_gear(self):
        return {section: slot.json() for section, slot in self.gears.items()}

    def get_item(self, name: str) -> item.Item | None:
        return self.items.get(name)

    def get_gear(self, section: str) -> item.Item | None:
        return self.gears.get(section) and self.gears[section].item

    def trash(self, item: item.Item):
        status, msg = self.items.trash(item)
        print(msg)
        return (status == OK)

    #Gears
    def equip(self, gear: item.Weapon | item.Armor) -> bool:
        if not self.items.has(gear):
            print("You don't have that gear!")
            return False
        status, msg = self.gears[gear.section].add(1)
        if status == ERROR:
            print(f'You already have a {gear.section} equipped.')
            return False
        status, msg = self.items.trash(gear)
        if status == ERROR:
            print(msg)
            self.gears[gear.section].remove(1)
            return False
        self.gears[gear.section].item = gear
        return True

    def unequip(self, section: str) -> bool:
        gear = self.gears[section].item
        status, msg = self.items.store(gear)
        if status == ERROR:
            print(msg)
            return False
        status, msg = self.gears[section].remove(1)
        if status == ERROR:
            print(msg)
            self.items.trash(gear)
            return False
        print(f'{gear.name} unequipped')
        return True


class Enemy(Combatant):

    def __repr__(self):
        return "E"


class Boss(Enemy):

    def __repr__(self):
        return "B"
