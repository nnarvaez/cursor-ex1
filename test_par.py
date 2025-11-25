"""Pruebas unitarias para la función `par`."""
import unittest
from par import par

class TestPar(unittest.TestCase):
    """Casos de prueba para la función `par`."""
    
    def test_par_5(self):
        """Verifica la salida cuando n es 5."""
        resultado = par(5)
        esperado = False
        self.assertEqual(resultado, esperado)   

    def test_par_4(self):
        """Verifica la salida cuando n es 4."""
        resultado = par(4)
        esperado = True
        self.assertEqual(resultado, esperado)

    def test_par_0(self):
        """Verifica la salida cuando n es 0."""
        resultado = par(0)
        esperado = True
        self.assertEqual(resultado, esperado)
        
    def test_par_menos_uno(self):
        """Verifica la salida cuando n es -1."""
        resultado = par(-1)
        esperado = False
        self.assertEqual(resultado, esperado)