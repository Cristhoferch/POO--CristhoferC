# Sistema simple de gestión de inventario

# Diccionario que almacenará todos los productos
inventario = {}

while True:
    # Menú principal mostrado en consola
    print("\n--- MENÚ DE INVENTARIO ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto por nombre")
    print("5. Mostrar todos")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    # Opción 1: Añadir un nuevo producto

    if opcion == "1":
        id_prod = input("ID del producto: ")
        if id_prod in inventario:
            print("❌ Ese ID ya existe.")
        else:
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            inventario[id_prod] = {"nombre": nombre, "cantidad": cantidad, "precio": precio}
            print("✅ Producto agregado.")

    # Opción 2: Eliminar un producto

    elif opcion == "2":
        id_prod = input("ID a eliminar: ")
        if id_prod in inventario:
            del inventario[id_prod]
            print("✅ Producto eliminado.")
        else:
            print("❌ No encontrado.")

    # Opción 3: Actualizar cantidad o precio

    elif opcion == "3":
        id_prod = input("ID a actualizar: ")
        if id_prod in inventario:
            cant = input("Nueva cantidad (Enter para no cambiar): ")
            prec = input("Nuevo precio (Enter para no cambiar): ")
            if cant: inventario[id_prod]["cantidad"] = int(cant)
            if prec: inventario[id_prod]["precio"] = float(prec)
            print("✅ Actualizado.")
        else:
            print("❌ No encontrado.")

    # Opción 4: Buscar productos por nombre

    elif opcion == "4":
        nombre_busq = input("Nombre a buscar: ").lower()
        encontrados = [p for p in inventario.values() if nombre_busq in p["nombre"].lower()]
        if encontrados:
            for p in encontrados:
                print(f"{p['nombre']} - Cantidad: {p['cantidad']} - Precio: ${p['precio']:.2f}")
        else:
            print("❌ No encontrado.")

    # Opción 5: Mostrar todos los productos

    elif opcion == "5":
        if inventario:
            for idp, p in inventario.items():
                print(f"ID: {idp} | {p['nombre']} - Cantidad: {p['cantidad']} - Precio: ${p['precio']:.2f}")
        else:
            print(" Inventario vacío.")

    # Opción 6: Salir del programa

    elif opcion == "6":
        print(" Saliendo...")
        break

    # Manejo de opción inválida

    else:
        print(" Opción inválida.")
