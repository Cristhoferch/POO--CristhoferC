from abc import ABC, abstractmethod

class MetodoPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto):
        pass  # ¡No se implementa aquí!

class TarjetaCredito(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Procesando pago de ${monto} con Tarjeta de Crédito (detalles: conexión SSL, validación CVV, etc.)")

class PayPal(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Procesando pago de ${monto} via PayPal (detalles: API REST,etc.)")

class Bitcoin(MetodoPago):
    def procesar_pago(self, monto):
        print(f"Procesando pago de ${monto} en Bitcoin (detalles: blockchain, confirmaciones, etc.)")

def realizar_compra(metodo_pago, monto):
    metodo_pago.procesar_pago(monto)

pago1 = TarjetaCredito()
pago2 = PayPal()
pago3 = Bitcoin()

realizar_compra(pago1, 100)
realizar_compra(pago2, 50)
realizar_compra(pago3, 75)