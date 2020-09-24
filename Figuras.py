import math

class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def hallarDistancia(self,otropunto):
        d = math.sqrt(math.pow(self.x - otropunto.x, 2) + math.pow(self.y - otropunto.y, 2))
        return d
    pass

class Rectangulo(Punto):
    def __init__(self,izqInf,derInf,izqSup,derSup):
        self.izqInf = izqInf
        self.derInf = derInf
        self.izqSup = izqSup
        self.derSup = derSup

    def hallarPerimetro(self):
        l1 = self.izqInf.hallarDistancia(self.derInf)
        l2 = self.izqSup.hallarDistancia(self.derSup)
        p = 2*l1+2*l2
        return p
    pass


