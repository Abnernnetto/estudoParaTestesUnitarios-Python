import unittest
from aplicacao.calculadora import soma, subtracao, multiplicacao, divisao


class MyTestCase(unittest.TestCase):

    def test_soma(self):
        resultado = soma(1, 2)
        self.assertEqual(3, resultado)


    def test_subtracao(self):
        resultado = subtracao(5, 2)
        self.assertEqual(3, resultado)


    def test_multiplicacao(self):
        resultado = multiplicacao(4, 2)
        self.assertEqual(8, resultado)


    def test_divisao(self):
        resultado = divisao(10, 2)
        self.assertEqual(5, resultado)

if __name__ == '__main__':
    unittest.main()
