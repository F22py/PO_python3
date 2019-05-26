from Organisms.Plants.Roslina import *


class Mlecz(Roslina):
    def __init__(self, my_world, x, y):
        Roslina.__init__(self, my_world, x, y)

        self.symbol = "M"
        self.title = "Mlecz"

        self.color = (10, 55, 102)

    def akcja(self, x=-1, y=-1):
        attempts = 3
        for i in range(0, attempts):
            super(Mlecz, self).akcja()

    def create_new_organizm(self, x, y):
        return Mlecz(self.World, x, y)

