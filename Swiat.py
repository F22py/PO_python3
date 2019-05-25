import queue

# from Organisms.Animals.Zwierze import *
# from Organisms.Animals.Wilk import *
# from Organisms.Animals.Owca import *
# from Organisms.Animals.Zolw import *
# from Organisms.Animals.Lis import *
# from Organisms.Animals.Antylopa import *
from Organisms.Animals.Czlowiek import *

from Organisms.OrganizmyList import *


class Swiat:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.moje_organizmy = [[None for i in range(width)] for j in range(height)]
        self.kolejka_ruchu = queue.PriorityQueue()

        self.tour_number = 0
        self.game_over = False

        self.Sasha = Czlowiek(self, int(width/2), int(height/2))
        self.Sasha.title = "Sasha"
        self.moje_organizmy[int(height/2)][int(width/2)] = self.Sasha

        self.dodaj_na_poczatek()

        # self.moje_organizmy[4][4] = Wilk(self, 4, 4)
        # self.moje_organizmy[2][2] = Owca(self, 2, 2)
        #
        # self.moje_organizmy[0][0] = Zolw(self, 0, 0)
        #
        # self.moje_organizmy[0][1] = Antylopa(self, 1, 0)
        # self.moje_organizmy[3][1] = Lis(self, 1, 3)
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

    def set_czlowiek_direction_global(self, direction):
        if self.Sasha is not None:
            self.Sasha.direction = direction

    def wykonaj_ture(self):
        if not self.game_over:
            while not self.kolejka_ruchu.empty():
                organizm = self.kolejka_ruchu.get()
                # print(organizm.polozenie)
                if self.moje_organizmy[organizm.polozenie[1]][organizm.polozenie[0]] is not None:
                    organizm.tour_life += 1
                    organizm.akcja()

            self.tour_number += 1
            self.update_queue()
            self.rysuj_swiat()

        return not self.game_over

    def init_organizmy(self, x, y, num):
        val = OrganizmyList(num)
        self.moje_organizmy[y][x] = \
            OrganizmyList.create_new_organizm(val, self, x, y)

    def zabij_organizm(self, x, y):
        if isinstance(self.moje_organizmy[y][x], Czlowiek):
            self.Sasha = None
            self.game_over = True

        self.moje_organizmy[y][x] = None

        storage = []
        while not self.kolejka_ruchu.empty():
            org = self.kolejka_ruchu.get()
            if self.moje_organizmy[org.polozenie[1]][org.polozenie[0]] is not None:
                storage.append(org)

        for organism in storage:
            self.kolejka_ruchu.put(organism)

    def try_to_activate_special(self):
        result = False

        if self.Sasha is not None:
            result = self.Sasha.activate_umejetnosc()

        return result

    def save_game(self):
        pass

    def dodaj_na_poczatek(self):
        r_x = 0
        r_y = 0

        for k in range(0, 10 + int(self.width*self.height/10)):
            running = True
            while running:
                r_x = random.randint(0, self.width-1)
                r_y = random.randint(0, self.height-1)

                if self.moje_organizmy[r_y][r_x] is None:
                    running = False

            self.init_organizmy(r_x, r_y, k % 10 + 1)

    def update_queue(self):
        for j in range(0, self.height):
            for k in range(0, self.width):
                if self.moje_organizmy[j][k] is not None:
                    self.kolejka_ruchu.put(self.moje_organizmy[j][k])

    def rysuj_swiat(self):
        for j in range(0, self.height):
            for k in range(0, self.width):
                if self.moje_organizmy[j][k] is not None:
                    print(self.moje_organizmy[j][k].symbol, end="")
                else:
                    print("+", end="")
            print()





# testing = Swiat(5, 5)
#
# # testing.wykonaj_ture()
# # print("--------------")
# # testing.wykonaj_ture()
# # print("--------------")
# # testing.wykonaj_ture()
# # print("--------------")
# # testing.wykonaj_ture()
# for i in range(0, 40):
#     testing.wykonaj_ture()
#     print("-----------------------------------")


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
