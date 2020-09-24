import Figuras

punto1 = Figuras.Punto(0,0)
punto2 = Figuras.Punto(0,2)
punto3 = Figuras.Punto(2,0)
punto4 = Figuras.Punto(2,2)

d=punto1.hallarDistancia(punto2)
print("La distancia entre el punto 1 y 2 es de "+str(d))

rectangulo1=Figuras.Rectangulo(punto1,punto2,punto3,punto4)
pr = rectangulo1.hallarPerimetro()
print("El perimetro del rectangulo es de  "+str(pr))

triangulo1=Figuras.Triangulo(punto1,punto2,punto3)
pt = triangulo1.hallarPerimetro()
at = triangulo1.hallarArea()
tt = triangulo1.determinarTipo()
print("El perimetro del triangulo es de  "+str(pt))
print("El area del triangulo es de  "+str(at))
print("El triangulo "+tt)

circulo1=Figuras.Circulo(punto1,2)
pc = circulo1.hallarPerimetro()
ac = circulo1.hallarArea()
print("El perimetro del circulo es de  "+str(pc))
print("El area del circulo es de "+str(ac))

