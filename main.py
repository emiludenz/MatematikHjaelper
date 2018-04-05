import Vector3D as V3D
from math import sqrt as sq
import Vectors as V
#import opgaver
#import GraphFun as GF
#import functions as Fun
#from sympy import Symbol


def main():
    """
    v1 = V3D.Vector3D(1,2,-3)
    v2 = V3D.Vector3D(-3,12,-8)
    print(v1.vinkel(v2))

    v1 = V3D.Vector3D(-7,1,-3)
    v2 = V3D.Vector3D(-3,0,7)
    print(v1.vinkel(v2))

    v1 = V3D.Vector3D(4,2,-3)
    v2 = V3D.Vector3D(0,-9,6)
    print(v1.vinkel(v2))

    v1 = V3D.Vector3D(4, 2, -3)
    v2 = V3D.Vector3D(0, -9, 6)
    v3=v1.krydsprodukt(v2)
    print(v3.out())
    """

    v1 = V3D.Vector3D(-1,-4,-6)
    v2 = V3D.Vector3D(5,-1,8)
    print(v1.areal_parallellogram(v2))


    v1 = V3D.Vector3D(1,-2,-2)
    v2 = V3D.Vector3D(-3,0,8)
    print(v1.areal_parallellogram(v2))


    v1 = V3D.Vector3D(1,7,-5)
    v2 = V3D.Vector3D(3,10,-7)
    print(v1.areal_parallellogram(v2))

    print("Heeey")

    return 0

if __name__ == "__main__":
    main()