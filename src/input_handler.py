import numpy as np

def preprocess_text(text):
    """Converts text to uppercase and removes non-alphabetic characters."""
    return ''.join(filter(str.isalpha, text.upper()))

def text_to_matrix(text, size):
    """Converts text to a numeric matrix of given size."""
    text = preprocess_text(text)
    padded_text = text + 'X' * (size**2 - len(text) % (size**2))
    matrix = [ord(char) - ord('A') for char in padded_text]
    return np.array(matrix).reshape(-1, size)

def matrix_to_text(matrix):
    """Converts a numeric matrix back to text."""
    return ''.join(chr(int(num) + ord('A')) for num in matrix.flatten())
