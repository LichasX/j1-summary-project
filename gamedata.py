import json

with open("gamedata.json", "r") as f:
    _data = json.load(f)

boss = _data["boss"]
enemy = _data["enemy"]