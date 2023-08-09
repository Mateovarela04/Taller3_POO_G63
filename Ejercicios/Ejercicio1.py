#Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.

class Vehiculo:

    def __init__(self, velocidad_maxima: float, kilometraje: float):
        self.velocidad_maxima: float =velocidad_maxima
        self.kilometraje: float =kilometraje

carro1 = Vehiculo(240,23563)
carro2 = Vehiculo(260,50000)
carro3 = Vehiculo(240,13200)

print(f"velocidad maxima: {carro1.velocidad_maxima} km/h")
print(f"kilometraje:{carro3.kilometraje} km/h" )