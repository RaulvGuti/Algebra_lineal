import customtkinter
import cargar_datos_labels_frame


class WindowSumaVector:
    def __init__(self):
        self.ventana = cargar_datos_labels_frame.cargar_datos()
        self.ventana.geometry("1000x600")
        self.frame = cargar_datos_labels_frame.frame1(self.ventana)
        color = '#3E4446'

        # Variables para almacenar los valores de los vectores
        self.vector1 = [0, 0, 0]
        self.vector2 = [0, 0, 0]
        self.result = [0, 0, 0]

        # Frame para el ingreso de datos
        self.data_frame = customtkinter.CTkFrame(self.ventana)
        self.data_frame.place(relx=0.5, rely=0.1, anchor=customtkinter.CENTER)

        # Etiquetas y campos de entrada para el vector 1
        customtkinter.CTkLabel(self.data_frame, text="Vector 1").grid(row=0, column=0, padx=5)
        for i in range(3):
            entry = customtkinter.CTkEntry(self.data_frame, width=5)
            entry.grid(row=0, column=i + 1, padx=5)
            entry.insert(customtkinter.END, '0')
            entry.bind("<FocusOut>", lambda event, idx=i: self.update_vector(event, idx, self.vector1))

        # Etiquetas y campos de entrada para el vector 2
        customtkinter.CTkLabel(self.data_frame, text="Vector 2").grid(row=1, column=0, padx=5)
        for i in range(3):
            entry = customtkinter.CTkEntry(self.data_frame, width=5)
            entry.grid(row=1, column=i + 1, padx=5)
            entry.insert(customtkinter.END, '0')
            entry.bind("<FocusOut>", lambda event, idx=i: self.update_vector(event, idx, self.vector2))

        # Botón para calcular la suma de los vectores
        customtkinter.CTkButton(self.ventana, text="Sumar", command=self.sum_vectors).place(relx=0.5, rely=0.3, anchor=customtkinter.CENTER)

        self.result_label = customtkinter.CTkLabel(self.ventana, text="")
        self.result_label.place(x=45, y=300)

        # Canvas para mostrar los vectores y el resultado
        self.canvas = customtkinter.CTkCanvas(self.ventana, width=600, height=400, bg="white")
        self.canvas.place(relx=0.5, rely=0.6, anchor=customtkinter.CENTER)

    def update_vector(self, event, idx, vector):
        # Actualiza los valores del vector cuando el usuario sale del campo de entrada
        entry_value = event.widget.get()
        try:
            vector[idx] = float(entry_value)
        except ValueError:
            vector[idx] = 0

    def sum_vectors(self):
        # Calcula la suma de los vectores
        procedure = "Vector1 + Vector2 = Resultado\n"
        for i in range(3):
            self.result[i] = self.vector1[i] + self.vector2[i]
            procedure += f"{self.vector1[i]} + {self.vector2[i]} = {self.result[i]}\n"

        # Actualiza el Label con el procedimiento y el resultado
        self.result_label.configure(text=procedure)

        # Limpia el canvas
        self.canvas.delete("all")

        # Dibuja el vector 1
        self.draw_vector(150, 250, self.vector1, "blue")

        # Dibuja el vector 2
        self.draw_vector(150 + self.vector1[0] * 20, 250 - self.vector1[1] * 20, self.vector2, "green")

        # Dibuja el resultado
        self.draw_vector(150, 250, self.result, "red")

    def draw_vector(self, x, y, vector, color):
        # Dibuja el vector como una línea desde (x, y) hasta (x + vx, y + vy)
        self.canvas.create_line(x, y, x + vector[0] * 20, y - vector[1] * 20, fill=color, arrow=customtkinter.LAST)
        # Muestra los valores del vector como texto al lado de la flecha
        self.canvas.create_text(x + vector[0] * 20 + 10, y - vector[1] * 20, text=str(vector), fill=color)
