# Placeholder for encryptor module
import numpy as np
from src.utils.matrix_operations import mod_matrix_multiply

def encrypt(plaintext_matrix, key_matrix, mod):
    """Encrypts the plaintext matrix using the key matrix and modulo."""
    return mod_matrix_multiply(plaintext_matrix, key_matrix, mod)
