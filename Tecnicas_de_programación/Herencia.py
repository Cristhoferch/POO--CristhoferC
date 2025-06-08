class Vehiculo:
    def __init__(self, marca):
        self.marca = marca

    def arrancar(self):
        print("El vehículo arranca")

class Moto(Vehiculo):
    def hacer_wheelie(self):
        print("¡Haciendo un wheelie!")

# Uso
mi_moto = Moto("Yamaha")
mi_moto.arrancar()
mi_moto.hacer_wheelie()