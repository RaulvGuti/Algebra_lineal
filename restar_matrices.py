import numpy as np


def solicitar_numero_matrices():
    while True:
        try:
            n = int(input("¿Cuántas matrices quieres restar? (2-4): "))
            if n < 2 or n > 4:
                raise ValueError
            return n
        except ValueError:
            print("Por favor, introduce un número entero entre 2 y 4.")


def solicitar_dimensiones_matriz():
    while True:
        try:
            filas = int(input("Introduce el número de filas de las matrices: "))
            columnas = int(input("Introduce el número de columnas de las matrices: "))
            if filas <= 0 or columnas <= 0:
                raise ValueError
            return filas, columnas
        except ValueError:
            print("Por favor, introduce números enteros positivos para filas y columnas.")


def leer_matriz(filas, columnas, indice):
    matriz = []
    print(f"\nIntroduce los elementos de la matriz {indice}:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            while True:
                try:
                    elemento = float(input(f"Elemento [{i + 1}][{j + 1}]: "))
                    break
                except ValueError:
                    print("Por favor, introduce un número válido.")
            fila.append(elemento)
        matriz.append(fila)
    return np.array(matriz)


def mostrar_matrices(matrices):
    for i, matriz in enumerate(matrices, start=1):
        print(f"\nMatriz {i}:")
        print(matriz)


def restar_matrices(matrices):
    resta_matrices = matrices[0]
    for matriz in matrices[1:]:
        resta_matrices = np.subtract(resta_matrices, matriz)
    print("\nLa resta de las matrices es:")
    print(resta_matrices)


def ejecutar_programa():
    n = solicitar_numero_matrices()
    filas, columnas = solicitar_dimensiones_matriz()

    matrices = []
    for i in range(1, n + 1):
        matriz = leer_matriz(filas, columnas, i)
        matrices.append(matriz)

    print("\nHas introducido las siguientes matrices:")
    mostrar_matrices(matrices)

    restar_matrices(matrices)


ejecutar_programa()