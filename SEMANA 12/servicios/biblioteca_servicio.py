class BibliotecaServicio:

    def __init__(self):

        # Diccionario de libros disponibles
        # clave = ISBN
        # valor = objeto Libro
        self.libros_disponibles = {}

        # Diccionario de usuarios
        self.usuarios = {}

        # Set para IDs únicos
        self.ids_usuarios = set()

    # Añadir libro
    def añadir_libro(self, libro):

        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            return True
        return False

    # Quitar libro
    def quitar_libro(self, isbn):

        if isbn in self.libros_disponibles:
            del self.libros_disponibles[isbn]
            return True
        return False

    # Registrar usuario
    def registrar_usuario(self, usuario):

        if usuario.id_usuario not in self.ids_usuarios:

            self.ids_usuarios.add(usuario.id_usuario)
            self.usuarios[usuario.id_usuario] = usuario
            return True

        return False

    # Dar de baja usuario
    def dar_de_baja_usuario(self, id_usuario):

        if id_usuario in self.usuarios:

            usuario = self.usuarios[id_usuario]

            if len(usuario.libros_prestados) == 0:

                del self.usuarios[id_usuario]
                self.ids_usuarios.remove(id_usuario)
                return True

        return False

    # Prestar libro
    def prestar_libro(self, isbn, id_usuario):

        if isbn in self.libros_disponibles and id_usuario in self.usuarios:

            libro = self.libros_disponibles.pop(isbn)

            usuario = self.usuarios[id_usuario]

            usuario.libros_prestados.append(libro)

            return True

        return False

    # Devolver libro
    def devolver_libro(self, isbn, id_usuario):

        if id_usuario in self.usuarios:

            usuario = self.usuarios[id_usuario]

            for libro in usuario.libros_prestados:

                if libro.isbn == isbn:

                    usuario.libros_prestados.remove(libro)

                    self.libros_disponibles[isbn] = libro

                    return True

        return False

    # Buscar libros
    def buscar_libros(self, criterio, valor):

        resultados = []

        for libro in self.libros_disponibles.values():

            if criterio == "titulo" and valor.lower() in libro.obtener_titulo().lower():
                resultados.append(libro)

            elif criterio == "autor" and valor.lower() in libro.obtener_autor().lower():
                resultados.append(libro)

            elif criterio == "categoria" and valor.lower() in libro.categoria.lower():
                resultados.append(libro)

        return resultados

    # Listar libros prestados
    def listar_prestados(self, id_usuario):

        if id_usuario in self.usuarios:
            return self.usuarios[id_usuario].libros_prestados

        return []