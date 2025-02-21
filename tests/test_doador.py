import unittest
from src.Doador import Doador  

class TestDoador(unittest.TestCase):
    def setUp(self):
        self.doador = Doador(1, "João Silva", "joao@example.com", "Individual")

    def test_criar_doador_com_dados_validos(self):
        self.assertEqual(self.doador.id, 1)
        self.assertEqual(self.doador.nome, "João Silva")
        self.assertEqual(self.doador.contato, "joao@example.com")
        self.assertEqual(self.doador.tipo, "Individual")

    def test_criar_doador_com_nome_vazio(self):
        with self.assertRaises(ValueError):
            Doador(2, "", "maria@example.com", "Individual")

    def test_criar_doador_com_contato_vazio(self):
        with self.assertRaises(ValueError):
            Doador(3, "Maria Oliveira", "", "Individual")

    def test_criar_doador_com_tipo_invalido(self):
        with self.assertRaises(ValueError):
            Doador(4, "Carlos Souza", "carlos@example.com", "Invalido")

    def test_atualizar_contato_valido(self):
        self.doador.atualizar_contato("joao.silva@example.com")
        self.assertEqual(self.doador.contato, "joao.silva@example.com")

    def test_atualizar_contato_vazio(self):
        with self.assertRaises(ValueError):
            self.doador.atualizar_contato("")

    def test_atualizar_contato_com_novo_contato_nulo(self):
        with self.assertRaises(ValueError):
            self.doador.atualizar_contato(None)

    def test_nome_apos_criacao(self):
        self.assertEqual(self.doador.nome, "João Silva")

    def test_contato_apos_criacao(self):
        self.assertEqual(self.doador.contato, "joao@example.com")

    def test_tipo_apos_criacao(self):
        self.assertEqual(self.doador.tipo, "Individual")

    def test_atualizar_contato_com_novo_contato_muito_longo(self):
        novo_contato = "a" * 1000
        self.doador.atualizar_contato(novo_contato)
        self.assertEqual(self.doador.contato, novo_contato)

    def test_mensagem_erro_nome_vazio(self):
        with self.assertRaises(ValueError) as context:
            Doador(5, "", "joao@example.com", "Individual")
        self.assertEqual(str(context.exception), "O nome não pode estar vazio.")

    def test_mensagem_erro_contato_vazio(self):
        with self.assertRaises(ValueError) as context:
            Doador(6, "João Silva", "", "Individual")
        self.assertEqual(str(context.exception), "O contato não pode estar vazio.")

    def test_mensagem_erro_tipo_invalido(self):
        with self.assertRaises(ValueError) as context:
            Doador(7, "João Silva", "joao@example.com", "Invalido")
        self.assertEqual(str(context.exception), "O tipo deve ser 'Individual' ou 'Instituição'.")

    def test_representacao_string(self):
        doador = Doador(8, "Maria Oliveira", "maria@example.com", "Instituição")
        self.assertEqual(str(doador), "Doador(id=8, nome=Maria Oliveira, contato=maria@example.com, tipo=Instituição)")
