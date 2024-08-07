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

#Potion list
lesser_healing_potion = Potions(["Heals 2 hp to the player", 2])
normal_healing_potion = ["Heals 5 hp to the player", 5]
greater_healing_potion = ["Heals 10 hp to the player ", 10]
supreme_healing_potion = ["Heals 20 hp to the player", 20]

strength_potion = Potions(["Add 10 att to the player's strength stats", 10])
speed_potion = Potions(["Add 5 speed to the player's speed stats", 5])
almond_potion = Potions(["Add 2 to each of the player's stat"])

bleach = Potions(["Kills you instantly, toddler approved!", -9999999999999])