# Placeholder for modular_arithmetic module

def mod_inverse(a, mod):
    """Finds the modular inverse of a under modulo mod."""
    a = a % mod
    for x in range(1, mod):
        if (a * x) % mod == 1:
            return x
    raise ValueError(f"No modular inverse for {a} under modulo {mod}")
