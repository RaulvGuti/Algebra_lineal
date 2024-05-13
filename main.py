import customtkinter
from window_op_matriz import WindowMatriz
from window_inversa import WindowInversa
from window_determinante import WindowDeterminante
from window_rango import WindowRango
from window_cifrado import WindowCifrado
from window_markov import WindowMarkov
from window_vectores import WindowVectores

app = customtkinter.CTk()


def window_matriz():
    ventana = WindowMatriz()


def window_inversa():
    ventana = WindowInversa()


def window_determinante():
    ventana = WindowDeterminante()


def window_rango():
    ventana = WindowRango()


def window_cifrado():
    ventana = WindowCifrado()


def window_markov():
    ventana = WindowMarkov()


def window_vectores():
    ventana = WindowVectores()


def main_window():
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    app.title("MENU")
    app.geometry("980x460")
    app.wm_attributes("-topmost", False)
    frame = customtkinter.CTkFrame(master=app)
    frame.pack(pady=10, padx=10, fill='both', expand=True)
    buttons(frame)

    # botones
    app.mainloop()


def buttons(frame):
    button_operaciones = customtkinter.CTkButton(master=frame, text='Operaciones con Matrices', height=100, width=250,
                                          font=("Arial", 20), fg_color="#3E4446", command=window_matriz)

    button_operaciones.pack(pady=10, padx=10)
    button_operaciones.place(x=50, y=10)

    button_inversa = customtkinter.CTkButton(master=frame, text='Matriz Inversa', height=100, width=250,
                                          font=("Arial", 20), fg_color="#3E4446", command=window_inversa)

    button_inversa.pack(pady=10, padx=10)
    button_inversa.place(x=50, y=150)

    button_determinante = customtkinter.CTkButton(master=frame, text='Determinante', height=100, width=250,
                                                  font=("Arial", 20), fg_color="#3E4446", command=window_determinante)

    button_determinante.pack(pady=10, padx=10)
    button_determinante.place(x=50, y=290)

    button_rango = customtkinter.CTkButton(master=frame, text='Rango', height=100, width=250,
                                                    font=("Arial", 20), fg_color="#3E4446", command=window_rango)

    button_rango.pack(pady=10, padx=10)
    button_rango.place(x=400, y=10)

    button_cifrado = customtkinter.CTkButton(master=frame, text='Cifrado', height=100, width=250,
                                           font=("Arial", 20), fg_color="#3E4446", command=window_cifrado)

    button_cifrado.pack(pady=10, padx=10)
    button_cifrado.place(x=400, y=150)

    button_markov = customtkinter.CTkButton(master=frame, text='Markov', height=100, width=250,
                                             font=("Arial", 20), fg_color="#3E4446", command=window_markov)

    button_markov.pack(pady=10, padx=10)
    button_markov.place(x=400, y=290)

    button_vectores = customtkinter.CTkButton(master=frame, text='Vectores', height=100, width=250,
                                           font=("Arial", 20), fg_color="#3E4446", command=window_vectores)

    button_vectores.pack(pady=10, padx=10)
    button_vectores.place(x=700, y=10)


main_window()
