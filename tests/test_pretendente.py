import unittest
from src.Pretendente import Pretendente 

class TestPretendente(unittest.TestCase):
    def setUp(self):
        self.pretendente = Pretendente(1, "João Silva", "joao@example.com")

    def test_criar_pretendente_com_dados_validos(self):
        self.assertEqual(self.pretendente.id, 1)
        self.assertEqual(self.pretendente.nome, "João Silva")
        self.assertEqual(self.pretendente.contato, "joao@example.com")

    def test_criar_pretendente_com_nome_vazio(self):
        with self.assertRaises(ValueError):
            Pretendente(2, "", "maria@example.com")

    def test_criar_pretendente_com_contato_vazio(self):
        with self.assertRaises(ValueError):
            Pretendente(3, "Maria Oliveira", "")

    def test_atualizar_contato_valido(self):
        self.pretendente.atualizar_contato("joao.silva@example.com")
        self.assertEqual(self.pretendente.contato, "joao.silva@example.com")

    def test_atualizar_contato_vazio(self):
        with self.assertRaises(ValueError):
            self.pretendente.atualizar_contato("")

    def test_atualizar_contato_com_novo_contato_nulo(self):
        with self.assertRaises(ValueError):
            self.pretendente.atualizar_contato(None)

    def test_nome_apos_criacao(self):
        self.assertEqual(self.pretendente.nome, "João Silva")

    def test_contato_apos_criacao(self):
        self.assertEqual(self.pretendente.contato, "joao@example.com")

    def test_atualizar_contato_com_novo_contato_muito_longo(self):
        novo_contato = "a" * 1000
        self.pretendente.atualizar_contato(novo_contato)
        self.assertEqual(self.pretendente.contato, novo_contato)

    def test_mensagem_erro_nome_vazio(self):
        with self.assertRaises(ValueError) as context:
            Pretendente(4, "", "joao@example.com")
        self.assertEqual(str(context.exception), "O nome não pode estar vazio.")

    def test_mensagem_erro_contato_vazio(self):
        with self.assertRaises(ValueError) as context:
            Pretendente(5, "João Silva", "")
        self.assertEqual(str(context.exception), "O contato não pode estar vazio.")

    def test_representacao_string(self):
        pretendente = Pretendente(6, "Maria Oliveira", "maria@example.com")
        self.assertEqual(str(pretendente), "Pretendente(id=6, nome=Maria Oliveira, contato=maria@example.com)")
