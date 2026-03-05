from modelos.libro import Libro
from modelos.usuario import Usuario
from servicios.biblioteca_servicio import BibliotecaServicio


def menu():
    servicio = BibliotecaServicio()

    while True:
        print("\n--- SISTEMA DE GESTIÓN DE BIBLIOTECA DIGITAL ---")
        print("1. Añadir Libro")
        print("2. Registrar Usuario")
        print("3. Prestar Libro")
        print("4. Devolver Libro")
        print("5. Buscar Libro")
        print("6. Listar Libros de Usuario")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            t = input("Título: ")
            a = input("Autor: ")
            c = input("Categoría: ")
            i = input("ISBN: ")
            servicio.añadir_libro(Libro(t, a, c, i))

        elif opcion == "2":
            n = input("Nombre: ")
            id_u = input("ID de Usuario: ")
            servicio.registrar_usuario(Usuario(n, id_u))

        elif opcion == "3":
            isbn = input("ISBN del libro: ")
            id_u = input("ID del usuario: ")
            servicio.prestar_libro(isbn, id_u)

        elif opcion == "4":
            isbn = input("ISBN del libro: ")
            id_u = input("ID del usuario: ")
            servicio.devolver_libro(isbn, id_u)

        elif opcion == "5":
            crit = input("Buscar por (titulo/autor/categoria): ").lower()
            val = input("Valor a buscar: ")
            res = servicio.buscar_libros(crit, val)
            for l in res: print(l)

        elif opcion == "6":
            id_u = input("ID del usuario: ")
            libros = servicio.listar_libros_usuario(id_u)
            if libros:
                for l in libros: print(l)
            else:
                print("No hay libros prestados.")

        elif opcion == "7":
            break


if __name__ == "__main__":
    menu()