import tkinter as tk
from tkinter import messagebox
from src.input_handler import text_to_matrix, matrix_to_text
from src.encryptor import encrypt
from src.utils.matrix_operations import mod_matrix_multiply
import numpy as np

def cipher_text():
    plaintext = entry.get()
    if not plaintext:
        messagebox.showerror("Error", "Please enter some text.")
        return

    # Example key matrix and modulo
    key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
    mod = 26

    try:
        plaintext_matrix = text_to_matrix(plaintext, key_matrix.shape[0])
        ciphertext_matrix = encrypt(plaintext_matrix, key_matrix, mod)
        ciphertext = matrix_to_text(ciphertext_matrix)
        messagebox.showinfo("Ciphered Text", f"Ciphered Text: {ciphertext}")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main window
root = tk.Tk()
root.title("Text Cipher")

# Create input field and button
label = tk.Label(root, text="Enter text to cipher:")
label.pack(pady=10)

entry = tk.Entry(root, width=40)
entry.pack(pady=10)

button = tk.Button(root, text="Cipher", command=cipher_text)
button.pack(pady=10)

# Run the application
root.mainloop()
