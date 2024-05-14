import customtkinter
import cargar_datos_labels_frame


class WindowSumaOp:
    def __init__(self):
        self.ventana = cargar_datos_labels_frame.cargar_datos()
        self.ventana.geometry("1000x600")
        self.frame = cargar_datos_labels_frame.frame1(self.ventana)
        color = "#3E4446"

        # Label Ventana
        self.suma_label = customtkinter.CTkLabel(master=self.frame, text='Suma de Matrices', font=("Arial", 40))
        self.suma_label.pack(padx=40, pady=40)
        self.suma_label.place(x=10, y=10)

        # Ingreso Tamaño de Matriz
        self.tamanio_input = customtkinter.CTkEntry(master=self.frame, placeholder_text='Tamaño', width=60, height=35)
        self.tamanio_input.pack(padx=40, pady=40)
        self.tamanio_input.place(x=10, y=60)

        self.tamanio_bt = customtkinter.CTkButton(master=self.frame, text='Tamaño', height=35,
                                                  width=60, font=("Arial", 20), fg_color="#3E4446")
        self.tamanio_bt.pack(padx=40, pady=40)
        self.tamanio_bt.place(x=75, y=60)
