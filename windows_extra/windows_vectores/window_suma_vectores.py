import customtkinter
import cargar_datos_labels_frame
import matplotlib.pyplot as plt
import numpy as np
from math import radians, cos, sin


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

        self.data_frame_suma = customtkinter.CTkFrame(self.ventana)
        self.data_frame_suma.place(relx=0.2, rely=0.1, anchor=customtkinter.CENTER)

        customtkinter.CTkLabel(self.data_frame_suma, text="Vector 1").grid(row=0, column=0, padx=5)
        for i in range(3):
            entry = customtkinter.CTkEntry(self.data_frame_suma, width=5)
            entry.grid(row=0, column=i + 1, padx=5)
            entry.insert(customtkinter.END, '0')
            entry.bind("<FocusOut>", lambda event, idx=i: self.update_vector(event, idx, self.vector1))

        customtkinter.CTkLabel(self.data_frame_suma, text="Vector 2").grid(row=1, column=0, padx=5)
        for i in range(3):
            entry = customtkinter.CTkEntry(self.data_frame_suma, width=5)
            entry.grid(row=1, column=i + 1, padx=5)
            entry.insert(customtkinter.END, '0')
            entry.bind("<FocusOut>", lambda event, idx=i: self.update_vector(event, idx, self.vector2))

        customtkinter.CTkButton(self.ventana, text="Sumar", command=self.sum_vectors).place(relx=0.2, rely=0.3,
                                                                                            anchor=customtkinter.CENTER)

        self.result_label = customtkinter.CTkLabel(self.ventana, text="")
        self.result_label.place(x=45, y=300)

        self.data_frame_conversion = customtkinter.CTkFrame(self.ventana)
        self.data_frame_conversion.place(relx=0.8, rely=0.1, anchor=customtkinter.CENTER)

        customtkinter.CTkLabel(self.data_frame_conversion, text="Magnitud").grid(row=0, column=0, padx=5)
        self.magnitude_entry = customtkinter.CTkEntry(self.data_frame_conversion, width=5)
        self.magnitude_entry.grid(row=0, column=1, padx=5)
        self.magnitude_entry.insert(customtkinter.END, '0')

        customtkinter.CTkLabel(self.data_frame_conversion, text="Ángulo").grid(row=1, column=0, padx=5)
        self.angle_entry = customtkinter.CTkEntry(self.data_frame_conversion, width=5)
        self.angle_entry.grid(row=1, column=1, padx=5)
        self.angle_entry.insert(customtkinter.END, '0')

        customtkinter.CTkButton(self.ventana, text="Calcular Componentes", command=self.calculate_components).place(
            relx=0.8, rely=0.3, anchor=customtkinter.CENTER)

    def update_vector(self, event, idx, vector):
        entry_value = event.widget.get()
        try:
            vector[idx] = float(entry_value)
        except ValueError:
            vector[idx] = 0

    def sum_vectors(self):
        procedure = "Vector1 + Vector2 = Resultado\n"
        for i in range(3):
            self.result[i] = self.vector1[i] + self.vector2[i]
            procedure += f"{self.vector1[i]} + {self.vector2[i]} = {self.result[i]}\n"

        self.result_label.configure(text=procedure)

        self.draw_vectors_with_pyplot(self.vector1, self.vector2, self.result)

    def calculate_components(self):
        magnitude = float(self.magnitude_entry.get())
        angle_degrees = float(self.angle_entry.get())
        angle_radians = radians(angle_degrees)

        x_component = magnitude * cos(angle_radians)
        y_component = magnitude * sin(angle_radians)

        self.result_label.configure(text=f"Componente X: {x_component:.2f}, Componente Y: {y_component:.2f}")

        self.draw_vector_with_pyplot(x_component, y_component)

    def draw_vectors_with_pyplot(self, vector1, vector2, result):
        fig, ax = plt.subplots()
        ax.quiver(0, 0, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='blue', label='Vector 1')
        ax.quiver(vector1[0], vector1[1], vector2[0], vector2[1], angles='xy', scale_units='xy', scale=1, color='green',
                  label='Vector 2')
        ax.quiver(0, 0, result[0], result[1], angles='xy', scale_units='xy', scale=1, color='red', label='Resultado')
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_aspect('equal', 'box')
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.grid(color='gray', linestyle='--', linewidth=0.5)
        ax.legend()
        plt.xlabel('Componente X')
        plt.ylabel('Componente Y')
        plt.title('Suma de Vectores')
        plt.show()

    def draw_vector_with_pyplot(self, x_component, y_component):
        fig, ax = plt.subplots()
        ax.quiver(0, 0, x_component, y_component, angles='xy', scale_units='xy', scale=1, color='blue')
        ax.set_xlim(-10, 10)
        ax.set_ylim(-10, 10)
        ax.set_aspect('equal', 'box')
        ax.axhline(0, color='black', linewidth=0.5)
        ax.axvline(0, color='black', linewidth=0.5)
        ax.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.xlabel('Componente X')
        plt.ylabel('Componente Y')
        plt.title('Vector Resultante')
        plt.show()