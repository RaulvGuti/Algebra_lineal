import customtkinter
import tkinter.messagebox as messagebox
import numpy as np


class WindowDeterminante(customtkinter.CTkToplevel):
    def __init__(self):
        super().__init__()
        self.title("Determinante de una Matriz")
        self.geometry('1280x500')

        self.frame = customtkinter.CTkFrame(self)
        self.frame.pack(pady=10, padx=10, fill='both', expand=True)

        self.label = customtkinter.CTkLabel(self.frame, text="Introduce el tamaño de la matriz cuadrada:")
        self.label.grid(row=0, column=0, padx=10, pady=10)

        self.entry = customtkinter.CTkEntry(self.frame)
        self.entry.grid(row=0, column=1, padx=10, pady=10)

        self.button = customtkinter.CTkButton(self.frame, text="Ingresar Matriz", command=self.ingresar_matriz)
        self.button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    def ingresar_matriz(self):
        try:
            n = int(self.entry.get())
            if n <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Por favor, introduce un número entero positivo.")
            return

        self.leer_matriz(n, n)

    def leer_matriz(self, filas, columnas):
        self.matriz_entries = []
        for i in range(filas):
            row_entries = []
            for j in range(columnas):
                entry = customtkinter.CTkEntry(self.frame, width=50)
                entry.grid(row=i + 2, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.matriz_entries.append(row_entries)

        submit_button = customtkinter.CTkButton(self.frame, text="Calcular Determinante", command=self.obtener_matriz)
        submit_button.grid(row=filas + 2, column=0, columnspan=columnas, pady=10)

    def obtener_matriz(self):
        filas = len(self.matriz_entries)
        columnas = len(self.matriz_entries[0])
        matriz = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                try:
                    elemento = float(self.matriz_entries[i][j].get())
                    fila.append(elemento)
                except ValueError:
                    messagebox.showerror("Error",
                                         "Por favor, introduce todos los elementos de la matriz como números válidos.")
                    return
            matriz.append(fila)
        self.matriz = np.array(matriz)
        messagebox.showinfo("Matriz Ingresada", f"La matriz ingresada es:\n{self.matriz}")

        try:
            det = self.calcular_determinante(self.matriz)
            messagebox.showinfo("Determinante", f"El determinante de la matriz es: {det}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    @staticmethod
    def calcular_determinante(matriz):
        n = len(matriz)
        if n != len(matriz[0]):
            raise ValueError("La matriz no es cuadrada.")

        det = np.linalg.det(matriz)
        return det


def window_determinante():
    ventana = WindowDeterminante()
    ventana.grab_set()  # Bloquea la ventana principal hasta que se cierre esta ventana secundaria
    ventana.mainloop()


app = customtkinter.CTk()
