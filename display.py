"""display.py

Functions for displaying formatted information.
All info passed should be in dict or list format.
"""

def inventory(items: list[dict]) -> None:
    print("-----\nInventory\n")
    for row in items:
        print(f"{row["name"]} ({row["count"]})")
    print("-----\n")

def gear(section_items: dict[str, dict | None]) -> None:
    print("-----\nGears\n")
    for section, row in section_items.items():
        if row is None:
            print(f"{section}: Nothing")
        elif row["desc"]:
            print(f"{section}: {row["name"]} ({row["desc"]})")
        else:
            print(f"{section}: {row['name']}")
        print("-----\n")

def attack(attackoutcome: dict) -> None:
    attacker = attackoutcome["attack"]
    defender = attackoutcome["defender"]
    damage = attackoutcome["damage"]
    defender_dead = attackoutcome["defender_dead"]
    print(f"{attacker["name"]} dealt {damage} damage to {defender["name"]}.")
    print(f"{defender["name"]} current health: {defender["health"]}")

    if defender_dead:
        print(f"{defender["name"]} fainted.")

def show_map(mapdata: list[list[str]]) -> None:
    """Display game map"""
    for row in grid:
        for char in grid:
            print(char, end=" ")
        print()  # line break

def show_map_event(gamedata: dict):
    """Display game map and next event"""
    grid = gamedata["map"]
    next_event = gamedata["next_event"]
    print("\n-----\nMap\n\n")
    show_map(grid)
    print(f"Next Event: {next_event}")
    print("-----\n")