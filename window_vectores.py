import customtkinter
import cargar_datos_labels_frame
from windows_extra.windows_vectores.window_suma_vectores import WindowSumaVector
from windows_extra.windows_vectores.window_punto_vectores import WindowPuntoVector


class WindowVectores:
    def __init__(self):
        # ventana
        self.ventana = cargar_datos_labels_frame.cargar_datos()
        self.ventana.geometry('570x190')
        self.frame = cargar_datos_labels_frame.frame1(self.ventana)
        color = "#3E4446"

        # buttons
        self.button_suma = customtkinter.CTkButton(master=self.frame, text='Suma', height=100, width=210,
                                                   font=("Arial", 20), fg_color="#3E4446", command=self.open_suma)

        self.button_suma.pack(pady=10, padx=10)
        self.button_suma.place(x=50, y=10)

        self.button_punto = customtkinter.CTkButton(master=self.frame, text='Producto Punto', height=100, width=210,
                                                    font=("Arial", 20), fg_color="#3E4446", command=self.open_punto)

        self.button_punto.pack(pady=10, padx=10)
        self.button_punto.place(x=300, y=10)

    def open_suma(self):
        ventana = WindowSumaVector()

    def open_punto(self):
        ventana = WindowPuntoVector()
