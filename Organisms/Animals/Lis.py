from Organisms.Animals.Zwierze import *


class Lis(Zwierze):
    def __init__(self, my_world, x, y):
        Zwierze.__init__(self, my_world, x, y)

        self.sila = 3
        self.inicjatywa = 7

        self.symbol = "L"
        self.title = "Lis"

        self.img = "NO"

    def create_new_organizm(self, x, y):
        return Lis(self.World, x, y)

    def akcja(self, x=-1, y=-1):
        coordinates = self.get_move_coord()

        x = coordinates[0]
        y = coordinates[1]

        tX = self.polozenie[0]
        tY = self.polozenie[1]

        if self.organizmy[y][x] is None:
            super(Lis, self).akcja(x, y)
        else:
            if self.sila > self.organizmy[y][x].sila:
                self.organizmy[y][x].kolizja(tX, tY)
