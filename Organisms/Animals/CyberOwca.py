from Organisms.Animals.Owca import *
from Organisms.Plants.Barszcz import *

import math


class CyberOwca(Owca):
    def __init__(self, my_world, x, y):
        Owca.__init__(self, my_world, x, y)

        self.sila = 11
        self.inicjatywa = 4

        self.symbol = "Q"
        self.title = "CyberOwca"

        self.color = (153, 102, 153)

        self.target = None

        self.find_barszcz()

    #           3    4      2     1
    # direction (UP, DOWN , LEFT, RIGHT)
    def akcja(self, x=-1, y=-1):
        if self.target is None:
            self.find_barszcz();
            super(CyberOwca, self).akcja()
        else:
            delta_x = self.polozenie[0] - self.target.polozenie[0]
            delta_y = self.polozenie[1] - self.target.polozenie[1]
            coord = [0, 0]
            if delta_x > 0:
                coord = self.get_move_coord(2)
            elif delta_x < 0:
                coord = self.get_move_coord(1)
            elif delta_y > 0:
                coord = self.get_move_coord(3)
            elif delta_y < 0:
                coord = self.get_move_coord(4)
            if coord != [0, 0]:
                super(CyberOwca, self).akcja(coord[0], coord[1])
            else:
                self.target = None
                self.akcja()

    def find_barszcz(self):
        barszcz_list = []
        for i in range(0, self.World.height):
            for k in range(0, self.World.width):
                if isinstance(self.organizmy[i][k], Barszcz):
                    barszcz_list.append(self.organizmy[i][k])
        # dist = math.sqrt((self.World.width - self.polozenie[0]) ** 2 + (self.World.height - self.polozenie[1]) ** 2)
        dist = self.World.width * self.World.height
        for org in barszcz_list:
            org_dist = abs(org.polozenie[0]-self.polozenie[0]) + abs(org.polozenie[1]-self.polozenie[1])
            if org_dist < dist:
                dist = org_dist
                self.target = org

    def create_new_organizm(self, x, y):
        return CyberOwca(self.World, x, y)
