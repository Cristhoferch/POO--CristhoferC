import tkinter as tk
from tkinter import messagebox

# Función para agregar texto a la lista
def agregar_dato():
    dato = entrada_dato.get()
    if dato:
        lista_datos.insert(tk.END, dato)
        entrada_dato.delete(0, tk.END)
    else:
        messagebox.showwarning("Campo vacío", "Por favor, ingresa algún texto antes de agregar.")

# Función para limpiar campo de texto y selección de la lista
def limpiar():
    entrada_dato.delete(0, tk.END)
    lista_datos.selection_clear(0, tk.END)
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Gestor de Información")
ventana.geometry("400x400")
ventana.resizable(False, False)

# Etiqueta de instrucción
etiqueta = tk.Label(ventana, text="Ingresa un dato y presiona 'Agregar':")
etiqueta.pack(pady=10)

# Campo de texto
entrada_dato = tk.Entry(ventana, width=40)
entrada_dato.pack(pady=5)

# Botón Agregar
boton_agregar = tk.Button(ventana, text="Agregar", width=15, command=agregar_dato)
boton_agregar.pack(pady=5)

# Botón Limpiar
boton_limpiar = tk.Button(ventana, text="Limpiar", width=15, command=limpiar)
boton_limpiar.pack()

# Lista para mostrar datos
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=10)

#Botón pa limpiar la lista
# Botón Limpiar Lista
boton_limpiar_lista = tk.Button(ventana, text="Limpiar Lista", width=15, command=limpiar_lista)
boton_limpiar_lista.pack(pady=5)

# Ejecutar la aplicación
ventana.mainloop()
