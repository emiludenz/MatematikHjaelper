import Vector3D as V3D
#import Vectors as V
#import opgaver
#import GraphFun as GF
#import functions as Fun
#from sympy import Symbol


def main():
    # a(3t-1,12)
    # b(6,t+8)
    #opgaver.opgave1()
    """
    print("__________Example______________")
    a = V.Vector2D(1,6)
    b = V.Vector2D(5,2)
    c = a.projektering(b)
    print("X:{}\nY:{}".format(c.x,c.y))

    print("____________Opgave 1.26____________")
    a = V.Vector2D(1,2)
    b = V.Vector2D(4,1)
    c = a.projektering(b)
    print("a)\nX:{}\nY:{}\n".format(c.x,c.y))

    a = V.Vector2D(-3,-1)
    b = V.Vector2D(-5,4)
    c = a.projektering(b)
    print("b)\nX:{}\nY:{}\n".format(c.x,c.y))
    """
    """
    a = V.Vector2D(-6,3)
    b = V.Vector2D(10,4)
    c = V.Vector2D(1,10)
    d = V.Vector2D(20,5)
    L = [a,b,c,d]

    V.show_vectors(L)
    """

    """
    l = GF.AndenGrads("-3*x**2+6*x+2")
    l.differentabel()
    """

    """
    b = a.tver_vektor()
    print("Vx:{}  Vy:{}".format(b.x,b.y))
    """

    #opgaver.opgave2()
    #x = Symbol("x")

    """
    f = Fun.Function("20+150*log(8*x+1)")
    f.show_function()

    #f.show_function(range(-100,100))
    
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


    v1 = V3D.Vector3D(-1,-4,-6)
    v2 = V3D.Vector3D(5,-1,8)
    print(v1.areal_parallellogram(v2))


    v1 = V3D.Vector3D(1,-2,-2)
    v2 = V3D.Vector3D(-3,0,8)
    print(v1.areal_parallellogram(v2))

    v1 = V3D.Vector3D(1,7,-5)
    v2 = V3D.Vector3D(3,10,-7)
    print(v1.areal_parallellogram(v2))

    return 0

if __name__ == "__main__":
    main()