import pytest
from io import StringIO
import sys
from main import amigos

def parse_solucion_file(filename):
    """Lee el archivo solucion.txt y extrae los pares esperados"""
    pares = []
    tiempo = None
    
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        parts = line.split()
        
        # Si tiene 2 números, es un par (i, s)
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            pares.append((int(parts[0]), int(parts[1])))
        # Si tiene 1 número decimal, es el tiempo
        elif len(parts) == 1:
            try:
                tiempo = float(parts[0])
            except ValueError:
                pass
    
    return pares, tiempo

class TestAmigos:
    """Suite de pruebas para la función amigos()"""
    
    @classmethod
    def setup_class(cls):
        """Carga los datos esperados del archivo solucion.txt"""
        cls.expected_pares, cls.expected_tiempo = parse_solucion_file('solucion.txt')
    
    def capture_amigos_output(self, MAX):
        """Captura el output de la función amigos()"""
        captured_output = StringIO()
        sys.stdout = captured_output
        amigos(MAX)
        sys.stdout = sys.__stdout__
        return captured_output.getvalue()
    
    def parse_output(self, output):
        """Parsea el output y extrae los pares (i, s)"""
        lines = output.strip().split('\n')
        pares = []
        tiempo = None
        
        for line in lines:
            line = line.strip()
            if not line:
                continue
            
            parts = line.split()
            
            # Si tiene 2 números, es un par (i, s)
            if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
                pares.append((int(parts[0]), int(parts[1])))
            # Si tiene 1 número decimal, es el tiempo
            elif len(parts) == 1:
                try:
                    tiempo = float(parts[0])
                except ValueError:
                    pass
        
        return pares, tiempo
    
    def test_archivo_solucion_existe(self):
        """Verifica que el archivo solucion.txt existe"""
        assert len(self.expected_pares) > 0, "No se pudo leer el archivo solucion.txt"
    
    def test_solucion_tiene_pares_esperados(self):
        """Verifica que se leyeron pares del archivo"""
        assert len(self.expected_pares) == 31, f"Se esperaban 31 pares, se encontraron {len(self.expected_pares)}"

    def test_amigos_small_range(self):
        """Verifica resultados en un rango pequeño (0-30)"""
        output = self.capture_amigos_output(30)
        pares, _ = self.parse_output(output)
        expected_small = [(0, 0), (6, 6), (28, 28)]
        assert pares == expected_small
    
    def test_perfect_numbers_from_solution(self):
        """Verifica que los números perfectos coinciden con solucion.txt"""
        output = self.capture_amigos_output(100000)
        pares, _ = self.parse_output(output)
        
        perfect_from_output = [(i, s) for i, s in pares if i == s]
        perfect_from_file = [(i, s) for i, s in self.expected_pares if i == s]
        
        assert perfect_from_output == perfect_from_file