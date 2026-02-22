import json
import os
from modelos.producto import Producto

class Inventario:
    def __init__(self, archivo='data/inventario.json'):
        self.archivo = archivo
        self.productos = {} # Estructura de datos: Diccionario para búsqueda rápida por ID
        self.cargar_desde_archivo()

    def añadir_producto(self, producto):
        if producto.id in self.productos:
            raise ValueError("El ID ya existe en el inventario.")
        self.productos[producto.id] = producto
        self.guardar_en_archivo()

    def eliminar_producto(self, id_prod):
        if id_prod in self.productos:
            del self.productos[id_prod]
            self.guardar_en_archivo()
        else:
            raise KeyError("El producto no existe.")

    def buscar_por_nombre(self, nombre):
        # Búsqueda con coincidencia parcial
        return [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]

    def guardar_en_archivo(self):
        try:
            with open(self.archivo, 'w') as f:
                datos = {id_p: p.to_dict() for id_p, p in self.productos.items()}
                json.dump(datos, f, indent=4)
        except IOError as e:
            print(f"Error al guardar los datos: {e}")

    def cargar_desde_archivo(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as f:
                    datos = json.load(f)
                    for id_p, d in datos.items():
                        self.productos[id_p] = Producto(id_p, d['nombre'], d['cantidad'], d['precio'])
            except (json.JSONDecodeError, IOError):
                print("Error al cargar el archivo. Iniciando inventario vacío.")