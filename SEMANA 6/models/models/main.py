
# main.py
# -------------------------------------------------------------
# Punto de entrada del programa. Crea objetos, usa herencia,
# encapsulación y demuestra polimorfismo.
# -------------------------------------------------------------

from models.animal import Perro, Gato
from services.zoologico_service import ZoologicoService


def main():
    # Crear instancias de clases derivadas
    perro = Perro("Firulais", 4)
    gato = Gato("Mishi", 2)

    # Modificar atributo usando setter (encapsulación)
    gato.nombre = "Bigotes"

    # Lista de animales (polimorfismo)
    animales = [perro, gato]

    # Usar el servicio
    zoo = ZoologicoService()
    zoo.mostrar_sonidos(animales)


if __name__ == "__main__":
    main()
