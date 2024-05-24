import customtkinter
import cargar_datos_labels_frame


class WindowCifrar:
    def __init__(self):
        self.ventana = cargar_datos_labels_frame.cargar_datos()
        self.ventana.geometry("400x400")
        self.frame = cargar_datos_labels_frame.frame1(self.ventana)
        color = "#3E4446"

        self.label = customtkinter.CTkLabel(master=self.frame, text="Ingrese el mensaje a cifrar:")
        self.label.place(x=10, y=10)

        self.entry = customtkinter.CTkEntry(master=self.frame)
        self.entry.place(x=10, y=30)

        self.encrypt_button = customtkinter.CTkButton(master=self.frame, text="Cifrar Mensaje", command=self.encrypt_message)
        self.encrypt_button.place(x=10, y=60)

        self.result_label = customtkinter.CTkLabel(master=self.frame, text="")
        self.result_label.place(x=10, y=90)

    def encrypt_message(self):
        message = self.entry.get().lower()
        encrypted_message, steps = self.encrypt(message)
        self.result_label.configure(text=f"Pasos de cifrado:\n{steps}")

    def encrypt(self, message):
        key_matrix = [[-1, 1, 1],
                      [-2, -3, 1],
                      [3, 1, -2]]

        n = len(message) // 3 + (1 if len(message) % 3 != 0 else 0)
        message_matrix = [[0 for _ in range(3)] for _ in range(n)]
        steps = []

        for i, char in enumerate(message):
            if char == ' ':
                message_matrix[i // 3][i % 3] = 26
            else:
                message_matrix[i // 3][i % 3] = ord(char) - ord('a') + 1

        steps.append(f"Matriz del mensaje:\n{message_matrix}")

        transposed_message_matrix = [[message_matrix[j][i] for j in range(n)] for i in range(3)]
        steps.append(f"Matriz del mensaje transpuesta:\n{transposed_message_matrix}")

        result_matrix = [[0 for _ in range(3)] for _ in range(n)]
        for i in range(3):
            for j in range(n):
                for k in range(3):
                    result_matrix[j][i] += transposed_message_matrix[k][j] * key_matrix[k][i]

        steps.append(f"Matriz resultado de la multiplicación:\n{result_matrix}")

        encrypted_message = ''.join(
            [chr((result_matrix[j][i] - 1) % 26 + ord('a')) if (result_matrix[j][i] - 1) % 26 != 26 else ' ' for i in
             range(3) for j in range(n)])
        return encrypted_message, '\n\n'.join(steps)
