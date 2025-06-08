class PersonajeCientificoRobot:

    def __init__(self, nombre, inteligencia, energia, resistencia, salud):
        self.nombre = nombre
        self.inteligencia = inteligencia
        self.energia = energia
        self.resistencia = resistencia
        self.salud = salud

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("·Inteligencia:", self.inteligencia)
        print("·Energía:", self.energia)
        print("·Resistencia:", self.resistencia)
        print("·Salud:", self.salud)

    def subir_nivel(self, inteligencia, energia, resistencia):
        self.inteligencia += inteligencia
        self.energia += energia
        self.resistencia += resistencia

    def esta_operativo(self):
        return self.salud > 0

    def desactivar(self):
        self.salud = 0
        print(self.nombre, "se ha desactivado")

    def calcular_daño(self, oponente):
        return self.energia - oponente.resistencia

    def atacar(self, oponente):
        daño = self.calcular_daño(oponente)
        oponente.salud -= daño
        print(self.nombre, "ha causado", daño, "puntos de daño a", oponente.nombre)
        if oponente.esta_operativo():
            print("Salud de", oponente.nombre, "es", oponente.salud)
        else:
            oponente.desactivar()


class Cientifico(PersonajeCientificoRobot):

    def __init__(self, nombre, inteligencia, energia, resistencia, salud, invento):
        super().__init__(nombre, inteligencia, energia, resistencia, salud)
        self.invento = invento

    def cambiar_invento(self):
        opcion = int(input("Elige un invento: (1) Rayo láser, potencia 5. (2) Nanobots, potencia 8"))
        if opcion == 1:
            self.invento = 5
        elif opcion == 2:
            self.invento = 8
        else:
            print("Opción de invento incorrecta")

    def atributos(self):
        super().atributos()
        print("·Invento:", self.invento)

    def calcular_daño(self, oponente):
        return self.inteligencia * self.invento - oponente.resistencia


class Robot(PersonajeCientificoRobot):

    def __init__(self, nombre, inteligencia, energia, resistencia, salud, arma):
        super().__init__(nombre, inteligencia, energia, resistencia, salud)
        self.arma = arma

    def atributos(self):
        super().atributos()
        print("·Arma:", self.arma)

    def calcular_daño(self, oponente):
        return self.energia * self.arma - oponente.resistencia


def simulador_combate(participante_1, participante_2):
    ronda = 0
    while participante_1.esta_operativo() and participante_2.esta_operativo():
        print("\nRonda", ronda)
        print(">>> Acción de", participante_1.nombre, ":")
        participante_1.atacar(participante_2)
        print(">>> Acción de", participante_2.nombre, ":")
        participante_2.atacar(participante_1)
        ronda += 1

    if participante_1.esta_operativo():
        print("\nEl ganador es", participante_1.nombre)
    elif participante_2.esta_operativo():
        print("\nEl ganador es", participante_2.nombre)
    else:
        print("\n¡Ambos quedaron fuera de combate!")


cientifico = Cientifico("Dra. Tesla", 15, 10, 6, 120, 3)
robot = Robot("AX-9000", 8, 18, 7, 110, 4)

cientifico.atributos()
print()
robot.atributos()

print("\n¡COMIENZA LA SIMULACIÓN DE COMBATE!")
simulador_combate(cientifico, robot)