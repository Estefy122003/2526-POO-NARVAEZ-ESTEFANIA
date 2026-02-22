import json
import os
from modelos.producto import Producto

class Inventario:
    def __init__(self, archivo='inventario.json'):
        self.archivo = archivo
        self.productos = self._cargar_datos()

    def _cargar_datos(self):
        """Carga datos desde un archivo JSON al iniciar."""
        if not os.path.exists(self.archivo):
            return {}
        try:
            with open(self.archivo, 'r') as f:
                datos = json.load(f)
                # Reconstruir objetos Producto
                return {id_p: Producto(id_p, v['nombre'], v['cantidad'], v['precio'])
                        for id_p, v in datos.items()}
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def guardar_datos(self):
        """Persistencia de datos en JSON."""
        with open(self.archivo, 'w') as f:
            json.dump({id_p: p.to_dict() for id_p, p in self.productos.items()}, f, indent=4)

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            raise ValueError(f"Error: El ID {producto.id} ya existe.")
        self.productos[producto.id] = producto
        self.guardar_datos()

    def eliminar_producto(self, id_prod):
        if id_prod in self.productos:
            del self.productos[id_prod]
            self.guardar_datos()
            return True
        return False

    def actualizar_producto(self, id_prod, cantidad=None, precio=None):
        if id_prod in self.productos:
            if cantidad is not None: self.productos[id_prod].cantidad = cantidad
            if precio is not None: self.productos[id_prod].precio = precio
            self.guardar_datos()
            return True
        return False

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]

    def obtener_todos(self):
        return self.productos.values()