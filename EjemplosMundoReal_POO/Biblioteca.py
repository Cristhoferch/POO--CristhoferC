# Clases del sistema
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        return f"{self.info[0]} por {self.info[1]} (ISBN: {self.isbn}, Categoría: {self.categoria})"

class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []

    def __str__(self):
        return f"{self.nombre} (ID: {self.id_usuario})"

class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}
        self.usuarios_registrados = {}
        self.ids_usuarios = set()
        self.historial_prestamos = []

    def agregar_libro(self):
        titulo = input("Título del libro: ")
        autor = input("Autor del libro: ")
        categoria = input("Categoría: ")
        isbn = input("ISBN: ")
        if isbn not in self.libros_disponibles:
            libro = Libro(titulo, autor, categoria, isbn)
            self.libros_disponibles[isbn] = libro
            print("✅ Libro añadido correctamente.")
        else:
            print("⚠️ Este ISBN ya está registrado.")

    def quitar_libro(self):
        isbn = input("ISBN del libro a eliminar: ")
        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            print("✅ Libro eliminado.")
        else:
            print("⚠️ Libro no encontrado.")

    def registrar_usuario(self):
        nombre = input("Nombre del usuario: ")
        id_usuario = input("ID de usuario único: ")
        if id_usuario not in self.ids_usuarios:
            usuario = Usuario(nombre, id_usuario)
            self.usuarios_registrados[id_usuario] = usuario
            self.ids_usuarios.add(id_usuario)
            print("✅ Usuario registrado correctamente.")
        else:
            print("⚠️ El ID ya está en uso.")

    def dar_baja_usuario(self):
        id_usuario = input("ID del usuario a dar de baja: ")
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            if usuario.libros_prestados:
                print("⚠️ No se puede dar de baja: el usuario tiene libros prestados.")
            else:
                del self.usuarios_registrados[id_usuario]
                self.ids_usuarios.remove(id_usuario)
                print("✅ Usuario dado de baja.")
        else:
            print("⚠️ Usuario no encontrado.")

    def prestar_libro(self):
        id_usuario = input("ID del usuario: ")
        isbn = input("ISBN del libro: ")
        if id_usuario not in self.usuarios_registrados:
            print("⚠️ Usuario no registrado.")
            return
        if isbn not in self.libros_disponibles:
            print("⚠️ Libro no disponible.")
            return
        libro = self.libros_disponibles.pop(isbn)
        self.usuarios_registrados[id_usuario].libros_prestados.append(libro)
        self.historial_prestamos.append((id_usuario, isbn))
        print(f"✅ Libro prestado a {self.usuarios_registrados[id_usuario].nombre}.")

    def devolver_libro(self):
        id_usuario = input("ID del usuario: ")
        isbn = input("ISBN del libro: ")
        if id_usuario not in self.usuarios_registrados:
            print("⚠️ Usuario no registrado.")
            return
        usuario = self.usuarios_registrados[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                self.libros_disponibles[isbn] = libro
                print("✅ Libro devuelto.")
                return
        print("⚠️ Este usuario no tiene ese libro prestado.")

    def buscar_libros(self):
        print("\nBuscar por:\n1. Título\n2. Autor\n3. Categoría")
        opcion = input("Opción (1-3): ")
        valor = input("Buscar: ")
        encontrados = []
        for libro in self.libros_disponibles.values():
            if opcion == "1" and valor.lower() in libro.info[0].lower():
                encontrados.append(libro)
            elif opcion == "2" and valor.lower() in libro.info[1].lower():
                encontrados.append(libro)
            elif opcion == "3" and valor.lower() == libro.categoria.lower():
                encontrados.append(libro)
        print("\n📚 Libros encontrados:")
        if encontrados:
            for l in encontrados:
                print(l)
        else:
            print("⚠️ No se encontraron libros.")

    def listar_prestamos(self):
        id_usuario = input("ID del usuario: ")
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            print(f"\n📚 Libros prestados a {usuario.nombre}:")
            if usuario.libros_prestados:
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print("No tiene libros prestados.")
        else:
            print("⚠️ Usuario no encontrado.")

# Menú interactivo
def menu():
    biblio = Biblioteca()
    while True:
        print("\n===== SISTEMA DE BIBLIOTECA DIGITAL =====")
        print("1. Agregar libro")
        print("2. Quitar libro")
        print("3. Registrar usuario")
        print("4. Dar de baja usuario")
        print("5. Prestar libro")
        print("6. Devolver libro")
        print("7. Buscar libros")
        print("8. Listar libros prestados a un usuario")
        print("9. Salir")
        opcion = input("Elige una opción (1-9): ")

        if opcion == "1":
            biblio.agregar_libro()
        elif opcion == "2":
            biblio.quitar_libro()
        elif opcion == "3":
            biblio.registrar_usuario()
        elif opcion == "4":
            biblio.dar_baja_usuario()
        elif opcion == "5":
            biblio.prestar_libro()
        elif opcion == "6":
            biblio.devolver_libro()
        elif opcion == "7":
            biblio.buscar_libros()
        elif opcion == "8":
            biblio.listar_prestamos()
        elif opcion == "9":
            print("👋 Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("⚠️ Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
