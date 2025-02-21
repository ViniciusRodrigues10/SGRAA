import unittest
from src.Voluntario import Voluntario 

class TestVoluntario(unittest.TestCase):
    def setUp(self):
        self.voluntario = Voluntario(1, "Carlos Souza", "carlos@example.com", "Resgate")

    def test_criar_voluntario_com_dados_validos(self):
        self.assertEqual(self.voluntario.id, 1)
        self.assertEqual(self.voluntario.nome, "Carlos Souza")
        self.assertEqual(self.voluntario.contato, "carlos@example.com")
        self.assertEqual(self.voluntario.funcao, "Resgate")

    def test_criar_voluntario_com_nome_vazio(self):
        with self.assertRaises(ValueError):
            Voluntario(2, "", "maria@example.com", "Assistência")

    def test_criar_voluntario_com_contato_vazio(self):
        with self.assertRaises(ValueError):
            Voluntario(3, "Maria Oliveira", "", "Assistência")

    def test_criar_voluntario_com_funcao_vazia(self):
        with self.assertRaises(ValueError):
            Voluntario(4, "João Silva", "joao@example.com", "")

    def test_atualizar_funcao_valida(self):
        self.voluntario.atualizar_funcao("Assistência")
        self.assertEqual(self.voluntario.funcao, "Assistência")

    def test_atualizar_funcao_vazia(self):
        with self.assertRaises(ValueError):
            self.voluntario.atualizar_funcao("")

    def test_atualizar_funcao_nula(self):
        with self.assertRaises(ValueError):
            self.voluntario.atualizar_funcao(None)

    def test_nome_apos_criacao(self):
        self.assertEqual(self.voluntario.nome, "Carlos Souza")

    def test_contato_apos_criacao(self):
        self.assertEqual(self.voluntario.contato, "carlos@example.com")

    def test_funcao_apos_criacao(self):
        self.assertEqual(self.voluntario.funcao, "Resgate")

    def test_atualizar_funcao_com_nova_funcao_muito_longa(self):
        nova_funcao = "a" * 1000
        self.voluntario.atualizar_funcao(nova_funcao)
        self.assertEqual(self.voluntario.funcao, nova_funcao)

    def test_mensagem_erro_nome_vazio(self):
        with self.assertRaises(ValueError) as context:
            Voluntario(5, "", "joao@example.com", "Resgate")
        self.assertEqual(str(context.exception), "O nome não pode estar vazio.")

    def test_mensagem_erro_contato_vazio(self):
        with self.assertRaises(ValueError) as context:
            Voluntario(6, "João Silva", "", "Resgate")
        self.assertEqual(str(context.exception), "O contato não pode estar vazio.")

    def test_mensagem_erro_funcao_vazia(self):
        with self.assertRaises(ValueError) as context:
            Voluntario(7, "João Silva", "joao@example.com", "")
        self.assertEqual(str(context.exception), "A função não pode estar vazia.")

    def test_representacao_string(self):
        voluntario = Voluntario(8, "Maria Oliveira", "maria@example.com", "Assistência")
        self.assertEqual(str(voluntario), "Voluntario(id=8, nome=Maria Oliveira, contato=maria@example.com, funcao=Assistência)")
