from Organisms.Plants.Roslina import *


class Jagody(Roslina):
    def __init__(self, my_world, x, y):
        Roslina.__init__(self, my_world, x, y)

        self.sila = 99

        self.symbol = "J"
        self.title = "Jagody"

        self.img = "NO"

    def czy_odbil_atak(self, atakujacy):
        return True

    def create_new_organizm(self, x, y):
        return Jagody(self.World, x, y)

