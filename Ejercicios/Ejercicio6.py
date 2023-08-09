class Carta:
    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta

class Pinta:
    CORAZON = "Corazón"
    DIAMANTE = "Diamante"
    TREBOL = "Trébol"
    ESPADA = "Espada"

# Ejemplo
carta1 = Carta(7, Pinta.CORAZON)
carta2 = Carta(10, Pinta.ESPADA)

print(f"Carta 1: Valor {carta1.valor}, Pinta {carta1.pinta}")
print(f"Carta 2: Valor {carta2.valor}, Pinta {carta2.pinta}")
