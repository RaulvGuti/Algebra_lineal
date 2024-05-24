def get_matrix():
    """Solicita al usuario los elementos de la matriz cuadrada elemento por elemento."""
    n = int(input("Ingrese el tamaño de la matriz cuadrada (n x n): "))
    matrix = []
    print("Ingrese los elementos de la matriz uno por uno:")
    for i in range(n):
        row = []
        for j in range(n):
            element = int(input(f"Elemento ({i + 1}, {j + 1}): "))
            row.append(element)
        matrix.append(row)
    return matrix


def minor(matrix, i, j):
    """Devuelve el menor de la matriz excluyendo la fila i y la columna j."""
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


def print_matrix(matrix):
    """Imprime la matriz."""
    for row in matrix:
        print(" ".join(map(str, row)))


def determinant(matrix, level=0):
    """Calcula el determinante de una matriz cuadrada recursivamente."""
    n = len(matrix)

    # Caso base: matriz 2x2
    if n == 2:
        det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        print("  " * level + f"Determinante de la submatriz 2x2: {det}")
        return det

    det = 0
    for j in range(n):
        # Calculamos el menor
        minor_matrix = minor(matrix, 0, j)
        cofactor = ((-1) ** j) * matrix[0][j]
        print("  " * level + f"Expansión por cofactores usando el elemento ({0}, {j}) = {matrix[0][j]}")
        print("  " * level + f"Submatriz menor excluyendo la fila 0 y la columna {j}:")
        print_matrix(minor_matrix)

        # Recursivamente calculamos el determinante del menor
        minor_det = determinant(minor_matrix, level + 1)
        print("  " * level + f"Cofactor: {cofactor}, Determinante del menor: {minor_det}")

        # Sumamos al determinante total
        det += cofactor * minor_det
        print("  " * level + f"Determinante acumulado: {det}")

    return det


def main():
    matrix = get_matrix()
    print("La matriz ingresada es:")
    print_matrix(matrix)

    det = determinant(matrix)
    print(f"El determinante de la matriz es: {det}")


if __name__ == "__main__":
    main()
