# Programa para calcular el área y el perímetro de un rectángulo

# Esta es función que calcula el área de un rectángulo
def calcular_area(base: float, altura: float) -> float:
    return base * altura


# Función que calcula el perímetro de un rectángulo
def calcular_perimetro(base: float, altura: float) -> float:
    return 2 * (base + altura)


# Solicitar datos al usuario
nombre_usuario = input("Ingrese su nombre: ")  # tipo string
print(f"Hola, {nombre_usuario}. Voy a calcular el área y el perímetro de un rectángulo.")

# Convierto las entradas a tipo float
base = float(input("Ingrese la base del rectángulo en centímetros: "))
altura = float(input("Ingrese la altura del rectángulo en centímetros: "))

# Validación básica de datos
datos_validos = base > 0 and altura > 0  # tipo boolean

if datos_validos:
    area = calcular_area(base, altura)
    perimetro = calcular_perimetro(base, altura)

    # Resultados
    print(f"\nResultados para el rectángulo con base {base} cm y altura {altura} cm:")
    print(f"Área: {area} cm²")  # tipo float
    print(f"Perímetro: {perimetro} cm")  # tipo float
else:
    print("\nError: Las medidas deben ser mayores que cero.")
