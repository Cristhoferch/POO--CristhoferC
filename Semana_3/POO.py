# ===== PROGRAMA ORIENTADO A OBJETOS (POO) =====
#Metodo aplicado : ENCAPSULAMIENTO SIN __
# Calcula el promedio semanal de temperaturas usando clases.

class ClimaSemanal:
    """Clase que representa las temperaturas de una semana."""

    def __init__(self):
        """Constructor: Inicializa los días y temperaturas."""
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
        self.temperaturas = {}  # Diccionario para guardar {día: temperatura}

    def ingresar_temperaturas(self):
        """Método para registrar temperaturas en la semana."""
        for dia in self.dias:
            while True:
                try:
                    temp = float(input(f"Ingrese la temperatura del {dia}: "))
                    self.temperaturas[dia] = temp  # Guarda en el diccionario
                    break
                except ValueError:
                    print("¡Error! Ingrese un número válido.")

    def calcular_promedio(self):
        """Método que calcula el promedio semanal."""
        if not self.temperaturas:  # Si no hay datos
            return 0
        return sum(self.temperaturas.values()) / len(self.temperaturas)

    def mostrar_promedio(self):
        """Método que muestra el resultado."""
        promedio = self.calcular_promedio()
        print(f"\nEl promedio semanal es: {promedio:.1f}°C")


# Función principal para ejecutar el programa
def main():
    print("=== PROMEDIO SEMANAL DE TEMPERATURAS (POO) ===")
    clima = ClimaSemanal()  # Paso 1: Crear objeto
    clima.ingresar_temperaturas()  # Paso 2: Llenar datos
    clima.mostrar_promedio()  # Paso 3: Calcular y mostrar resultado


# Ejecuta el programa solo si es el archivo principal :)
if __name__ == "__main__":
    main()