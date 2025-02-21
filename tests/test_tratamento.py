import unittest
from datetime import date
from src.Animal import Animal
from src.Tratamento import Tratamento

class TestTratamento(unittest.TestCase):
    def setUp(self):
        self.animal = Animal(1, "Rex", "Cão", "Vira-lata", 3, "Macho", "Médio", "Marrom", "Disponível", date(2023, 10, 1))
        self.tratamento1 = Tratamento(1, "Vacinação", ["Vacina A"])
        self.tratamento2 = Tratamento(2, "Cirurgia", ["Anestésico", "Analgésico"])

    def test_adicionar_tratamento_com_um_medicamento(self):
        tratamento = Tratamento(1, "Vacinação", ["Vacina A"])
        self.animal.adicionar_tratamento(tratamento)
        self.assertIn(tratamento, self.animal.tratamentos)

    def test_adicionar_tratamento_com_varios_medicamentos(self):
        tratamento = Tratamento(2, "Vacinação", ["Vacina A", "Vacina B"])
        self.animal.adicionar_tratamento(tratamento)
        self.assertIn(tratamento, self.animal.tratamentos)

    def test_adicionar_tratamento_e_verificar_atributos(self):
        tratamento = Tratamento(3, "Vacinação", ["Vacina A"])
        self.animal.adicionar_tratamento(tratamento)
        self.assertEqual(tratamento.descricao, "Vacinação")
        self.assertEqual(tratamento.medicamentos, ["Vacina A"])

    def test_adicionar_tratamento_e_conferir_registro(self):
        tratamento = Tratamento(4, "Vacinação", ["Vacina A"])
        self.animal.adicionar_tratamento(tratamento)
        self.assertIn(tratamento, self.animal.tratamentos)

    def test_adicionar_tratamento_sem_medicamentos(self):
        with self.assertRaises(ValueError):
            Tratamento(1, "Vacinação", [])

    def test_adicionar_tratamento_com_medicamento_nulo(self):
        with self.assertRaises(ValueError):
            Tratamento(2, "Vacinação", [None])

    # Talvez não seja necessário esse teste
    # def test_adicionar_tratamento_com_medicamento_invalido(self):
    #     with self.assertRaises(ValueError):
    #         Tratamento(3, "Vacinação", ["Invalido"])

    # Remover esse teste, teste duplicado 
    # def test_verificar_erro_ao_adicionar_tratamento_sem_medicamento(self):
    #     with self.assertRaises(ValueError):
    #         Tratamento(4, "Vacinação", [])

    def test_adicionar_varios_tratamentos_e_listar(self):
        self.animal.adicionar_tratamento(self.tratamento1)
        self.animal.adicionar_tratamento(self.tratamento2)
        self.assertEqual(len(self.animal.tratamentos), 2)

    def test_listar_tratamentos_e_verificar_ordem(self):
        self.animal.adicionar_tratamento(self.tratamento1)
        self.animal.adicionar_tratamento(self.tratamento2)
        self.assertEqual(self.animal.tratamentos[0].descricao, "Vacinação")
        self.assertEqual(self.animal.tratamentos[1].descricao, "Cirurgia")

    def test_listar_tratamentos_e_conferir_medicamentos(self):
        self.animal.adicionar_tratamento(self.tratamento1)
        self.assertEqual(self.animal.tratamentos[0].medicamentos, ["Vacina A"])

    def test_listar_tratamentos_e_verificar_exibicao_correta(self):
        self.animal.adicionar_tratamento(self.tratamento1)
        self.assertEqual(str(self.animal.tratamentos[0]), "Tratamento: Vacinação, Medicamentos: ['Vacina A']")
        