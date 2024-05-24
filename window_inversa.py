import customtkinter
import numpy as np


# Parte de la interfaz gráfica
class WindowInversa:
    def __init__(self):
        # ventana
        self.ventana = cargar_datos()
        self.ventana.geometry('600x400')
        self.frame = frame1(self.ventana)
        self.ventana.configure(bg="#3E4446")

        # Añadir widgets
        self.label = customtkinter.CTkLabel(self.frame, text="Introduce el tamaño de la matriz:")
        self.label.pack(pady=10)
        self.entry_size = customtkinter.CTkEntry(self.frame)
        self.entry_size.pack(pady=10)

        self.entry_matrix = []
        self.size = 0

        self.button_size = customtkinter.CTkButton(self.frame, text="Aceptar", command=self.capturar_tamano)
        self.button_size.pack(pady=10)
        self.button_calculate = customtkinter.CTkButton(self.frame, text="Calcular Inversa",
                                                        command=self.calcular_inversa)
        self.button_calculate.pack(pady=10)
        self.result_label = customtkinter.CTkLabel(self.frame, text="")
        self.result_label.pack(pady=10)

        # Añadir Textbox para los pasos
        self.steps_textbox = customtkinter.CTkTextbox(self.frame, width=500, height=200)
        self.steps_textbox.pack(pady=10)

    def capturar_tamano(self):
        try:
            self.size = int(self.entry_size.get())
            if self.size <= 0:
                raise ValueError("El tamaño debe ser un número entero positivo.")
            self.crear_entradas_matriz()
        except ValueError as e:
            self.result_label.configure(text=str(e))

    def crear_entradas_matriz(self):
        # Limpiar entradas anteriores si existen
        for row_entries in self.entry_matrix:
            for entry in row_entries:
                entry.destroy()

        self.entry_matrix = []

        for i in range(self.size):
            row_entries = []
            row_frame = customtkinter.CTkFrame(self.frame)
            row_frame.pack(pady=5)
            for j in range(self.size):
                entry = customtkinter.CTkEntry(row_frame, width=50)
                entry.pack(side='left', padx=5)
                row_entries.append(entry)
            self.entry_matrix.append(row_entries)

    def capturar_matriz(self):
        matriz = []
        try:
            for i in range(self.size):
                fila = []
                for j in range(self.size):
                    elemento = float(self.entry_matrix[i][j].get())
                    fila.append(elemento)
                matriz.append(fila)
            return np.array(matriz)
        except ValueError:
            self.result_label.configure(text="Por favor, introduce todos los números válidos.")
            return None

    def calcular_inversa(self):
        self.steps_textbox.delete(1.0, customtkinter.END)  # Limpiar el Textbox
        matriz = self.capturar_matriz()
        if matriz is None:
            return
        self.mostrar_matriz(matriz, "La matriz ingresada es:")
        matriz_identidad = np.identity(self.size)
        matriz_ampliada = np.concatenate((matriz, matriz_identidad), axis=1)
        self.mostrar_matriz(matriz_ampliada, "\nMatriz aumentada con la identidad:")

        try:
            matriz_inversa = gauss_jordan(matriz_ampliada, self.mostrar_matriz)
            resultado = np.array(matriz_inversa)
            self.result_label.configure(text=f"\nLa matriz inversa es:\n{resultado}")
        except ValueError as e:
            self.result_label.configure(text=str(e))

    def mostrar_matriz(self, matriz, mensaje):
        self.steps_textbox.insert(customtkinter.END, f"{mensaje}\n{matriz}\n\n")
        self.steps_textbox.yview(customtkinter.END)  # Scroll hasta el final


def cargar_datos():
    customtkinter.set_appearance_mode('dark')
    customtkinter.set_default_color_theme('dark-blue')
    ventana = customtkinter.CTkToplevel()
    ventana.grab_set()
    ventana.title("Proyecto Álgebra")
    ventana.geometry('1280x500')
    return ventana


def frame1(ventana):
    frame = customtkinter.CTkFrame(master=ventana)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    return frame


def gauss_jordan(A, mostrar_func):
    n = len(A)
    for i in range(n):
        pivot = A[i][i]
        if pivot == 0:
            raise ValueError("La matriz no es invertible.")
        for j in range(n * 2):
            A[i][j] /= pivot
        mostrar_func(A, f"Dividiendo fila {i + 1} por el pivote {pivot}:")

        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(n * 2):
                    A[k][j] -= factor * A[i][j]
                mostrar_func(A, f"Restando {factor} veces la fila {i + 1} de la fila {k + 1}:")
    inv = [row[n:] for row in A]
    return inv


if __name__ == "__main__":
    root = customtkinter.CTk()
    app = WindowInversa()
    root.mainloop()
