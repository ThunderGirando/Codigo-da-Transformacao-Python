import unittest
from calculadora import Calculadora 

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()


    def test_somar_positivos(self):
        resultado = self.calc.somar(10, 5)
        self.assertEqual(resultado, 15)

    def test_somar_negativos(self):
        resultado = self.calc.somar(10, -5)
        self.assertEqual(resultado, 5)
        
    def test_dividir_inteiros(self):
        resultado = self.calc.dividir(10, 2)
        self.assertEqual(resultado, 5)

    def test_dividir_flutuantes(self):
        resultado = self.calc.dividir(5, 2)
        self.assertAlmostEqual(resultado, 2.5) 
        
    #Exercício 3 ->
    def test_dividir_por_zero(self):
        with self.assertRaises(ValueError):
            self.calc.dividir(10, 0)
            

    def test_multiplicar_por_zero(self):
        resultado = self.calc.multiplicar(10, 0)
        self.assertEqual(resultado, 0)



if __name__ == '__main__':
    unittest.main()