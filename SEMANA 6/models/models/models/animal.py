# models/animal.py
# -------------------------------------------------------------
# Este archivo demuestra:
# - Clase Base: Animal
# - Herencia: Perro y Gato
# - Encapsulación: uso de atributos privados y getters/setters
# - Polimorfismo: método hacer_sonido() definido distinto en cada clase
# -------------------------------------------------------------


class Animal:
    """Clase base: representa un animal genérico."""

    def __init__(self, nombre: str, edad: int):
        # Encapsulación: atributos privados
        self._nombre = nombre
        self._edad = edad

    # Getter del nombre
    @property
    def nombre(self):
        return self._nombre

    # Setter con validación
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre.strip() == "":
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nuevo_nombre

    # Método que será redefinido (polimorfismo)
    def hacer_sonido(self):
        return "Sonido genérico"


# Clase derivada 1
class Perro(Animal):

    def hacer_sonido(self):
        return "Guau Guau"


# Clase derivada 2
class Gato(Animal):

    def hacer_sonido(self):
        return "Miau Miau"
