# Clase que representa a un cliente del hotel
class Cliente:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula

    def __str__(self):
        return f"{self.nombre} (Cedula: {self.cedula})"


# Clase que representa una habitación del hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero  # número de habitación
        self.tipo = tipo      # tipo de habitación (Ej: simple, doble)
        self.precio = precio  # precio por noche
        self.ocupada = False  # estado de ocupación

    def __str__(self):
        estado = "Ocupada" if self.ocupada else "Disponible"
        return f"Habitación {self.numero} ({self.tipo}) - ${self.precio}/noche - {estado}"


# Clase que representa una reserva hecha por un cliente
class Reserva:
    def __init__(self, cliente, habitacion, dias):
        self.cliente = cliente
        self.habitacion = habitacion
        self.dias = dias
        self.total = dias * habitacion.precio
        self.habitacion.ocupada = True  # al hacer la reserva, se marca la habitación como ocupada

    def __str__(self):
        return (f"Reserva para {self.cliente}\n"
                f"{self.habitacion}\n"
                f"Días: {self.dias} - Total: ${self.total}")


# Clase principal que gestiona el hotel y sus reservas
class Hotel:
    def __init__(self, nombre):
        self.nombre = nombre
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        print(f"\nHabitaciones disponibles en {self.nombre}:")
        for hab in self.habitaciones:
            if not hab.ocupada:
                print(hab)

    def hacer_reserva(self, cliente, tipo_habitacion, dias):
        for hab in self.habitaciones:
            if hab.tipo == tipo_habitacion and not hab.ocupada:
                reserva = Reserva(cliente, hab, dias)
                self.reservas.append(reserva)
                print(f"\nReserva realizada con éxito:\n{reserva}")
                return
        print(f"\nNo hay habitaciones disponibles del tipo '{tipo_habitacion}'.")


# ---------------------- Uso del programa ----------------------

# Creamos instancia del hotel
mi_hotel = Hotel("Hotel Cris")

# Agregar habitaciones
mi_hotel.agregar_habitacion(Habitacion(101, "simple", 50))
mi_hotel.agregar_habitacion(Habitacion(102, "doble", 80))
mi_hotel.agregar_habitacion(Habitacion(103, "simple", 50))

# Muestra las habitaciones disponibles
mi_hotel.mostrar_habitaciones_disponibles()

# Creamos clientes
cliente1 = Cliente("Cristhofer CH", "1234567890")
cliente2 = Cliente("Vidal G", "0987654321")

# Realiza reservas
mi_hotel.hacer_reserva(cliente1, "simple", 3)
mi_hotel.hacer_reserva(cliente2, "doble", 2)

# Muestra las habitaciones disponibles luego de las reservas
mi_hotel.mostrar_habitaciones_disponibles()
