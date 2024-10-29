# src/combinations.py

from itertools import combinations

def generar_combinaciones(elementos, r):
    """Genera combinaciones sin repetición."""
    return list(combinations(elementos, r))
