from Organisms.Plants.Roslina import *


class Trawa(Roslina):
    def __init__(self, my_world, x, y):
        Roslina.__init__(self, my_world, x, y)

        self.symbol = "T"
        self.title = "Trawa"

        self.color = (0, 255, 0)

    def create_new_organizm(self, x, y):
        return Trawa(self.World, x, y)

