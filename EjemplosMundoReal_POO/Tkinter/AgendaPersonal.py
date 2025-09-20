import tkinter as tk
from tkinter import messagebox
from datetime import datetime


class AgendaSimple:
    def __init__(self, root):
        self.root = root
        self.root.title("Mi Agenda Personal")
        self.root.geometry("600x500")

        # Lista para almacenar eventos
        self.eventos = []

        # Crear interfaz
        self.crear_interfaz()

    def crear_interfaz(self):
        # Título
        titulo = tk.Label(self.root, text="MI AGENDA", font=("Arial", 16, "bold"))
        titulo.pack(pady=10)

        # Marco para nuevos eventos
        marco_nuevo = tk.LabelFrame(self.root, text="Nuevo Evento", padx=10, pady=10)
        marco_nuevo.pack(pady=10, padx=20, fill="x")

        # Fecha
        tk.Label(marco_nuevo, text="Fecha:").grid(row=0, column=0, sticky="w", pady=5)

        # Marco para los selectores de fecha
        marco_fecha = tk.Frame(marco_nuevo)
        marco_fecha.grid(row=0, column=1, pady=5, padx=5, sticky="w")

        # Día
        self.dia_var = tk.StringVar(value=str(datetime.now().day))
        tk.Label(marco_fecha, text="Día:").pack(side="left")
        spin_dia = tk.Spinbox(marco_fecha, from_=1, to=31, width=3, textvariable=self.dia_var)
        spin_dia.pack(side="left", padx=5)

        # Mes
        self.mes_var = tk.StringVar(value=str(datetime.now().month))
        tk.Label(marco_fecha, text="Mes:").pack(side="left", padx=(10, 0))
        spin_mes = tk.Spinbox(marco_fecha, from_=1, to=12, width=3, textvariable=self.mes_var)
        spin_mes.pack(side="left", padx=5)

        # Año
        self.anio_var = tk.StringVar(value=str(datetime.now().year))
        tk.Label(marco_fecha, text="Año:").pack(side="left", padx=(10, 0))
        spin_anio = tk.Spinbox(marco_fecha, from_=2020, to=2030, width=5, textvariable=self.anio_var)
        spin_anio.pack(side="left", padx=5)

        # Hora
        tk.Label(marco_nuevo, text="Hora (hh:mm):").grid(row=1, column=0, sticky="w", pady=5)
        self.entry_hora = tk.Entry(marco_nuevo, width=10)
        self.entry_hora.grid(row=1, column=1, pady=5, padx=5, sticky="w")
        self.entry_hora.insert(0, "")  # Hora por defecto

        # Descripción
        tk.Label(marco_nuevo, text="Descripción:").grid(row=2, column=0, sticky="w", pady=5)
        self.entry_desc = tk.Entry(marco_nuevo, width=30)
        self.entry_desc.grid(row=2, column=1, pady=5, padx=5, sticky="w")

        # Botones
        marco_botones = tk.Frame(marco_nuevo)
        marco_botones.grid(row=3, column=0, columnspan=2, pady=10)

        btn_agregar = tk.Button(marco_botones, text=" Agregar", command=self.agregar_evento, bg="lightgreen")
        btn_agregar.pack(side="left", padx=5)

        btn_eliminar = tk.Button(marco_botones, text=" Eliminar", command=self.eliminar_evento, bg="lightcoral")
        btn_eliminar.pack(side="left", padx=5)

        btn_salir = tk.Button(marco_botones, text=" Salir", command=self.root.quit, bg="lightblue")
        btn_salir.pack(side="left", padx=5)

        # Lista de eventos
        marco_lista = tk.LabelFrame(self.root, text="Mis Eventos", padx=10, pady=10)
        marco_lista.pack(pady=10, padx=20, fill="both", expand=True)

    def obtener_fecha(self):
        try:
            dia = self.dia_var.get().zfill(2)
            mes = self.mes_var.get().zfill(2)
            anio = self.anio_var.get()

            return f"{dia}/{mes}/{anio}"
        except:
            return None

    def agregar_evento(self):
        # Obtener fecha seleccionada y hora escrita
        fecha = self.obtener_fecha()
        hora = self.entry_hora.get()
        desc = self.entry_desc.get()

        # Validar que no estén vacíos
        if not fecha or not hora or not desc:
            messagebox.showerror("Error", " Todos los campos son obligatorios")
            return

        # Crear texto del evento
        evento_texto = f"{fecha} - {hora} - {desc}"

        # Agregar a la lista
        self.eventos.append(evento_texto)
        self.lista_eventos.insert(tk.END, evento_texto)

        # Limpiar campo de descripción
        self.entry_desc.delete(0, tk.END)

        messagebox.showinfo("Éxito", " Evento agregado correctamente")

    def eliminar_evento(self):
        # Verificar si hay evento seleccionado
        seleccionado = self.lista_eventos.curselection()
        if not seleccionado:
            messagebox.showwarning("Advertencia", " Selecciona un evento para eliminar")
            return

        # Confirmar eliminación
        if messagebox.askyesno("Confirmar", "¿Estás seguro de eliminar este evento?"):
            # Eliminar de la lista y del Listbox
            index = seleccionado[0]
            self.lista_eventos.delete(index)
            if index < len(self.eventos):
                self.eventos.pop(index)

            messagebox.showinfo("Éxito", " Evento eliminado correctamente")


# Crear y ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaSimple(root)
    root.mainloop()