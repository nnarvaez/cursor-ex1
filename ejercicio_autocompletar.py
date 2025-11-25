"""Genera listas con los cuadrados de los primeros números naturales."""


def cuadrados(n: int) -> list[int]:
    """Devuelve los cuadrados desde 1 hasta n inclusive."""
    return [i**2 for i in range(1, n + 1)]