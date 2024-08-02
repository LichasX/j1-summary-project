class Enemy:
    def __init__(self, type):
        if type == "Brute":
            self.health, self.attack, self.defense = 10, 2, 1
        else:
            self.health, self.attack, self.defense = 5, 1, 0

    def fight(self, player_obj):
        pass
