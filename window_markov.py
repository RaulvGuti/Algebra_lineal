import customtkinter as ctk
import cargar_datos_labels_frame as cdl
from sympy import Matrix
from tkinter import simpledialog


class WindowMarkov:
    def __init__(self):
        # ventana
        self.ventana = cdl.cargar_datos()
        self.ventana.geometry('800x600')
        self.frame = cdl.frame1(self.ventana)
        self.color = "#3E4446"

        # Labels and Entries for matriz base
        self.label_filas_base = ctk.CTkLabel(self.frame, text="Filas de la matriz base:")
        self.label_filas_base.pack(pady=5)
        self.entry_filas_base = ctk.CTkEntry(self.frame)
        self.entry_filas_base.pack(pady=5)

        self.label_columnas_base = ctk.CTkLabel(self.frame, text="Columnas de la matriz base:")
        self.label_columnas_base.pack(pady=5)
        self.entry_columnas_base = ctk.CTkEntry(self.frame)
        self.entry_columnas_base.pack(pady=5)

        self.button_solicitar_base = ctk.CTkButton(self.frame, text="Introducir Matriz Base",
                                                   command=self.solicitar_matriz_base)
        self.button_solicitar_base.pack(pady=10)

        # Labels and Entries for matriz multiplicadora
        self.label_filas_multiplicadora = ctk.CTkLabel(self.frame, text="Filas de la matriz multiplicadora:")
        self.label_filas_multiplicadora.pack(pady=5)
        self.entry_filas_multiplicadora = ctk.CTkEntry(self.frame)
        self.entry_filas_multiplicadora.pack(pady=5)

        self.label_columnas_multiplicadora = ctk.CTkLabel(self.frame, text="Columnas de la matriz multiplicadora:")
        self.label_columnas_multiplicadora.pack(pady=5)
        self.entry_columnas_multiplicadora = ctk.CTkEntry(self.frame)
        self.entry_columnas_multiplicadora.pack(pady=5)

        self.button_solicitar_multiplicadora = ctk.CTkButton(self.frame, text="Introducir Matriz Multiplicadora",
                                                             command=self.solicitar_matriz_multiplicadora)
        self.button_solicitar_multiplicadora.pack(pady=10)

        # Entry for number of iterations
        self.label_veces = ctk.CTkLabel(self.frame, text="Número de iteraciones:")
        self.label_veces.pack(pady=5)
        self.entry_veces = ctk.CTkEntry(self.frame)
        self.entry_veces.pack(pady=5)

        self.button_calcular = ctk.CTkButton(self.frame, text="Calcular", command=self.calcular_resultado)
        self.button_calcular.pack(pady=20)

        # Textbox for displaying results
        self.textbox_resultado = ctk.CTkTextbox(self.frame)
        self.textbox_resultado.pack(pady=10, padx=10, fill='both', expand=True)

        # Initializing matrices and parameters
        self.matriz_base = []
        self.matriz_multiplicadora = []
        self.veces = 0

    def solicitar_matriz_base(self):
        filas = int(self.entry_filas_base.get())
        columnas = int(self.entry_columnas_base.get())
        self.matriz_base = self.solicitar_matriz("Introduce los elementos de la matriz base:", filas, columnas)
        self.mostrar_matriz(self.matriz_base, "\nMatriz base:")

    def solicitar_matriz_multiplicadora(self):
        filas = int(self.entry_filas_multiplicadora.get())
        columnas = int(self.entry_columnas_multiplicadora.get())
        self.matriz_multiplicadora = self.solicitar_matriz("Introduce los elementos de la matriz multiplicadora:",
                                                           filas, columnas)
        self.mostrar_matriz(self.matriz_multiplicadora, "\nMatriz multiplicadora:")

    def solicitar_matriz(self, mensaje, filas, columnas):
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                elemento = self.obtener_elemento(f"Elemento [{i + 1}][{j + 1}]: ")
                fila.append(elemento)
            matriz.append(fila)
        return matriz

    def obtener_elemento(self, mensaje):
        # Using tkinter's simpledialog to ask for user input
        elemento = float(simpledialog.askstring("Input", mensaje, parent=self.ventana))
        return elemento

    def mostrar_matriz(self, matriz, mensaje):
        self.textbox_resultado.insert(ctk.END, f"{mensaje}\n")
        for fila in matriz:
            self.textbox_resultado.insert(ctk.END, f"{fila}\n")

    def calcular_resultado(self):
        self.veces = int(self.entry_veces.get())
        a = Matrix(self.matriz_base)
        a_arreglo = a.transpose()
        b = Matrix(self.matriz_multiplicadora)
        c = a_arreglo * b

        self.textbox_resultado.insert(ctk.END, "\nPasos importantes:\n")
        contador = 1
        while contador <= self.veces:
            c = a_arreglo * c
            self.textbox_resultado.insert(ctk.END, f"{contador}) {c}\n")
            contador += 1
        d = c
        e = d * 100
        self.textbox_resultado.insert(ctk.END, "\nResultado final:\n")
        self.textbox_resultado.insert(ctk.END, f"{e}\n")


if __name__ == "__main__":
    app = WindowMarkov()
    app.ventana.mainloop()