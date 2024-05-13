import customtkinter
import cargar_datos_labels_frame


class WindowCifrado:
    def __init__(self):
        # ventana
        self.ventana = cargar_datos_labels_frame.cargar_datos()
        self.ventana.geometry('600x200')
        self.frame = cargar_datos_labels_frame.frame1(self.ventana)
        color = "#3E4446"

        # buttons
        self.button_suma = customtkinter.CTkButton(master=self.frame, text='Cifrado', height=100, width=210,
                                                   font=("Arial", 20), fg_color="#3E4446")

        self.button_suma.pack(pady=10, padx=10)
        self.button_suma.place(x=50, y=10)

        self.button_multi = customtkinter.CTkButton(master=self.frame, text='Descifrado', height=100, width=210,
                                                    font=("Arial", 20), fg_color="#3E4446")

        self.button_multi.pack(pady=10, padx=10)
        self.button_multi.place(x=350, y=10)
