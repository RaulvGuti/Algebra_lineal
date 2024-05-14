import customtkinter
import cargar_datos_labels_frame


class WindowPuntoOp:
    def __init__(self):
        self.ventana = cargar_datos_labels_frame.cargar_datos()
        self.ventana.geometry("1000x600")
        self.frame = cargar_datos_labels_frame.frame1(self.ventana)
        color = "#3E4446"
