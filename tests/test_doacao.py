import unittest
from datetime import date
from typing import List
from src.Doacao import Doacao  

class TestDoacao(unittest.TestCase):
    def setUp(self):
        self.doacao = Doacao(1, 1, ["Ração", "Medicamento"], 10, date(2023, 10, 1))

    def test_criar_doacao_com_dados_validos(self):
        self.assertEqual(self.doacao.id, 1)
        self.assertEqual(self.doacao.idDoador, 1)
        self.assertEqual(self.doacao.items, ["Ração", "Medicamento"])
        self.assertEqual(self.doacao.quantidade, 10)
        self.assertEqual(self.doacao.data, date(2023, 10, 1))

    def test_criar_doacao_com_items_vazios(self):
        with self.assertRaises(ValueError):
            Doacao(2, 2, [], 5, date(2023, 10, 2))

    def test_criar_doacao_com_quantidade_negativa(self):
        with self.assertRaises(ValueError):
            Doacao(3, 3, ["Ração"], -5, date(2023, 10, 3))

    def test_criar_doacao_com_quantidade_zero(self):
        with self.assertRaises(ValueError):
            Doacao(4, 4, ["Ração"], 0, date(2023, 10, 4))

    def test_criar_doacao_com_data_invalida(self):
        with self.assertRaises(ValueError):
            Doacao(5, 5, ["Ração"], 5, "2023-10-05")

    def test_adicionar_item_valido(self):
        self.doacao.adicionar_item("Coleira", 2)
        self.assertIn("Coleira", self.doacao.items)
        self.assertEqual(self.doacao.quantidade, 12)

    def test_adicionar_item_com_quantidade_zero(self):
        with self.assertRaises(ValueError):
            self.doacao.adicionar_item("Coleira", 0)

    def test_adicionar_item_com_quantidade_negativa(self):
        with self.assertRaises(ValueError):
            self.doacao.adicionar_item("Coleira", -2)

    def test_adicionar_item_duplicado(self):
        self.doacao.adicionar_item("Ração", 5)
        self.assertEqual(self.doacao.items.count("Ração"), 1) 
        self.assertEqual(self.doacao.quantidade, 15)

    def test_quantidade_apos_adicionar_item(self):
        self.doacao.adicionar_item("Coleira", 3)
        self.assertEqual(self.doacao.quantidade, 13)

    def test_items_apos_adicionar_item(self):
        self.doacao.adicionar_item("Coleira", 3)
        self.assertIn("Coleira", self.doacao.items)

    def test_adicionar_multiplos_items(self):
        self.doacao.adicionar_item("Coleira", 2)
        self.doacao.adicionar_item("Brinquedo", 1)
        self.assertEqual(self.doacao.items, ["Ração", "Medicamento", "Coleira", "Brinquedo"])
        self.assertEqual(self.doacao.quantidade, 13)

    def test_adicionar_item_com_quantidade_muito_grande(self):
        self.doacao.adicionar_item("Ração", 1000)
        self.assertEqual(self.doacao.quantidade, 1010)

    def test_mensagem_erro_items_vazios(self):
        with self.assertRaises(ValueError) as context:
            Doacao(6, 6, [], 5, date(2023, 10, 6))
        self.assertEqual(str(context.exception), "A lista de itens não pode estar vazia.")

    def test_mensagem_erro_quantidade_negativa(self):
        with self.assertRaises(ValueError) as context:
            Doacao(7, 7, ["Ração"], -5, date(2023, 10, 7))
        self.assertEqual(str(context.exception), "A quantidade não pode ser negativa ou zero.")

    def test_mensagem_erro_quantidade_zero(self):
        with self.assertRaises(ValueError) as context:
            Doacao(8, 8, ["Ração"], 0, date(2023, 10, 8))
        self.assertEqual(str(context.exception), "A quantidade não pode ser negativa ou zero.")

    def test_mensagem_erro_data_invalida(self):
        with self.assertRaises(ValueError) as context:
            Doacao(9, 9, ["Ração"], 5, "2023-10-09")
        self.assertEqual(str(context.exception), "A data deve ser do tipo date.")

    def test_representacao_string(self):
        doacao = Doacao(10, 10, ["Ração"], 5, date(2023, 10, 10))
        self.assertEqual(str(doacao), "Doacao(id=10, idDoador=10, items=['Ração'], quantidade=5, data=2023-10-10)")
