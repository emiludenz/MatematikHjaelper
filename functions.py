import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from sympy import Symbol,log, exp
from sympy.solvers import solve
from sympy.plotting import plot

x = Symbol("x")

class Function:
    def __init__(self, formula):

        self.formula = formula
        self.eFormula = eval(self.formula)
        self.args = self.eFormula.as_coefficients_dict()
        self.a = self.args[1]
        self.b = self.args[x]
        self.c = self.args[x**2]
        self.roots = self.get_roots()

    def get_roots(self):
        return solve(self.eFormula,x)

    def integrate(self):
        return self.eFormula.integrate()

    def differential(self):
        return self.eFormula.diff()

    def factor(self):
        return self.eFormula.factor()

    def simplify(self):
        return self.eFormula.simplify()

    def show_function(self, diff=False):
        if len(self.roots) > 1:
            p = plot(self.eFormula,(x,self.roots[0],self.roots[-1]))
        elif len(self.roots) >= 0:
            p = plot(self.eFormula,(x,-100,100))



    def print_office_form(self):

        print("x = {} or {}".format(self.roots[0], self.roots[-1]))




"""
def graph_window(Function):

    colors = ["yellow", "limegreen", "cyan", "purple", "red", "black", "grey"]
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    graph(Function,range(-100,100))
    # Major ticks every 20, minor ticks every 5
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)
    plt.show()
"""