from .modelos.ticket import Ticket
from .servicios.impresora_tickets import ImpresoraTickets


def caso_olvido_cerrar() -> None:
    """
    CASO A: el estudiante OLVIDA cerrar la impresora.
    - __del__ de ImpresoraTickets será quien cierre el archivo.
    """
    print("\n=== CASO A: el estudiante OLVIDA cerrar ===")
    impresora = ImpresoraTickets("tickets.txt")
    ticket = Ticket("Cliente Ana", 12.50)
    impresora.imprimir(f"Ticket - {ticket.cliente} - Total: ${ticket.total:.2f}")
    # Simulamos el olvido eliminando la referencia sin llamar a cerrar()
    del impresora


def caso_cierre_correcto() -> None:
    """
    CASO B: el estudiante CIERRA correctamente la impresora.
    """
    print("\n=== CASO B: el estudiante CIERRA correctamente ===")
    impresora = ImpresoraTickets("tickets.txt")
    ticket = Ticket("Cliente Bolivar", 20.00)
    impresora.imprimir(f"Ticket - {ticket.cliente} - Total: ${ticket.total:.2f}")
    impresora.cerrar()


if __name__ == "__main__":
    caso_olvido_cerrar()
    caso_cierre_correcto()
    print("\nRevisa el archivo tickets.txt para ver los tickets guardados.")
