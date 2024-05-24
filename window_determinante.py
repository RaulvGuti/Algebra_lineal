import customtkinter
import cargar_datos_labels_frame
import tkinter as tk


class WindowDeterminante:
    def __init__(self):
        # ventana
        self.ventana = cargar_datos_labels_frame.cargar_datos()
        self.ventana.geometry('600x600')
        self.frame = cargar_datos_labels_frame.frame1(self.ventana)

        # Título
        self.label_title = customtkinter.CTkLabel(master=self.frame, text="Calculadora de Determinante de Matriz",
                                                  font=("Arial", 20))
        self.label_title.pack(pady=12, padx=10)

        # Entrada para el tamaño de la matriz
        self.label_size = customtkinter.CTkLabel(master=self.frame, text="Tamaño de la matriz (n x n):")
        self.label_size.pack(pady=5, padx=10)
        self.entry_size = customtkinter.CTkEntry(master=self.frame)
        self.entry_size.pack(pady=5, padx=10)

        # Botón para confirmar el tamaño de la matriz
        self.button_confirm_size = customtkinter.CTkButton(master=self.frame, text="Confirmar Tamaño",
                                                           command=self.create_matrix_inputs)
        self.button_confirm_size.pack(pady=5, padx=10)

        # Frame para los inputs de la matriz
        self.matrix_frame = customtkinter.CTkFrame(master=self.frame)
        self.matrix_frame.pack(pady=10, padx=10, fill='both', expand=True)

        # Botón para calcular el determinante
        self.button_calculate = customtkinter.CTkButton(master=self.frame, text="Calcular Determinante",
                                                        command=self.calculate_determinant)
        self.button_calculate.pack(pady=10, padx=10)

        # Label para mostrar el resultado
        self.result_label = customtkinter.CTkLabel(master=self.frame, text="")
        self.result_label.pack(pady=10, padx=10)

        # Text widget para mostrar los pasos
        self.steps_text = tk.Text(master=self.frame, height=10, state='disabled', bg='#212121', fg='white',
                                  insertbackground='white')
        self.steps_text.pack(pady=10, padx=10, fill='both', expand=True)

    def create_matrix_inputs(self):
        # Elimina cualquier entrada de matriz existente
        for widget in self.matrix_frame.winfo_children():
            widget.destroy()

        # Obtiene el tamaño de la matriz
        self.n = int(self.entry_size.get())

        # Crea las entradas para la matriz
        self.matrix_entries = []
        for i in range(self.n):
            row_entries = []
            for j in range(self.n):
                entry = customtkinter.CTkEntry(master=self.matrix_frame, width=40)
                entry.grid(row=i, column=j, padx=5, pady=5)
                row_entries.append(entry)
            self.matrix_entries.append(row_entries)

    def get_matrix_from_inputs(self):
        matrix = []
        for row_entries in self.matrix_entries:
            row = []
            for entry in row_entries:
                row.append(int(entry.get()))
            matrix.append(row)
        return matrix

    def calculate_determinant(self):
        matrix = self.get_matrix_from_inputs()
        self.steps_text.configure(state='normal')
        self.steps_text.delete(1.0, tk.END)  # Limpiar el Text widget
        det = self.determinant(matrix)
        self.steps_text.configure(state='disabled')
        self.result_label.configure(text=f"El determinante de la matriz es: {det}")

    def log_step(self, message):
        self.steps_text.insert(tk.END, message + '\n')
        self.steps_text.see(tk.END)

    def determinant(self, matrix, level=0):
        """Calcula el determinante de una matriz cuadrada recursivamente."""
        n = len(matrix)

        # Caso base: matriz 2x2
        if n == 2:
            det = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
            self.log_step("  " * level + f"Determinante de la submatriz 2x2: {det}")
            return det

        det = 0
        for j in range(n):
            # Calculamos el menor
            minor_matrix = minor(matrix, 0, j)
            cofactor = ((-1) ** j) * matrix[0][j]
            self.log_step("  " * level + f"Expansión por cofactores usando el elemento ({0}, {j}) = {matrix[0][j]}")
            self.log_step("  " * level + f"Submatriz menor excluyendo la fila 0 y la columna {j}:")
            self.log_step("  " * level + '\n'.join(["  " * level + " ".join(map(str, row)) for row in minor_matrix]))

            # Recursivamente calculamos el determinante del menor
            minor_det = self.determinant(minor_matrix, level + 1)
            self.log_step("  " * level + f"Cofactor: {cofactor}, Determinante del menor: {minor_det}")

            # Sumamos al determinante total
            det += cofactor * minor_det
            self.log_step("  " * level + f"Determinante acumulado: {det}")

        return det


def minor(matrix, i, j):
    """Devuelve el menor de la matriz excluyendo la fila i y la columna j."""
    return [row[:j] + row[j + 1:] for row in (matrix[:i] + matrix[i + 1:])]


if __name__ == "__main__":
    app = WindowDeterminante()
    app.ventana.mainloop()
