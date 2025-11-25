"""Suite de pruebas para los componentes del contador de palabras."""

import unittest
import tempfile
import os
from unittest.mock import Mock, patch
from contador import (
    LectorArchivoLocal,
    ExtractorPalabrasRegex,
    PresentadorConsola,
    ContadorDePalabras,
    OrquestadorProcesamiento
)


class TestLectorArchivoLocal(unittest.TestCase):
    """Tests para LectorArchivoLocal."""
    
    def test_leer_archivo_existente(self):
        """Test leer un archivo que existe."""
        # Crear archivo temporal
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("Hola mundo")
            archivo_path = f.name
        
        try:
            lector = LectorArchivoLocal()
            resultado = lector.leer(archivo_path)
            
            self.assertEqual(resultado, "Hola mundo")
        finally:
            # Limpiar archivo temporal
            os.unlink(archivo_path)
    
    def test_leer_archivo_no_existe(self):
        """Test leer un archivo que no existe."""
        lector = LectorArchivoLocal()
        resultado = lector.leer("archivo_inexistente.txt")
        
        self.assertIsNone(resultado)
    
    @patch('builtins.print')
    def test_leer_archivo_no_existe_mensaje(self, mock_print):
        """Test que se muestre mensaje de error."""
        lector = LectorArchivoLocal()
        lector.leer("archivo_inexistente.txt")
        
        mock_print.assert_called_with("El archivo no existe")


class TestExtractorPalabrasRegex(unittest.TestCase):
    """Tests para ExtractorPalabrasRegex."""
    
    def test_extraer_palabras_basico(self):
        """Test extraer palabras básico."""
        extractor = ExtractorPalabrasRegex()
        resultado = extractor.extraer("Hola mundo")
        
        self.assertEqual(resultado, ["Hola", "mundo"])
    
    def test_extraer_palabras_con_puntuacion(self):
        """Test extraer palabras con puntuación."""
        extractor = ExtractorPalabrasRegex()
        resultado = extractor.extraer("Hola, mundo! ¿Cómo estás?")
        
        self.assertEqual(resultado, ["Hola", "mundo", "Cómo", "estás"])
    
    def test_extraer_texto_vacio(self):
        """Test extraer de texto vacío."""
        extractor = ExtractorPalabrasRegex()
        resultado = extractor.extraer("")
        
        self.assertEqual(resultado, [])
    
    def test_extraer_texto_none(self):
        """Test extraer de texto None."""
        extractor = ExtractorPalabrasRegex()
        resultado = extractor.extraer(None)
        
        self.assertEqual(resultado, [])


class TestPresentadorConsola(unittest.TestCase):
    """Tests para PresentadorConsola."""
    
    @patch('builtins.print')
    def test_mostrar_resultados(self, mock_print):
        """Test mostrar resultados en consola."""
        presentador = PresentadorConsola()
        presentador.mostrar("Hola mundo", ["Hola", "mundo"], 2)
        
        # Verificar que se llamó print 4 veces
        self.assertEqual(mock_print.call_count, 4)
        
        # Verificar contenido específico
        calls = mock_print.call_args_list
        self.assertIn("Contenido del archivo:", str(calls[0]))
        self.assertIn("Hola mundo", str(calls[1]))
        self.assertIn("Palabras encontradas:", str(calls[2]))
        self.assertIn("Total de palabras: 2", str(calls[3]))


class TestContadorDePalabras(unittest.TestCase):
    """Tests para ContadorDePalabras."""
    
    def test_contar_palabras_basico(self):
        """Test contar palabras básico."""
        extractor = ExtractorPalabrasRegex()
        contador = ContadorDePalabras(extractor)
        
        resultado = contador.contar("Hola mundo")
        
        self.assertEqual(resultado, 2)
    
    def test_contar_texto_vacio(self):
        """Test contar texto vacío."""
        extractor = ExtractorPalabrasRegex()
        contador = ContadorDePalabras(extractor)
        
        resultado = contador.contar("")
        
        self.assertEqual(resultado, 0)
    
    def test_contar_texto_none(self):
        """Test contar texto None."""
        extractor = ExtractorPalabrasRegex()
        contador = ContadorDePalabras(extractor)
        
        resultado = contador.contar(None)
        
        self.assertEqual(resultado, 0)


