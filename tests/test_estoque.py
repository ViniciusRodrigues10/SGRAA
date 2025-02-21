# import unittest
# from src.Estoque import Estoque

# class TestEstoque(unittest.TestCase):
#     def setUp(self):
#         """Configuração inicial para cada teste."""
#         self.estoque = Estoque(id=1, item="Ração", quantidade=50)

#     def test_criacao_estoque(self):
#         """Teste para verificar se os atributos do estoque são atribuídos corretamente."""
#         self.assertEqual(self.estoque.id, 1)
#         self.assertEqual(self.estoque.item, "Ração")
#         self.assertEqual(self.estoque.quantidade, 50)

#     def test_atualizar_quantidade(self):
#         """Teste para verificar se a atualização da quantidade funciona corretamente."""
#         self.estoque.atualizar_quantidade(30)
#         self.assertEqual(self.estoque.quantidade, 30)

#     def test_registrar_consumo_valido(self):
#         """Teste para verificar se o consumo válido reduz a quantidade corretamente."""
#         self.estoque.registrar_consumo(20)
#         self.assertEqual(self.estoque.quantidade, 30)

#     def test_registrar_consumo_insuficiente(self):
#         """Teste para verificar se o consumo excessivo levanta um erro."""
#         with self.assertRaises(ValueError) as context:
#             self.estoque.registrar_consumo(60)  # Quantidade maior que o disponível
#         self.assertEqual(str(context.exception), "Quantidade insuficiente em estoque.")

# if __name__ == '__main__':
#     unittest.main()

import unittest
from src.Estoque import Estoque

class TestAtualizacaoEstoque(unittest.TestCase):
    def setUp(self):
        self.estoque = Estoque(1, "Ração", 100)

    def test_adicionar_novo_item_ao_estoque(self):
        self.estoque.atualizar_quantidade(150)
        self.assertEqual(self.estoque.quantidade, 150)

    def test_atualizar_quantidade_item_existente(self):
        self.estoque.atualizar_quantidade(200)
        self.assertEqual(self.estoque.quantidade, 200)

    def test_registrar_consumo_dentro_do_estoque(self):
        self.estoque.registrar_consumo(50)
        self.assertEqual(self.estoque.quantidade, 50)

    def test_conferir_quantidade_apos_atualizacao(self):
        self.estoque.atualizar_quantidade(300)
        self.assertEqual(self.estoque.quantidade, 300)

    def setUp(self):
        self.estoque = Estoque(1, "Ração", 100)

    def test_tentar_consumir_mais_que_disponivel(self):
        with self.assertRaises(ValueError):
            self.estoque.registrar_consumo(150)

    def test_tentar_consumir_item_inexistente(self):
        with self.assertRaises(ValueError):
            estoque = Estoque(2, "Medicamento", 0)
            estoque.registrar_consumo(10)

    def test_verificar_quantidade_apos_consumo(self):
        self.estoque.registrar_consumo(50)
        self.assertEqual(self.estoque.quantidade, 50)

    def test_garantir_erro_ao_consumir_mais_que_permitido(self):
        with self.assertRaises(ValueError):
            self.estoque.registrar_consumo(200)
            