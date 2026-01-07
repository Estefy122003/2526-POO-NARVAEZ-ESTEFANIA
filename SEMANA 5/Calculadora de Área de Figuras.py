# Programa: calculadora_area.py
# Funcionalidad: Este programa calcula el área de diferentes figuras geométricas
# (rectángulo, círculo y triángulo) según la elección del usuario.
# Se utilizan distintos tipos de datos y se aplican identificadores descriptivos en snake_case.

import math  # Importa la librería matemática para usar la constante pi


# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un rectángulo.
    base: float - base del rectángulo
    altura: float - altura del rectángulo
    return: float - área calculada
    """
    return base * altura


# Función para calcular el área de un círculo
def calcular_area_circulo(radio: float) -> float:
    """
    Calcula el área de un círculo.
    radio: float - radio del círculo
    return: float - área calculada
    """
    return math.pi * radio ** 2


# Función para calcular el área de un triángulo
def calcular_area_triangulo(base: float, altura: float) -> float:
    """
    Calcula el área de un triángulo.
    base: float - base del triángulo
    altura: float - altura del triángulo
    return: float - área calculada
    """
    return (base * altura) / 2


# Función principal del programa
def main():
    print("Bienvenido a la Calculadora de Áreas")

    # Solicita al usuario elegir la figura
    figura: str = input("Ingrese la figura a calcular (rectangulo/circulo/triangulo): ").lower()

    if figura == "rectangulo":
        base: float = float(input("Ingrese la base del rectángulo: "))
        altura: float = float(input("Ingrese la altura del rectángulo: "))
        area: float = calcular_area_rectangulo(base, altura)
        print(f"El área del rectángulo es: {area:.2f}")

    elif figura == "circulo":
        radio: float = float(input("Ingrese el radio del círculo: "))
        area: float = calcular_area_circulo(radio)
        print(f"El área del círculo es: {area:.2f}")

    elif figura == "triangulo":
        base: float = float(input("Ingrese la base del triángulo: "))
        altura: float = float(input("Ingrese la altura del triángulo: "))
        area: float = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo es: {area:.2f}")

    else:
        print("Figura no reconocida. Por favor ingrese rectangulo, circulo o triangulo.")


# Ejecuta la función principal si el archivo es ejecutado directamente
if __name__ == "__main__":
    main()
