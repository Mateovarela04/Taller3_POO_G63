#Cree una clase Punto que represente un punto en el plano cartesiano.

class Punto:
    def __init__(self, x:float, y:float):
        self.x: float = x
        self.y: float = y

punto1= Punto(6,10)
punto2= Punto(0,1)

print(f"x esta en:{punto1.x} y esta en:{punto1.y}")
print(f"x esta en:{punto2.x} y esta en:{punto2.y}")