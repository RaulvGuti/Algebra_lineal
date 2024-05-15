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
        self.tamanio_filas_input = customtkinter.CTkEntry(master=self.frame, placeholder_text='Fil', width=60, height=35)
        self.tamanio_filas_input.pack(padx=40, pady=40)
        self.tamanio_filas_input.place(x=10, y=60)

        self.tamanio_columnas_input = customtkinter.CTkEntry(master=self.frame, placeholder_text='Col', width=60, height=35)
        self.tamanio_columnas_input.pack(padx=40, pady=40)
        self.tamanio_columnas_input.place(x=75, y=60)

        self.tamanio_bt = customtkinter.CTkButton(master=self.frame, text='Tamaño', height=35,
                                                  width=60, font=("Arial", 20), fg_color="#3E4446", command=self.tamanio_action)
        self.tamanio_bt.pack(padx=40, pady=40)
        self.tamanio_bt.place(x=140, y=60)

        self.tamanio_label = customtkinter.CTkLabel(master=self.frame, text='Al Realizar una Suma de matrices, ambas '
                                                                            'matrices deben ser del mismo '
                                                                            'orden.\nIngresar tamaño: 3=3x3',
                                                    font=("Arial", 12))
        self.tamanio_label.pack(padx=40, pady=40)
        self.tamanio_label.place(x=250, y=60)

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
        if int(self.tamanio_filas_input.get()) <= 1 or int(self.tamanio_columnas_input.get()) <= 1:
            CTkMessagebox(master=self.frame, width=100, height=100, title='Advertencia',
                          message='Número No valido\nIngresar Número mayor a 1')
        elif int(self.tamanio_filas_input.get()) >= 5 or int(self.tamanio_columnas_input.get()) >= 5:
            CTkMessagebox(master=self.frame, width=100, height=100, title='Advertencia',
                          message='Número No valido\nIngresar Número menor a 5')
        else:
            self.generar_matrizA(int(self.tamanio_filas_input.get()), int(self.tamanio_columnas_input.get()))
            self.generar_matrizB(int(self.tamanio_filas_input.get()), int(self.tamanio_columnas_input.get()))
            self.generar_matrizC(int(self.tamanio_filas_input.get()), int(self.tamanio_columnas_input.get()))
            self.generar_matrizD(int(self.tamanio_filas_input.get()), int(self.tamanio_columnas_input.get()))

    def no_matrices_action(self):  # Accion del numero de matrices boton, verifica el dato y me da el numero de matrices
        if int(self.no_matrices_input.get()) < 1:
            CTkMessagebox(master=self.frame, width=100, height=100, title='Advertencia',
                          message='Número No valido\nIngresar Número mayor a 0')
        elif int(self.no_matrices_input.get()) > 4:
            CTkMessagebox(master=self.frame, width=100, height=100, title='Advertencia',
                          message='Número No valido\nIngresar Número menor a 5')
        else:
            pass

    def generar_matrizA(self, tamanio_fila, tamanio_columna):  # Generar La Matriz A
        if tamanio_columna == tamanio_fila:
            if tamanio_fila == 4:
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
            elif tamanio_fila == 3:
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
            elif tamanio_fila == 2:
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
        else:
            if tamanio_fila == 2:
                if tamanio_columna == 3:
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
                elif tamanio_columna == 4:
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
            elif tamanio_fila == 3:
                if tamanio_columna == 2:
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

                    self.matrizA_5_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizA_5_input.pack(padx=40, pady=40)
                    self.matrizA_5_input.place(x=10, y=270)

                    self.matrizA_6_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizA_6_input.pack(padx=40, pady=40)
                    self.matrizA_6_input.place(x=55, y=270)
                elif tamanio_columna == 4:
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
            elif tamanio_fila == 4:
                if tamanio_columna == 2:
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
                    self.matrizA_3_input.place(x=145, y=180)

                    self.matrizA_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizA_4_input.pack(padx=40, pady=40)
                    self.matrizA_4_input.place(x=10, y=225)

                    self.matrizA_5_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizA_5_input.pack(padx=40, pady=40)
                    self.matrizA_5_input.place(x=100, y=225)

                    self.matrizA_6_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizA_6_input.pack(padx=40, pady=40)
                    self.matrizA_6_input.place(x=145, y=225)

                    self.matrizA_7_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizA_7_input.pack(padx=40, pady=40)
                    self.matrizA_7_input.place(x=55, y=270)

                    self.matrizA_8_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizA_8_input.pack(padx=40, pady=40)
                    self.matrizA_8_input.place(x=100, y=270)

                    self.matrizA_9_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizA_9_input.pack(padx=40, pady=40)
                    self.matrizA_9_input.place(x=10, y=315)

                    self.matrizA_10_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizA_10_input.pack(padx=40, pady=40)
                    self.matrizA_10_input.place(x=55, y=315)
                elif tamanio_columna == 3:
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

                    self.matrizA_10_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizA_10_input.pack(padx=40, pady=40)
                    self.matrizA_10_input.place(x=10, y=315)

                    self.matrizA_11_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizA_11_input.pack(padx=40, pady=40)
                    self.matrizA_11_input.place(x=55, y=315)

                    self.matrizA_12_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizA_12_input.pack(padx=40, pady=40)
                    self.matrizA_12_input.place(x=100, y=315)

    def generar_matrizB(self, tamanio_fila, tamanio_columna):  # Generar La Matriz B
        if tamanio_fila == tamanio_columna:
            if tamanio_fila == 4:
                self.matrizB_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 2', font=("Arial", 15))
                self.matrizB_label.pack(padx=40, pady=40)
                self.matrizB_label.place(x=255, y=150)

                self.matrizB_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_1_input.pack(padx=40, pady=40)
                self.matrizB_1_input.place(x=210, y=180)

                self.matrizB_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_2_input.pack(padx=40, pady=40)
                self.matrizB_2_input.place(x=255, y=180)

                self.matrizB_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_3_input.pack(padx=40, pady=40)
                self.matrizB_3_input.place(x=300, y=180)

                self.matrizB_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_4_input.pack(padx=40, pady=40)
                self.matrizB_4_input.place(x=345, y=180)

                self.matrizB_5_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_5_input.pack(padx=40, pady=40)
                self.matrizB_5_input.place(x=210, y=225)

                self.matrizB_6_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_6_input.pack(padx=40, pady=40)
                self.matrizB_6_input.place(x=255, y=225)

                self.matrizB_7_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_7_input.pack(padx=40, pady=40)
                self.matrizB_7_input.place(x=300, y=225)

                self.matrizB_8_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_8_input.pack(padx=40, pady=40)
                self.matrizB_8_input.place(x=345, y=225)

                self.matrizB_9_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_9_input.pack(padx=40, pady=40)
                self.matrizB_9_input.place(x=210, y=270)

                self.matrizB_10_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_10_input.pack(padx=40, pady=40)
                self.matrizB_10_input.place(x=255, y=270)

                self.matrizB_11_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_11_input.pack(padx=40, pady=40)
                self.matrizB_11_input.place(x=300, y=270)

                self.matrizB_12_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_12_input.pack(padx=40, pady=40)
                self.matrizB_12_input.place(x=345, y=270)

                self.matrizB_13_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_13_input.pack(padx=40, pady=40)
                self.matrizB_13_input.place(x=210, y=315)

                self.matrizB_14_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_14_input.pack(padx=40, pady=40)
                self.matrizB_14_input.place(x=255, y=315)

                self.matrizB_15_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_15_input.pack(padx=40, pady=40)
                self.matrizB_15_input.place(x=300, y=315)

                self.matrizB_16_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_16_input.pack(padx=40, pady=40)
                self.matrizB_16_input.place(x=345, y=315)
            elif tamanio_fila == 3:
                self.matrizB_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 2', font=("Arial", 15))
                self.matrizB_label.pack(padx=40, pady=40)
                self.matrizB_label.place(x=255, y=150)

                self.matrizB_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_1_input.pack(padx=40, pady=40)
                self.matrizB_1_input.place(x=210, y=180)

                self.matrizB_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_2_input.pack(padx=40, pady=40)
                self.matrizB_2_input.place(x=255, y=180)

                self.matrizB_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_3_input.pack(padx=40, pady=40)
                self.matrizB_3_input.place(x=300, y=180)

                self.matrizB_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_4_input.pack(padx=40, pady=40)
                self.matrizB_4_input.place(x=210, y=225)

                self.matrizB_5_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_5_input.pack(padx=40, pady=40)
                self.matrizB_5_input.place(x=255, y=225)

                self.matrizB_6_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_6_input.pack(padx=40, pady=40)
                self.matrizB_6_input.place(x=300, y=225)

                self.matrizB_7_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_7_input.pack(padx=40, pady=40)
                self.matrizB_7_input.place(x=210, y=270)

                self.matrizB_8_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_8_input.pack(padx=40, pady=40)
                self.matrizB_8_input.place(x=255, y=270)

                self.matrizB_9_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_9_input.pack(padx=40, pady=40)
                self.matrizB_9_input.place(x=300, y=270)
            elif tamanio_fila == 2:
                self.matrizB_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 2', font=("Arial", 15))
                self.matrizB_label.pack(padx=40, pady=40)
                self.matrizB_label.place(x=255, y=150)

                self.matrizB_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_1_input.pack(padx=40, pady=40)
                self.matrizB_1_input.place(x=210, y=180)

                self.matrizB_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_2_input.pack(padx=40, pady=40)
                self.matrizB_2_input.place(x=255, y=180)

                self.matrizB_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_3_input.pack(padx=40, pady=40)
                self.matrizB_3_input.place(x=210, y=225)

                self.matrizB_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizB_4_input.pack(padx=40, pady=40)
                self.matrizB_4_input.place(x=255, y=225)
        else:
            if tamanio_fila == 2:
                if tamanio_columna == 3:
                    self.matrizB_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 2', font=("Arial", 15))
                    self.matrizB_label.pack(padx=40, pady=40)
                    self.matrizB_label.place(x=255, y=150)

                    self.matrizB_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_1_input.pack(padx=40, pady=40)
                    self.matrizB_1_input.place(x=210, y=180)

                    self.matrizB_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_2_input.pack(padx=40, pady=40)
                    self.matrizB_2_input.place(x=255, y=180)

                    self.matrizB_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_3_input.pack(padx=40, pady=40)
                    self.matrizB_3_input.place(x=300, y=180)

                    self.matrizB_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_4_input.pack(padx=40, pady=40)
                    self.matrizB_4_input.place(x=210, y=225)

                    self.matrizB_5_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_5_input.pack(padx=40, pady=40)
                    self.matrizB_5_input.place(x=255, y=225)

                    self.matrizB_6_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_6_input.pack(padx=40, pady=40)
                    self.matrizB_6_input.place(x=300, y=225)
                elif tamanio_columna == 4:
                    self.matrizB_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 2', font=("Arial", 15))
                    self.matrizB_label.pack(padx=40, pady=40)
                    self.matrizB_label.place(x=255, y=150)

                    self.matrizB_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_1_input.pack(padx=40, pady=40)
                    self.matrizB_1_input.place(x=210, y=180)

                    self.matrizB_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_2_input.pack(padx=40, pady=40)
                    self.matrizB_2_input.place(x=255, y=180)

                    self.matrizB_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_3_input.pack(padx=40, pady=40)
                    self.matrizB_3_input.place(x=300, y=180)

                    self.matrizB_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_4_input.pack(padx=40, pady=40)
                    self.matrizB_4_input.place(x=345, y=180)

                    self.matrizB_5_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_5_input.pack(padx=40, pady=40)
                    self.matrizB_5_input.place(x=210, y=225)

                    self.matrizB_6_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_6_input.pack(padx=40, pady=40)
                    self.matrizB_6_input.place(x=255, y=225)

                    self.matrizB_7_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_7_input.pack(padx=40, pady=40)
                    self.matrizB_7_input.place(x=300, y=225)

                    self.matrizB_8_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_8_input.pack(padx=40, pady=40)
                    self.matrizB_8_input.place(x=345, y=225)
            elif tamanio_fila == 3:
                if tamanio_columna == 2:
                    self.matrizB_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 2', font=("Arial", 15))
                    self.matrizB_label.pack(padx=40, pady=40)
                    self.matrizB_label.place(x=255, y=150)

                    self.matrizB_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_1_input.pack(padx=40, pady=40)
                    self.matrizB_1_input.place(x=210, y=180)

                    self.matrizB_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_2_input.pack(padx=40, pady=40)
                    self.matrizB_2_input.place(x=255, y=180)

                    self.matrizB_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_3_input.pack(padx=40, pady=40)
                    self.matrizB_3_input.place(x=210, y=225)

                    self.matrizB_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_4_input.pack(padx=40, pady=40)
                    self.matrizB_4_input.place(x=255, y=225)

                    self.matrizB_5_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_5_input.pack(padx=40, pady=40)
                    self.matrizB_5_input.place(x=210, y=270)

                    self.matrizB_6_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_6_input.pack(padx=40, pady=40)
                    self.matrizB_6_input.place(x=255, y=270)
                elif tamanio_columna == 4:
                    self.matrizB_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 2', font=("Arial", 15))
                    self.matrizB_label.pack(padx=40, pady=40)
                    self.matrizB_label.place(x=255, y=150)

                    self.matrizB_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_1_input.pack(padx=40, pady=40)
                    self.matrizB_1_input.place(x=210, y=180)

                    self.matrizB_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_2_input.pack(padx=40, pady=40)
                    self.matrizB_2_input.place(x=255, y=180)

                    self.matrizB_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_3_input.pack(padx=40, pady=40)
                    self.matrizB_3_input.place(x=300, y=180)

                    self.matrizB_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_4_input.pack(padx=40, pady=40)
                    self.matrizB_4_input.place(x=345, y=180)

                    self.matrizB_5_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_5_input.pack(padx=40, pady=40)
                    self.matrizB_5_input.place(x=210, y=225)

                    self.matrizB_6_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_6_input.pack(padx=40, pady=40)
                    self.matrizB_6_input.place(x=255, y=225)

                    self.matrizB_7_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_7_input.pack(padx=40, pady=40)
                    self.matrizB_7_input.place(x=300, y=225)

                    self.matrizB_8_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_8_input.pack(padx=40, pady=40)
                    self.matrizB_8_input.place(x=345, y=225)

                    self.matrizB_9_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_9_input.pack(padx=40, pady=40)
                    self.matrizB_9_input.place(x=210, y=270)

                    self.matrizB_10_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_10_input.pack(padx=40, pady=40)
                    self.matrizB_10_input.place(x=255, y=270)

                    self.matrizB_11_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_11_input.pack(padx=40, pady=40)
                    self.matrizB_11_input.place(x=300, y=270)

                    self.matrizB_12_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_12_input.pack(padx=40, pady=40)
                    self.matrizB_12_input.place(x=345, y=270)
            elif tamanio_fila == 4:
                if tamanio_columna == 2:
                    self.matrizB_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 2', font=("Arial", 15))
                    self.matrizB_label.pack(padx=40, pady=40)
                    self.matrizB_label.place(x=255, y=150)

                    self.matrizB_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_1_input.pack(padx=40, pady=40)
                    self.matrizB_1_input.place(x=210, y=180)

                    self.matrizB_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_2_input.pack(padx=40, pady=40)
                    self.matrizB_2_input.place(x=255, y=180)

                    self.matrizB_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_3_input.pack(padx=40, pady=40)
                    self.matrizB_3_input.place(x=345, y=180)

                    self.matrizB_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_4_input.pack(padx=40, pady=40)
                    self.matrizB_4_input.place(x=210, y=225)

                    self.matrizB_5_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_5_input.pack(padx=40, pady=40)
                    self.matrizB_5_input.place(x=300, y=225)

                    self.matrizB_6_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_6_input.pack(padx=40, pady=40)
                    self.matrizB_6_input.place(x=345, y=225)

                    self.matrizB_7_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_7_input.pack(padx=40, pady=40)
                    self.matrizB_7_input.place(x=255, y=270)

                    self.matrizB_8_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_8_input.pack(padx=40, pady=40)
                    self.matrizB_8_input.place(x=300, y=270)

                    self.matrizB_9_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_9_input.pack(padx=40, pady=40)
                    self.matrizB_9_input.place(x=210, y=315)

                    self.matrizB_10_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_10_input.pack(padx=40, pady=40)
                    self.matrizB_10_input.place(x=255, y=315)
                elif tamanio_columna == 3:
                    self.matrizB_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 2', font=("Arial", 15))
                    self.matrizB_label.pack(padx=40, pady=40)
                    self.matrizB_label.place(x=255, y=150)

                    self.matrizB_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_1_input.pack(padx=40, pady=40)
                    self.matrizB_1_input.place(x=210, y=180)

                    self.matrizB_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_2_input.pack(padx=40, pady=40)
                    self.matrizB_2_input.place(x=255, y=180)

                    self.matrizB_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_3_input.pack(padx=40, pady=40)
                    self.matrizB_3_input.place(x=300, y=180)

                    self.matrizB_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_4_input.pack(padx=40, pady=40)
                    self.matrizB_4_input.place(x=210, y=225)

                    self.matrizB_5_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_5_input.pack(padx=40, pady=40)
                    self.matrizB_5_input.place(x=255, y=225)

                    self.matrizB_6_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_6_input.pack(padx=40, pady=40)
                    self.matrizB_6_input.place(x=300, y=225)

                    self.matrizB_7_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_7_input.pack(padx=40, pady=40)
                    self.matrizB_7_input.place(x=210, y=270)

                    self.matrizB_8_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_8_input.pack(padx=40, pady=40)
                    self.matrizB_8_input.place(x=255, y=270)

                    self.matrizB_9_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_9_input.pack(padx=40, pady=40)
                    self.matrizB_9_input.place(x=300, y=270)

                    self.matrizB_10_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_10_input.pack(padx=40, pady=40)
                    self.matrizB_10_input.place(x=210, y=315)

                    self.matrizB_11_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_11_input.pack(padx=40, pady=40)
                    self.matrizB_11_input.place(x=255, y=315)

                    self.matrizB_12_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_12_input.pack(padx=40, pady=40)
                    self.matrizB_12_input.place(x=300, y=315)

    def generar_matrizC(self, tamanio_fila, tamanio_columna):  # Generar La Matriz C
        if tamanio_fila == tamanio_columna:
            if tamanio_fila == 4:
                self.matrizC_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 3', font=("Arial", 15))
                self.matrizC_label.pack(padx=40, pady=40)
                self.matrizC_label.place(x=455, y=150)

                self.matrizC_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_1_input.pack(padx=40, pady=40)
                self.matrizC_1_input.place(x=410, y=180)

                self.matrizC_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_2_input.pack(padx=40, pady=40)
                self.matrizC_2_input.place(x=455, y=180)

                self.matrizC_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_3_input.pack(padx=40, pady=40)
                self.matrizC_3_input.place(x=500, y=180)

                self.matrizC_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_4_input.pack(padx=40, pady=40)
                self.matrizC_4_input.place(x=545, y=180)

                self.matrizC_5_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_5_input.pack(padx=40, pady=40)
                self.matrizC_5_input.place(x=410, y=225)

                self.matrizC_6_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_6_input.pack(padx=40, pady=40)
                self.matrizC_6_input.place(x=455, y=225)

                self.matrizC_7_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_7_input.pack(padx=40, pady=40)
                self.matrizC_7_input.place(x=500, y=225)

                self.matrizC_8_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_8_input.pack(padx=40, pady=40)
                self.matrizC_8_input.place(x=545, y=225)

                self.matrizC_9_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_9_input.pack(padx=40, pady=40)
                self.matrizC_9_input.place(x=410, y=270)

                self.matrizC_10_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_10_input.pack(padx=40, pady=40)
                self.matrizC_10_input.place(x=455, y=270)

                self.matrizC_11_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_11_input.pack(padx=40, pady=40)
                self.matrizC_11_input.place(x=500, y=270)

                self.matrizC_12_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_12_input.pack(padx=40, pady=40)
                self.matrizC_12_input.place(x=545, y=270)

                self.matrizC_13_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_13_input.pack(padx=40, pady=40)
                self.matrizC_13_input.place(x=410, y=315)

                self.matrizC_14_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_14_input.pack(padx=40, pady=40)
                self.matrizC_14_input.place(x=455, y=315)

                self.matrizC_15_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_15_input.pack(padx=40, pady=40)
                self.matrizC_15_input.place(x=500, y=315)

                self.matrizC_16_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_16_input.pack(padx=40, pady=40)
                self.matrizC_16_input.place(x=545, y=315)
            elif tamanio_fila == 3:
                self.matrizC_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 3', font=("Arial", 15))
                self.matrizC_label.pack(padx=40, pady=40)
                self.matrizC_label.place(x=455, y=150)

                self.matrizC_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_1_input.pack(padx=40, pady=40)
                self.matrizC_1_input.place(x=410, y=180)

                self.matrizC_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_2_input.pack(padx=40, pady=40)
                self.matrizC_2_input.place(x=455, y=180)

                self.matrizC_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_3_input.pack(padx=40, pady=40)
                self.matrizC_3_input.place(x=500, y=180)

                self.matrizC_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_4_input.pack(padx=40, pady=40)
                self.matrizC_4_input.place(x=410, y=225)

                self.matrizC_5_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_5_input.pack(padx=40, pady=40)
                self.matrizC_5_input.place(x=455, y=225)

                self.matrizC_6_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_6_input.pack(padx=40, pady=40)
                self.matrizC_6_input.place(x=500, y=225)

                self.matrizC_7_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_7_input.pack(padx=40, pady=40)
                self.matrizC_7_input.place(x=410, y=270)

                self.matrizC_8_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_8_input.pack(padx=40, pady=40)
                self.matrizC_8_input.place(x=455, y=270)

                self.matrizC_9_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_9_input.pack(padx=40, pady=40)
                self.matrizC_9_input.place(x=500, y=270)
            elif tamanio_fila == 2:
                self.matrizC_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 3', font=("Arial", 15))
                self.matrizC_label.pack(padx=40, pady=40)
                self.matrizC_label.place(x=455, y=150)

                self.matrizC_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_1_input.pack(padx=40, pady=40)
                self.matrizC_1_input.place(x=410, y=180)

                self.matrizC_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_2_input.pack(padx=40, pady=40)
                self.matrizC_2_input.place(x=455, y=180)

                self.matrizC_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_3_input.pack(padx=40, pady=40)
                self.matrizC_3_input.place(x=410, y=225)

                self.matrizC_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizC_4_input.pack(padx=40, pady=40)
                self.matrizC_4_input.place(x=455, y=225)

    def generar_matrizD(self, tamanio_fila, tamanio_columna):  # Generar La Matriz D
        if tamanio_fila == tamanio_columna:
            if tamanio_fila == 4:
                self.matrizD_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 4', font=("Arial", 15))
                self.matrizD_label.pack(padx=40, pady=40)
                self.matrizD_label.place(x=655, y=150)

                self.matrizD_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_1_input.pack(padx=40, pady=40)
                self.matrizD_1_input.place(x=610, y=180)

                self.matrizD_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_2_input.pack(padx=40, pady=40)
                self.matrizD_2_input.place(x=655, y=180)

                self.matrizD_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_3_input.pack(padx=40, pady=40)
                self.matrizD_3_input.place(x=700, y=180)

                self.matrizD_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_4_input.pack(padx=40, pady=40)
                self.matrizD_4_input.place(x=745, y=180)

                self.matrizD_5_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_5_input.pack(padx=40, pady=40)
                self.matrizD_5_input.place(x=610, y=225)

                self.matrizD_6_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_6_input.pack(padx=40, pady=40)
                self.matrizD_6_input.place(x=655, y=225)

                self.matrizD_7_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_7_input.pack(padx=40, pady=40)
                self.matrizD_7_input.place(x=700, y=225)

                self.matrizD_8_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_8_input.pack(padx=40, pady=40)
                self.matrizD_8_input.place(x=745, y=225)

                self.matrizD_9_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_9_input.pack(padx=40, pady=40)
                self.matrizD_9_input.place(x=610, y=270)

                self.matrizD_10_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_10_input.pack(padx=40, pady=40)
                self.matrizD_10_input.place(x=655, y=270)

                self.matrizD_11_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_11_input.pack(padx=40, pady=40)
                self.matrizD_11_input.place(x=700, y=270)

                self.matrizD_12_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_12_input.pack(padx=40, pady=40)
                self.matrizD_12_input.place(x=745, y=270)

                self.matrizD_13_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_13_input.pack(padx=40, pady=40)
                self.matrizD_13_input.place(x=610, y=315)

                self.matrizD_14_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_14_input.pack(padx=40, pady=40)
                self.matrizD_14_input.place(x=655, y=315)

                self.matrizD_15_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_15_input.pack(padx=40, pady=40)
                self.matrizD_15_input.place(x=700, y=315)

                self.matrizD_16_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_16_input.pack(padx=40, pady=40)
                self.matrizD_16_input.place(x=745, y=315)
            elif tamanio_fila == 3:
                self.matrizD_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 4', font=("Arial", 15))
                self.matrizD_label.pack(padx=40, pady=40)
                self.matrizD_label.place(x=655, y=150)

                self.matrizD_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_1_input.pack(padx=40, pady=40)
                self.matrizD_1_input.place(x=610, y=180)

                self.matrizD_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_2_input.pack(padx=40, pady=40)
                self.matrizD_2_input.place(x=655, y=180)

                self.matrizD_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_3_input.pack(padx=40, pady=40)
                self.matrizD_3_input.place(x=700, y=180)

                self.matrizD_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_4_input.pack(padx=40, pady=40)
                self.matrizD_4_input.place(x=610, y=225)

                self.matrizD_5_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_5_input.pack(padx=40, pady=40)
                self.matrizD_5_input.place(x=655, y=225)

                self.matrizD_6_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_6_input.pack(padx=40, pady=40)
                self.matrizD_6_input.place(x=700, y=225)

                self.matrizD_7_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_7_input.pack(padx=40, pady=40)
                self.matrizD_7_input.place(x=610, y=270)

                self.matrizD_8_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_8_input.pack(padx=40, pady=40)
                self.matrizD_8_input.place(x=655, y=270)

                self.matrizD_9_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_9_input.pack(padx=40, pady=40)
                self.matrizD_9_input.place(x=700, y=270)
            elif tamanio_fila == 2:
                self.matrizD_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 4', font=("Arial", 15))
                self.matrizD_label.pack(padx=40, pady=40)
                self.matrizD_label.place(x=655, y=150)

                self.matrizD_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_1_input.pack(padx=40, pady=40)
                self.matrizD_1_input.place(x=610, y=180)

                self.matrizD_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_2_input.pack(padx=40, pady=40)
                self.matrizD_2_input.place(x=655, y=180)

                self.matrizD_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_3_input.pack(padx=40, pady=40)
                self.matrizD_3_input.place(x=610, y=225)

                self.matrizD_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.matrizD_4_input.pack(padx=40, pady=40)
                self.matrizD_4_input.place(x=655, y=225)
