class pollito:
    def cantar(self):
        print("Amarillito dice:Pío pío")

class Gato:
    def cantar(self):
        print("Tom dice: Miau")


def hacer_cantar(animal):
    animal.cantar()

# Uso
amarillito = pollito()
tom = Gato()
hacer_cantar(amarillito)
hacer_cantar(tom)