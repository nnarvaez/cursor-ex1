"""Utilidades para verificar si un número es par."""


def par(n: int) -> bool:
    """Retorna True si el número es par, False en caso contrario."""
    if n % 2 == 0:
        return True
    else:
        return False