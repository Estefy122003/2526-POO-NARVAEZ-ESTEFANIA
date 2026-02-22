import json
import os


class Producto:
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters y Setters
    def get_id(self): return self._id

    def get_nombre(self): return self._nombre

    def get_cantidad(self): return self._cantidad

    def get_precio(self): return self._precio

    def set_cantidad(self, cantidad): self._cantidad = cantidad

    def set_precio(self, precio): self._precio = precio

    def to_dict(self):
        """Convierte el objeto a diccionario para serialización JSON."""
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }


class Inventario:
    def __init__(self):
        # Usamos un diccionario para búsqueda rápida por ID
        self.productos = {}
        self.archivo = "inventario.json"
        self.cargar_desde_archivo()

    def añadir_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Error: El ID ya existe.")
        else:
            self.productos[producto.get_id()] = producto
            self.guardar_en_archivo()
            print("Producto añadido con éxito.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar_en_archivo()
            print("Producto eliminado.")
        else:
            print("Error: Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None: self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None: self.productos[id_producto].set_precio(precio)
            self.guardar_en_archivo()
            print("Producto actualizado.")
        else:
            print("Error: ID no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [p for p in self.productos.values() if nombre.lower() in p.get_nombre().lower()]
        return encontrados

    def mostrar_todos(self):
        return list(self.productos.values())

    # Persistencia de Datos
    def guardar_en_archivo(self):
        try:
            with open(self.archivo, 'w') as f:
                # Serializamos la colección
                datos = {id_p: p.to_dict() for id_p, p in self.productos.items()}
                json.dump(datos, f, indent=4)
        except Exception as e:
            print(f"Error al guardar: {e}")

    def cargar_desde_archivo(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as f:
                    datos = json.load(f)
                    for d in datos.values():
                        p = Producto(d['id'], d['nombre'], d['cantidad'], d['precio'])
                        self.productos[p.get_id()] = p
            except Exception as e:
                print(f"Error al cargar: {e}")


# Interfaz de Usuario (Consola)
def menu():
    inv = Inventario()
    while True:
        print("\n--- SISTEMA DE GESTIÓN DE INVENTARIO ---")
        print("1. Añadir Producto\n2. Eliminar\n3. Actualizar\n4. Buscar\n5. Mostrar Todo\n6. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            id_p = input("ID único: ")
            nom = input("Nombre: ")
            cant = int(input("Cantidad: "))
            pre = float(input("Precio: "))
            inv.añadir_producto(Producto(id_p, nom, cant, pre))

        elif opcion == '2':
            id_p = input("ID a eliminar: ")
            inv.eliminar_producto(id_p)

        elif opcion == '3':
            id_p = input("ID a actualizar: ")
            c = input("Nueva cantidad (dejar vacío para no cambiar): ")
            p = input("Nuevo precio (dejar vacío para no cambiar): ")
            inv.actualizar_producto(id_p, int(c) if c else None, float(p) if p else None)

        elif opcion == '4':
            nom = input("Nombre a buscar: ")
            resultados = inv.buscar_por_nombre(nom)
            for r in resultados:
                print(f"ID: {r.get_id()} | {r.get_nombre()} | Cant: {r.get_cantidad()} | ${r.get_precio()}")

        elif opcion == '5':
            for r in inv.mostrar_todos():
                print(f"ID: {r.get_id()} | {r.get_nombre()} | Cant: {r.get_cantidad()} | ${r.get_precio()}")

        elif opcion == '6':
            break


if __name__ == "__main__":
    menu()