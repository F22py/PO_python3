from Organisms.Animals.Zwierze import *


class Zolw(Zwierze):
    def __init__(self, my_world, x, y):
        Zwierze.__init__(self, my_world, x, y)

        self.sila = 2
        self.inicjatywa = 1

        self.symbol = "Z"
        self.title = "Zolw"

        self.img = "NO"

    def create_new_organizm(self, x, y):
        return Zolw(self.World, x, y)

    def akcja(self, x=-1, y=-1):
        rand = random.randint(1, 100)
        if rand < 25:
            super(Zolw, self).akcja()
