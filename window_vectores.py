import customtkinter
import cargar_datos_labels_frame


class WindowVectores:
    def __init__(self):
        # ventana
        self.ventana = cargar_datos_labels_frame.cargar_datos()
        self.ventana.geometry('600x300')
        self.frame = cargar_datos_labels_frame.frame1(self.ventana)
        color = "#3E4446"

        # buttons
        self.button_suma = customtkinter.CTkButton(master=self.frame, text='Suma', height=100, width=210,
                                                   font=("Arial", 20), fg_color="#3E4446")

        self.button_suma.pack(pady=10, padx=10)
        self.button_suma.place(x=50, y=10)

        self.button_resta = customtkinter.CTkButton(master=self.frame, text='Producto Punto', height=100, width=210,
                                                    font=("Arial", 20), fg_color="#3E4446")

        self.button_resta.pack(pady=10, padx=10)
        self.button_resta.place(x=200, y=150)

        self.button_multi = customtkinter.CTkButton(master=self.frame, text='Producto Cruz', height=100, width=210,
                                                    font=("Arial", 20), fg_color="#3E4446")

        self.button_multi.pack(pady=10, padx=10)
        self.button_multi.place(x=350, y=10)
