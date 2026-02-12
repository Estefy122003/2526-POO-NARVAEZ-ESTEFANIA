from __future__ import annotations


class Ticket:
    """
    Ticket simple:
    - cliente: nombre del cliente
    - total: monto total

    __init__: inicializa los datos obligatorios.
    __del__: mensaje didáctico para evidenciar destrucción.
    """

    def __init__(self, cliente: str, total: float) -> None:
        if not cliente:
            raise ValueError("El nombre del cliente es obligatorio.")
        try:
            self.total: float = float(total)
        except (TypeError, ValueError):
            raise ValueError("El total debe ser numérico.")
        self.cliente: str = cliente

    def __del__(self) -> None:
        # El momento exacto depende del GC
        try:
            print(f"[__del__ Ticket] Ticket de '{self.cliente}' destruido.")
        except Exception:
            # Nunca propagues errores desde __del__
            pass
