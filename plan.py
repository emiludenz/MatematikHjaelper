from sympy import Symbol
from math import sqrt
from Vector3D import Vector3D as V3

class Plan:
    def __init__(self, ligning):
        x = Symbol("x")
        y = Symbol("y")
        z = Symbol("z")
        self.ligning = eval(ligning)


    def afstand_til_punkt(self, punkt):
        self.punkt = punkt
        self.bottom = self.ligning.coeff("x")**2+self.ligning.coeff("y")**2+self.ligning.coeff("z")**2


        self.lig = self.ligning.replace("x", self.punkt[0])
        self.lig = self.lig.replace("y", self.punkt[1])
        self.lig = self.lig.replace("z", self.punkt[2])

        self.top = self.lig
        self.dist = round(self.top/sqrt(self.bottom),2)


    def get(self, v=False):
        print("Ligningen: {0} ;\tAfstand til Punktet{2} er {1}".format(self.ligning,self.dist,self.punkt))
        if v:
            print("\n{}".format(self.top))
            breaker = 10 * "_"
            print("{} = {}".format(breaker,self.dist))

            print("sqrt({})".format(self.bottom))

        print("\n")


def planens_parameterfrem(vec1,vec2,vec3):
    u = vec1.sub(vec2)
    v = vec1.sub(vec3)

    print("(x,y,z)={0}+s{1}+t{2}, s,t € R".format(vec1.get(),u.get(),v.get()))

def kuglens_ligningen_punkt(centrum,punkt,radius=0):
    if radius == 0:
        v1 = V3(punkt[0], punkt[1], punkt[2])
        v2 = V3(centrum[0], centrum[1], centrum[2])
        v=v1.sub(v2)
        radius = v.lengde()


    print("x-{})**2+(y-{})**2+(z-{})**2".format(c[0],c[1],c[2]))

