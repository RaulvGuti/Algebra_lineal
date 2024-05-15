import customtkinter
import cargar_datos_labels_frame
from CTkMessagebox import CTkMessagebox


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
                                                  width=60, font=("Arial", 20), fg_color="#3E4446", command=self.tamanio_action)
        self.tamanio_bt.pack(padx=40, pady=40)
        self.tamanio_bt.place(x=75, y=60)

        self.tamanio_label = customtkinter.CTkLabel(master=self.frame, text='Al Realizar una Suma de matrices, ambas '
                                                                            'matrices deben ser cuadradas del mismo '
                                                                            'orden.\nIngresar tamaño: 3=3x3',
                                                    font=("Arial", 12))
        self.tamanio_label.pack(padx=40, pady=40)
        self.tamanio_label.place(x=200, y=60)

        # Ingreso Cantidad de matrices
        self.no_matrices_input = customtkinter.CTkEntry(master=self.frame, placeholder_text='No. Matrices', width=85, height=35)
        self.no_matrices_input.pack(padx=40, pady=40)
        self.no_matrices_input.place(x=10, y=100)

        self.no_matrices_bt = customtkinter.CTkButton(master=self.frame, text='Aplicar', height=35,
                                                  width=60, font=("Arial", 20), fg_color="#3E4446",
                                                  command=self.no_matrices_action)
        self.no_matrices_bt.pack(padx=40, pady=40)
        self.no_matrices_bt.place(x=100, y=100)

        self.no_matrices_label = customtkinter.CTkLabel(master=self.frame, text='¿Cuántas Matrices Sumará?\nMaximo 4('
                                                                                'para no ocupar mucho espacio)',
                                                    font=("Arial", 12))
        self.no_matrices_label.pack(padx=40, pady=40)
        self.no_matrices_label.place(x=200, y=100)

    def tamanio_action(self):  # Accion del tamaño boton, verifica el dato, y pone la cantidad de ingresos que habrán
        if int(self.tamanio_input.get()) <= 1:
            CTkMessagebox(master=self.frame, width=100, height=100, title='Advertencia',
                          message='Número No valido\nIngresar Número mayor a 1')
        elif int(self.tamanio_input.get()) >= 5:
            CTkMessagebox(master=self.frame, width=100, height=100, title='Advertencia',
                          message='Número No valido\nIngresar Número menor a 5')
        else:
            self.generar_matrizA(int(self.tamanio_input.get()))

    def no_matrices_action(self):  # Accion del numero de matrices boton, verifica el dato y me da el numero de matrices
        if int(self.no_matrices_input.get()) < 1:
            CTkMessagebox(master=self.frame, width=100, height=100, title='Advertencia',
                          message='Número No valido\nIngresar Número mayor a 0')
        elif int(self.no_matrices_input.get()) > 4:
            CTkMessagebox(master=self.frame, width=100, height=100, title='Advertencia',
                          message='Número No valido\nIngresar Número menor a 5')
        else:
            pass

    def generar_matrizA(self, tamanio):  # Generar La Matriz A
        if tamanio == 4:
            self.matrizA_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 1', font=("Arial", 15))
            self.matrizA_label.pack(padx=40, pady=40)
            self.matrizA_label.place(x=55, y=150)

            self.matrizA_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_1_input.pack(padx=40, pady=40)
            self.matrizA_1_input.place(x=10, y=180)

            self.matrizA_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_2_input.pack(padx=40, pady=40)
            self.matrizA_2_input.place(x=55, y=180)

            self.matrizA_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_3_input.pack(padx=40, pady=40)
            self.matrizA_3_input.place(x=100, y=180)

            self.matrizA_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_4_input.pack(padx=40, pady=40)
            self.matrizA_4_input.place(x=145, y=180)

            self.matrizA_5_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_5_input.pack(padx=40, pady=40)
            self.matrizA_5_input.place(x=10, y=225)

            self.matrizA_6_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_6_input.pack(padx=40, pady=40)
            self.matrizA_6_input.place(x=55, y=225)

            self.matrizA_7_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_7_input.pack(padx=40, pady=40)
            self.matrizA_7_input.place(x=100, y=225)

            self.matrizA_8_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_8_input.pack(padx=40, pady=40)
            self.matrizA_8_input.place(x=145, y=225)

            self.matrizA_9_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_9_input.pack(padx=40, pady=40)
            self.matrizA_9_input.place(x=10, y=270)

            self.matrizA_10_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_10_input.pack(padx=40, pady=40)
            self.matrizA_10_input.place(x=55, y=270)

            self.matrizA_11_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_11_input.pack(padx=40, pady=40)
            self.matrizA_11_input.place(x=100, y=270)

            self.matrizA_12_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_12_input.pack(padx=40, pady=40)
            self.matrizA_12_input.place(x=145, y=270)

            self.matrizA_13_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_13_input.pack(padx=40, pady=40)
            self.matrizA_13_input.place(x=10, y=315)

            self.matrizA_14_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_14_input.pack(padx=40, pady=40)
            self.matrizA_14_input.place(x=55, y=315)

            self.matrizA_15_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_15_input.pack(padx=40, pady=40)
            self.matrizA_15_input.place(x=100, y=315)

            self.matrizA_16_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_16_input.pack(padx=40, pady=40)
            self.matrizA_16_input.place(x=145, y=315)
        elif tamanio == 3:
            self.matrizA_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 1', font=("Arial", 15))
            self.matrizA_label.pack(padx=40, pady=40)
            self.matrizA_label.place(x=55, y=150)

            self.matrizA_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_1_input.pack(padx=40, pady=40)
            self.matrizA_1_input.place(x=10, y=180)

            self.matrizA_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_2_input.pack(padx=40, pady=40)
            self.matrizA_2_input.place(x=55, y=180)

            self.matrizA_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_3_input.pack(padx=40, pady=40)
            self.matrizA_3_input.place(x=100, y=180)

            self.matrizA_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_4_input.pack(padx=40, pady=40)
            self.matrizA_4_input.place(x=10, y=225)

            self.matrizA_5_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_5_input.pack(padx=40, pady=40)
            self.matrizA_5_input.place(x=55, y=225)

            self.matrizA_6_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_6_input.pack(padx=40, pady=40)
            self.matrizA_6_input.place(x=100, y=225)

            self.matrizA_7_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_7_input.pack(padx=40, pady=40)
            self.matrizA_7_input.place(x=10, y=270)

            self.matrizA_8_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_8_input.pack(padx=40, pady=40)
            self.matrizA_8_input.place(x=55, y=270)

            self.matrizA_9_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_9_input.pack(padx=40, pady=40)
            self.matrizA_9_input.place(x=100, y=270)
        elif tamanio == 2:
            self.matrizA_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 1', font=("Arial", 15))
            self.matrizA_label.pack(padx=40, pady=40)
            self.matrizA_label.place(x=55, y=150)

            self.matrizA_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_1_input.pack(padx=40, pady=40)
            self.matrizA_1_input.place(x=10, y=180)

            self.matrizA_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_2_input.pack(padx=40, pady=40)
            self.matrizA_2_input.place(x=55, y=180)

            self.matrizA_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_3_input.pack(padx=40, pady=40)
            self.matrizA_3_input.place(x=10, y=225)

            self.matrizA_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
            self.matrizA_4_input.pack(padx=40, pady=40)
            self.matrizA_4_input.place(x=55, y=225)