class TestOrquestadorProcesamiento(unittest.TestCase):
    """Tests para OrquestadorProcesamiento."""
    
    def test_procesar_archivo_exitoso(self):
        """Test procesar archivo exitosamente."""
        # Crear mocks
        mock_lector = Mock()
        mock_lector.leer.return_value = "Hola mundo"
        
        mock_contador = Mock()
        mock_contador.contar.return_value = 2
        mock_contador.extractor.extraer.return_value = ["Hola", "mundo"]
        
        mock_presentador = Mock()
        
        # Crear orquestador con mocks
        orquestador = OrquestadorProcesamiento(
            mock_lector, mock_contador, mock_presentador
        )
        
        # Procesar archivo
        resultado = orquestador.procesar_archivo("test.txt")
        
        # Verificar resultado
        self.assertTrue(resultado)
        
        # Verificar que se llamaron los métodos
        mock_lector.leer.assert_called_once_with("test.txt")
        mock_contador.contar.assert_called_once_with("Hola mundo")
        mock_contador.extractor.extraer.assert_called_once_with("Hola mundo")
        mock_presentador.mostrar.assert_called_once_with(
            "Hola mundo", ["Hola", "mundo"], 2
        )
    
    def test_procesar_archivo_error_lectura(self):
        """Test procesar archivo con error de lectura."""
        # Crear mocks
        mock_lector = Mock()
        mock_lector.leer.return_value = None
        
        mock_contador = Mock()
        mock_presentador = Mock()
        
        # Crear orquestador con mocks
        orquestador = OrquestadorProcesamiento(
            mock_lector, mock_contador, mock_presentador
        )
        
        # Procesar archivo
        resultado = orquestador.procesar_archivo("archivo_inexistente.txt")
        
        # Verificar resultado
        self.assertFalse(resultado)
        
        # Verificar que solo se llamó leer
        mock_lector.leer.assert_called_once_with("archivo_inexistente.txt")
        mock_contador.contar.assert_not_called()
        mock_presentador.mostrar.assert_not_called()


class TestIntegracion(unittest.TestCase):
    """Tests de integración."""
    
    def test_flujo_completo(self):
        """Test del flujo completo con implementaciones reales."""
        # Crear archivo temporal
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("Hola mundo, ¿cómo estás?")
            archivo_path = f.name
        
        try:
            # Crear componentes reales
            lector = LectorArchivoLocal()
            extractor = ExtractorPalabrasRegex()
            contador = ContadorDePalabras(extractor)
            presentador = PresentadorConsola()
            
            orquestador = OrquestadorProcesamiento(lector, contador, presentador)
            
            # Procesar archivo
            resultado = orquestador.procesar_archivo(archivo_path)
            
            # Verificar resultado
            self.assertTrue(resultado)
        finally:
            # Limpiar archivo temporal
            os.unlink(archivo_path)


class TestCasosEspeciales(unittest.TestCase):
    """Tests para casos especiales."""
    
    def test_contar_palabras_multiples_casos(self):
        """Test contar palabras con múltiples casos."""
        extractor = ExtractorPalabrasRegex()
        contador = ContadorDePalabras(extractor)
        
        casos = [
            ("Hola mundo", 2),
            ("", 0),
            ("Una sola palabra", 3),
            ("¡Hola, mundo! ¿Cómo estás?", 4),
            ("   ", 0),
            ("a b c d e", 5),
        ]
        
        for texto, esperado in casos:
            with self.subTest(texto=texto):
                resultado = contador.contar(texto)
                self.assertEqual(resultado, esperado)


if __name__ == '__main__':
    # Ejecutar todos los tests
    unittest.main(verbosity=2)
