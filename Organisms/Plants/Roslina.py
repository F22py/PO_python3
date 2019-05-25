from Organisms.Organizm import *


class Roslina(Organizm):
    def __init__(self, my_world, x, y):
        Organizm.__init__(self, my_world, x, y)

        self.sila = 0
        self.inicjatywa = 0

    def akcja(self, x=-1, y=-1):

        rand = random.randint(1, 100)

        if rand > 93:
            self.rozmnoz_sie()

    def kolizja(self, x, y):
        at_def = self.czy_odbil_atak(self.organizmy[y][x])

        tX = self.polozenie[0]
        tY = self.polozenie[1]

        if not at_def:
            self.World.zabij_organizm(tX, tY)
            self.organizmy[y][x].akcja(tX, tY)
        else:
            self.World.zabij_organizm(x, y)

    def czy_odbil_atak(self, atakujacy):
        return False

    def create_new_organizm(self, x, y):
        pass
