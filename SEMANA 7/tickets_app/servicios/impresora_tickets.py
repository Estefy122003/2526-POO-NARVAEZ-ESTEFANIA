from __future__ import annotations
from typing import Optional, TextIO
from datetime import datetime


class ImpresoraTickets:
    """
    Simula una impresora escribiendo en un archivo de texto.

    __init__: abre el recurso (archivo).
    cerrar(): cierre explícito (mejor práctica).
    __del__: cierra si el estudiante olvidó hacerlo (liberación de recursos).
    """

    def __init__(self, ruta_archivo: str = "tickets.txt") -> None:
        self.ruta_archivo: str = ruta_archivo
        self._f: Optional[TextIO] = None

        try:
            self._f = open(self.ruta_archivo, mode="a", encoding="utf-8")
            self._escribir_linea(f"=== Inicio sesión impresión {datetime.now():%Y-%m-%d %H:%M:%S} ===")
        except OSError as e:
            print(f"[ImpresoraTickets] No se pudo abrir '{self.ruta_archivo}': {e}")
            self._f = None

    def imprimir(self, texto: str) -> None:
        """
        Imprime una línea en el archivo.
        """
        if self._f is None:
            print("[ImpresoraTickets] No hay archivo de salida disponible.")
            return
        self._escribir_linea(texto)

    def cerrar(self) -> None:
        """
        Cierre explícito del archivo (recomendado).
        """
        if self._f is not None and not self._f.closed:
            self._escribir_linea(
                f"=== Cierre sesión impresión {datetime.now():%Y-%m-%d %H:%M:%S} (cerrar explícito) ===\n"
            )
            self._f.close()

    # ----------------- utilitaria interna -----------------
    def _escribir_linea(self, linea: str) -> None:
        if self._f is not None:
            self._f.write(linea + "\n")
            self._f.flush()
        else:
            print(linea)

    def __del__(self) -> None:
        """
        Si el archivo quedó abierto por olvido, lo cerramos aquí.
        """
        try:
            if self._f is not None and not self._f.closed:
                self._escribir_linea(
                    f"=== Cierre sesión impresión {datetime.now():%Y-%m-%d %H:%M:%S} (via __del__) ===\n"
                )
                self._f.close()
                print(f"[__del__ ImpresoraTickets] '{self.ruta_archivo}' cerrado en __del__ (olvido de cerrar).")
        except Exception:
            # Nunca lances errores desde __del__
            pass
