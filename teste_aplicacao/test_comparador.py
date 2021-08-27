import unittest
from aplicacao.comparador import compara_numeros_simples, compara_numeros_quadraplos


class MyTestCase(unittest.TestCase):
    def test_comparacao_de_valores_a_maior(self):
        resultado = compara_numeros_simples(5, 2)
        self.assertTrue(resultado)

    def test_comparacao_de_valores_b_maior(self):
        resultado = compara_numeros_simples(1, 2)
        self.assertTrue(resultado)

    def test_comparacao_de_valores_iguais(self):
        resultado = compara_numeros_simples(5, 5)
        self.assertFalse(resultado)

    # ===========================

    # VV = V
    def test_comparacao_amaiorb_xmenory(self):
        resultado = compara_numeros_quadraplos(6, 5, 1, 2)
        self.assertTrue(resultado)

    # VF = F
    def test_comparacao_amaiorb_xmaiory(self):
        resultado = compara_numeros_quadraplos(6, 5, 3, 2)
        self.assertFalse(resultado)

    # FV = F
    def test_comparacao_amenorb_xmenory(self):
        resultado = compara_numeros_quadraplos(1, 5, 1, 2)
        self.assertFalse(resultado)

    # FF = F
    def test_comparacao_amenorb_xmaiory(self):
        resultado = compara_numeros_quadraplos(1, 5, 7, 2)
        self.assertFalse(resultado)

    def test_comparacao_aigualb_xigualy(self):
        resultado = compara_numeros_quadraplos(1, 1, 1, 1)
        self.assertFalse(resultado)

    def test_comparacao_aigualb_xmaiory(self):
        resultado = compara_numeros_quadraplos(1, 1, 2, 1)
        self.assertFalse(resultado)

    def test_comparacao_aigualb_xmenory(self):
        resultado = compara_numeros_quadraplos(1, 1, 1, 2)
        self.assertFalse(resultado)

    def test_comparacao_amenorb_xigualy(self):
        resultado = compara_numeros_quadraplos(1, 2, 3, 3)
        self.assertFalse(resultado)

    def test_comparacao_amaiorb_xigualy(self):
        resultado = compara_numeros_quadraplos(2, 1, 5, 5)
        self.assertFalse(resultado)


if __name__ == '__main__':
    unittest.main()
