import unittest
from aplicacao.comparador_de_decisao import comparar_decisao

class MyTestCase(unittest.TestCase):
    def test_decisao_numero_menor(self):
        resultado = comparar_decisao(2)
        self.assertFalse(resultado)


    def test_decisao_numero_maior(self):
        resultado = comparar_decisao(6)
        self.assertTrue(resultado)


    def test_decisao_numero_igual(self):
        resultado = comparar_decisao(5)
        self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main()
