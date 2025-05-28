import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
from src.input_handler import text_to_matrix, matrix_to_text
from src.encryptor import encrypt
from src.decryptor import decrypt

def strip_padding(text):
    """Removes padding 'X' characters from the end of the text."""
    return text.rstrip('X')

def main():
    # Input plaintext, key matrix, and modulo
    plaintext = input("Enter the plaintext: ")
    key_matrix = np.array([[6, 24, 1], [13, 16, 10], [20, 17, 15]])  # Example 3x3 key matrix
    mod = 26  # Modulo for encryption and decryption

    # Convert plaintext to matrix
    plaintext_matrix = text_to_matrix(plaintext, key_matrix.shape[0])

    # Encrypt the plaintext
    ciphertext_matrix = encrypt(plaintext_matrix, key_matrix, mod)
    ciphertext = matrix_to_text(ciphertext_matrix)
    print(f"Ciphertext: {ciphertext}")

    # Decrypt the ciphertext
    decrypted_matrix = decrypt(ciphertext_matrix, key_matrix, mod)
    decrypted_text = strip_padding(matrix_to_text(decrypted_matrix))
    print(f"Decrypted Text: {decrypted_text}")

if __name__ == "__main__":
    main()
