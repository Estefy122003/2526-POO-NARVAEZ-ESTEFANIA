from modelos.libro import Libro
from modelos.usuario import Usuario

class BibliotecaServicio:
    def __init__(self):
        # Diccionario para libros: Clave=ISBN, Valor=Objeto Libro (Requisito técnico)
        self.libros_disponibles = {}
        # Diccionario para objetos usuario: Clave=ID_Usuario, Valor=Objeto Usuario
        self.usuarios_registrados = {}
        # Conjunto (set) para IDs únicos (Requisito técnico)
        self.ids_usuarios = set()

    def añadir_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro añadido: {libro.info[0]}")
        else:
            print("Error: El ISBN ya existe en el sistema.")

    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            eliminado = self.libros_disponibles.pop(isbn)
            print(f"Libro eliminado: {eliminado.info[0]}")
        else:
            print("Error: Libro no encontrado.")

    def registrar_usuario(self, usuario):
        if usuario.id_usuario not in self.ids_usuarios:
            self.usuarios_registrados[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario registrado: {usuario.nombre}")
        else:
            print("Error: El ID de usuario ya está registrado.")

    def dar_de_baja_usuario(self, id_usuario):
        if id_usuario in self.ids_usuarios:
            # Validar que no tenga libros pendientes
            if not self.usuarios_registrados[id_usuario].libros_prestados:
                self.usuarios_registrados.pop(id_usuario)
                self.ids_usuarios.remove(id_usuario)
                print(f"Usuario con ID {id_usuario} eliminado.")
            else:
                print("Error: El usuario tiene libros pendientes de devolución.")
        else:
            print("Error: Usuario no encontrado.")

    def prestar_libro(self, isbn, id_usuario):
        if isbn in self.libros_disponibles and id_usuario in self.usuarios_registrados:
            libro = self.libros_disponibles.pop(isbn)
            self.usuarios_registrados[id_usuario].libros_prestados.append(libro)
            print(f"Préstamo exitoso: '{libro.info[0]}' entregado a {self.usuarios_registrados[id_usuario].nombre}")
        else:
            print("Error: Libro o Usuario no disponible.")

    def devolver_libro(self, isbn, id_usuario):
        if id_usuario in self.usuarios_registrados:
            usuario = self.usuarios_registrados[id_usuario]
            for i, libro in enumerate(usuario.libros_prestados):
                if libro.isbn == isbn:
                    libro_devuelto = usuario.libros_prestados.pop(i)
                    self.libros_disponibles[isbn] = libro_devuelto
                    print(f"Devolución exitosa: '{libro_devuelto.info[0]}'")
                    return
            print("Error: El usuario no tiene ese libro.")
        else:
            print("Error: Usuario no registrado.")

    def buscar_libros(self, criterio, valor):
        # Búsqueda por Título (index 0 de tupla), Autor (index 1) o Categoría
        resultados = []
        for libro in self.libros_disponibles.values():
            if criterio == "titulo" and valor.lower() in libro.info[0].lower():
                resultados.append(libro)
            elif criterio == "autor" and valor.lower() in libro.info[1].lower():
                resultados.append(libro)
            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)
        return resultados

    def listar_libros_usuario(self, id_usuario):
        if id_usuario in self.usuarios_registrados:
            return self.usuarios_registrados[id_usuario].libros_prestados
        return []