import math

class Punto:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def hallarDistancia(self,otropunto):
        d = math.sqrt(math.pow(self.x - otropunto.x, 2) + math.pow(self.y - otropunto.y, 2))
        return d
    pass

