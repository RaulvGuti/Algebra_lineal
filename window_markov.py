import customtkinter
import cargar_datos_labels_frame


class WindowMarkov:
    def __init__(self):
        # ventana
        self.ventana = cargar_datos_labels_frame.cargar_datos()
        self.ventana.geometry('600x400')
        self.frame = cargar_datos_labels_frame.frame1(self.ventana)
        color = "#3E4446"
