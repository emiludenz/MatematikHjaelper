from math import acos,degrees,asin, sin

class Trekant:
    def __init__(self, a=0.0, b=0.0, c=0.0, A=0.0, B=0.0, C=0.0):
        # Sides
        self.a = a
        self.b = b
        self.c = c
        # Angles
        self.C = C
        self.B = B
        self.A = A
        self.rect = self.checkIsRet()

    def checkIsRet(self):
        if self.a ** +self.b ** 2 == self.c ** 2:
            return True
        else:
            return False

    def getAngles(self):
        if self.rect:
            if self.b > 0 and self.c > 0:
                cosA = self.b/self.c
                self.A = degrees(acos(cosA))

        else:
            # getting angle C
            cosC = (self.a**2+self.b**2-self.c**2)/(2*self.a*self.b)
            self.C = degrees(acos(cosC))
            self.C_rad = acos(cosC)
            # getting angel B
            sinB = (self.b*sin(self.C_rad))/self.c
            self.B = degrees(asin(sinB))
            self.B_rad = asin(sinB)
            # getting angel A
            sinA = (self.a * sin(self.C_rad)) / self.c
            self.A = degrees(asin(sinA))
            self.A_rad = asin(sinA)




