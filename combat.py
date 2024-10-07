import random

import character


class AttackOutcome:

    def __init__(
        self,
        attacker: character.Combatant,
        defender: character.Combatant,
        damage: int,
        defender_dead: bool = False,
    ):
        self.attacker = attacker
        self.defender = defender
        self.damage = damage
        self.defender_dead = defender_dead

    def json(self) -> dict:
        return {
            "attacker": self.attacker.json(),
            "defender": self.defender.json(),
            "damage": self.damage,
            "defender_dead": self.defender_dead,
        }


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


def single_attack(attacker: character.Combatant,
                  defender: character.Combatant) -> AttackOutcome:
    damage = calculate_damage(attacker, defender)
    defender.take_damage(damage)
    return AttackOutcome(attacker, defender, damage, defender.is_dead())
