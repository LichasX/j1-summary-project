import time

import character


def player_combat(player: character.Player, enemy: character.Enemy) -> bool | int:
    print("\n")
    time.sleep(0.5)
    crit = 1  #if there is no crit does not change

    if player.gears["weapon"].crit():
        crit = 2  # double the damage when it crits

    damage = (player.gears['weapon'].attack + player.attack -
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

def enemy_combat(enemy: character.Enemy, player: character.Player) -> bool | int:
    print("\n")
    time.sleep(0.5)
    damage = (enemy.attack - player.defense)  #enemy doesn't crit
    
    if damage < 0:
        damage = 1
    
    player.health -= damage  #lose health
    
    print(f"You received {damage} damage from the {enemy.name}."
          )  #print damage to player
    
    print(f"{player.name} current health:{player.health}")  #print hp left
    
    if player.health <= 0:
        player.health = 0
        print("You fainted. Skill Issue.")
        return -1
    else:
        return False

def boss_combat(boss: character.Boss, player: character.Player) -> bool | int:
    print("\n")
    time.sleep(0.5)
    damage = (boss.attack - player.defense)  #enemy doesn't crit

    if damage < 0:
        damage = 1

    player.health -= damage  #lose health

    print(f"You received {damage} damage from the {boss.name}."
          )  #print damage to player

    print(f"{player.name} current health:{player.health}")  #print hp left

    if player.health <= 0:
        player.health = 0
        print("You fainted. Skill Issue.")
        return -666
    else:
        return False

def combat(attacker, defender):
    crit = 1  #if there is no crit does not change
    if isinstance(attacker, character.Player) and attacker.gears["weapon"].crit():
        crit = 2
    damage = (attacker.gears['weapon'].attack + attacker.attack -           defender.defense) * crit
    if damage <= 0:
        damage = 1

    defender.health -= damage

    print(f"{attacker} dealt {damage} damage to {defender}.")

    print(f"{defender} current health: {defender.health}")

    if defender.health <= 0:
        defender.health = 0
        print(f"{defender} fainted.")
        if isinstance(defender, Boss):
            return -888
        if isinstance(defender, character.Player):
            defender.health = 0
            print("You fainted. Skill Issue.")
            return -666
        return True
    else:
        return False
