import numpy as np
from src.utils.matrix_operations import mod_matrix_inverse, mod_matrix_multiply

def decrypt(ciphertext_matrix, key_matrix, mod):
    """Decrypts the ciphertext matrix using the inverse of the key matrix and modulo."""
    key_inverse = mod_matrix_inverse(key_matrix, mod)
    return mod_matrix_multiply(ciphertext_matrix, key_inverse, mod)
