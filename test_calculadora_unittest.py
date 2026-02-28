# test_calculadora_unittest.py
import unittest
from calculadora import sumar, dividir

class TestCalculadora(unittest.TestCase):

    def test_sumar_positivos(self):
        self.assertEqual(sumar(3, 5), 8)

    def test_sumar_negativos(self):
        self.assertEqual(sumar(-1, -3), -4)

    def test_dividir_normal(self):
        self.assertAlmostEqual(dividir(10, 4), 2.5)

    def test_dividir_por_cero_lanza_excepcion(self):
        with self.assertRaises(ValueError):
            dividir(10, 0)

if __name__ == '__main__':
    unittest.main()