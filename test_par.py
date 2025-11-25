"""
Pruebas unitarias para la función par()
"""
import unittest
from par import par

class TestPar(unittest.TestCase):
    """Clase de pruebas para la función par"""
    
    def test_par_5(self):
        """Prueba con n=5"""
        resultado = par(5)
        esperado = False
        self.assertEqual(resultado, esperado)   

    def test_par_4(self):
        """Prueba con n=4"""
        resultado = par(4)
        esperado = True
        self.assertEqual(resultado, esperado)

    def test_par_0(self):
        """Prueba con n=0"""
        resultado = par(0)
        esperado = True
        self.assertEqual(resultado, esperado)
        
    def test_par_menos_uno(self):
            """Prueba con n=-1"""
            resultado = par(-1)
            esperado = False
            self.assertEqual(resultado, esperado)