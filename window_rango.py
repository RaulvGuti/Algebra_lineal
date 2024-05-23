import customtkinter as ctk
import cargar_datos_labels_frame as cdl
import numpy as np
from tkinter import messagebox


class WindowRango:
    def __init__(self):
        # ventana
        self.ventana = cdl.cargar_datos()
        self.ventana.geometry('800x600')
        self.frame = cdl.frame1(self.ventana)
        self.color = "#3E4446"

        # Labels and Entries for matrix dimensions
        self.label_filas = ctk.CTkLabel(self.frame, text="Filas de la matriz:")
        self.label_filas.pack(pady=5)
        self.entry_filas = ctk.CTkEntry(self.frame)
        self.entry_filas.pack(pady=5)

        self.label_columnas = ctk.CTkLabel(self.frame, text="Columnas de la matriz:")
        self.label_columnas.pack(pady=5)
        self.entry_columnas = ctk.CTkEntry(self.frame)
        self.entry_columnas.pack(pady=5)

        self.button_solicitar_matriz = ctk.CTkButton(self.frame, text="Introducir Matriz",
                                                     command=self.solicitar_matriz)
        self.button_solicitar_matriz.pack(pady=10)

        self.button_calcular = ctk.CTkButton(self.frame, text="Calcular Rango", command=self.calcular_rango)
        self.button_calcular.pack(pady=20)

        # Frame for matrix entries
        self.matrix_frame = ctk.CTkFrame(self.frame)
        self.matrix_frame.pack(pady=10)

        self.entry_matrix = []

        # Textbox for displaying results
        self.textbox_resultado = ctk.CTkTextbox(self.frame)
        self.textbox_resultado.pack(pady=10, padx=10, fill='both', expand=True)

        # Initializing matrices and parameters
        self.matriz = None
        self.pasos_gauss = []

    def solicitar_matriz(self):
        try:
            filas = int(self.entry_filas.get())
            columnas = int(self.entry_columnas.get())
            if filas <= 0 or columnas <= 0:
                raise ValueError("Las filas y columnas deben ser números enteros positivos.")
            self.crear_entradas_matriz(filas, columnas)
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def crear_entradas_matriz(self, filas, columnas):
        # Clear previous entries if exist
        for row_entries in self.entry_matrix:
            for entry in row_entries:
                entry.destroy()

        self.entry_matrix = []

        # Create entries for matrix
        for i in range(filas):
            row_entries = []
            for j in range(columnas):
                entry = ctk.CTkEntry(self.matrix_frame, width=5)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.entry_matrix.append(row_entries)

    def obtener_matriz(self):
        filas = len(self.entry_matrix)
        columnas = len(self.entry_matrix[0])
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                valor = self.entry_matrix[i][j].get()
                try:
                    valor = float(valor)
                except ValueError:
                    messagebox.showerror("Error", "Por favor, introduce números válidos en todas las celdas.")
                    return None
                fila.append(valor)
            matriz.append(fila)
        return matriz

    def mostrar_matriz(self, matriz, mensaje):
        self.textbox_resultado.insert(ctk.END, f"{mensaje}\n")
        self.textbox_resultado.insert(ctk.END, f"{matriz}\n")

    def gauss_elimination(self, A):
        n = len(A)
        m = len(A[0])
        row, col = 0, 0
        self.pasos_gauss = []
        self.pasos_gauss.append(np.copy(A))
        while row < n and col < m:
            max_row = max(range(row, n), key=lambda i: abs(A[i][col]))
            if A[max_row][col] == 0:
                col += 1
            else:
                if max_row != row:
                    A[[row, max_row]] = A[[max_row, row]]
                    self.pasos_gauss.append(np.copy(A))
                for i in range(row + 1, n):
                    factor = A[i][col] / A[row][col]
                    A[i] -= factor * A[row]
                row += 1
                col += 1
        return A

    def calcular_rango(self):
        matriz = self.obtener_matriz()
        if matriz is not None:
            A = self.gauss_elimination(np.array(matriz))
            rank = np.linalg.matrix_rank(A)
            self.mostrar_pasos_gauss()
            messagebox.showinfo("Rango", f"El rango de la matriz es: {rank}")

    def mostrar_pasos_gauss(self):
        self.textbox_resultado.delete('1.0', ctk.END)
        for i, paso in enumerate(self.pasos_gauss):
            self.textbox_resultado.insert(ctk.END, f"Paso {i + 1}:\n{paso}\n\n")


if __name__ == "__main__":
    app = WindowRango()
    app.ventana.mainloop()
