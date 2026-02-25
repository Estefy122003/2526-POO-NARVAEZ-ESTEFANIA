import os

class Producto:
    """Representa un producto individual en el inventario."""
    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.cantidad = int(cantidad)
        self.precio = float(precio)

    def __str__(self):
        return f"ID: {self.id_producto:4} | Producto: {self.nombre:15} | Stock: {self.cantidad:5} | Precio: ${self.precio:8.2f}"

    def formato_archivo(self):
        """Prepara los datos para ser escritos en el archivo .txt"""
        return f"{self.id_producto},{self.nombre},{self.cantidad},{self.precio}\n"


class Inventario:
    """Gestiona la lógica de almacenamiento y persistencia en archivos."""
    def __init__(self, nombre_archivo="inventario.txt"):
        self.nombre_archivo = nombre_archivo
        self.productos = {}
        # Carga automática al instanciar la clase
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """Lee el archivo .txt y reconstruye el diccionario de productos."""
        try:
            # Si el archivo no existe, lo creamos preventivamente
            if not os.path.exists(self.nombre_archivo):
                with open(self.nombre_archivo, 'w', encoding='utf-8') as f:
                    pass
                return

            with open(self.nombre_archivo, 'r', encoding='utf-8') as f:
                for num_linea, linea in enumerate(f, 1):
                    linea = linea.strip()
                    if not linea: continue # Saltar líneas vacías

                    try:
                        id_p, nombre, cant, precio = linea.split(',')
                        self.productos[id_p] = Producto(id_p, nombre, cant, precio)
                    except ValueError:
                        print(f"⚠️ Advertencia: Error de formato en línea {num_linea}. Se omitió este registro.")

            print("✅ Datos cargados correctamente desde el almacenamiento.")

        except PermissionError:
            print("❌ Error: No se tienen permisos para leer el archivo.")
        except Exception as e:
            print(f"❌ Error inesperado al cargar: {e}")

    def guardar_en_archivo(self):
        """Sobrescribe el archivo con la información actual del diccionario."""
        try:
            with open(self.nombre_archivo, 'w', encoding='utf-8') as f:
                for p in self.productos.values():
                    f.write(p.formato_archivo())
        except PermissionError:
            print("❌ Error: No se pudo escribir en el archivo (Permiso denegado).")
        except Exception as e:
            print(f"❌ Error al guardar datos: {e}")

    def agregar(self, producto):
        if producto.id_producto in self.productos:
            print("❌ Error: Ya existe un producto con ese ID.")
        else:
            self.productos[producto.id_producto] = producto
            self.guardar_en_archivo()
            print(f"✅ '{producto.nombre}' guardado exitosamente.")

    def actualizar(self, id_p, nueva_cantidad):
        if id_p in self.productos:
            self.productos[id_p].cantidad = nueva_cantidad
            self.guardar_en_archivo()
            print(f"✅ Stock de ID {id_p} actualizado en el archivo.")
        else:
            print("❌ Error: El producto no existe.")

    def eliminar(self, id_p):
        if id_p in self.productos:
            eliminado = self.productos.pop(id_p)
            self.guardar_en_archivo()
            print(f"🗑️ Producto '{eliminado.nombre}' eliminado del archivo.")
        else:
            print("❌ Error: No se encontró el ID.")

    def listar(self):
        if not self.productos:
            print("\n--- El inventario está vacío ---")
        else:
            print("\n--- INVENTARIO ACTUAL ---")
            for p in self.productos.values():
                print(p)


def ejecutar_menu():
    """Interfaz de consola para interactuar con el usuario."""
    sistema = Inventario()

    while True:
        print("\n--- MENÚ DE GESTIÓN (PERSISTENTE) ---")
        print("1. Agregar producto")
        print("2. Ver inventario")
        print("3. Actualizar stock")
        print("4. Eliminar producto")
        print("5. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            try:
                id_i = input("ID: ")
                nom = input("Nombre: ")
                can = int(input("Cantidad: "))
                pre = float(input("Precio: "))
                sistema.agregar(Producto(id_i, nom, can, pre))
            except ValueError:
                print("❌ Error: Cantidad y Precio deben ser números.")

        elif opcion == '2':
            sistema.listar()

        elif opcion == '3':
            id_i = input("ID del producto: ")
            try:
                nueva_can = int(input("Nueva cantidad: "))
                sistema.actualizar(id_i, nueva_can)
            except ValueError:
                print("❌ Error: Ingresa un número válido.")

        elif opcion == '4':
            id_i = input("ID a eliminar: ")
            sistema.eliminar(id_i)

        elif opcion == '5':
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❓ Opción no válida.")

if __name__ == "__main__":
    ejecutar_menu()