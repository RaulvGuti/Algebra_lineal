from sympy import Matrix


def solicitar_matriz(mensaje, filas, columnas):
    matriz = []
    print(mensaje)
    for i in range(filas):
        fila = []
        for j in range(columnas):
            while True:
                try:
                    elemento = float(input(f'Elemento [{i + 1}][{j + 1}]: '))
                    break
                except ValueError:
                    print("Por favor, introduce un número válido.")
            fila.append(elemento)
        matriz.append(fila)
    return matriz


def mostrar_matriz(matriz, mensaje):
    print(mensaje)
    for fila in matriz:
        print(fila)


def ejecutar_programa():
    print('Bienvenido a matrices de Markov')
    filas_base = int(input('Cuantas filas contendrá la matriz base: '))
    columnas_base = int(input('Cuantas columnas tendrá la matriz base: '))
    matriz_base = solicitar_matriz("Introduce los elementos de la matriz base:", filas_base, columnas_base)
    mostrar_matriz(matriz_base, "\nMatriz base:")

    filas_multiplicadora = int(input('Cuantas filas contendrá la matriz multiplicadora (recomendado 3): '))
    columnas_multiplicadora = int(input('Cuantas columnas tendrá la matriz multiplicadora (recomendado 1): '))
    matriz_multiplicadora = solicitar_matriz("Introduce los elementos de la matriz multiplicadora:",
                                             filas_multiplicadora, columnas_multiplicadora)
    mostrar_matriz(matriz_multiplicadora, "\nMatriz multiplicadora:")

    veces = int(input('Cuantas veces se hará: '))

    a = Matrix(matriz_base)
    a_arreglo = a.transpose()
    b = Matrix(matriz_multiplicadora)
    c = a_arreglo * b

    print("\nPasos importantes:")
    contador = 1
    while contador <= veces:
        c = a_arreglo * c
        print(contador, ')', c)
        contador += 1
    d = c
    e = d * 100
    print("\nResultado final:")
    print(e)


ejecutar_programa()
