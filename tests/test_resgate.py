import unittest
from datetime import date
from src.Resgate import Resgate  
from src.Animal import Animal 

class TestResgate(unittest.TestCase):
    def setUp(self):
        self.animal1 = Animal(1, "Rex", "Cão", "Vira-lata", 3, "Macho", "Médio", "Marrom", "Disponível", date(2023, 10, 1))
        self.animal2 = Animal(2, "Luna", "Gato", "Siamês", 2, "Fêmea", "Pequeno", "Branco", "Disponível", date(2023, 10, 2))
        self.resgate = Resgate(1, date(2023, 10, 3), "Rua A", [self.animal1])

    def test_criar_resgate_com_dados_validos(self):
        self.assertEqual(self.resgate.id, 1)
        self.assertEqual(self.resgate.data, date(2023, 10, 3))
        self.assertEqual(self.resgate.localidade, "Rua A")
        self.assertEqual(self.resgate.animaisResgatados, [self.animal1])

    def test_criar_resgate_com_data_invalida(self):
        with self.assertRaises(ValueError):
            Resgate(2, "2023-10-04", "Rua B", [self.animal2])

    def test_criar_resgate_com_localidade_vazia(self):
        with self.assertRaises(ValueError):
            Resgate(3, date(2023, 10, 5), "", [self.animal1])

    def test_criar_resgate_sem_animais(self):
        with self.assertRaises(ValueError):
            Resgate(4, date(2023, 10, 6), "Rua C", [])

    def test_adicionar_animal_resgatado_valido(self):
        self.resgate.adicionar_animal_resgatado(self.animal2)
        self.assertIn(self.animal2, self.resgate.animaisResgatados)

    def test_adicionar_animal_resgatado_nulo(self):
        with self.assertRaises(ValueError):
            self.resgate.adicionar_animal_resgatado(None)

    def test_adicionar_animal_resgatado_duplicado(self):
        self.resgate.adicionar_animal_resgatado(self.animal1)
        self.assertEqual(self.resgate.animaisResgatados.count(self.animal1), 1)  

    def test_localidade_apos_criacao(self):
        self.assertEqual(self.resgate.localidade, "Rua A")

    def test_data_apos_criacao(self):
        self.assertEqual(self.resgate.data, date(2023, 10, 3))

    def test_animais_resgatados_apos_criacao(self):
        self.assertEqual(self.resgate.animaisResgatados, [self.animal1])

    def test_adicionar_multiplos_animais_resgatados(self):
        self.resgate.adicionar_animal_resgatado(self.animal2)
        self.assertEqual(len(self.resgate.animaisResgatados), 2)

    def test_mensagem_erro_data_invalida(self):
        with self.assertRaises(ValueError) as context:
            Resgate(5, "2023-10-07", "Rua D", [self.animal1])
        self.assertEqual(str(context.exception), "A data deve ser do tipo date.")

    def test_mensagem_erro_localidade_vazia(self):
        with self.assertRaises(ValueError) as context:
            Resgate(6, date(2023, 10, 8), "", [self.animal1])
        self.assertEqual(str(context.exception), "A localidade não pode estar vazia.")

    def test_mensagem_erro_sem_animais(self):
        with self.assertRaises(ValueError) as context:
            Resgate(7, date(2023, 10, 9), "Rua E", [])
        self.assertEqual(str(context.exception), "A lista de animais resgatados não pode estar vazia.")

    def test_representacao_string(self):
        resgate = Resgate(8, date(2023, 10, 10), "Rua F", [self.animal1, self.animal2])
        self.assertEqual(str(resgate), "Resgate(id=8, data=2023-10-10, localidade=Rua F, animaisResgatados=[Animal(id=1, nome=Rex), Animal(id=2, nome=Luna)])")
