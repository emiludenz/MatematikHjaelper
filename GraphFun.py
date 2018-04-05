import matplotlib.pyplot as plt
import math
from numpy import array
from sympy import Symbol


class AndenGrads:
    def __init__(self, formula):
        # gets string, eval to get args
        x = Symbol("x")
        self.formula = formula
        self.evalFormula = eval(formula)
        # Getting arguments
        self.c = self.evalFormula.args[0]
        self.b = self.evalFormula.coeff(x)
        self.a = self.evalFormula.coeff(x**2)

        # Getting d
        self.d = self.b**2-4*self.a*self.c

        # Getting roots
        self.x1 = (-self.b-math.sqrt(self.d))/(2*self.a)
        self.x2 = (-self.b+math.sqrt(self.d))/(2*self.a)

        # Getting Top point coordinates
        self.Tx = -(self.b) / (2 * self.a)
        self.Ty = -(self.d) / (4 * self.a)

    def differentabel(self):
        x = Symbol("x")
        y = eval(self.formula)
        yprime = y.diff(x)
        print("f(x)={}\nf'(x)={}".format(self.formula,yprime))

    def print_it(self):
        print("D:{}".format(self.d))
        print("X:{} X.{}".format(self.x1,self.x2))
        print("Toppunkt Koordinator: ({},{})".format(self.Tx,self.Ty))

    def show_it(self,x_range):
        x = Symbol("x")
        x = array(x_range)
        y = eval(self.formula)
        plt.plot(x, y)
        plt.show()





def find_potens(avector, bvector):
    # log(y2)-log(y1)/log(x2)-log(x1)
    print("Finding Potens a by using log")
    potens = (math.log(bvector.y) - math.log(avector.y)) / (math.log(bvector.x) - math.log(avector.x))
    print("log({0})-log({1})\n_____________={4}\nlog({2})log({3})".format(bvector.y, avector.y, bvector.x, avector.x, potens))
    return potens


def finding_b(potens, avector, bvector):
    # y1 = b *x1**a >> b = y1/x1**a
    # virker for begge kooardinator
    print("Finding b")
    print("y1=b*x1^a >> b = y1/x1**a")
    b1 = round(avector.y / avector.x ** potens, 10)
    b2 = round(bvector.y / bvector.x ** potens, 10)
    print("{0}={1}/{2}**{3}".format(b1, avector.y, avector.x, potens))
    print("b1:{0} b2:{1}".format(round(b1, 10), round(b2, 10)))
    if b1 == b2:
        return b1

"""
a = V.Vector2D(20, 0.035)
b = V.Vector2D(80, 0.1)
s = find_potens(a, b)
print(s)
#0.7572865864148793
print(finding_b(s, a, b))
#0.003620891239297886
x = finding_b(s, a, b)


def go(x, s, n):
    return x * n ** s

go(x, s, 45) #0.0646801683001436

p=go(x,s,45)
#45/100*300+45 = 58.5
q=go(x,s,58.5)
print(q-p)
#0.014216545357059102

"""