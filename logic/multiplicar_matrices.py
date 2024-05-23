import numpy as np


def solicitar_dimensiones_matriz():
    while True:
        try:
            filas = int(input("Introduce el número de filas de la primera matriz: "))
            columnas = int(
                input("Introduce el número de columnas de la primera matriz (y filas de la segunda matriz): "))
            columnas_matriz2 = int(input("Introduce el número de columnas de la segunda matriz: "))
            if filas <= 0 or columnas <= 0 or columnas_matriz2 <= 0:
                raise ValueError
            return filas, columnas, columnas_matriz2
        except ValueError:
            print("Por favor, introduce números enteros positivos para las dimensiones.")


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


def multiplicar_matrices(matriz1, matriz2):
    filas_m1, columnas_m1 = matriz1.shape
    filas_m2, columnas_m2 = matriz2.shape

    if columnas_m1 != filas_m2:
        raise ValueError(
            "El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz.")

    resultado = np.zeros((filas_m1, columnas_m2))

    print("\nMultiplicación de matrices (mostrando pasos):")
    for i in range(filas_m1):
        for j in range(columnas_m2):
            for k in range(columnas_m1):
                print(
                    f"Multiplicando {matriz1[i][k]} (Matriz 1 [{i + 1}][{k + 1}]) * {matriz2[k][j]} (Matriz 2 [{k + 1}][{j + 1}]) y sumando al resultado actual {resultado[i][j]}")
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
                print(f"Resultado actual para posición [{i + 1}][{j + 1}]: {resultado[i][j]}")

    print("\nEl resultado de la multiplicación de las matrices es:")
    print(resultado)


def ejecutar_programa():
    filas, columnas, columnas_matriz2 = solicitar_dimensiones_matriz()

    matriz1 = leer_matriz(filas, columnas, 1)
    matriz2 = leer_matriz(columnas, columnas_matriz2, 2)

    print("\nHas introducido las siguientes matrices:")
    mostrar_matrices([matriz1, matriz2])

    multiplicar_matrices(matriz1, matriz2)


ejecutar_programa()
