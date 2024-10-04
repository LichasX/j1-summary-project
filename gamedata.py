import json

with open("gamedata.json", "r") as f:
    _data = json.load(f)

boss = _data["boss"]
enemy = _data["enemy"]
weapons = _data["weapons"]
armor = _data["armor"]
potions = _data["potions"]
