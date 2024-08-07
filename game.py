from random import randint
class Game:
    def __init__(self, name):
        self.n = 10
        self.e = 5
        self.x = 0, self.y = 0
        self.enemies = {}
        map = [['.'for i in range(10)]]
        player = Player(name)
    def printmap(self):
        for i in range(self.n):
            print(''.join(map[i]))

    def random_map():
        dic = {}
        for i in range(5):
            co = (randint(0, self.n-1), randint(0, self.n-1))
            if co in dic:
                i-=1
                continue
            self.enemies[co] = True

    def play():
        self.random_map()
        while (self.x!=self.n-1 and self.y!=self.n-1):
            move = input()
            if move=='w' and self.x > 0:
                self.x-=1
            elif move=='a' and self.y > 0:
                self.y+=1
            elif move=='s' and self.x < self.n:
                self.x-=1
            elif move=='d' and self.y < self.n:
                self.y-=1
            else:
                print("Invalid Move!")
                continue
            self.printmap()
            if ((self.x, self.y) in self.enemies):
                print("The ememy has been summoned!")
                if self.fight(self.enemies[(self.x, self.y)]):
                    self.lose()
                    return
        self.win()
        return


    def fight(self, enemy):
        return False

    def win(self):
        print("You have arrived safely. Well done!")
    def lose(self):
        print("Game over")
