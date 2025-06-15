# Programa para calcular el promedio semanal de temperaturas (enfoque POO)

class SemanaClima:
    #Clase que representa el clima de una semana

    def __init__(self):
        self.dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        self.temperaturas = {}

    def ingresar_temperaturas(self):
        #Metodo para ingresar las temperaturas de la semana
        for dia in self.dias_semana:
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura para {dia}: "))
                    self.temperaturas[dia] = temp
                    break
                except ValueError:
                    print("Por favor, ingrese un número válido.")

    def calcular_promedio(self):
        #Metodo para calcular el promedio de temperaturas
        if not self.temperaturas:
            return 0
        return sum(self.temperaturas.values()) / len(self.temperaturas)

    def mostrar_promedio(self):
        #metodo para mostrar el resultado
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal de temperatura es: {promedio:.2f}°C")


class InformeClima(SemanaClima):
    #Clase pa detallar informes de la temperatura

    def mostrar_informe_detallado(self):
        print("\n=== INFORME DETALLADO DE TEMPERATURAS ===")
        for dia, temp in self.temperaturas.items():
            print(f"{dia}: {temp}°C")

        promedio = self.calcular_promedio()
        print(f"\nPromedio semanal: {promedio:.2f}°C")

        max_temp = max(self.temperaturas.values())
        min_temp = min(self.temperaturas.values())
        print(f"Temperatura máxima: {max_temp}°C")
        print(f"Temperatura mínima: {min_temp}°C")


def main():
    #primera función
    print("=== CALCULADORA DE PROMEDIO SEMANAL DE TEMPERATURAS (POO) ===")
    print("Por favor ingrese las temperaturas para cada día de la semana:\n")

    # Versión básica
    clima_semana = SemanaClima()
    clima_semana.ingresar_temperaturas()
    clima_semana.mostrar_promedio()

    # Versión extendida con herencia
    print("\n=== VERSIÓN EXTENDIDA CON HERENCIA ===")
    informe = InformeClima()
    informe.ingresar_temperaturas()
    informe.mostrar_informe_detallado()


if __name__ == "__main__":
    main()