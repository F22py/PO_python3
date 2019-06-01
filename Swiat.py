import queue
import datetime

# from Organisms.Animals.Zwierze import *
# from Organisms.Animals.Wilk import *
# from Organisms.Animals.Owca import *
# from Organisms.Animals.Zolw import *
# from Organisms.Animals.Lis import *
# from Organisms.Animals.Antylopa import *


from Organisms.Animals.Czlowiek import *

from Organisms.OrganizmyList import *
import Komentator as Bob


class Swiat:
    def __init__(self, width, height, path=None):
        Bob.Komentator.clear_file()

        self.width = width
        self.height = height

        self.moje_organizmy = [[None for i in range(width)] for j in range(height)]
        self.kolejka_ruchu = queue.PriorityQueue()

        self.tour_number = 0
        self.game_over = False
        if not path:
            self.dodaj_na_poczatek()

        self.Sasha = Czlowiek(self, int(width/2), int(height/2))
        self.Sasha.title = "Sasha"
        self.moje_organizmy[int(self.height/2)][int(self.width / 2)] = self.Sasha

        if path:
            with open(path, "r") as file:
                self.width = int(file.readline())
                self.height = int(file.readline())
                self.moje_organizmy = [[None for i in range(self.width)] for j in range(self.height)]
                tour_life_max = 0
                for line in file.readlines():
                    data = line.split("\n")[0].split(" ")
                    x = int(data[1])
                    y = int(data[2])
                    if data[0] is not "C":
                        self.moje_organizmy[y][x] = \
                            OrganizmyList.create_new_organizm(OrganizmyList[data[0]], self, x, y)
                        self.moje_organizmy[y][x].sila = int(data[3])
                        self.moje_organizmy[y][x].inicjatywa = int(data[4])
                        self.moje_organizmy[y][x].tour_life = int(data[5])
                    else:
                        self.Sasha = Czlowiek(self, x, y)
                        self.Sasha.title = "Sasha"
                        self.Sasha.sila = int(data[3])
                        self.Sasha.inicjatywa = int(data[4])
                        self.Sasha.tour_life = int(data[5])
                        self.Sasha.special = int(data[6])
                        self.Sasha.stepR = int(data[7])
                        self.moje_organizmy[y][x] = self.Sasha

                    if int(data[5]) > tour_life_max:
                        tour_life_max = int(data[5])
                self.tour_number = tour_life_max

    def set_czlowiek_direction_global(self, direction):
        if self.Sasha is not None:
            self.Sasha.direction = direction
            self.wykonaj_ture()

    def wykonaj_ture(self):
        if not self.game_over:
            while not self.kolejka_ruchu.empty():
                organizm = self.kolejka_ruchu.get()
                print(organizm)
                if self.moje_organizmy[organizm.polozenie[1]][organizm.polozenie[0]] is not None:
                    organizm.tour_life += 1
                    organizm.akcja()

            self.tour_number += 1
            self.update_queue()
            # self.rysuj_swiat()

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
        title = datetime.datetime.now().strftime("%Y-%m-%d-%H.%M.%S")
        directory = "../saves/"
        path = directory + title + ".txt"
        all_games_path = directory + "games.txt"
        with open(path, "w+") as file:
            file.write(str(self.width) + "\n")
            file.write(str(self.height) + "\n")
            for i in range(0, self.height):
                for k in range(0, self.width):
                    if self.moje_organizmy[i][k] is not None:
                        file.write(self.moje_organizmy[i][k].generate_data_to_save() + "\n")
        with open(all_games_path, "a") as file:
            file.write(title + "\n")
        return True

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

            self.init_organizmy(r_x, r_y, k % 11 + 1)

    def update_queue(self):
        for j in range(0, self.height):
            for k in range(0, self.width):
                if self.moje_organizmy[j][k] is not None:
                    self.kolejka_ruchu.put(self.moje_organizmy[j][k])

    def is_cyber_owca(self, x, y):
        if isinstance(self.moje_organizmy[y][x], CyberOwca):
            return True
        return False

    def rysuj_swiat(self):
        for j in range(0, self.height):
            for k in range(0, self.width):
                if self.moje_organizmy[j][k] is not None:
                    print(self.moje_organizmy[j][k].symbol, end="")
                else:
                    print("+", end="")
            print()
        print("----------------------------------------------")





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
