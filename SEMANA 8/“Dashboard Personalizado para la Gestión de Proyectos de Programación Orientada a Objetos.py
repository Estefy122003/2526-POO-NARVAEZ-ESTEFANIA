import os
import subprocess
import sys
from datetime import datetime

"""
Dashboard personalizado - Estefanía Narváez
Proyecto: Programación Orientada a Objetos

MEJORAS IMPLEMENTADAS:
✔ Interfaz mejor organizada
✔ Historial de scripts ejecutados con hora
✔ Validación de existencia de carpetas
✔ Opción para limpiar pantalla
✔ Opción para ver código antes de ejecutar
✔ Uso de sys.executable para mayor compatibilidad
"""

historial = []


def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')


def mostrar_codigo(ruta_script):
    try:
        with open(ruta_script, 'r', encoding='utf-8') as archivo:
            print(f"\n===== CÓDIGO DE {os.path.basename(ruta_script)} =====\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")


def ejecutar_codigo(ruta_script):
    try:
        historial.append(f"{os.path.basename(ruta_script)} - {datetime.now().strftime('%H:%M:%S')}")
        subprocess.Popen([sys.executable, ruta_script])
    except Exception as e:
        print(f"Error al ejecutar el script: {e}")


def mostrar_historial():
    limpiar_pantalla()
    print("===== HISTORIAL DE SCRIPTS EJECUTADOS =====\n")
    if not historial:
        print("Aún no se ha ejecutado ningún script.")
    else:
        for item in historial:
            print("•", item)
    input("\nPresiona Enter para volver...")


def mostrar_menu():
    ruta_base = os.path.dirname(__file__)

    while True:
        limpiar_pantalla()
        print("======================================")
        print("   DASHBOARD POO - ESTEFANÍA NARVÁEZ  ")
        print("======================================")
        print("1 - Unidad 1")
        print("2 - Unidad 2")
        print("3 - Ver historial")
        print("0 - Salir")

        opcion = input("\nSelecciona una opción: ")

        if opcion == '0':
            print("Saliendo del programa...")
            break
        elif opcion == '3':
            mostrar_historial()
        elif opcion in ['1', '2']:
            ruta_unidad = os.path.join(ruta_base, f"Unidad {opcion}")
            if os.path.exists(ruta_unidad):
                mostrar_sub_menu(ruta_unidad)
            else:
                print("La carpeta no existe.")
                input("Enter para continuar...")
        else:
            print("Opción inválida.")
            input("Enter para continuar...")


def mostrar_sub_menu(ruta_unidad):
    while True:
        limpiar_pantalla()
        print(f"📂 Unidad actual: {ruta_unidad}\n")

        sub_carpetas = [f.name for f in os.scandir(ruta_unidad) if f.is_dir()]
        if not sub_carpetas:
            print("No hay subcarpetas en esta unidad.")
            input("Enter para volver...")
            return

        for i, carpeta in enumerate(sub_carpetas, 1):
            print(f"{i} - {carpeta}")
        print("0 - Volver")

        opcion = input("\nSelecciona carpeta: ")

        if opcion == '0':
            return

        try:
            idx = int(opcion) - 1
            if 0 <= idx < len(sub_carpetas):
                mostrar_scripts(os.path.join(ruta_unidad, sub_carpetas[idx]))
        except ValueError:
            print("Entrada inválida.")
            input("Enter para continuar...")


def mostrar_scripts(ruta_sub):
    while True:
        limpiar_pantalla()
        print(f"📁 Carpeta: {ruta_sub}\n")

        scripts = [f.name for f in os.scandir(ruta_sub) if f.is_file() and f.name.endswith('.py')]
        if not scripts:
            print("No hay scripts en esta carpeta.")
            input("Enter para volver...")
            return

        print(f"Total de scripts: {len(scripts)}\n")
        for i, script in enumerate(scripts, 1):
            print(f"{i} - {script}")
        print("0 - Volver")

        opcion = input("\nSelecciona script: ")

        if opcion == '0':
            return

        try:
            idx = int(opcion) - 1
            if 0 <= idx < len(scripts):
                ruta_script = os.path.join(ruta_sub, scripts[idx])

                ver = input("¿Ver código? (1=Sí / 0=No): ")
                if ver == '1':
                    mostrar_codigo(ruta_script)

                run = input("¿Ejecutar script? (1=Sí / 0=No): ")
                if run == '1':
                    ejecutar_codigo(ruta_script)

                input("\nPresiona Enter para continuar...")
        except ValueError:
            print("Entrada inválida.")
            input("Enter para continuar...")


if __name__ == "__main__":
    mostrar_menu()
