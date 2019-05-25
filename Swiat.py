import queue

from Organisms.Animals.Zwierze import *
from Organisms.Animals.Czlowiek import *
from Organisms.Animals.Wilk import *
from Organisms.Animals.Owca import *
from Organisms.Animals.Zolw import *
from Organisms.Animals.Lis import *
from Organisms.Animals.Antylopa import *

from Organisms.OrganizmyList import *


class Swiat:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.moje_organizmy = [[None for i in range(width)] for j in range(height)]
        self.kolejkaRuchu = queue.PriorityQueue()

        self.tour_number = 0
        self.game_over = False

        self.moje_organizmy[4][4] = Wilk(self, 4, 4)
        self.moje_organizmy[2][2] = Owca(self, 2, 2)

        self.moje_organizmy[0][0] = Zolw(self, 0, 0)

        self.moje_organizmy[0][1] = Antylopa(self, 1, 0)
        self.moje_organizmy[3][1] = Lis(self, 1, 3)
    # def get_organizmy(self):
    #     return self.moje_organizmy
    #
    # def get_size(self):
    #     return self.width, self.height
    #
    # def get_tour_number(self):
    #     return self.tour_number
    #
    # def get_game_over(self):
    #     return self.game_over

    def set_czlowiek_direction_global(self, dir):
        pass

    def wykonaj_ture(self):
        if not self.game_over:
            while not self.kolejkaRuchu.empty():
                organizm = self.kolejkaRuchu.get()
                print(organizm.polozenie)
                if self.moje_organizmy[organizm.polozenie[1]][organizm.polozenie[0]] is not None:
                    organizm.tour_life += 1
                    organizm.akcja()

            self.tour_number += 1
            self.update_queue()
            self.rysuj_swiat()

    def init_organizmy(self, x, y, num):
        pass

    def zabij_organizm(self, x, y):
        if isinstance(self.moje_organizmy[y][x], Czloweik):
            pass

        self.moje_organizmy[y][x] = None

        storage = []
        while not self.kolejkaRuchu.empty():
            org = self.kolejkaRuchu.get()
            if self.moje_organizmy[org.polozenie[1]][org.polozenie[0]] is not None:
                storage.append(org)

        for organism in storage:
            self.kolejkaRuchu.put(organism)

    def try_to_activate_special(self):
        pass

    def save_game(self):
        pass

    def dodaj_na_poczatek(self):
        pass

    def update_queue(self):
        for j in range(0, self.height):
            for k in range(0, self.width):
                if self.moje_organizmy[j][k] is not None:
                    self.kolejkaRuchu.put(self.moje_organizmy[j][k])

    def rysuj_swiat(self):
        for j in range(0, self.height):
            for k in range(0, self.width):
                if self.moje_organizmy[j][k] is not None:
                    print(self.moje_organizmy[j][k].symbol, end="")
                else:
                    print("+", end="")
            print()





testing = Swiat(5, 5)

# testing.wykonaj_ture()
# print("--------------")
# testing.wykonaj_ture()
# print("--------------")
# testing.wykonaj_ture()
# print("--------------")
# testing.wykonaj_ture()

for i in range(0, 30):
    testing.wykonaj_ture()

kkk = OrganizmyList
print(kkk.size())
print(kkk.create_new_organizm(OrganizmyList.Barszcz, testing, 5, 5))

# ttt = Zwierze(testing, 5, 3)
# ttt.rozmnoz_sie()
#
# ttt5 = Zwierze(testing, 5, 10)
# ttt5.sila = 100
# ttt5.rozmnoz_sie()
# print(ttt.sila)
# print(ttt.czy_odbil_atak(ttt5))
#
# print(ttt.get_random_dir([0, 0, 0, 0]))
# print(ttt.get_direction())
# print(ttt.get_direction())
# print(ttt.get_direction())
# print(ttt.get_direction())
# print(ttt.get_direction())

# print(ttt.organizmy)
# print(testing.to_print)
# testing.test()
