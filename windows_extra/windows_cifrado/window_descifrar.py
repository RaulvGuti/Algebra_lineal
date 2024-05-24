import customtkinter
import numpy as np

import cargar_datos_labels_frame


class WindowDescifrar:
    def __init__(self):
        self.ventana = cargar_datos_labels_frame.cargar_datos()
        self.ventana.geometry("400x400")
        self.frame = cargar_datos_labels_frame.frame1(self.ventana)
        color = "#3E4446"

        self.label = customtkinter.CTkLabel(master=self.frame,
                                            text="Ingrese el vector numérico cifrado (separado por comas):")
        self.label.place(x=10, y=10)

        self.entry = customtkinter.CTkEntry(master=self.frame)
        self.entry.place(x=10, y=30)

        self.decrypt_button = customtkinter.CTkButton(master=self.frame, text="Descifrar Mensaje",
                                                      command=self.decrypt_message)
        self.decrypt_button.place(x=10, y=60)

        self.result_label = customtkinter.CTkLabel(master=self.frame, text="")
        self.result_label.place(x=10, y=90)

    def decrypt_message(self):
        encrypted_vector = [int(x) for x in self.entry.get().split(",")]
        decrypted_message, steps = self.decrypt(encrypted_vector)
        self.result_label.configure(text=f"Pasos de descifrado:\n{steps}\nMensaje descifrado:\n{decrypted_message}")

    def decrypt(self, vector):
        clave = [[-1, 1, 1],
                 [-2, -3, 1],
                 [3, 1, -2]]
        clave_inversa = self.calcular_inversa(clave)

        n = len(vector) // 3
        matrix = [[0 for _ in range(3)] for _ in range(n)]

        for i, num in enumerate(vector):
            matrix[i // 3][i % 3] = num

        steps = []

        transposed_matrix = [[matrix[j][i] for j in range(n)] for i in range(3)]
        steps.append(f"Matriz transpuesta del vector:\n{transposed_matrix}")

        decrypted_matrix = [[0 for _ in range(3)] for _ in range(n)]
        for i in range(3):
            for j in range(n):
                for k in range(3):
                    decrypted_matrix[j][i] += int(transposed_matrix[k][j] * clave_inversa[k][i])

        steps.append(f"Matriz resultado de la multiplicación:\n{decrypted_matrix}")

        decrypted_message = ''.join(
            [chr(int(decrypted_matrix[i][j]) + ord('a') - 1) if int(decrypted_matrix[i][j]) != 27 else ' ' for i in
             range(n) for j in range(3)])
        return decrypted_message, '\n\n'.join(steps)

    def calcular_inversa(self, matriz):
        det = matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1]) - \
              matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0]) + \
              matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0])

        if det == 0:
            return None

        inv_det = 1 / det

        inv_matriz = [
            [(matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1]) * inv_det,
             (matriz[0][2] * matriz[2][1] - matriz[0][1] * matriz[2][2]) * inv_det,
             (matriz[0][1] * matriz[1][2] - matriz[0][2] * matriz[1][1]) * inv_det],
            [(matriz[1][2] * matriz[2][0] - matriz[1][0] * matriz[2][2]) * inv_det,
             (matriz[0][0] * matriz[2][2] - matriz[0][2] * matriz[2][0]) * inv_det,
             (matriz[0][2] * matriz[1][0] - matriz[0][0] * matriz[1][2]) * inv_det],
            [(matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0]) * inv_det,
             (matriz[0][1] * matriz[2][0] - matriz[0][0] * matriz[2][1]) * inv_det,
             (matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]) * inv_det]
        ]

        return inv_matriz
