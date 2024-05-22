import numpy as np


def leer_matriz(filas, columnas):
    matriz = []
    print("Introduce los elementos de la matriz:")
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


def mostrar_matriz(matriz, mensaje):
    print(mensaje)
    print(matriz)


def gauss_elimination(A):
    n = len(A)
    m = len(A[0])
    row, col = 0, 0
    while row < n and col < m:
        # Encontrar el máximo valor en la columna para hacerlo pivote
        max_row = max(range(row, n), key=lambda i: abs(A[i][col]))
        if A[max_row][col] == 0:
            col += 1
        else:
            # Intercambiar filas si es necesario
            if max_row != row:
                A[[row, max_row]] = A[[max_row, row]]
            # Hacer ceros en la columna para abajo del pivote
            for i in range(row + 1, n):
                factor = A[i][col] / A[row][col]
                A[i] -= factor * A[row]
            row += 1
            col += 1
    return A


def calcular_rango(matriz):
    A = gauss_elimination(matriz)
    rank = np.linalg.matrix_rank(A)
    return rank


def ejecutar_programa():
    try:
        filas = int(input("Introduce el número de filas de la matriz: "))
        columnas = int(input("Introduce el número de columnas de la matriz: "))
        if filas <= 0 or columnas <= 0:
            raise ValueError
    except ValueError:
        print("Por favor, introduce un número entero positivo para filas y columnas.")
        return

    matriz = leer_matriz(filas, columnas)
    mostrar_matriz(matriz, "La matriz ingresada es:")

    rank = calcular_rango(matriz)
    print("\nEl rango de la matriz es:", rank)


ejecutar_programa()
