import unittest
from src.Estoque import Estoque

class TestEstoque(unittest.TestCase):
    def setUp(self):
        """Configuração inicial para cada teste."""
        self.estoque = Estoque(id=1, item="Ração", quantidade=50)

    def test_criacao_estoque(self):
        """Teste para verificar se os atributos do estoque são atribuídos corretamente."""
        self.assertEqual(self.estoque.id, 1)
        self.assertEqual(self.estoque.item, "Ração")
        self.assertEqual(self.estoque.quantidade, 50)

    def test_atualizar_quantidade(self):
        """Teste para verificar se a atualização da quantidade funciona corretamente."""
        self.estoque.atualizar_quantidade(30)
        self.assertEqual(self.estoque.quantidade, 30)

    def test_registrar_consumo_valido(self):
        """Teste para verificar se o consumo válido reduz a quantidade corretamente."""
        self.estoque.registrar_consumo(20)
        self.assertEqual(self.estoque.quantidade, 30)

    def test_registrar_consumo_insuficiente(self):
        """Teste para verificar se o consumo excessivo levanta um erro."""
        with self.assertRaises(ValueError) as context:
            self.estoque.registrar_consumo(60)  # Quantidade maior que o disponível
        self.assertEqual(str(context.exception), "Quantidade insuficiente em estoque.")

if __name__ == '__main__':
    unittest.main()
