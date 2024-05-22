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


def gauss_jordan(A):
    n = len(A)
    for i in range(n):
        # Pivote para la columna actual y hacerlo 1
        pivot = A[i][i]
        if pivot == 0:
            raise ValueError("La matriz no es invertible.")
        for j in range(n * 2):
            A[i][j] /= pivot
        mostrar_matriz(A, f"Dividiendo fila {i + 1} por el pivote {pivot}:")

        # Hacer 0 los otros elementos en la columna y fila
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(n * 2):
                    A[k][j] -= factor * A[i][j]
                mostrar_matriz(A, f"Restando {factor} veces la fila {i + 1} de la fila {k + 1}:")
    # Extraer la inversa de la parte derecha
    inv = [row[n:] for row in A]
    return inv


def calcular_determinante(matriz):
    n = len(matriz)
    if n != len(matriz[0]):
        raise ValueError("La matriz no es cuadrada.")

    if n == 1:
        return matriz[0][0]

    det = 1
    for i in range(n):
        det *= matriz[i][i]
    return det


def ejecutar_programa():
    try:
        n = int(input("Introduce el tamaño de la matriz cuadrada: "))
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Por favor, introduce un número entero positivo.")
        return

    matriz = leer_matriz(n, n)
    mostrar_matriz(matriz, "La matriz ingresada es:")

    try:
        det = calcular_determinante(matriz)
        print("\nLa determinante de la matriz es:", det)
    except ValueError as e:
        print(e)


ejecutar_programa()
