from servicios.inventario import Inventario
from modelos.producto import Producto

def menu():
    inv = Inventario()
    while True:
        print("\n--- MENÚ DE INVENTARIO ---")
        print("1. Añadir | 2. Eliminar | 3. Actualizar | 4. Buscar | 5. Listar | 6. Salir")
        opc = input("Seleccione una opción: ")

        try:
            if opc == '1':
                id_p = input("ID: ")
                nom = input("Nombre: ")
                cant = int(input("Cantidad: "))
                pre = float(input("Precio: "))
                inv.añadir_producto(Producto(id_p, nom, cant, pre))
                print("Producto añadido.")
            # ... implementar el resto de opciones siguiendo la misma lógica ...
            elif opc == '6':
                break
        except ValueError as e:
            print(f"Error de entrada: {e}")

if __name__ == "__main__":
    menu()