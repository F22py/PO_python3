from Organisms.Animals.Antylopa import *
from Organisms.Animals.Lis import *
from Organisms.Animals.CyberOwca import *
from Organisms.Animals.Wilk import *
from Organisms.Animals.Zolw import *

from Organisms.Plants.Barszcz import *
from Organisms.Plants.Guarana import *
from Organisms.Plants.Jagody import *
from Organisms.Plants.Mlecz import *
from Organisms.Plants.Trawa import *

from enum import Enum


class OrganizmyList(Enum):
    Zolw = 1
    Wilk = 2
    Jagody = 3
    Trawa = 4
    Owca = 5
    Mlecz = 6
    Guarana = 7
    Barszcz = 8
    Antylopa = 9
    Lis = 10
    CyberOwca = 11

    Z = 1
    W = 2
    J = 3
    T = 4
    O = 5
    M = 6
    G = 7
    B = 8
    A = 9
    L = 10
    Q = 11

    @staticmethod
    def size():
        counter = 0
        for i in OrganizmyList:
            counter += 1
        return counter

    @staticmethod
    def create_new_organizm(val, world, x, y):
        if val == OrganizmyList.Zolw:
            return Zolw(world, x, y)
        elif val == OrganizmyList.Wilk:
            return Wilk(world, x, y)
        elif val == OrganizmyList.Jagody:
            return Jagody(world, x, y)
        elif val == OrganizmyList.Trawa:
            return Trawa(world, x, y)
        elif val == OrganizmyList.Owca:
            return Owca(world, x, y)
        elif val == OrganizmyList.Mlecz:
            return Mlecz(world, x, y)
        elif val == OrganizmyList.Guarana:
            return Guarana(world, x, y)
        elif val == OrganizmyList.Barszcz:
            return Barszcz(world, x, y)
        elif val == OrganizmyList.Antylopa:
            return Antylopa(world, x, y)
        elif val == OrganizmyList.Lis:
            return Lis(world, x, y)
        elif val == OrganizmyList.CyberOwca:
            return CyberOwca(world, x, y)
