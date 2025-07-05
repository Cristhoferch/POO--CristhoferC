# Clase base
class Mascota:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Atributo encapsulado
        self.__edad = edad

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_edad(self):
        return self.__edad

    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad

#Metodo comun que sera sobreescrito por clases hijas: polimorfismo
    def hacer_sonido(self):
        return "Sonido genérico de mascota"

    def describir(self):
        return f"{self.get_nombre()} tiene {self.get_edad()} años."


# Clase derivada: Perro
class Perro(Mascota):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)#llamada al constructor de la clase base
        self.raza = raza

    #Metodo sobreescrito: polimorfismo
    def hacer_sonido(self):
        return "Y hace: ¡Guau!"

    def describir(self):
        return f"{self.get_nombre()} es un perro de raza {self.raza} y tiene {self.get_edad()} años."


# Clase derivada: Gato
class Gato(Mascota):
    def __init__(self, nombre, edad, color):
        super().__init__(nombre, edad)
        self.color = color

    #Metodo sobre escrito: polimorfismo
    def hacer_sonido(self):
        return "Y hace: ¡Miau!"

    def describir(self):
        return f"{self.get_nombre()} es un gato de color {self.color} y tiene {self.get_edad()} años."


# Código de prueba (sin condicional)
def main():
    perro1 = Perro("Max", 5, "Labrador")
    gato1 = Gato("Luna", 3, "Gris")

    print(perro1.describir())
    print(perro1.hacer_sonido())

    print(gato1.describir())
    print(gato1.hacer_sonido())

#Encapsulación: para cambiar el nombre y la edad del gato
    gato1.set_nombre("Mishi")
    gato1.set_edad(2)
    print(gato1.describir())

main()
