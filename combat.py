import random

import character


def is_crit(critc: int, sides: int = 100) -> bool:
    """Simulates a dice roll to determine if the attack will crit."""
    assert sides > 0, "sides must be greater than 0"
    x = random.randint(1, sides)
    return (x < critc)


def calculate_damage(attacker: character.Combatant,
                     defender: character.Combatant) -> int:
    multiplier = 1
    if is_crit(attacker.get_crit_chance()):
        multiplier = 2
    attacker_attack = attacker.get_weapon_attack() + attacker.attack
    damage = (attacker_attack - defender.defense) * multiplier
    if damage <= 0:
        damage = 1
    return damage


def single_attack(attacker: character.Combatant, defender: character.Combatant):
    damage = calculate_damage(attacker, defender)
    defender.take_damage(damage)

    print(f"{attacker} dealt {damage} damage to {defender}.")

    print(f"{defender} current health: {defender.health}")

    if defender.is_dead():
        print(f"{defender} fainted.")
        if isinstance(defender, character.Boss):
            return -888
        if isinstance(defender, character.Player):
            print("You fainted. Skill Issue.")
            return -666
        return True
    else:
        return False
