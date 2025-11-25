"""Pruebas unitarias para la función `cuadrados`."""
import unittest
from ejercicio_autocompletar import cuadrados

class TestCuadrados(unittest.TestCase):
    """Casos de prueba para la función `cuadrados`."""
    
    def test_cuadrados_5(self):
        """Verifica la salida cuando n es 5."""
        resultado = cuadrados(5)
        esperado = [1, 4, 9, 16, 25]
        self.assertEqual(resultado, esperado)
    
    def test_cuadrados_3(self):
        """Verifica la salida cuando n es 3."""
        resultado = cuadrados(3)
        esperado = [1, 4, 9]
        self.assertEqual(resultado, esperado)
    
    def test_cuadrados_0(self):
        """Verifica el caso límite cuando n es 0."""
        resultado = cuadrados(0)
        esperado = []
        self.assertEqual(resultado, esperado)
    
    def test_cuadrados_1(self):
        """Verifica el caso mínimo cuando n es 1."""
        resultado = cuadrados(1)
        esperado = [1]
        self.assertEqual(resultado, esperado)
    
    def test_cuadrados_10(self):
        """Verifica la salida cuando n es 10."""
        resultado = cuadrados(10)
        esperado = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertEqual(resultado, esperado)

if __name__ == '__main__':
    unittest.main()
