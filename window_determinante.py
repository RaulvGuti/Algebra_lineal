import numpy as np
import tkinter as tk
from tkinter import messagebox


def leer_matriz():
    matriz = []
    for i in range(n):
        fila = []
        for j in range(n):
            elemento = float(entries[(i, j)].get())
            fila.append(elemento)
        matriz.append(fila)
    return np.array(matriz)


def mostrar_matriz(matriz):
    for i in range(n):
        for j in range(n):
            entries[(i, j)].delete(0, tk.END)
            entries[(i, j)].insert(0, matriz[i][j])


def ejecutar_programa():
    global n
    try:
        n = int(entry_size.get())
        if n <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número entero positivo.")
        return

    matriz = leer_matriz()
    mostrar_matriz(matriz)

    try:
        det = np.linalg.det(matriz)
        messagebox.showinfo("Determinante", f"La determinante de la matriz es: {det}")
    except np.linalg.LinAlgError as e:
        messagebox.showerror("Error", "La matriz no es invertible.")


# Crear ventana
window = tk.Tk()
window.title("Gauss-Jordan y Determinante")

# Tamaño de la matriz
label_size = tk.Label(window, text="Tamaño de la matriz cuadrada:")
label_size.grid(row=0, column=0)
entry_size = tk.Entry(window)
entry_size.grid(row=0, column=1)

# Botón para ejecutar el programa
button_execute = tk.Button(window, text="Ejecutar", command=ejecutar_programa)
button_execute.grid(row=0, column=2)

# Entradas para la matriz
entries = {}
n = 0
for i in range(5):
    for j in range(5):
        entry = tk.Entry(window, width=8)
        entry.grid(row=i + 1, column=j)
        entries[(i, j)] = entry

# Ejecutar la ventana
window.mainloop()
