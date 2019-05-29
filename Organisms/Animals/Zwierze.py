from Organisms.Organizm import *


class Zwierze(Organizm):
    def __init__(self, my_world, x, y):
        Organizm.__init__(self, my_world, x, y)

    def akcja(self, x=-1, y=-1):
        if x == -1 and y == -1:
            coordinates = self.get_move_coord()

            x = coordinates[0]
            y = coordinates[1]

        tX = self.polozenie[0]
        tY = self.polozenie[1]

        if self.organizmy[y][x] is None:
            self.set_new_polozenie(x, y)

            self.organizmy[y][x] = self.organizmy[tY][tX]
            self.organizmy[tY][tX] = None
        else:
            self.organizmy[y][x].kolizja(tX, tY)

    def kolizja(self, x, y):
        at_def = self.czy_odbil_atak(self.organizmy[y][x])

        tX = self.polozenie[0]
        tY = self.polozenie[1]

        same_organismy = self.check_organizm(self.organizmy[y][x], self.organizmy[tY][tX])

        if not same_organismy:
            if not at_def:
                Bob.Komentator.new_record(self.organizmy[y][x].title + " zabił " + self.organizmy[tY][tX].title)
                self.World.zabij_organizm(tX, tY)
                self.organizmy[y][x].akcja(tX, tY)
            else:
                Bob.Komentator.new_record(self.organizmy[tY][tX].title + " zabił " + self.organizmy[y][x].title)
                self.World.zabij_organizm(x, y)
        else:
            self.rozmnoz_sie()

    def czy_odbil_atak(self, atakujacy):
        return self.sila > atakujacy.sila

    def create_new_organizm(self, x, y):
        pass
