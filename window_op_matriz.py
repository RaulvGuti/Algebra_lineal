import customtkinter
import cargar_datos_labels_frame
from windows_extra.windows_op_matriz.window_suma_op import WindowSumaOp
from windows_extra.windows_op_matriz.window_resta_op import WindowRestaOp
from windows_extra.windows_op_matriz.window_multiplicar_op import WindowMultiplicarOp
from windows_extra.windows_op_matriz.window_punto_op import WindowPuntoOp


class WindowMatriz:
    def __init__(self):
        # ventana
        self.ventana = cargar_datos_labels_frame.cargar_datos()
        self.ventana.geometry('450x300')
        self.frame = cargar_datos_labels_frame.frame1(self.ventana)
        color = "#3E4446"

        # buttons
        self.button_suma = customtkinter.CTkButton(master=self.frame, text='Suma', height=100,
                                                     width=150,
                                                     font=("Arial", 20), fg_color="#3E4446", command=self.open_suma)

        self.button_suma.pack(pady=10, padx=10)
        self.button_suma.place(x=50, y=10)

        self.button_resta = customtkinter.CTkButton(master=self.frame, text='Resta', height=100,
                                                   width=150,
                                                   font=("Arial", 20), fg_color="#3E4446", command=self.open_resta)

        self.button_resta.pack(pady=10, padx=10)
        self.button_resta.place(x=50, y=150)

        self.button_multi = customtkinter.CTkButton(master=self.frame, text='Multiplicación', height=100,
                                                   width=150,
                                                   font=("Arial", 20), fg_color="#3E4446", command=self.open_multiplicar)

        self.button_multi.pack(pady=10, padx=10)
        self.button_multi.place(x=230, y=10)

        self.button_punto = customtkinter.CTkButton(master=self.frame, text='Producto Punto', height=100,
                                                    width=150,
                                                    font=("Arial", 20), fg_color="#3E4446", command=self.open_punto)

        self.button_punto.pack(pady=10, padx=10)
        self.button_punto.place(x=230, y=150)

    def open_suma(self):
        ventana = WindowSumaOp()

    def open_resta(self):
        ventana = WindowRestaOp()

    def open_multiplicar(self):
        ventana = WindowMultiplicarOp()

    def open_punto(self):
        ventana = WindowPuntoOp()
