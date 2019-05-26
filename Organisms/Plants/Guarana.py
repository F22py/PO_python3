from Organisms.Plants.Roslina import *


class Guarana(Roslina):
    def __init__(self, my_world, x, y):
        Roslina.__init__(self, my_world, x, y)

        self.symbol = "G"
        self.title = "Guarana"

        self.color = (255, 0 , 0)

    def kolizja(self, x, y):
        self.organizmy[y][x].sila *= 3
        super(Guarana, self).kolizja(x, y)

    def create_new_organizm(self, x, y):
        return Guarana(self.World, x, y)