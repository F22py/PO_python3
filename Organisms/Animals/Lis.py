from Organisms.Animals.Zwierze import *


class Lis(Zwierze):
    def __init__(self, my_world, x, y):
        Zwierze.__init__(self, my_world, x, y)

        self.sila = 3
        self.inicjatywa = 7

        self.symbol = "L"
        self.title = "Lis"

        self.color = (255, 140, 0)

    def create_new_organizm(self, x, y):
        return Lis(self.World, x, y)

    def akcja(self, x=-1, y=-1):
        coordinates = self.get_move_coord()

        x = coordinates[0]
        y = coordinates[1]

        tX = self.polozenie[0]
        tY = self.polozenie[1]

        if self.organizmy[y][x] is None:
            super(Lis, self).akcja(x, y)
        else:
            mozliwosci = self.find_free_place()
            print(mozliwosci)

            direction = self.get_random_dir(mozliwosci)

            if direction != -1:
                coordinates = self.get_move_coord(direction)

                new_x = coordinates[0]
                new_y = coordinates[1]

                super(Lis, self).akcja(new_x, new_y)
            else:
                self.organizmy[y][x].kolizja(tX, tY)

    def find_free_place(self):
        direction = [0, 0, 0, 0]

        tX = self.polozenie[0]
        tY = self.polozenie[1]

        step = self.step

        w_w = self.World.width
        w_h = self.World.height

        if ((tY - step) >= 0) and (self.organizmy[tY - step][tX] is None
                                   or (self.organizmy[tY - step][tX].sila <= self.sila)):
            direction[0] = 3
        if ((tY + step) < w_h) and (self.organizmy[tY + step][tX] is None
                                    or (self.organizmy[tY + step][tX].sila <= self.sila)):
            direction[1] = 4

        if ((tX - step) >= 0) and (self.organizmy[tY][tX - step] is None
                                   or (self.organizmy[tY][tX - step].sila <= self.sila)):
            direction[2] = 2

        if ((tX + step) < w_w) and (self.organizmy[tY][tX + step] is None
                                    or (self.organizmy[tY][tX + step].sila <= self.sila)):
            direction[3] = 1

        #           3    4      2     1
        # direction (UP, DOWN , LEFT, RIGHT)
        return direction
