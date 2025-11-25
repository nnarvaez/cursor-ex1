"""Implementación sencilla del juego FizzBuzz."""


def ejecutar_fizzbuzz(inicio: int = 1, fin: int = 50) -> None:
    """Imprime la secuencia FizzBuzz en el rango dado."""
    for i in range(inicio, fin):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == "__main__":
    ejecutar_fizzbuzz()
