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

        # procedimiento
        self.label_proc = customtkinter.CTkLabel(master=self.frame, text='', font=("Arial", 12))
        self.label_proc.pack(padx=40, pady=40)
        self.label_proc.place(x=210, y=405)

        # Generar bloques de matrices
        self.matrizA_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 1', font=("Arial", 15))
        self.matrizA_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizA_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizA_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizA_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizA_5_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizA_6_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizA_7_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizA_8_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizA_9_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizA_10_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizA_11_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizA_12_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizA_13_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizA_14_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizA_15_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizA_16_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)

        self.matrizB_label = customtkinter.CTkLabel(master=self.frame, text='Matriz 1', font=("Arial", 15))
        self.matrizB_1_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizB_2_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizB_3_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizB_4_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizB_5_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizB_6_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizB_7_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizB_8_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizB_9_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizB_10_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizB_11_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizB_12_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizB_13_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizB_14_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizB_15_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
        self.matrizB_16_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)

        self.resultadol = customtkinter.CTkLabel(master=self.frame, text='Resultado', font=("Arial", 15))
        self.resultado1 = customtkinter.CTkEntry(master=self.frame, width=40, height=40, state='disabled')
        self.resultado2 = customtkinter.CTkEntry(master=self.frame, width=40, height=40, state='disabled')
        self.resultado3 = customtkinter.CTkEntry(master=self.frame, width=40, height=40, state='disabled')
        self.resultado4 = customtkinter.CTkEntry(master=self.frame, width=40, height=40, state='disabled')
        self.resultado5 = customtkinter.CTkEntry(master=self.frame, width=40, height=40, state='disabled')
        self.resultado6 = customtkinter.CTkEntry(master=self.frame, width=40, height=40, state='disabled')
        self.resultado7 = customtkinter.CTkEntry(master=self.frame, width=40, height=40, state='disabled')
        self.resultado8 = customtkinter.CTkEntry(master=self.frame, width=40, height=40, state='disabled')
        self.resultado9 = customtkinter.CTkEntry(master=self.frame, width=40, height=40, state='disabled')
        self.resultado10 = customtkinter.CTkEntry(master=self.frame, width=40, height=40, state='disabled')
        self.resultado11 = customtkinter.CTkEntry(master=self.frame, width=40, height=40, state='disabled')
        self.resultado12 = customtkinter.CTkEntry(master=self.frame, width=40, height=40, state='disabled')
        self.resultado13 = customtkinter.CTkEntry(master=self.frame, width=40, height=40, state='disabled')
        self.resultado14 = customtkinter.CTkEntry(master=self.frame, width=40, height=40, state='disabled')
        self.resultado15 = customtkinter.CTkEntry(master=self.frame, width=40, height=40, state='disabled')
        self.resultado16 = customtkinter.CTkEntry(master=self.frame, width=40, height=40, state='disabled')

        # Generar Boton suma
        self.suma_bt = customtkinter.CTkButton(master=self.frame, text='SUMAR', height=35, width=60,
                                               font=("Arial", 20), fg_color="#3E4446", command=self.sumar_matriz)
        self.suma_bt.pack(padx=40, pady=40)
        self.suma_bt.place(x=800, y=250)

    def tamanio_action(self):  # Accion del tamaño boton, verifica el dato, y pone la cantidad de ingresos que habrán
        if int(self.tamanio_filas_input.get()) <= 1 or int(self.tamanio_columnas_input.get()) <= 1:
            CTkMessagebox(master=self.frame, width=100, height=100, title='Advertencia',
                          message='Número No valido\nIngresar Número mayor a 1')
        elif int(self.tamanio_filas_input.get()) >= 5 or int(self.tamanio_columnas_input.get()) >= 5:
            CTkMessagebox(master=self.frame, width=100, height=100, title='Advertencia',
                          message='Número No valido\nIngresar Número menor a 5')
        else:
            self.clear_window()
            self.generar_matrizA(int(self.tamanio_filas_input.get()), int(self.tamanio_columnas_input.get()))
            self.generar_matrizB(int(self.tamanio_filas_input.get()), int(self.tamanio_columnas_input.get()))

    def clear_window(self):
        self.matrizA_label.destroy()
        self.matrizA_1_input.destroy()
        self.matrizA_2_input.destroy()
        self.matrizA_3_input.destroy()
        self.matrizA_4_input.destroy()
        self.matrizA_5_input.destroy()
        self.matrizA_6_input.destroy()
        self.matrizA_7_input.destroy()
        self.matrizA_8_input.destroy()
        self.matrizA_9_input.destroy()
        self.matrizA_10_input.destroy()
        self.matrizA_11_input.destroy()
        self.matrizA_12_input.destroy()
        self.matrizA_13_input.destroy()
        self.matrizA_14_input.destroy()
        self.matrizA_15_input.destroy()
        self.matrizA_16_input.destroy()

        self.matrizB_label.destroy()
        self.matrizB_1_input.destroy()
        self.matrizB_2_input.destroy()
        self.matrizB_3_input.destroy()
        self.matrizB_4_input.destroy()
        self.matrizB_5_input.destroy()
        self.matrizB_6_input.destroy()
        self.matrizB_7_input.destroy()
        self.matrizB_8_input.destroy()
        self.matrizB_9_input.destroy()
        self.matrizB_10_input.destroy()
        self.matrizB_11_input.destroy()
        self.matrizB_12_input.destroy()
        self.matrizB_13_input.destroy()
        self.matrizB_14_input.destroy()
        self.matrizB_15_input.destroy()
        self.matrizB_16_input.destroy()

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

                    self.matrizA_7_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizA_7_input.pack(padx=40, pady=40)
                    self.matrizA_7_input.place(x=10, y=315)

                    self.matrizA_8_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizA_8_input.pack(padx=40, pady=40)
                    self.matrizA_8_input.place(x=55, y=315)
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

                    self.matrizB_7_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_7_input.pack(padx=40, pady=40)
                    self.matrizB_7_input.place(x=210, y=315)

                    self.matrizB_8_input = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.matrizB_8_input.pack(padx=40, pady=40)
                    self.matrizB_8_input.place(x=255, y=315)
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

    def generar_resultado(self, tamanio_fila, tamanio_columna):  # Generar La Matriz Resultado
        if tamanio_columna == tamanio_fila:
            if tamanio_fila == 4:
                self.resultadol.pack(padx=40, pady=40)
                self.resultadol.place(x=55, y=375)

                self.resultado1 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado1.pack(padx=40, pady=40)
                self.resultado1.place(x=10, y=405)

                self.resultado2 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado2.pack(padx=40, pady=40)
                self.resultado2.place(x=55, y=405)

                self.resultado3 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado3.pack(padx=40, pady=40)
                self.resultado3.place(x=100, y=405)

                self.resultado4 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado4.pack(padx=40, pady=40)
                self.resultado4.place(x=145, y=405)

                self.resultado5 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado5.pack(padx=40, pady=40)
                self.resultado5.place(x=10, y=450)

                self.resultado6 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado6.pack(padx=40, pady=40)
                self.resultado6.place(x=55, y=450)

                self.resultado7 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado7.pack(padx=40, pady=40)
                self.resultado7.place(x=100, y=450)

                self.resultado8 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado8.pack(padx=40, pady=40)
                self.resultado8.place(x=145, y=450)

                self.resultado9 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado9.pack(padx=40, pady=40)
                self.resultado9.place(x=10, y=495)

                self.resultado10 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado10.pack(padx=40, pady=40)
                self.resultado10.place(x=55, y=495)

                self.resultado11 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado11.pack(padx=40, pady=40)
                self.resultado11.place(x=100, y=495)

                self.resultado12 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado12.pack(padx=40, pady=40)
                self.resultado12.place(x=145, y=495)

                self.resultado13 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado13.pack(padx=40, pady=40)
                self.resultado13.place(x=10, y=540)

                self.resultado14 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado14.pack(padx=40, pady=40)
                self.resultado14.place(x=55, y=540)

                self.resultado15 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado15.pack(padx=40, pady=40)
                self.resultado15.place(x=100, y=540)

                self.resultado16 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado16.pack(padx=40, pady=40)
                self.resultado16.place(x=145, y=540)
            elif tamanio_fila == 3:
                self.resultadol.pack(padx=40, pady=40)
                self.resultadol.place(x=55, y=375)

                self.resultado1 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado1.pack(padx=40, pady=40)
                self.resultado1.place(x=10, y=405)

                self.resultado2 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado2.pack(padx=40, pady=40)
                self.resultado2.place(x=55, y=405)

                self.resultado3 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado3.pack(padx=40, pady=40)
                self.resultado3.place(x=100, y=405)

                self.resultado4 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado4.pack(padx=40, pady=40)
                self.resultado4.place(x=10, y=450)

                self.resultado5 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado5.pack(padx=40, pady=40)
                self.resultado5.place(x=55, y=450)

                self.resultado6 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado6.pack(padx=40, pady=40)
                self.resultado6.place(x=100, y=450)

                self.resultado7 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado7.pack(padx=40, pady=40)
                self.resultado7.place(x=10, y=495)

                self.resultado8 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado8.pack(padx=40, pady=40)
                self.resultado8.place(x=55, y=495)

                self.resultado9 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado9.pack(padx=40, pady=40)
                self.resultado9.place(x=100, y=495)
            elif tamanio_fila == 2:
                self.resultadol.pack(padx=40, pady=40)
                self.resultadol.place(x=55, y=375)

                self.resultado1 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado1.pack(padx=40, pady=40)
                self.resultado1.place(x=10, y=405)

                self.resultado2 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado2.pack(padx=40, pady=40)
                self.resultado2.place(x=55, y=405)

                self.resultado3 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado3.pack(padx=40, pady=40)
                self.resultado3.place(x=10, y=450)

                self.resultado4 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                self.resultado4.pack(padx=40, pady=40)
                self.resultado4.place(x=55, y=450)
        else:
            if tamanio_fila == 2:
                if tamanio_columna == 3:
                    self.resultadol.pack(padx=40, pady=40)
                    self.resultadol.place(x=55, y=375)

                    self.resultado1 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado1.pack(padx=40, pady=40)
                    self.resultado1.place(x=10, y=405)

                    self.resultado2 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado2.pack(padx=40, pady=40)
                    self.resultado2.place(x=55, y=405)

                    self.resultado3 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado3.pack(padx=40, pady=40)
                    self.resultado3.place(x=100, y=405)

                    self.resultado4 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado4.pack(padx=40, pady=40)
                    self.resultado4.place(x=10, y=450)

                    self.resultado5 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado5.pack(padx=40, pady=40)
                    self.resultado5.place(x=55, y=450)

                    self.resultado6 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado6.pack(padx=40, pady=40)
                    self.resultado6.place(x=100, y=450)
                elif tamanio_columna == 4:
                    self.resultadol.pack(padx=40, pady=40)
                    self.resultadol.place(x=55, y=375)

                    self.resultado1 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado1.pack(padx=40, pady=40)
                    self.resultado1.place(x=10, y=405)

                    self.resultado2 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado2.pack(padx=40, pady=40)
                    self.resultado2.place(x=55, y=405)

                    self.resultado3 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado3.pack(padx=40, pady=40)
                    self.resultado3.place(x=100, y=405)

                    self.resultado4 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado4.pack(padx=40, pady=40)
                    self.resultado4.place(x=145, y=405)

                    self.resultado5 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado5.pack(padx=40, pady=40)
                    self.resultado5.place(x=10, y=450)

                    self.resultado6 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado6.pack(padx=40, pady=40)
                    self.resultado6.place(x=55, y=450)

                    self.resultado7 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado7.pack(padx=40, pady=40)
                    self.resultado7.place(x=100, y=450)

                    self.resultado8 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado8.pack(padx=40, pady=40)
                    self.resultado8.place(x=145, y=450)
            elif tamanio_fila == 3:
                if tamanio_columna == 2:
                    self.resultadol.pack(padx=40, pady=40)
                    self.resultadol.place(x=55, y=375)

                    self.resultado1 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado1.pack(padx=40, pady=40)
                    self.resultado1.place(x=10, y=405)

                    self.resultado2 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado2.pack(padx=40, pady=40)
                    self.resultado2.place(x=55, y=405)

                    self.resultado3 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado3.pack(padx=40, pady=40)
                    self.resultado3.place(x=10, y=450)

                    self.resultado4 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado4.pack(padx=40, pady=40)
                    self.resultado4.place(x=55, y=450)

                    self.resultado5 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado5.pack(padx=40, pady=40)
                    self.resultado5.place(x=10, y=495)

                    self.resultado6 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado6.pack(padx=40, pady=40)
                    self.resultado6.place(x=55, y=495)
                elif tamanio_columna == 4:
                    self.resultadol.pack(padx=40, pady=40)
                    self.resultadol.place(x=55, y=375)

                    self.resultado1 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado1.pack(padx=40, pady=40)
                    self.resultado1.place(x=10, y=405)

                    self.resultado2 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado2.pack(padx=40, pady=40)
                    self.resultado2.place(x=55, y=405)

                    self.resultado3 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado3.pack(padx=40, pady=40)
                    self.resultado3.place(x=100, y=405)

                    self.resultado4 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado4.pack(padx=40, pady=40)
                    self.resultado4.place(x=145, y=405)

                    self.resultado5 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado5.pack(padx=40, pady=40)
                    self.resultado5.place(x=10, y=450)

                    self.resultado6 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado6.pack(padx=40, pady=40)
                    self.resultado6.place(x=55, y=450)

                    self.resultado7 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado7.pack(padx=40, pady=40)
                    self.resultado7.place(x=100, y=450)

                    self.resultado8 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado8.pack(padx=40, pady=40)
                    self.resultado8.place(x=145, y=450)

                    self.resultado9 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado9.pack(padx=40, pady=40)
                    self.resultado9.place(x=10, y=495)

                    self.resultado10 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado10.pack(padx=40, pady=40)
                    self.resultado10.place(x=55, y=495)

                    self.resultado11 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado11.pack(padx=40, pady=40)
                    self.resultado11.place(x=100, y=495)

                    self.resultado12 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado12.pack(padx=40, pady=40)
                    self.resultado12.place(x=145, y=495)
            elif tamanio_fila == 4:
                if tamanio_columna == 2:
                    self.resultadol.pack(padx=40, pady=40)
                    self.resultadol.place(x=55, y=375)

                    self.resultado1 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado1.pack(padx=40, pady=40)
                    self.resultado1.place(x=10, y=405)

                    self.resultado2 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado2.pack(padx=40, pady=40)
                    self.resultado2.place(x=55, y=405)

                    self.resultado3 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado3.pack(padx=40, pady=40)
                    self.resultado3.place(x=10, y=450)

                    self.resultado4 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado4.pack(padx=40, pady=40)
                    self.resultado4.place(x=55, y=450)

                    self.resultado5 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado5.pack(padx=40, pady=40)
                    self.resultado5.place(x=10, y=495)

                    self.resultado6 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado6.pack(padx=40, pady=40)
                    self.resultado6.place(x=55, y=495)

                    self.resultado7 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado7.pack(padx=40, pady=40)
                    self.resultado7.place(x=10, y=540)

                    self.resultado8 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado8.pack(padx=40, pady=40)
                    self.resultado8.place(x=55, y=540)
                elif tamanio_columna == 3:
                    self.resultadol.pack(padx=40, pady=40)
                    self.resultadol.place(x=55, y=375)

                    self.resultado1 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado1.pack(padx=40, pady=40)
                    self.resultado1.place(x=10, y=405)

                    self.resultado2 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado2.pack(padx=40, pady=40)
                    self.resultado2.place(x=55, y=405)

                    self.resultado3 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado3.pack(padx=40, pady=40)
                    self.resultado3.place(x=100, y=405)

                    self.resultado4 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado4.pack(padx=40, pady=40)
                    self.resultado4.place(x=10, y=450)

                    self.resultado5 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado5.pack(padx=40, pady=40)
                    self.resultado5.place(x=55, y=450)

                    self.resultado6 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado6.pack(padx=40, pady=40)
                    self.resultado6.place(x=100, y=450)

                    self.resultado7 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado7.pack(padx=40, pady=40)
                    self.resultado7.place(x=10, y=495)

                    self.resultado8 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado8.pack(padx=40, pady=40)
                    self.resultado8.place(x=55, y=495)

                    self.resultado9 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado9.pack(padx=40, pady=40)
                    self.resultado9.place(x=100, y=495)

                    self.resultado10 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado10.pack(padx=40, pady=40)
                    self.resultado10.place(x=10, y=540)

                    self.resultado11 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado11.pack(padx=40, pady=40)
                    self.resultado11.place(x=55, y=540)

                    self.resultado12 = customtkinter.CTkEntry(master=self.frame, width=40, height=40)
                    self.resultado12.pack(padx=40, pady=40)
                    self.resultado12.place(x=100, y=540)

    def sumar_matriz(self):  # Parte logica de la suma
        self.generar_resultado(int(self.tamanio_filas_input.get()), int(self.tamanio_columnas_input.get()))
        text = 'PROCEDIMIENTO\n'
        if int(self.tamanio_columnas_input.get()) == int(self.tamanio_filas_input.get()):
            if int(self.tamanio_filas_input.get()) == 4:
                resultado1 = int(self.matrizA_1_input.get()) + int(self.matrizB_1_input.get())
                resultado2 = int(self.matrizA_2_input.get()) + int(self.matrizB_2_input.get())
                resultado3 = int(self.matrizA_3_input.get()) + int(self.matrizB_3_input.get())
                resultado4 = int(self.matrizA_4_input.get()) + int(self.matrizB_4_input.get())
                resultado5 = int(self.matrizA_5_input.get()) + int(self.matrizB_5_input.get())
                resultado6 = int(self.matrizA_6_input.get()) + int(self.matrizB_6_input.get())
                resultado7 = int(self.matrizA_7_input.get()) + int(self.matrizB_7_input.get())
                resultado8 = int(self.matrizA_8_input.get()) + int(self.matrizB_8_input.get())
                resultado9 = int(self.matrizA_9_input.get()) + int(self.matrizB_9_input.get())
                resultado10 = int(self.matrizA_10_input.get()) + int(self.matrizB_10_input.get())
                resultado11 = int(self.matrizA_11_input.get()) + int(self.matrizB_11_input.get())
                resultado12 = int(self.matrizA_12_input.get()) + int(self.matrizB_12_input.get())
                resultado13 = int(self.matrizA_13_input.get()) + int(self.matrizB_13_input.get())
                resultado14 = int(self.matrizA_14_input.get()) + int(self.matrizB_14_input.get())
                resultado15 = int(self.matrizA_15_input.get()) + int(self.matrizB_15_input.get())
                resultado16 = int(self.matrizA_16_input.get()) + int(self.matrizB_16_input.get())

                text += f'{self.matrizA_1_input.get()} + {self.matrizB_1_input.get()} = {resultado1} \n'
                text += f'{self.matrizA_2_input.get()} + {self.matrizB_2_input.get()} = {resultado2} \n'
                text += f'{self.matrizA_3_input.get()} + {self.matrizB_3_input.get()} = {resultado3} \n'
                text += f'{self.matrizA_4_input.get()} + {self.matrizB_4_input.get()} = {resultado4} \n'
                text += f'{self.matrizA_5_input.get()} + {self.matrizB_5_input.get()} = {resultado5} \n'
                text += f'{self.matrizA_6_input.get()} + {self.matrizB_6_input.get()} = {resultado6} \n'
                text += f'{self.matrizA_7_input.get()} + {self.matrizB_7_input.get()} = {resultado7} \n'
                text += f'{self.matrizA_8_input.get()} + {self.matrizB_8_input.get()} = {resultado8} \n'
                text += f'{self.matrizA_9_input.get()} + {self.matrizB_9_input.get()} = {resultado9} \n'
                text += f'{self.matrizA_10_input.get()} + {self.matrizB_10_input.get()} = {resultado10} \n'
                text += f'{self.matrizA_11_input.get()} + {self.matrizB_11_input.get()} = {resultado11} \n'
                text += f'{self.matrizA_12_input.get()} + {self.matrizB_12_input.get()} = {resultado12} \n'
                text += f'{self.matrizA_13_input.get()} + {self.matrizB_13_input.get()} = {resultado13} \n'
                text += f'{self.matrizA_14_input.get()} + {self.matrizB_14_input.get()} = {resultado14} \n'
                text += f'{self.matrizA_15_input.get()} + {self.matrizB_15_input.get()} = {resultado15} \n'
                text += f'{self.matrizA_16_input.get()} + {self.matrizB_16_input.get()} = {resultado16} \n'

                self.label_proc.configure(text=text)

                self.resultado1.configure(placeholder_text=str(resultado1))
                self.resultado2.configure(placeholder_text=str(resultado2))
                self.resultado3.configure(placeholder_text=str(resultado3))
                self.resultado4.configure(placeholder_text=str(resultado4))
                self.resultado5.configure(placeholder_text=str(resultado5))
                self.resultado6.configure(placeholder_text=str(resultado6))
                self.resultado7.configure(placeholder_text=str(resultado7))
                self.resultado8.configure(placeholder_text=str(resultado8))
                self.resultado9.configure(placeholder_text=str(resultado9))
                self.resultado10.configure(placeholder_text=str(resultado10))
                self.resultado11.configure(placeholder_text=str(resultado11))
                self.resultado12.configure(placeholder_text=str(resultado12))
                self.resultado13.configure(placeholder_text=str(resultado13))
                self.resultado14.configure(placeholder_text=str(resultado14))
                self.resultado15.configure(placeholder_text=str(resultado15))
                self.resultado16.configure(placeholder_text=str(resultado16))
            elif int(self.tamanio_filas_input.get()) == 3:
                resultado1 = int(self.matrizA_1_input.get()) + int(self.matrizB_1_input.get())
                resultado2 = int(self.matrizA_2_input.get()) + int(self.matrizB_2_input.get())
                resultado3 = int(self.matrizA_3_input.get()) + int(self.matrizB_3_input.get())
                resultado4 = int(self.matrizA_4_input.get()) + int(self.matrizB_4_input.get())
                resultado5 = int(self.matrizA_5_input.get()) + int(self.matrizB_5_input.get())
                resultado6 = int(self.matrizA_6_input.get()) + int(self.matrizB_6_input.get())
                resultado7 = int(self.matrizA_7_input.get()) + int(self.matrizB_7_input.get())
                resultado8 = int(self.matrizA_8_input.get()) + int(self.matrizB_8_input.get())
                resultado9 = int(self.matrizA_9_input.get()) + int(self.matrizB_9_input.get())

                text += f'{self.matrizA_1_input.get()} + {self.matrizB_1_input.get()} = {resultado1} \n'
                text += f'{self.matrizA_2_input.get()} + {self.matrizB_2_input.get()} = {resultado2} \n'
                text += f'{self.matrizA_3_input.get()} + {self.matrizB_3_input.get()} = {resultado3} \n'
                text += f'{self.matrizA_4_input.get()} + {self.matrizB_4_input.get()} = {resultado4} \n'
                text += f'{self.matrizA_5_input.get()} + {self.matrizB_5_input.get()} = {resultado5} \n'
                text += f'{self.matrizA_6_input.get()} + {self.matrizB_6_input.get()} = {resultado6} \n'
                text += f'{self.matrizA_7_input.get()} + {self.matrizB_7_input.get()} = {resultado7} \n'
                text += f'{self.matrizA_8_input.get()} + {self.matrizB_8_input.get()} = {resultado8} \n'
                text += f'{self.matrizA_9_input.get()} + {self.matrizB_9_input.get()} = {resultado9} \n'

                self.label_proc.configure(text=text)

                self.resultado1.configure(placeholder_text=str(resultado1))
                self.resultado2.configure(placeholder_text=str(resultado2))
                self.resultado3.configure(placeholder_text=str(resultado3))
                self.resultado4.configure(placeholder_text=str(resultado4))
                self.resultado5.configure(placeholder_text=str(resultado5))
                self.resultado6.configure(placeholder_text=str(resultado6))
                self.resultado7.configure(placeholder_text=str(resultado7))
                self.resultado8.configure(placeholder_text=str(resultado8))
                self.resultado9.configure(placeholder_text=str(resultado9))
            elif int(self.tamanio_filas_input.get()) == 2:
                resultado1 = int(self.matrizA_1_input.get()) + int(self.matrizB_1_input.get())
                resultado2 = int(self.matrizA_2_input.get()) + int(self.matrizB_2_input.get())
                resultado3 = int(self.matrizA_3_input.get()) + int(self.matrizB_3_input.get())
                resultado4 = int(self.matrizA_4_input.get()) + int(self.matrizB_4_input.get())

                text += f'{self.matrizA_1_input.get()} + {self.matrizB_1_input.get()} = {resultado1} \n'
                text += f'{self.matrizA_2_input.get()} + {self.matrizB_2_input.get()} = {resultado2} \n'
                text += f'{self.matrizA_3_input.get()} + {self.matrizB_3_input.get()} = {resultado3} \n'
                text += f'{self.matrizA_4_input.get()} + {self.matrizB_4_input.get()} = {resultado4} \n'

                self.label_proc.configure(text=text)

                self.resultado1.configure(placeholder_text=str(resultado1))
                self.resultado2.configure(placeholder_text=str(resultado2))
                self.resultado3.configure(placeholder_text=str(resultado3))
                self.resultado4.configure(placeholder_text=str(resultado4))
        else:
            if int(self.tamanio_filas_input.get()) == 2:
                if int(self.tamanio_columnas_input.get()) == 3:
                    resultado1 = int(self.matrizA_1_input.get()) + int(self.matrizB_1_input.get())
                    resultado2 = int(self.matrizA_2_input.get()) + int(self.matrizB_2_input.get())
                    resultado3 = int(self.matrizA_3_input.get()) + int(self.matrizB_3_input.get())
                    resultado4 = int(self.matrizA_4_input.get()) + int(self.matrizB_4_input.get())
                    resultado5 = int(self.matrizA_5_input.get()) + int(self.matrizB_5_input.get())
                    resultado6 = int(self.matrizA_6_input.get()) + int(self.matrizB_6_input.get())

                    text += f'{self.matrizA_1_input.get()} + {self.matrizB_1_input.get()} = {resultado1} \n'
                    text += f'{self.matrizA_2_input.get()} + {self.matrizB_2_input.get()} = {resultado2} \n'
                    text += f'{self.matrizA_3_input.get()} + {self.matrizB_3_input.get()} = {resultado3} \n'
                    text += f'{self.matrizA_4_input.get()} + {self.matrizB_4_input.get()} = {resultado4} \n'
                    text += f'{self.matrizA_5_input.get()} + {self.matrizB_5_input.get()} = {resultado5} \n'
                    text += f'{self.matrizA_6_input.get()} + {self.matrizB_6_input.get()} = {resultado6} \n'

                    self.label_proc.configure(text=text)

                    self.resultado1.configure(placeholder_text=str(resultado1))
                    self.resultado2.configure(placeholder_text=str(resultado2))
                    self.resultado3.configure(placeholder_text=str(resultado3))
                    self.resultado4.configure(placeholder_text=str(resultado4))
                    self.resultado5.configure(placeholder_text=str(resultado5))
                    self.resultado6.configure(placeholder_text=str(resultado6))
                elif int(self.tamanio_columnas_input.get()) == 4:
                    resultado1 = int(self.matrizA_1_input.get()) + int(self.matrizB_1_input.get())
                    resultado2 = int(self.matrizA_2_input.get()) + int(self.matrizB_2_input.get())
                    resultado3 = int(self.matrizA_3_input.get()) + int(self.matrizB_3_input.get())
                    resultado4 = int(self.matrizA_4_input.get()) + int(self.matrizB_4_input.get())
                    resultado5 = int(self.matrizA_5_input.get()) + int(self.matrizB_5_input.get())
                    resultado6 = int(self.matrizA_6_input.get()) + int(self.matrizB_6_input.get())
                    resultado7 = int(self.matrizA_7_input.get()) + int(self.matrizB_7_input.get())
                    resultado8 = int(self.matrizA_8_input.get()) + int(self.matrizB_8_input.get())

                    text += f'{self.matrizA_1_input.get()} + {self.matrizB_1_input.get()} = {resultado1} \n'
                    text += f'{self.matrizA_2_input.get()} + {self.matrizB_2_input.get()} = {resultado2} \n'
                    text += f'{self.matrizA_3_input.get()} + {self.matrizB_3_input.get()} = {resultado3} \n'
                    text += f'{self.matrizA_4_input.get()} + {self.matrizB_4_input.get()} = {resultado4} \n'
                    text += f'{self.matrizA_5_input.get()} + {self.matrizB_5_input.get()} = {resultado5} \n'
                    text += f'{self.matrizA_6_input.get()} + {self.matrizB_6_input.get()} = {resultado6} \n'
                    text += f'{self.matrizA_7_input.get()} + {self.matrizB_7_input.get()} = {resultado7} \n'
                    text += f'{self.matrizA_8_input.get()} + {self.matrizB_8_input.get()} = {resultado8} \n'

                    self.label_proc.configure(text=text)

                    self.resultado1.configure(placeholder_text=str(resultado1))
                    self.resultado2.configure(placeholder_text=str(resultado2))
                    self.resultado3.configure(placeholder_text=str(resultado3))
                    self.resultado4.configure(placeholder_text=str(resultado4))
                    self.resultado5.configure(placeholder_text=str(resultado5))
                    self.resultado6.configure(placeholder_text=str(resultado6))
                    self.resultado7.configure(placeholder_text=str(resultado7))
                    self.resultado8.configure(placeholder_text=str(resultado8))
            elif int(self.tamanio_filas_input.get()) == 3:
                if int(self.tamanio_columnas_input.get()) == 2:
                    resultado1 = int(self.matrizA_1_input.get()) + int(self.matrizB_1_input.get())
                    resultado2 = int(self.matrizA_2_input.get()) + int(self.matrizB_2_input.get())
                    resultado3 = int(self.matrizA_3_input.get()) + int(self.matrizB_3_input.get())
                    resultado4 = int(self.matrizA_4_input.get()) + int(self.matrizB_4_input.get())
                    resultado5 = int(self.matrizA_5_input.get()) + int(self.matrizB_5_input.get())
                    resultado6 = int(self.matrizA_6_input.get()) + int(self.matrizB_6_input.get())

                    text += f'{self.matrizA_1_input.get()} + {self.matrizB_1_input.get()} = {resultado1} \n'
                    text += f'{self.matrizA_2_input.get()} + {self.matrizB_2_input.get()} = {resultado2} \n'
                    text += f'{self.matrizA_3_input.get()} + {self.matrizB_3_input.get()} = {resultado3} \n'
                    text += f'{self.matrizA_4_input.get()} + {self.matrizB_4_input.get()} = {resultado4} \n'
                    text += f'{self.matrizA_5_input.get()} + {self.matrizB_5_input.get()} = {resultado5} \n'
                    text += f'{self.matrizA_6_input.get()} + {self.matrizB_6_input.get()} = {resultado6} \n'

                    self.label_proc.configure(text=text)

                    self.resultado1.configure(placeholder_text=str(resultado1))
                    self.resultado2.configure(placeholder_text=str(resultado2))
                    self.resultado3.configure(placeholder_text=str(resultado3))
                    self.resultado4.configure(placeholder_text=str(resultado4))
                    self.resultado5.configure(placeholder_text=str(resultado5))
                    self.resultado6.configure(placeholder_text=str(resultado6))
                elif int(self.tamanio_columnas_input.get()) == 4:
                    resultado1 = int(self.matrizA_1_input.get()) + int(self.matrizB_1_input.get())
                    resultado2 = int(self.matrizA_2_input.get()) + int(self.matrizB_2_input.get())
                    resultado3 = int(self.matrizA_3_input.get()) + int(self.matrizB_3_input.get())
                    resultado4 = int(self.matrizA_4_input.get()) + int(self.matrizB_4_input.get())
                    resultado5 = int(self.matrizA_5_input.get()) + int(self.matrizB_5_input.get())
                    resultado6 = int(self.matrizA_6_input.get()) + int(self.matrizB_6_input.get())
                    resultado7 = int(self.matrizA_7_input.get()) + int(self.matrizB_7_input.get())
                    resultado8 = int(self.matrizA_8_input.get()) + int(self.matrizB_8_input.get())
                    resultado9 = int(self.matrizA_9_input.get()) + int(self.matrizB_9_input.get())
                    resultado10 = int(self.matrizA_10_input.get()) + int(self.matrizB_10_input.get())
                    resultado11 = int(self.matrizA_11_input.get()) + int(self.matrizB_11_input.get())
                    resultado12 = int(self.matrizA_12_input.get()) + int(self.matrizB_12_input.get())

                    text += f'{self.matrizA_1_input.get()} + {self.matrizB_1_input.get()} = {resultado1} \n'
                    text += f'{self.matrizA_2_input.get()} + {self.matrizB_2_input.get()} = {resultado2} \n'
                    text += f'{self.matrizA_3_input.get()} + {self.matrizB_3_input.get()} = {resultado3} \n'
                    text += f'{self.matrizA_4_input.get()} + {self.matrizB_4_input.get()} = {resultado4} \n'
                    text += f'{self.matrizA_5_input.get()} + {self.matrizB_5_input.get()} = {resultado5} \n'
                    text += f'{self.matrizA_6_input.get()} + {self.matrizB_6_input.get()} = {resultado6} \n'
                    text += f'{self.matrizA_7_input.get()} + {self.matrizB_7_input.get()} = {resultado7} \n'
                    text += f'{self.matrizA_8_input.get()} + {self.matrizB_8_input.get()} = {resultado8} \n'
                    text += f'{self.matrizA_9_input.get()} + {self.matrizB_9_input.get()} = {resultado9} \n'
                    text += f'{self.matrizA_10_input.get()} + {self.matrizB_10_input.get()} = {resultado10} \n'
                    text += f'{self.matrizA_11_input.get()} + {self.matrizB_11_input.get()} = {resultado11} \n'
                    text += f'{self.matrizA_12_input.get()} + {self.matrizB_12_input.get()} = {resultado12} \n'

                    self.label_proc.configure(text=text)

                    self.resultado1.configure(placeholder_text=str(resultado1))
                    self.resultado2.configure(placeholder_text=str(resultado2))
                    self.resultado3.configure(placeholder_text=str(resultado3))
                    self.resultado4.configure(placeholder_text=str(resultado4))
                    self.resultado5.configure(placeholder_text=str(resultado5))
                    self.resultado6.configure(placeholder_text=str(resultado6))
                    self.resultado7.configure(placeholder_text=str(resultado7))
                    self.resultado8.configure(placeholder_text=str(resultado8))
                    self.resultado9.configure(placeholder_text=str(resultado9))
                    self.resultado10.configure(placeholder_text=str(resultado10))
                    self.resultado11.configure(placeholder_text=str(resultado11))
                    self.resultado12.configure(placeholder_text=str(resultado12))
            elif int(self.tamanio_filas_input.get()) == 4:
                if int(self.tamanio_columnas_input.get()) == 2:
                    resultado1 = int(self.matrizA_1_input.get()) + int(self.matrizB_1_input.get())
                    resultado2 = int(self.matrizA_2_input.get()) + int(self.matrizB_2_input.get())
                    resultado3 = int(self.matrizA_3_input.get()) + int(self.matrizB_3_input.get())
                    resultado4 = int(self.matrizA_4_input.get()) + int(self.matrizB_4_input.get())
                    resultado5 = int(self.matrizA_5_input.get()) + int(self.matrizB_5_input.get())
                    resultado6 = int(self.matrizA_6_input.get()) + int(self.matrizB_6_input.get())
                    resultado7 = int(self.matrizA_7_input.get()) + int(self.matrizB_7_input.get())
                    resultado8 = int(self.matrizA_8_input.get()) + int(self.matrizB_8_input.get())

                    text += f'{self.matrizA_1_input.get()} + {self.matrizB_1_input.get()} = {resultado1} \n'
                    text += f'{self.matrizA_2_input.get()} + {self.matrizB_2_input.get()} = {resultado2} \n'
                    text += f'{self.matrizA_3_input.get()} + {self.matrizB_3_input.get()} = {resultado3} \n'
                    text += f'{self.matrizA_4_input.get()} + {self.matrizB_4_input.get()} = {resultado4} \n'
                    text += f'{self.matrizA_5_input.get()} + {self.matrizB_5_input.get()} = {resultado5} \n'
                    text += f'{self.matrizA_6_input.get()} + {self.matrizB_6_input.get()} = {resultado6} \n'
                    text += f'{self.matrizA_7_input.get()} + {self.matrizB_7_input.get()} = {resultado7} \n'
                    text += f'{self.matrizA_8_input.get()} + {self.matrizB_8_input.get()} = {resultado8} \n'

                    self.label_proc.configure(text=text)

                    self.resultado1.configure(placeholder_text=str(resultado1))
                    self.resultado2.configure(placeholder_text=str(resultado2))
                    self.resultado3.configure(placeholder_text=str(resultado3))
                    self.resultado4.configure(placeholder_text=str(resultado4))
                    self.resultado5.configure(placeholder_text=str(resultado5))
                    self.resultado6.configure(placeholder_text=str(resultado6))
                    self.resultado7.configure(placeholder_text=str(resultado7))
                    self.resultado8.configure(placeholder_text=str(resultado8))
                elif int(self.tamanio_columnas_input.get()) == 3:
                    resultado1 = int(self.matrizA_1_input.get()) + int(self.matrizB_1_input.get())
                    resultado2 = int(self.matrizA_2_input.get()) + int(self.matrizB_2_input.get())
                    resultado3 = int(self.matrizA_3_input.get()) + int(self.matrizB_3_input.get())
                    resultado4 = int(self.matrizA_4_input.get()) + int(self.matrizB_4_input.get())
                    resultado5 = int(self.matrizA_5_input.get()) + int(self.matrizB_5_input.get())
                    resultado6 = int(self.matrizA_6_input.get()) + int(self.matrizB_6_input.get())
                    resultado7 = int(self.matrizA_7_input.get()) + int(self.matrizB_7_input.get())
                    resultado8 = int(self.matrizA_8_input.get()) + int(self.matrizB_8_input.get())
                    resultado9 = int(self.matrizA_9_input.get()) + int(self.matrizB_9_input.get())
                    resultado10 = int(self.matrizA_10_input.get()) + int(self.matrizB_10_input.get())
                    resultado11 = int(self.matrizA_11_input.get()) + int(self.matrizB_11_input.get())
                    resultado12 = int(self.matrizA_12_input.get()) + int(self.matrizB_12_input.get())

                    text += f'{self.matrizA_1_input.get()} + {self.matrizB_1_input.get()} = {resultado1} \n'
                    text += f'{self.matrizA_2_input.get()} + {self.matrizB_2_input.get()} = {resultado2} \n'
                    text += f'{self.matrizA_3_input.get()} + {self.matrizB_3_input.get()} = {resultado3} \n'
                    text += f'{self.matrizA_4_input.get()} + {self.matrizB_4_input.get()} = {resultado4} \n'
                    text += f'{self.matrizA_5_input.get()} + {self.matrizB_5_input.get()} = {resultado5} \n'
                    text += f'{self.matrizA_6_input.get()} + {self.matrizB_6_input.get()} = {resultado6} \n'
                    text += f'{self.matrizA_7_input.get()} + {self.matrizB_7_input.get()} = {resultado7} \n'
                    text += f'{self.matrizA_8_input.get()} + {self.matrizB_8_input.get()} = {resultado8} \n'
                    text += f'{self.matrizA_9_input.get()} + {self.matrizB_9_input.get()} = {resultado9} \n'
                    text += f'{self.matrizA_10_input.get()} + {self.matrizB_10_input.get()} = {resultado10} \n'
                    text += f'{self.matrizA_11_input.get()} + {self.matrizB_11_input.get()} = {resultado11} \n'
                    text += f'{self.matrizA_12_input.get()} + {self.matrizB_12_input.get()} = {resultado12} \n'

                    self.label_proc.configure(text=text)

                    self.resultado1.configure(placeholder_text=str(resultado1))
                    self.resultado2.configure(placeholder_text=str(resultado2))
                    self.resultado3.configure(placeholder_text=str(resultado3))
                    self.resultado4.configure(placeholder_text=str(resultado4))
                    self.resultado5.configure(placeholder_text=str(resultado5))
                    self.resultado6.configure(placeholder_text=str(resultado6))
                    self.resultado7.configure(placeholder_text=str(resultado7))
                    self.resultado8.configure(placeholder_text=str(resultado8))
                    self.resultado9.configure(placeholder_text=str(resultado9))
                    self.resultado10.configure(placeholder_text=str(resultado10))
                    self.resultado11.configure(placeholder_text=str(resultado11))
                    self.resultado12.configure(placeholder_text=str(resultado12))
