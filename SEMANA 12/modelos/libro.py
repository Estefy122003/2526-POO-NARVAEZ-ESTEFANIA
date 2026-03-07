class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Título y autor almacenados como tupla (inmutable)
        self.info = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    def obtener_titulo(self):
        return self.info[0]

    def obtener_autor(self):
        return self.info[1]

    def __str__(self):
        return f"{self.info[0]} - {self.info[1]} | Categoría: {self.categoria} | ISBN: {self.isbn}"