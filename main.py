

#Programacion numerica y no numerica-tarea 3

    #ANDERSON ESCOBAR - DCN0501IIV1
    #ALBERT RANGEL - DCN0501IIV1

import os
import matplotlib.pyplot as plt
import math

def mostrar_titulo():
    banner = """
    ################################
    #                              #
    #           PROGRAMA           #
    #              DE              #
    #           CALCULO            #
    #                              #
    ################################
    """
    print(banner)

def tui():
    os.system("cls|| clear")
    mostrar_titulo()
    while True:
        
        print("1: Calcular Función Cuadrática")
        print("2: Salir")
        opcion = input("Ingrese la opcion deseada: ")
        if opcion == "1":
            calcular_funcion_cuadratica()
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida.")

def calcular_funcion_cuadratica():
    while True:
        try:
            a = float(input("Ingrese el coeficiente de x^2: "))
            b = float(input("Ingrese el coeficiente de x: "))
            c = float(input("Ingrese el término independiente: "))
            break
        except ValueError:
            print("Por favor, ingrese solo números.")

    valores_x = [-2, -1, 0, 1, 2]
    valores_y = [a * x**2 + b * x + c for x in valores_x]

    print("Pares de coordenadas (X, Y):")
    for x, y in zip(valores_x, valores_y):
        print(f"({x}, {y})")

    graficar = input("Desea graficar la función? (s/n): ")
    if graficar.lower() == "s":
        plt.plot(valores_x, valores_y)
        plt.title("Gráfica de la Función Cuadrática")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True)
        plt.show()
        # os.system("cls|| clear")

if __name__ == "__main__":
    tui()