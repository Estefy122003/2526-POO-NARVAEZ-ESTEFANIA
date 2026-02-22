import os

class Producto:
    def __init__(self, id_prod, nombre, cantidad, precio):
        self.id_prod = id_prod
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        # Formato para guardar en el archivo: id,nombre,cantidad,precio
        return f"{self.id_prod},{self.nombre},{self.cantidad},{self.precio}"

class Inventario:
    def __init__(self, archivo="inventario.txt"):
        self.archivo = archivo
        self.productos = {}
        # Al instanciar, cargamos los datos existentes
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Recupera los datos del archivo .txt al iniciar el programa."""
        try:
            # Requisito: Manejar caso en que el archivo no exista
            if not os.path.exists(self.archivo):
                with open(self.archivo, 'w', encoding='utf-8') as f:
                    pass # Crea el archivo vacío
                print(f"[INFO] Archivo '{self.archivo}' no encontrado. Se ha creado uno nuevo.")
                return

            with open(self.archivo, 'r', encoding='utf-8') as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        # Reconstrucción del inventario
                        id_p, nombre, cant, precio = linea.split(',')
                        self.productos[id_p] = Producto(id_p, nombre, int(cant), float(precio))

            print(f"[ÉXITO] Se cargaron {len(self.productos)} productos del archivo.")

        except FileNotFoundError:
            print("[ERROR] El archivo de inventario no pudo ser localizado.")
        except PermissionError:
            print("[ERROR] No tienes permisos para leer el archivo de inventario.")
        except Exception as e:
            print(f"[ERROR] Error inesperado al cargar el archivo: {e}")

    def guardar_en_archivo(self):
        """Refleja los cambios de la memoria en el archivo de texto."""
        try:
            with open(self.archivo, 'w', encoding='utf-8') as f:
                for p in self.productos.values():
                    f.write(str(p) + "\n")
            return True
        except PermissionError:
            print("[ERROR] Error de permisos: No se puede escribir en el archivo.")
            return False
        except Exception as e:
            print(f"[ERROR] No se pudo guardar la información: {e}")
            return False

    def añadir_producto(self, producto):
        if producto.id_prod in self.productos:
            print(f"[AVISO] El ID {producto.id_prod} ya existe.")
        else:
            self.productos[producto.id_prod] = producto
            # Requisito: Modificaciones reflejadas en el archivo
            if self.guardar_en_archivo():
                print(f"[NOTIFICACIÓN] '{producto.nombre}' guardado exitosamente en el archivo.")

    def actualizar_producto(self, id_prod, nueva_cantidad):
        if id_prod in self.productos:
            self.productos[id_prod].cantidad = nueva_cantidad
            if self.guardar_en_archivo():
                print(f"[NOTIFICACIÓN] Cantidad del producto {id_prod} actualizada en el archivo.")
        else:
            print("[ERROR] Producto no encontrado.")

    def eliminar_producto(self, id_prod):
        if id_prod in self.productos:
            eliminado = self.productos.pop(id_prod)
            if self.guardar_en_archivo():
                print(f"[NOTIFICACIÓN] Producto '{eliminado.nombre}' eliminado del archivo.")
        else:
            print("[ERROR] No se encontró el producto para eliminar.")

    def mostrar_inventario(self):
        if not self.productos:
            print("\nEl inventario está vacío.")
        else:
            print("\n--- ESTADO DEL INVENTARIO ---")
            for p in self.productos.values():
                print(f"ID: {p.id_prod} | Nombre: {p.nombre} | Stock: {p.cantidad} | Precio: ${p.precio}")

# --- Interfaz de Usuario ---
def ejecutar_menu():
    mi_inventario = Inventario()

    while True:
        print("\n--- SISTEMA DE GESTIÓN DE INVENTARIOS ---")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Cantidad")
        print("4. Mostrar Inventario")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                id_p = input("ID del producto: ")
                nom = input("Nombre: ")
                can = int(input("Cantidad: "))
                pre = float(input("Precio: "))
                mi_inventario.añadir_producto(Producto(id_p, nom, can, pre))
            except ValueError:
                print("[ERROR] Por favor, ingrese valores numéricos válidos para cantidad y precio.")

        elif opcion == "2":
            id_p = input("Ingrese el ID a eliminar: ")
            mi_inventario.eliminar_producto(id_p)

        elif opcion == "3":
            try:
                id_p = input("ID del producto: ")
                can = int(input("Nueva cantidad: "))
                mi_inventario.actualizar_producto(id_p, can)
            except ValueError:
                print("[ERROR] Cantidad inválida.")

        elif opcion == "4":
            mi_inventario.mostrar_inventario()

        elif opcion == "5":
            print("Cerrando el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    ejecutar_menu()