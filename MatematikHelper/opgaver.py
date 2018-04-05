import Vectors as V
from sympy import *
import matplotlib.pyplot as pli
import math
def get_t(vecAx,vecAy, vecBx,vecBy):
    #Get sovler to work

    t = Symbol("t")
    s = solve((vecAx) * (vecBx) + (vecAy) * (vecBy),t)
    return s


def opgave1():
    # Opgaver på side s34-35.
    a = V.Vector2D(4, 2)
    b = V.Vector2D(-1, -1)
    print("Øvelse 1.20 a) {}".format(a.scaler(b)))

    a = V.Vector2D(5, 2)
    b = V.Vector2D(4, 1)
    s = V.Angel(a.scaler(b))
    print("Øvelse 1.21 a) Skalar product: {} Det er en: {}".format(s.v, s.what_kind()))

    # ______________________________
    t = Symbol("t")
    print("Øvelse 1.24 {}".format(get_t(3*t+12,t**2+t-12,t-3,-1)))

    a = V.Vector2D(4, 1)
    b = V.Vector2D(1, 4)
    a2 = V.Vector2D(1, 2)
    b2 = V.Vector2D(-5, -2)
    print("Øvelse 1.25 a) {}\nØvelse 1.25 b) {}".format(a.get_angel(b), a2.get_angel(b2)))

def opgave2():
    print("Side 311\nOpgave 1.3")
    a = V.Vector2D(2,1)
    b = V.Vector2D(3,-2)
    c = V.Vector2D(-6,-3)
    d = V.Vector2D(1,float(-2/3))
    vectors = [a,b,c,d]
    names = ["a","b","c","d"]
    n = 0
    for v in vectors:
        print("Vektor {} har vinkelen {}'".format(names[n],round(v.get_angel(),2)))
        n += 1

    # Show vectors
    #V.show_vectors(vectors)

    n = 0
    a = V.Vector2D(1, 1)
    b = V.Vector2D(-3, -4)
    c = V.Vector2D(math.sqrt(3), math.sqrt(4))
    d = V.Vector2D(-5,-12)
    vectors = [a, b, c, d]
    print("\nOpgave 1.4")
    for v in vectors:
        print("Vektoren {} har længden {}".format(names[n],round(v.length(),2)))
        n += 1


    a = V.Vector2D(1, -1)
    a1 = V.Vector2D(2, 3)
    b = V.Vector2D(-3, 2)
    b1 = V.Vector2D(6, 1)
    c = V.Vector2D(1,-1)
    c1 = V.Vector2D(2,2)


    vectors = [a, b, c]
    vec = [a1, b1, c1]
    
    print("\nOpgave 1.16")
    n = 0
    for v in vectors:
        print("Vektoren a og b har vinklen {}".format(round(v.get_angel(vec[n]), 2)))
        n += 1

    a = V.Vector2D(1, 1)
    a1 = V.Vector2D(2, 3)
    b = V.Vector2D(-1, 4)
    b1 = V.Vector2D(3, 3)
    c = V.Vector2D(2, 2)
    c1 = V.Vector2D(-6, -6)
    vectors = [a, b, c]
    vec = [a1, b1, c1]

    n = 0
    print("Opgave 1.20\n")
    for v in vectors:

        print("Vektoren a og b har determinanten {}".format(round(v.determinant(vec[n]), 2)))
        n += 1

    print("\nOpgave 1.18\n")
    a = V.Vector2D(1, 1)
    a1 = V.Vector2D(2, 3)
    b = V.Vector2D(-1, 4)
    b1 = V.Vector2D(3, 3)
    c = V.Vector2D(2, 2)
    c1 = V.Vector2D(-6, -6)
    vectors = [a, b, c]
    vec = [a1, b1, c1]
    n = 0

    for v in vectors:

        print("Vektoren a projekteret på b = {} og {}".format(v.projektering(vec[n]).x,v.projektering(vec[n]).y))

        n += 1
