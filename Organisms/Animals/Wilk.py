from Organisms.Animals.Zwierze import *


class Wilk(Zwierze):
    def __init__(self, my_world, x, y):
        Zwierze.__init__(self, my_world, x, y)

        self.sila = 9
        self.inicjatywa = 5

        self.symbol = "W"
        self.title = "Wilk"

        self.img = "NO"

    def create_new_organizm(self, x, y):
        return Wilk(self.World, x, y)
