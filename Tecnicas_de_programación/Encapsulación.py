class Coche:
    def __init__(self):
        self.__kilometraje = 0

    def avanzar(self, km):
        if km > 0:
            self.__kilometraje += km

    def get_kilometraje(self):
        return self.__kilometraje


mi_coche = Coche()
mi_coche.avanzar(50)
print(mi_coche.get_kilometraje())