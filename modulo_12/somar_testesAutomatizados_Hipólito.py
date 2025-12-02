

import unittest

from somar import somar

class TestSomar(unittest.TestCase):


    def test_soma_numeros_positivos(self):
        resultado = somar(5, 7)
        self.assertEqual(resultado, 12, "Deve ser 11")

    def test_soma_com_zero(self):
        resultado = somar(10, 0)
        self.assertEqual(resultado, 10, "Deve ser 10")

    def test_soma_numeros_negativos(self):
        resultado = somar(-5, -3)
        self.assertEqual(resultado, -8, "Deve ser -8")

    def test_soma_positivo_e_negativo(self):
        resultado = somar(10, -5)
        self.assertEqual(resultado, 5, "Deve ser 5")


if __name__ == '__main__':
    unittest.main()