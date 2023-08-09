#Cree una clase Circulo que tenga las propiedades centro y radio,
# las cuales se inicializan con parámetros en el constructor.
# Defina métodos en la clase para calcular el área,
# el perímetro e indicar si un punto pertenece al círculo o no.


import math
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def pertenece(self, punto):
        distancia = math.sqrt((punto.x - self.centro.x) ** 2 + (punto.y - self.centro.y) ** 2)
        return distancia <= self.radio


# Ejemplo
centro = Punto(0, 0)
circulo1 = Circulo(centro, 5)

punto1 = Punto(3, 4)
punto2 = Punto(7, 2)

print(f"Área del círculo: {circulo1.calcular_area()}")
print(f"Perímetro del círculo: {circulo1.calcular_perimetro()}")

print(f"¿El punto 1 pertenece al círculo?: {circulo1.punto_pertenece(punto1)}")
print(f"¿El punto 2 pertenece al círculo?: {circulo1.punto_pertenece(punto2)}")
