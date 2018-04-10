#import Vectors as V
import plan as pl
import Vector3D as V3


#import trekanter as Tre

#from math import sqrt as sq
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
    """
    """
    a = Tre.Trekant(10,15,21)

    a.getAngles()
    print("Vinkel C:{}\tVinkel B:{}\tVinkel A:{} ".format(a.C,a.B,a.A))
    print("Vinklerne sammenlagt: {}".format(a.A+a.C+a.B))
    va = V.Vector2D(leng=21, angle=26)
    va.x = va.x/2
    vb = V.Vector2D(10,0)

    newset= va.sub(vb)

    """
    """
    v1 = V.Vector2D(5,0)
    v2 = V.Vector2D(-2.8,6.4)

    v3 = v1.sub(v2)
    v3 = V.Vector2D(v3[0],v3[1])
    print(v3.length())

    print(v3.get_angel(v2,p=True))"""

    #v1=V.Vector2D(leng=3.9, angle=33)
    """
    print("Eks 37")
    p = pl.Plan("2*x-y-2*z+3")
    p.afstand_til_punkt((3,5,-7))
    p.get()

    print("Øvelse 1.110")
    p = pl.Plan("x-y+2*z+8")
    p.afstand_til_punkt((2,4,6))
    p.get(v=True)

    print("Øvelse 1.111")
    p = pl.Plan("3*x+2*y-2*z-2")
    p.afstand_til_punkt((3,1,1))
    p.get()

    print("Øvelse 1.112")
    p = pl.Plan("x+3*y+5*z+15")
    p.afstand_til_punkt((0,0,2))
    p.get()

    print("Eks tavle")
    p = pl.Plan("2*x-3*y+z-5")
    p.afstand_til_punkt((2, -1, 3))
    p.get(v=True)
    
    
    v1 = V3.Vector3D(3,1,-2)
    v2 = V3.Vector3D(5,6,4)
    v3 = V3.Vector3D(-2,2,1)
    p = pl.planens_parameterfrem(v1,v2,v3)


    v1 = V3.Vector3D(-1,-1,3)
    v2 = V3.Vector3D(3,-1,-2)
    v3 = V3.Vector3D(2,-5,-3)
    p = pl.planens_parameterfrem(v1, v2, v3)


    v1 = V3.Vector3D(4, 1, 0)
    v2 = V3.Vector3D(3, 2, 2)
    v3 = V3.Vector3D(1, 2, -1)
    p = pl.planens_parameterfrem(v1, v2, v3)


    v1 = V3.Vector3D(3, 0, 0)
    v2 = V3.Vector3D(-1, 4, 1)
    v3 = V3.Vector3D(-2, -2, 4)
    p = pl.planens_parameterfrem(v1, v2, v3)
    """


    p = pl.kuglens_ligningen_punkt(2,3,-1)



    return 0

if __name__ == "__main__":
    main()