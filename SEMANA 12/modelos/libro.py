class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Almacenamos titulo y autor como tupla (Requisito)
        self.detalles = (titulo, autor)
        self.categoria = categoria
        self.isbn = isbn

    @property
    def titulo(self): return self.detalles[0]

    @property
    def autor(self): return self.detalles[1]

    def __str__(self):
        return f"[{self.isbn}] {self.titulo} - {self.autor} ({self.categoria})"