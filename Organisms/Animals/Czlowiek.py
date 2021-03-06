from Organisms.Animals.Zwierze import *


class Czlowiek(Zwierze):
    def __init__(self, my_world, x, y):
        Zwierze.__init__(self, my_world, x, y)

        self.sila = 5
        self.inicjatywa = 4

        self.symbol = "C"
        self.title = "Human being"

        self.color = (0, 255, 255)

        self.direction = 0
        self.special = 0

    def akcja(self, x=-1, y=-1):
        if self.direction != 0:
            self.check_special()

            coordinates = self.get_move_coord(self.direction)

            x = coordinates[0]
            y = coordinates[1]

            super(Czlowiek, self).akcja(x, y)
            self.direction = 0

    def activate_umejetnosc(self):
        if self.special == 0:
            self.special = 6
            Bob.Komentator.new_record("Specjalna umejętność " + self.title + "aktywna!")
            return True
        return False

    def check_special(self):
        if self.special > 0:
            if self.special > 3:
                self.step = 2
            else:
                rand = random.randint(1, 100)

                if rand >= 50:
                    self.step = 2
                else:
                    self.step = 1

            self.special -= 1

            if self.special == 1:
                self.end_special()

        if self.special < 0:
            self.special -= 1

        if self.special == -6:
            self.special = 0

    def end_special(self):
        self.step = 1
        self.special = -1

    def generate_data_to_save(self):
        out = super(Czlowiek, self).generate_data_to_save() + " " + str(self.special) + " " + str(self.step)
        return out



