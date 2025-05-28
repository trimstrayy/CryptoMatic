# Placeholder for matrix_operations module

import numpy as np
from src.utils.modular_arithmetic import mod_inverse

def mod_matrix_multiply(matrix_a, matrix_b, mod):
    """Performs modular matrix multiplication."""
    return np.dot(matrix_a, matrix_b) % mod

def mod_matrix_inverse(matrix, mod):
    """Computes the modular inverse of a matrix."""
    det = int(round(np.linalg.det(matrix)))
    det_inv = mod_inverse(det, mod)
    adjugate = np.round(np.linalg.inv(matrix) * det).astype(int)
    return (det_inv * adjugate) % mod
