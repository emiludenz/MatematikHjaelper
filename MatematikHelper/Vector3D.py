from math import sqrt as sq
from math import acos, degrees

class Vector3D:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.vec = (self.x, self.y,self.z)

    def out(self):
        print("x:{}  y:{}  z:{}".format(self.x,self.y,self.z))

    def add(self,vec=0):
        if vec == 0:
            other_vec = Vector3D()
        else:
            other_vec = vec
        x = self.x + other_vec.x
        y = self.y + other_vec.y
        z = self.z + other_vec.z
        return Vector3D(x,y,z)

    def sub(self, vec=0):
        if vec == 0:
            other_vec = Vector3D()
        else:
            other_vec = vec
        x = self.x - other_vec.x
        y = self.y - other_vec.y
        z = self.z - other_vec.z
        return Vector3D(x, y, z)

    def skaler_produkt(self,vec=0):
        if vec == 0:
            other_vec = Vector3D()
        else:
            other_vec = vec
        x = self.x * other_vec.x
        y = self.y * other_vec.y
        z = self.z * other_vec.z
        return x+y+z

    def lengde(self):
        lengde = (self.x**2)+(self.y**2)+(self.z**2)
        return sq(lengde)

    def areal_parallellogram(self, vec=0):
        if vec == 0:
            other_vec = Vector3D()
        else:
            other_vec = vec
        v3 = self.krydsprodukt(other_vec)
        return v3.lengde()

    def vinkel(self,vec=0):
        if vec == 0:
            other_vec = Vector3D()
        else:
            other_vec = vec
        # skalar produktet
        skalar_p = self.skaler_produkt(other_vec)
        # længden af de to vektorer
        lengde_p = self.lengde()*other_vec.lengde()
        return degrees(acos(skalar_p/lengde_p))

    def krydsprodukt(self,vec=0):
        if vec == 0:
            other_vec = Vector3D()
        else:
            other_vec = vec

        x = self.y*other_vec.z - self.z*other_vec.y
        y = (self.x*other_vec.z - self.z*other_vec.x)*-1
        z = self.z*other_vec.x - self.y*other_vec.x
        return Vector3D(x,y,z)