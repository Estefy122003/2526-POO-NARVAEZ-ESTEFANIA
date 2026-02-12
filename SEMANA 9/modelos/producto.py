class Producto:
    def __init__(self, id_prod, nombre, cantidad, precio):
        self.__id = id_prod  # Atributos privados (Encapsulamiento)
        self.__nombre = nombre
        self.__cantidad = cantidad
        self.__precio = precio

    # Getters y Setters
    @property
    def id(self): return self.__id

    @property
    def nombre(self): return self.__nombre
    @nombre.setter
    def nombre(self, valor): self.__nombre = valor

    @property
    def cantidad(self): return self.__cantidad
    @cantidad.setter
    def cantidad(self, valor): self.__cantidad = valor

    @property
    def precio(self): return self.__precio
    @precio.setter
    def precio(self, valor): self.__precio = valor

    def to_dict(self):
        return {"id": self.__id, "nombre": self.__nombre, "cantidad": self.__cantidad, "precio": self.__precio}