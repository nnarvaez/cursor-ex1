"""
Pruebas unitarias para la función cuadrados()
"""
import unittest
from ejercicio_autocompletar import cuadrados

class TestCuadrados(unittest.TestCase):
    """Clase de pruebas para la función cuadrados"""
    
    def test_cuadrados_5(self):
        """Prueba con n=5"""
        resultado = cuadrados(5)
        esperado = [1, 4, 9, 16, 25]
        self.assertEqual(resultado, esperado)
    
    def test_cuadrados_3(self):
        """Prueba con n=3"""
        resultado = cuadrados(3)
        esperado = [1, 4, 9]
        self.assertEqual(resultado, esperado)
    
    def test_cuadrados_0(self):
        """Prueba con n=0 (caso límite)"""
        resultado = cuadrados(0)
        esperado = []
        self.assertEqual(resultado, esperado)
    
    def test_cuadrados_1(self):
        """Prueba con n=1 (caso mínimo)"""
        resultado = cuadrados(1)
        esperado = [1]
        self.assertEqual(resultado, esperado)
    
    def test_cuadrados_10(self):
        """Prueba con n=10"""
        resultado = cuadrados(10)
        esperado = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertEqual(resultado, esperado)

if __name__ == '__main__':
    unittest.main()
