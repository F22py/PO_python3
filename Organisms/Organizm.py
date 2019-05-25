import random

class Organizm:
    def __init__(self, my_world, x, y):
        self.sila = 0
        self.inicjatywa = 0
        self.polozenie = []

        self.symbol = ""
        self.title = ""
        self.img = ""

        self.tour_life = 0
        self.step = 1
        self.alive = True

        self.World = my_world
        self.polozenie.append(x)
        self.polozenie.append(y)

        self.organizmy = self.World.moje_organizmy

    def __lt__(self, other):
        return self.tour_life > other.tour_life

    def generate_data_to_save(self):
        pass

    def akcja(self):
        pass

    def akcja(self, x, y):
        pass

    def kolizja(self, x, y):
        pass

    def get_direction(self):
        return random.randint(1, 4)

    def get_random_dir(self, seq):
        random.choice(seq)
        return random.choice(seq)





