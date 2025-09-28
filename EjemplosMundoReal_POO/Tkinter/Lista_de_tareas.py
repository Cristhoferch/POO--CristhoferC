import tkinter as tk
from tkinter import ttk, messagebox


class TodoListApp:
    def __init__(self, root):
        """
        Inicializa la aplicación de lista de tareas.
        """
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("500x300")

        # Lista para almacenar las tareas
        self.tasks = []

        # Configurar la interfaz
        self.setup_ui()

    def setup_ui(self):
        """Configura todos los elementos de la interfaz de usuario."""

        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Campo de entrada para nuevas tareas
        ttk.Label(main_frame, text="Nueva Tarea:").pack(anchor=tk.W, pady=(0, 5))

        self.task_entry = ttk.Entry(main_frame, width=40)
        self.task_entry.pack(fill=tk.X, pady=(0, 10))

        # Frame para los botones
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(0, 10))

        # Botones de acción
        self.add_button = ttk.Button(button_frame, text="Añadir Tarea (enter)",
                                     command=self.add_task)
        self.add_button.pack(side=tk.LEFT, padx=(0, 5))

        self.complete_button = ttk.Button(button_frame, text="Marcar Completada (ctrl+c)",
                                          command=self.mark_completed)
        self.complete_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = ttk.Button(button_frame, text="Eliminar Tarea (ctrl+x)",
                                        command=self.delete_task)
        self.delete_button.pack(side=tk.LEFT, padx=5)

        # Lista de tareas usando Listbox
        self.setup_task_list(main_frame)

        # Configurar eventos del teclado
        self.setup_keyboard_events()

    def setup_task_list(self, parent_frame):
        """Configura el Listbox para mostrar las tareas."""
        # Frame para la lista y scrollbar
        list_frame = ttk.Frame(parent_frame)
        list_frame.pack(fill=tk.BOTH, expand=True)

        # Listbox para las tareas
        self.task_listbox = tk.Listbox(list_frame, height=15)
        self.task_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Scrollbar para la lista
        scrollbar = ttk.Scrollbar(list_frame, command=self.task_listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.task_listbox.config(yscrollcommand=scrollbar.set)

        # Configurar evento de doble clic
        self.task_listbox.bind("<Double-1>", self.on_double_click)

    def setup_keyboard_events(self):
        """Configura los eventos del teclado."""
        # Enter para añadir tarea
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        # Atajos de teclado
        self.root.bind("<Control-x>", lambda event: self.delete_task())
        self.root.bind("<Control-c>", lambda event: self.mark_completed())

    def add_task(self):
        """Añade una nueva tarea a la lista."""
        task_text = self.task_entry.get().strip()

        if task_text:
            # Añadir a la lista interna
            self.tasks.append({
                "text": task_text,
                "completed": False
            })

            # Actualizar la vista
            self.refresh_task_list()

            # Limpiar el campo de entrada
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Entrada vacía",
                                   "Por favor, escribe una tarea antes de añadirla.")

    def mark_completed(self):
        """Marca la tarea seleccionada como completada."""
        selected_index = self.task_listbox.curselection()

        if selected_index:
            index = selected_index[0]
            self.tasks[index]["completed"] = True
            self.refresh_task_list()
        else:
            messagebox.showwarning("Ninguna tarea seleccionada",
                                   "Por favor, selecciona una tarea para marcar como completada.")

    def delete_task(self):
        """Elimina la tarea seleccionada."""
        selected_index = self.task_listbox.curselection()

        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.refresh_task_list()
        else:
            messagebox.showwarning("Ninguna tarea seleccionada",
                                   "Por favor, selecciona una tarea para eliminar.")

    def on_double_click(self, event):
        """Maneja el evento de doble clic en una tarea."""
        # Marcar como completada/incompleta al hacer doble clic
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["completed"] = not self.tasks[index]["completed"]
            self.refresh_task_list()

    def refresh_task_list(self):
        """Actualiza la vista de la lista de tareas."""
        # Limpiar la lista actual
        self.task_listbox.delete(0, tk.END)

        # Añadir todas las tareas con formato
        for task in self.tasks:
            if task["completed"]:
                # Tarea completada - tachada
                display_text = f"✓ {task['text']}"
                self.task_listbox.insert(tk.END, display_text)
                # Cambiar color para tareas completadas
                self.task_listbox.itemconfig(tk.END, {'fg': 'gray'})
            else:
                # Tarea pendiente
                display_text = f"⏰ {task['text']}"
                self.task_listbox.insert(tk.END, display_text)


def main():
    """Función principal que inicia la aplicación."""
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()