import math

#A la clase del punto anterior, defínale los siguientes métodos:
#Un método mostrar que imprima por consola las coordenadas del punto
#Un método mover que cambie las coordenadas del punto
#Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.

class Punto:
    def __init__(self, x:float, y:float):
        self.x: float = x
        self.y: float = y

    def mostar(self):
        print(f"Las cordenadas del puntos son: ({self.x}, {self.y}) ")

    def mover(self, nuevo_x, nuevo_y):
        self.x = nuevo_x
        self.y = nuevo_y

    def calcular_distancia(self, otro_punto):
        distancia= math.sqrt((self.x - otro_punto.x)**2(self.y - otro_punto.y)**2)