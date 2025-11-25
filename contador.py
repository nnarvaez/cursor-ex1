"""Herramienta modular para contar palabras en archivos de texto."""
import re
from abc import ABC, abstractmethod
from typing import List, Optional


class LectorArchivo(ABC):
    """Interfaz para leer archivos (Dependency Inversion)."""
    
    @abstractmethod
    def leer(self, nombre_archivo: str) -> Optional[str]:
        """Lee el contenido de un archivo."""
        pass


class LectorArchivoLocal(LectorArchivo):
    """Implementación concreta para leer archivos del sistema local."""
    
    def leer(self, nombre_archivo: str) -> Optional[str]:
        """Lee el contenido de un archivo local."""
        try:
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                return archivo.read()
        except FileNotFoundError:
            print("El archivo no existe")
            return None
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return None


class ExtractorPalabras(ABC):
    """Interfaz para extraer palabras de texto (Dependency Inversion)."""
    
    @abstractmethod
    def extraer(self, texto: str) -> List[str]:
        """Extrae palabras de un texto."""
        pass


class ExtractorPalabrasRegex(ExtractorPalabras):
    """Implementación concreta usando expresiones regulares."""
    
    def extraer(self, texto: str) -> List[str]:
        """Extrae palabras usando regex."""
        if not texto:
            return []
        return re.findall(r'\b\w+\b', texto)


class PresentadorResultados(ABC):
    """Interfaz para presentar resultados (Dependency Inversion)."""
    
    @abstractmethod
    def mostrar(self, texto: str, palabras: List[str], total: int) -> None:
        """Muestra los resultados."""
        pass


class PresentadorConsola(PresentadorResultados):
    """Implementación concreta para mostrar en consola."""
    
    def mostrar(self, texto: str, palabras: List[str], total: int) -> None:
        """Muestra los resultados en consola."""
        print("Contenido del archivo:")
        print(texto)
        print("\nPalabras encontradas:")
        print(palabras)
        print(f"\nTotal de palabras: {total}")


class ContadorDePalabras:
    """Clase simple que solo cuenta palabras (Single Responsibility)."""
    
    def __init__(self, extractor: ExtractorPalabras):
        """Inicializa el contador con un extractor de palabras.

        Args:
            extractor: Implementación para extraer palabras
        """
        self.extractor = extractor
    
    def contar(self, texto: str) -> int:
        """Cuenta las palabras en un texto.

        Args:
            texto: Texto a analizar
            
        Returns:
            int: Número total de palabras encontradas
        """
        if not texto:
            return 0
        return len(self.extractor.extraer(texto))


class OrquestadorProcesamiento:
    """Clase que orquesta todo el proceso de conteo de palabras."""
    
    def __init__(self, 
                 lector: LectorArchivo, 
                 contador: ContadorDePalabras,
                 presentador: PresentadorResultados):
        """Inicializa el orquestador con sus dependencias.

        Args:
            lector: Implementación para leer archivos
            contador: Contador de palabras
            presentador: Implementación para mostrar resultados
        """
        self.lector = lector
        self.contador = contador
        self.presentador = presentador
    
    def procesar_archivo(self, nombre_archivo: str) -> bool:
        """Orquesta lectura, conteo y presentación de resultados.

        Args:
            nombre_archivo: Ruta del archivo a procesar
            
        Returns:
            bool: True si se procesó correctamente, False en caso contrario
        """
        # Leer archivo
        texto = self.lector.leer(nombre_archivo)
        if texto is None:
            return False
        
        # Contar palabras
        total = self.contador.contar(texto)
        palabras = self.contador.extractor.extraer(texto)
        
        # Mostrar resultados
        self.presentador.mostrar(texto, palabras, total)
        
        return True


def crear_orquestador() -> OrquestadorProcesamiento:
    """Factory method para crear un orquestador con dependencias por defecto."""
    lector = LectorArchivoLocal()
    extractor = ExtractorPalabrasRegex()
    contador = ContadorDePalabras(extractor)
    presentador = PresentadorConsola()
    
    return OrquestadorProcesamiento(lector, contador, presentador)


def main():
    """Función principal del programa."""
    orquestador = crear_orquestador()
    
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    orquestador.procesar_archivo(nombre_archivo)


if __name__ == "__main__":
    main()
