import queue

from Organisms.Animals.Zwierze import *
from Organisms.Animals.Czlowiek import *

class Swiat:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.to_print = 77

        self.moje_organizmy = [[None for i in range(width)] for j in range(height)]
        self.kolejkaRuchu = queue.PriorityQueue()

        self.tour_number = 0
        self.game_over = False

        self.moje_organizmy.append(Zwierze(self, 8, 8))


    def test(self):

        for i in range(0, 4):
            self.kolejkaRuchu.put(Zwierze(self, i, i))

        # self.__kolejkaRuchu.put(Organizm(8))
        # self.__kolejkaRuchu.put(Organizm(0))

        # print(self.__kolejkaRuchu.empty())

        while self.kolejkaRuchu.empty() is not True:
            ttt = self.kolejkaRuchu.get()
            print(ttt.num)

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
        pass

    def init_organizmy(self, x, y, num):
        pass

    def zabij_organizm(self, x, y):
        if isinstance(self.moje_organizmy[y][x], Czloweik):
            pass

        # self.kolejkaRuchu.get
        self.moje_organizmy[y][x] = None

    def try_to_activate_special(self):
        pass

    def save_game(self):
        pass

    def dodaj_na_poczatek(self):
        pass

    def update_queue(self):
        pass

    def rysuj_swiat(self):
        pass




testing = Swiat(20, 20)

ttt = Zwierze(testing, 5, 3)
ttt.rozmnoz_sie()

ttt5 = Organizm(testing, 5, 10)
ttt5.rozmnoz_sie()

print(ttt.check_organizm(ttt, ttt5))

print(ttt.get_random_dir([0, 0, 0, 0]))
# print(ttt.get_direction())
# print(ttt.get_direction())
# print(ttt.get_direction())
# print(ttt.get_direction())
# print(ttt.get_direction())

# print(ttt.organizmy)
# print(testing.to_print)
# testing.test()
