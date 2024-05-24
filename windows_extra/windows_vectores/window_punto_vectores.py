import customtkinter
import cargar_datos_labels_frame
import tkinter


class WindowPuntoVector:
    def __init__(self):
        # Ventana
        self.ventana = cargar_datos_labels_frame.cargar_datos()
        self.ventana.geometry('600x500')
        self.frame = cargar_datos_labels_frame.frame1(self.ventana)

        # Etiquetas de instrucción
        self.label_instruccion1 = customtkinter.CTkLabel(master=self.frame,
                                                         text="Ingrese los componentes de los vectores separados por espacio:")
        self.label_instruccion1.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.label_instruccion2 = customtkinter.CTkLabel(master=self.frame, text="Ejemplo: 1 2 3")
        self.label_instruccion2.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        # Entradas de los vectores
        self.label_vector1 = customtkinter.CTkLabel(master=self.frame, text="Vector 1:")
        self.label_vector1.grid(row=2, column=0, padx=5, pady=5)
        self.entry_vector1 = customtkinter.CTkEntry(master=self.frame)
        self.entry_vector1.grid(row=2, column=1, padx=5, pady=5)

        self.label_vector2 = customtkinter.CTkLabel(master=self.frame, text="Vector 2:")
        self.label_vector2.grid(row=3, column=0, padx=5, pady=5)
        self.entry_vector2 = customtkinter.CTkEntry(master=self.frame)
        self.entry_vector2.grid(row=3, column=1, padx=5, pady=5)

        # Botón para calcular el producto punto
        self.calcular_button = customtkinter.CTkButton(master=self.frame, text="Calcular",
                                                       command=self.calcular_producto_punto)
        self.calcular_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Etiqueta para mostrar los pasos importantes
        self.pasos_label = customtkinter.CTkLabel(master=self.frame, text="")
        self.pasos_label.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        # Etiqueta para mostrar el resultado
        self.resultado_label = customtkinter.CTkLabel(master=self.frame, text="")
        self.resultado_label.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def calcular_producto_punto(self):
        try:
            # Obtener los vectores ingresados por el usuario
            vector1 = [float(x) for x in self.entry_vector1.get().split()]
            vector2 = [float(x) for x in self.entry_vector2.get().split()]

            # Mostrar los pasos importantes
            pasos = self.obtener_pasos(vector1, vector2)
            self.pasos_label.configure(text=pasos)

            # Calcular el producto punto
            resultado = self.producto_punto(vector1, vector2)

            # Mostrar el resultado en la etiqueta resultado_label
            self.resultado_label.configure(text=f"El producto punto de los vectores es: {resultado}")

        except ValueError as e:
            # Manejar el caso de que ocurra un error al convertir los datos a números
            self.resultado_label.configure(text=str(e))

    @staticmethod
    def obtener_pasos(v1, v2):
        """
        Obtiene los pasos importantes del cálculo del producto punto.

        Args:
        v1 (list): Primer vector.
        v2 (list): Segundo vector.

        Returns:
        str: Pasos importantes del cálculo.
        """
        pasos = "Pasos importantes:\n"
        pasos += f"Vector 1: {v1}\n"
        pasos += f"Vector 2: {v2}\n"
        pasos += f"Producto de cada componente: {[x * y for x, y in zip(v1, v2)]}\n"
        pasos += f"Suma de los productos: {sum(x * y for x, y in zip(v1, v2))}\n"
        return pasos

    @staticmethod
    def producto_punto(v1, v2):
        """
        Calcula el producto punto de dos vectores.

        Args:
        v1 (list): Primer vector.
        v2 (list): Segundo vector.

        Returns:
        float: Producto punto de los dos vectores.
        """
        if len(v1) != len(v2):
            raise ValueError("Los vectores deben tener la misma longitud.")

        return sum(x * y for x, y in zip(v1, v2))


# Crear la ventana
if __name__ == "__main__":
    ventana_inversa = WindowPuntoVector()
    ventana_inversa.ventana.mainloop()
