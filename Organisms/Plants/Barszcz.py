from Organisms.Plants.Roslina import *


class Barszcz(Roslina):
    def __init__(self, my_world, x, y):
        Roslina.__init__(self, my_world, x, y)

        self.symbol = "B"
        self.title = "Barszcz"

        self.img = "NO"

    def akcja(self, x=-1, y=-1):
        tX = self.polozenie[0]
        tY = self.polozenie[1]

        w_w = self.World.width
        w_h = self.World.height

        krok = self.step

        if tX > 0:
            if self.organizmy[tY][tX - krok] is not None:
                self.World.zabij_organizm(tX - krok, tY)

        if tX < w_w - 1:
            if self.organizmy[tY][tX + krok] is not None:
                self.World.zabij_organizm(tX + krok, tY)

        if tY > 0:
            if self.organizmy[tY - krok][tX] is not None:
                self.World.zabij_organizm(tX, tY - krok)

        if tY < w_h - 1:
            if self.organizmy[tY + krok][tX] is not None:
                self.World.zabij_organizm(tX, tY + krok)

    def czy_odbil_atak(self, atakujacy):
        return True

    def create_new_organizm(self, x, y):
        return Barszcz(self.World, x, y)
