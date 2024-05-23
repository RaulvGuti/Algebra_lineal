import customtkinter
import cargar_datos_labels_frame


class WindowPuntoOp:
    def __init__(self):
        self.ventana = cargar_datos_labels_frame.cargar_datos()
        self.ventana.geometry("400x200")
        self.frame = cargar_datos_labels_frame.frame1(self.ventana)
        color = "#3E4446"

        # Label Ventana
        self.prd_label = customtkinter.CTkLabel(master=self.frame, text='Producto Punto', font=("Arial", 40))
        self.prd_label.pack(padx=40, pady=40)
        self.prd_label.place(x=10, y=10)

        self.tamanio_label = customtkinter.CTkLabel(master=self.frame, text='Inhabilitado Por el Momento',
                                                    font=("Arial", 15))
        self.tamanio_label.pack(padx=40, pady=40)
        self.tamanio_label.place(x=10, y=60)
