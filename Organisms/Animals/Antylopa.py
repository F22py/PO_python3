from Organisms.Animals.Zwierze import *


class Antylopa(Zwierze):
    def __init__(self, my_world, x, y):
        Zwierze.__init__(self, my_world, x, y)

        self.sila = 4
        self.inicjatywa = 4

        self.step = 2

        self.symbol = "A"
        self.title = "Antylopa"

        self.color = (255, 255, 0)

    def create_new_organizm(self, x, y):
        return Antylopa(self.World, x, y)

    def kolizja(self, x, y):
        rand = random.randint(1, 100)
        if rand >= 50:
            mozliwosci = self.find_free_place()

            direction = self.get_random_dir(mozliwosci)

            if direction != -1:
                coordinates = self.get_move_coord(direction)

                new_x = coordinates[0]
                new_y = coordinates[1]

                super(Antylopa, self).akcja(new_x, new_y)

            else:
                super(Antylopa, self).kolizja(x, y)
        else:
            super(Antylopa, self).kolizja(x, y)
