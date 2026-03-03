from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca_servicio import BibliotecaServicio


def ejecutar_menu():

    servicio = BibliotecaServicio()

    # Datos iniciales
    servicio.añadir_libro(Libro("Don Quijote", "Cervantes", "Clasico", "999"))
    servicio.registrar_usuario(Usuario("Orlando", "U1"))

    while True:

        print("\n--- GESTIÓN DE BIBLIOTECA ---")
        print("1. Añadir Libro")
        print("2. Prestar Libro")
        print("3. Devolver Libro")
        print("4. Buscar Libro")
        print("5. Listar libros prestados")
        print("6. Salir")

        op = input("Seleccione: ")

        if op == "1":

            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")

            libro = Libro(titulo, autor, categoria, isbn)

            servicio.añadir_libro(libro)

        elif op == "2":

            isbn = input("ISBN: ")
            id_usuario = input("ID Usuario: ")

            servicio.prestar_libro(isbn, id_usuario)

        elif op == "3":

            isbn = input("ISBN: ")
            id_usuario = input("ID Usuario: ")

            servicio.devolver_libro(isbn, id_usuario)

        elif op == "4":

            criterio = input("Criterio (titulo/autor/categoria): ")
            valor = input("Texto a buscar: ")

            resultados = servicio.buscar_libros(criterio, valor)

            for libro in resultados:
                print(libro)

        elif op == "5":

            id_usuario = input("ID Usuario: ")

            libros = servicio.listar_prestados(id_usuario)

            for libro in libros:
                print(libro)

        elif op == "6":

            print("Saliendo...")
            break


if __name__ == "__main__":
    ejecutar_menu()