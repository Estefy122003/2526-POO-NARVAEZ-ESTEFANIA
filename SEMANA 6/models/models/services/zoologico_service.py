# services/zoologico_service.py
# -------------------------------------------------------------
# Servicio que usa polimorfismo: recibe cualquier Animal y llama
# al método hacer_sonido() sin importar cuál clase hija sea.
# -------------------------------------------------------------


class ZoologicoService:

    def mostrar_sonidos(self, animales: list):
        """Muestra los sonidos de distintos animales (polimorfismo)."""
        for animal in animales:
            print(f"{animal.nombre} hace: {animal.hacer_sonido()}")
