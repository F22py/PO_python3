import random

class Organizm:
    def __init__(self, my_world, x, y):
        self.sila = 0
        self.inicjatywa = 0
        self.polozenie = []

        self.symbol = ""
        self.title = ""
        self.img = ""
        self.color = (0, 0, 0)

        self.tour_life = 0
        self.step = 1
        # self.alive = True

        self.World = my_world
        self.polozenie.append(x)
        self.polozenie.append(y)

        self.organizmy = self.World.moje_organizmy

    def __lt__(self, other):
        if self.inicjatywa == other.inicjatywa:
            return self.tour_life > other.tour_life

        return self.inicjatywa > other.inicjatywa

    def generate_data_to_save(self):
        pass

    def akcja(self, x=-1, y=-1):
        pass

    # def akcja(self, x, y):
    #     pass

    def kolizja(self, x, y):
        pass

    def create_new_organizm(self, x, y):
        pass

    def czy_odbil_atak(self, atakujacy):
        pass

    def get_direction(self):
        return random.randint(1, 4)

    def get_random_dir(self, seq):
        zeroes = 0
        direction = -1

        for i in seq:
            if i == 0:
                zeroes += 1

        if zeroes == 4:
            return direction
        else:
            running = True
            while running:
                direction = random.choice(seq)
                if direction > 0:
                    running = False

        return direction

    def get_move_coord(self, direction=0):
        coordinates = [0, 0]

        if direction == 0:
            direction = self.get_direction()

        if direction == 1:
            coordinates = self.set_new_position(1, 0, self.step)
        elif direction == 2:
            coordinates = self.set_new_position(-1, 0, self.step)
        elif direction == 3:
            coordinates = self.set_new_position(0, 1, self.step)
        elif direction == 4:
            coordinates = self.set_new_position(0, -1, self.step)

        return coordinates

    def set_new_position(self, x, y, distance):
        w_width = self.World.width
        w_height = self.World.height

        new_coordinates = [0, 0]

        if x == 1 and y == 0:
            new_coordinates[0] = self.polozenie[0] + distance
            new_coordinates[1] = self.polozenie[1]
        elif x == -1 and y == 0:
            new_coordinates[0] = self.polozenie[0] - distance
            new_coordinates[1] = self.polozenie[1]
        elif x == 0 and y == 1:
            new_coordinates[0] = self.polozenie[0]
            new_coordinates[1] = self.polozenie[1] - distance
        elif x == 0 and y == -1:
            new_coordinates[0] = self.polozenie[0]
            new_coordinates[1] = self.polozenie[1] + distance

        if new_coordinates[0] >= w_width:
            new_coordinates[0] -= 2 * distance

        if new_coordinates[0] < 0:
            new_coordinates[0] += 2 * distance

        if new_coordinates[1] >= w_height:
            new_coordinates[1] -= 2 * distance

        if new_coordinates[1] < 0:
            new_coordinates[1] += 2 * distance

        return new_coordinates

    def set_new_polozenie(self, x, y):
        self.polozenie[0] = x
        self.polozenie[1] = y

    def find_free_place(self):
        direction = [0, 0, 0, 0]

        tX = self.polozenie[0]
        tY = self.polozenie[1]

        step = self.step

        w_w = self.World.width
        w_h = self.World.height

        if ((tY - step) >= 0) and (self.organizmy[tY - step][tX] is None):
            direction[0] = 3

        if ((tY + step) < w_h) and (self.organizmy[tY + step][tX] is None):
            direction[1] = 4

        if ((tX - step) >= 0) and (self.organizmy[tY][tX - step] is None):
            direction[2] = 2

        if ((tX + step) < w_w) and (self.organizmy[tY][tX + step] is None):
            direction[3] = 1

        #           3    4      2     1
        # direction (UP, DOWN , LEFT, RIGHT)
        return direction

    def rozmnoz_sie(self):
        mozliwosci = self.find_free_place()

        direction = self.get_random_dir(mozliwosci)

        if direction != -1:
            coordinates = self.get_move_coord(direction)

            x = coordinates[0]
            y = coordinates[1]

            self.organizmy[y][x] = self.create_new_organizm(x, y)

    def check_organizm(self, o1, o2):
        if o1 is not None and o2 is not None:
            return type(o1) == type(o2)

        return False





