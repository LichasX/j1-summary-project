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