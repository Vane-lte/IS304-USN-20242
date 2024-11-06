# Función para agregar productos al inventario
def agregar_producto(inventario, nombre_producto, cantidad):
    if nombre_producto in inventario:
        inventario[nombre_producto] += cantidad
    else:
        inventario[nombre_producto] = cantidad
    print(f"Producto '{nombre_producto}' agregado o actualizado con éxito.")

# Función para eliminar una cantidad específica de un producto
def eliminar_producto(inventario, nombre_producto, cantidad):
    if nombre_producto in inventario:
        if inventario[nombre_producto] >= cantidad:
            inventario[nombre_producto] -= cantidad
            if inventario[nombre_producto] == 0:
                del inventario[nombre_producto]  # Eliminar producto si la cantidad es 0
            print(f"Se han eliminado {cantidad} unidades de '{nombre_producto}'.")
        else:
            print(f"No hay suficientes unidades de '{nombre_producto}' para eliminar.")
    else:
        print(f"El producto '{nombre_producto}' no se encuentra en el inventario.")

# Función para mostrar productos con cantidades bajas
def mostrar_productos_bajos(inventario, limite_bajo):
    productos_bajos = {producto for producto, cantidad in inventario.items() if cantidad <= limite_bajo}
    
    if productos_bajos:
        print("Productos con cantidades bajas:")
        for producto in productos_bajos:
            print(f" - {producto}: {inventario[producto]} unidades")
    else:
        print("No hay productos con cantidades bajas.")

# Función para mostrar todo el inventario
def mostrar_inventario(inventario):
    inventario_lista = [(producto, cantidad) for producto, cantidad in inventario.items()]
    print("\nInventario actual:")
    for producto, cantidad in sorted(inventario_lista):
        print(f" - {producto}: {cantidad} unidades")

# Función principal (main) que gestiona el inventario
def main():
    inventario = {}  # Diccionario para almacenar el inventario de productos
    while True:
        print("\n--- Gestión de Inventario ---")
        print("1. Agregar producto")
        print("2. Eliminar cantidad de producto")
        print("3. Mostrar productos con cantidades bajas")
        print("4. Mostrar todo el inventario")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            nombre_producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            agregar_producto(inventario, nombre_producto, cantidad)
        
        elif opcion == "2":
            nombre_producto = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad a eliminar: "))
            eliminar_producto(inventario, nombre_producto, cantidad)
        
        elif opcion == "3":
            limite_bajo = int(input("Ingrese el límite bajo de cantidad: "))
            mostrar_productos_bajos(inventario, limite_bajo)
        
        elif opcion == "4":
            mostrar_inventario(inventario)
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

# Punto de entrada del programa
if __name__ == '__main__':
    main()
