import customtkinter
import cargar_datos_labels_frame
from windows_extra.windows_cifrado.window_cifrar import WindowCifrar
from windows_extra.windows_cifrado.window_descifrar import WindowDescifrar


class WindowCifrado:
    def __init__(self):
        # ventana
        self.ventana = cargar_datos_labels_frame.cargar_datos()
        self.ventana.geometry('600x150')
        self.frame = cargar_datos_labels_frame.frame1(self.ventana)
        color = "#3E4446"

        # buttons
        self.button_cifrado = customtkinter.CTkButton(master=self.frame, text='Cifrado', height=100, width=210,
                                                   font=("Arial", 20), fg_color="#3E4446", command=self.open_cifrar)

        self.button_cifrado.pack(pady=10, padx=10)
        self.button_cifrado.place(x=50, y=10)

        self.button_descifrado = customtkinter.CTkButton(master=self.frame, text='Descifrado', height=100, width=210,
                                                    font=("Arial", 20), fg_color="#3E4446", command=self.open_descifrar)

        self.button_descifrado.pack(pady=10, padx=10)
        self.button_descifrado.place(x=320, y=10)

    def open_cifrar(self):
        ventana = WindowCifrar()

    def open_descifrar(self):
        ventana = WindowDescifrar()
