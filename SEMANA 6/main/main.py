class Animal:
    """Clase base que representa un animal genérico (POO)."""

    def __init__(self, nombre: str):
        self._nombre = None
        self.nombre = nombre  # usa el setter (encapsulación)

    @property
    def nombre(self) -> str:
        return self._nombre  # type: ignore[return-value]

    @nombre.setter
    def nombre(self, nuevo_nombre: str) -> None:
        if not nuevo_nombre or not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nuevo_nombre.strip().title()

    def hacer_sonido(self) -> str:
        return "Sonido genérico"


class Perro(Animal):
    def hacer_sonido(self) -> str:
        return "Guau Guau"


class Gato(Animal):
    def hacer_sonido(self) -> str:
        return "Miau Miau"

