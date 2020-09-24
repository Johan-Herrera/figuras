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

class Triangulo(Punto):

    def __init__(self,izq,der,sup):
        self.sup = sup;
        self.izq = izq;
        self.der = der;

    def hallarPerimetro(self):
        l1 = self.izq.hallarDistancia(self.der)
        l2 = self.izq.hallarDistancia(self.sup)
        l3 = self.der.hallarDistancia(self.sup)
        p = l1 + l2 + l3
        return p

    def hallarArea(self):
        l1 = self.izq.hallarDistancia(self.der)
        l2 = self.izq.hallarDistancia(self.sup)
        l3 = self.der.hallarDistancia(self.sup)
        s = (l1 + l2 + l3) / 2;
        a = math.sqrt(s * (s - l1) * (s - l2) * (s - l3))
        return a;

    def determinarTipo(self):
        l1 = self.izq.hallarDistancia(self.der)
        l2 = self.izq.hallarDistancia(self.sup)
        l3 = self.der.hallarDistancia(self.sup)
        if l1 == l2 and l1 == l3:
            return "Es equilatero"
        else:
            if l1 == l2 or l1 == l2 or l2 == l3:
                return "Es isosceles"
            else:
                return "Es escaleno"






