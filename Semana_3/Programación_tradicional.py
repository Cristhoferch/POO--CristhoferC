# PROGRAMA TRADICIONAL (FUNCIONES)
# Calcula el promedio semanal de temperaturas usando funciones.

# Función para ingresar temperaturas de la semana
def ingresar_temperaturas():
    #Solicita al usuario las temperaturas de los 7 días de la semana.
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    temperaturas = []  # Lista para almacenar las temperaturas

    for dia in dias:
        while True:
            try:
                temp = float(input(f"Ingrese la temperatura del {dia}: "))
                temperaturas.append(temp)  # Agrega la temperatura a la lista
                break
            except ValueError:
                print("¡Error! Ingrese un número válido.")

    return temperaturas  # Devuelve la lista completa


# Función para calcular el promedio
def calcular_promedio(temps):
    """Calcula el promedio de una lista de temperaturas."""
    if not temps:  # Si la lista está vacía
        return 0
    return sum(temps) / len(temps)  # Suma todas las temps y divide entre 7 días


# Función para mostrar el resultado
def mostrar_resultado(promedio):
    """Muestra el promedio de temperatura al usuario."""
    print(f"\nEl promedio semanal es: {promedio:.1f}°C")


# Función principal que ejecuta el programa
def main():
    print("=== PROMEDIO SEMANAL DE TEMPERATURAS (PROG. TRADICIONAL) ===")
    temps = ingresar_temperaturas()  # Paso 1: Ingresar datos
    promedio = calcular_promedio(temps)  # Paso 2: Calcular promedio
    mostrar_resultado(promedio)  # Paso 3: Mostrar resultado


# Ejecuta el programa solo si es el archivo principal
if __name__ == "__main__":
    main()