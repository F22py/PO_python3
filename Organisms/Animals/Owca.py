from Organisms.Animals.Zwierze import *


class Owca(Zwierze):
    def __init__(self, my_world, x, y):
        Zwierze.__init__(self, my_world, x, y)

        self.sila = 4
        self.inicjatywa = 4

        self.symbol = "O"
        self.title = "Owca"

        self.img = "NO"

    def create_new_organizm(self, x, y):
        return Owca(self.World, x, y)
