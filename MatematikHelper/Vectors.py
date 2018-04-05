import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


class Angel:

    def __init__(self, v):
        self.v = v

    def what_kind(self):
        if self.v < 90:
            return "Spids"
        elif self.v == 90:
            return "Retvinkel"
        elif self.v > 90:
            return "Stump"
        else:
            return "WHY!"



class Vector2D:
    # Class making my vectors the bestors
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.vec = (self.x, self.y)

    def length(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def get(self):
        return self.vec

    def set(self, x, y):
        self.x = x
        self.y = y

    def add(self, vec):
        x2 = self.x + vec.x
        y2 = self.y + vec.y
        return x2, y2

    def sub(self, vec):
        x2 = self.x - vec.x
        y2 = self.y - vec.y
        return x2, y2

    def dist(self, vec):
        x2 = vec.x - self.x
        y2 = vec.y - self.y
        return math.sqrt(abs(x2 ** 2) + abs(y2 ** 2))

    def multi(self, t):
        # T is multiplier
        return Vector2D(self.x * t, self.y * t)

    def scale_product(self, vec):
        # s = skala faktor
        s = vec.x / self.x
        return s

    def scaler(self, vec):
        x = self.x * vec.x
        y = self.y * vec.y
        return x + y


    """
        Find coordinator via vinkel
        |a| * cos(v) = a1
        |a| * sin(v) = a2

    """


    def get_angel(self, vecB=0, p=False):
        if vecB == 0:
            vecB = Vector2D(1,0)
        # cos(v) = A.x * B.x + A.y * B.y / |A|*|B|
        A = (self.x * vecB.x) + (self.y * vecB.y)
        B = np.sqrt(self.x**2 + self.y**2) * np.sqrt(vecB.x**2 + vecB.y**2)
        v = math.acos(float(A)/float(B))
        if p:
            print("\n[{}]A = ([{}]self.x * [{}]vecB.x) + ([{}]self.y * [{}]vecB.y)".format(A,self.x,vecB.x,self.y,vecB.y))
            print("[{}]B = np.sqrt([{}]self.x ** 2 + [{}]self.y ** 2) * np.sqrt([{}]vecB.x ** 2 + "
                  "[{}]vecB.y ** 2)".format(B,self.x**2,self.y**2,vecB.x**2,vecB.y**2))
            print("[{}]v = math.acos([{}]float(A) / [{}]float(B))".format(v,A,B))
            print("v in degress: [{}] ".format(math.degrees(v)))


            """
            #print("{}*{}+{}*{}".format(self.x,vecB.x,self.y,vecB.y))
            print("\nsqrt({}+{}*{}+{})".format(round(self.x**2,2),round(self.y**2,2),round(vecB.x**2,2),round(vecB.y**2,2)))
            print("{} / {} = acos({}) = {}\n".format(round(A,2),round(B,2),round(v,2),round(math.degrees(v),2)))
            """
        return math.degrees(v)

    def get_x_deg(self, deg):
        a = self.length()
        cos = np.cos(np.deg2rad(deg))
        return a * cos

    def get_y_deg(self, deg):
        a = self.length()
        sin = np.sin(np.radians(deg))
        return a * sin

    def projektering(self,vecB):
        # Projektering af en vektor på en vektor S36A (sætning 10)
        # kan findes som skalarproduktet af (a*b/|b|^2)*b
        upper = self.x*vecB.x+self.y*vecB.y
        lower = math.fabs(vecB.x**2+vecB.y**2)
        Vx = upper * vecB.x
        Vy = upper * vecB.y
        print("{}*{}\n____\n{}".format(upper,vecB.x,lower))
        print("\n")
        print("{}*{}\n____\n{}".format(upper, vecB.y, lower))
        return Vector2D(Vx / lower, Vy / lower)

    def tver_vektor(self):
        #90 grader drejet mod uret, se side 37
        a2 = self.y*-1
        a1 = self.x
        return Vector2D(a2,a1)

    def determinant(self, vecB):
        #Side 37
        #TODO: Make logic clear
        tver = self.tver_vektor()
        a = tver.x * vecB.x
        b = tver.y * vecB.y
        return a-(-b)

    def areal(self,vecB):
        c=self.determinant(vecB)

        print(math.fabs(c))

    def show_vector(self, vecB=0):
        V = np.array([[self.x, self.y]])
        if vecB == 0:
            print("yep")
            vecB = Vector2D(0,0)
        origin = [vecB.x], [vecB.y]  # origin point
        plt.quiver(*origin, V[:, 0], V[:, 1], color=['r', 'b', 'g'], scale=21)
        plt.show()




def format_graph_window(array):
    colors = ["yellow", "limegreen", "cyan", "purple", "red", "black", "grey"]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    V = np.array(array)
    origin = [0], [0]  # origin point

    plt.quiver(*origin, V[:, 0], V[:, 1], color=colors, scale=21)

    # Major ticks every 20, minor ticks every 5
    major_ticks = np.arange(-10, 11, 5)
    minor_ticks = np.arange(-10, 11, 1)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)

    # And a corresponding grid
    ax.grid(which='both')

    # Or if you want different settings for the grids:
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)
    return ax

def show_vectors(vecList):
    array = list()
    colors = ["yellow", "limegreen", "cyan", "purple", "red", "black", "grey"]
    for v in vecList:
        array.append([v.x,v.y])

    #TODO: Make this way smoother
    ax = format_graph_window(array)

    #-------Could be its own function--------#
    i = 0
    handles = list()
    for v in vecList:
        patch = mpatches.Patch(color=colors[i], label="({},{})".format(round(v.x,2),round(v.y,2)))
        handles.append(patch)
        i += 1

    plt.legend(handles=handles)
    plt.grid()
    plt.show()