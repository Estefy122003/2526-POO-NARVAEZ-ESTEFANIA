from servicios.inventario import Inventario
from modelos.producto import Producto

def menu():
    inv = Inventario()

    while True:
        print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
        print("1. Añadir Producto\n2. Eliminar\n3. Actualizar\n4. Buscar\n5. Listar Todo\n6. Salir")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == '1':
                id_p = input("ID único: ")
                nom = input("Nombre: ")
                cant = int(input("Cantidad: "))
                pre = float(input("Precio: "))
                inv.añadir_producto(Producto(id_p, nom, cant, pre))
                print("Producto añadido con éxito.")

            elif opcion == '2':
                id_p = input("ID a eliminar: ")
                if inv.eliminar_producto(id_p): print("Eliminado.")
                else: print("No encontrado.")

            elif opcion == '3':
                id_p = input("ID a actualizar: ")
                c = input("Nueva cantidad (dejar vacío para omitir): ")
                p = input("Nuevo precio (dejar vacío para omitir): ")
                cant = int(c) if c else None
                prec = float(p) if p else None
                if inv.actualizar_producto(id_p, cant, prec): print("Actualizado.")
                else: print("Error al actualizar.")

            elif opcion == '4':
                nom = input("Nombre a buscar: ")
                resultados = inv.buscar_por_nombre(nom)
                for r in resultados:
                    print(f"ID: {r.id} | {r.nombre} | Cant: {r.cantidad} | ${r.precio}")

            elif opcion == '5':
                for r in inv.obtener_todos():
                    print(f"ID: {r.id} | {r.nombre} | Cant: {r.cantidad} | ${r.precio}")

            elif opcion == '6':
                print("Saliendo del sistema...")
                break
        except ValueError as e:
            print(f"Error de dato: {e}. Intente de nuevo.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    menu()