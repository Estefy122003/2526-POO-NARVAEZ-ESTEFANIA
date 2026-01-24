import os
import subprocess

"""
Dashboard personalizado para la gestión de proyectos de Programación Orientada a Objetos.

Mejoras realizadas por Estefanía Narváez:
- Mensaje de bienvenida personalizado
- Se muestra la ruta actual en cada menú
- Se muestra el número total de scripts encontrados
- Se agregó opción para ver el código antes de ejecutarlo
"""

def mostrar_codigo(ruta_script):
    # Convierte la ruta en absoluta para evitar errores
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r') as archivo:
            codigo = archivo.read()
            print(f"\n--- Código de {ruta_script} ---\n")
            print(codigo)
            return codigo
    except FileNotFoundError:
        print("El archivo no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")
        return None


def ejecutar_codigo(ruta_script):
    # Ejecuta el script en una nueva terminal
    try:
        if os.name == 'nt':  # Windows
            subprocess.Popen(['cmd', '/k', 'python', ruta_script])
        else:  # Linux/Mac
            subprocess.Popen(['xterm', '-hold', '-e', 'python3', ruta_script])
    except Exception as e:
        print(f"Ocurrió un error al ejecutar el código: {e}")


def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    print("\n===== DASHBOARD DE PROGRAMACIÓN ORIENTADA A OBJETOS =====")
    print("Estudiante: Estefanía Narváez")
    print("Organizador de proyectos y scripts por unidades\n")

    unidades = {
        '1': 'Unidad 1',
        '2': 'Unidad 2'
    }

    while True:
        print("\nMenu Principal - Dashboard")
        for key in unidades:
            print(f"{key} - {unidades[key]}")
        print("0 - Salir")

        eleccion_unidad = input("Elige una unidad o '0' para salir: ")
        if eleccion_unidad == '0':
            print("Saliendo del programa.")
            break
        elif eleccion_unidad in unidades:
            mostrar_sub_menu(os.path.join(ruta_base, unidades[eleccion_unidad]))
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


def mostrar_sub_menu(ruta_unidad):
    print(f"\n📂 Ruta actual: {ruta_unidad}")
    sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]

    while True:
        print("\nSubmenú - Selecciona una subcarpeta")
        for i, carpeta in enumerate(sub_carpetas, start=1):
            print(f"{i} - {carpeta}")
        print("0 - Regresar al menú principal")

        eleccion_carpeta = input("Elige una subcarpeta o '0' para regresar: ")
        if eleccion_carpeta == '0':
            break
        else:
            try:
                eleccion_carpeta = int(eleccion_carpeta) - 1
                if 0 <= eleccion_carpeta < len(sub_carpetas):
                    mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[eleccion_carpeta]))
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")


def mostrar_scripts(ruta_sub_carpeta):
    print(f"\n📂 Carpeta de scripts: {ruta_sub_carpeta}")
    scripts = [f.name for f in os.scandir(ruta_sub_carpeta) if f.is_file() and f.name.endswith('.py')]
    print(f"Total de scripts encontrados: {len(scripts)}")

    while True:
        print("\nScripts disponibles")
        for i, script in enumerate(scripts, start=1):
            print(f"{i} - {script}")
        print("0 - Regresar al submenú")
        print("9 - Regresar al menú principal")

        eleccion_script = input("Elige un script: ")
        if eleccion_script == '0':
            break
        elif eleccion_script == '9':
            return
        else:
            try:
                eleccion_script = int(eleccion_script) - 1
                if 0 <= eleccion_script < len(scripts):
                    ruta_script = os.path.join(ruta_sub_carpeta, scripts[eleccion_script])

                    # NUEVA OPCIÓN AGREGADA
                    ver_codigo = input("¿Desea ver el código del script? (1: Sí, 0: No): ")
                    if ver_codigo == '1':
                        mostrar_codigo(ruta_script)

                    ejecutar = input("¿Desea ejecutar el script? (1: Sí, 0: No): ")
                    if ejecutar == '1':
                        ejecutar_codigo(ruta_script)

                    input("\nPresiona Enter para volver al menú de scripts.")
                else:
                    print("Opción no válida.")
            except ValueError:
                print("Opción no válida.")


if __name__ == "__main__":
    mostrar_menu()
