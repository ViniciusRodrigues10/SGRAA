import unittest
from datetime import date
from src.Animal import Animal
from src.Tratamento import Tratamento

class TestAnimal(unittest.TestCase):
    def setUp(self):
        """Configuração inicial para cada teste."""
        self.animal = Animal(
            id=1, 
            nome="Rex", 
            especie="Cachorro", 
            raca="Labrador", 
            idade=3, 
            sexo="Macho", 
            porte="Grande", 
            cor="Amarelo", 
            statusAdocao="Disponível", 
            dataChegada=date(2024, 2, 14)
        )

    def test_criacao_animal(self):
        """Teste para verificar se os atributos do animal são atribuídos corretamente."""
        self.assertEqual(self.animal.id, 1)
        self.assertEqual(self.animal.nome, "Rex")
        self.assertEqual(self.animal.especie, "Cachorro")
        self.assertEqual(self.animal.raca, "Labrador")
        self.assertEqual(self.animal.idade, 3)
        self.assertEqual(self.animal.sexo, "Macho")
        self.assertEqual(self.animal.porte, "Grande")
        self.assertEqual(self.animal.cor, "Amarelo")
        self.assertEqual(self.animal.statusAdocao, "Disponível")
        self.assertEqual(self.animal.dataChegada, date(2024, 2, 14))
        self.assertIsNone(self.animal.dataSaida)
        self.assertEqual(len(self.animal.tratamentos), 0)

    def test_adicionar_tratamento(self):
        """Teste para adicionar um tratamento e verificar se foi armazenado corretamente."""
        tratamento = Tratamento(1, "Vacinação", ["Vacina A", "Vacina B"])
        self.animal.adicionar_tratamento(tratamento)
        self.assertEqual(len(self.animal.tratamentos), 1)
        self.assertEqual(self.animal.tratamentos[0].descricao, "Vacinação")

    def test_marcar_como_adotado(self):
        """Teste para marcar um animal como adotado."""
        data_adocao = date(2024, 3, 1)
        self.animal.marcar_como_adotado(data_adocao)
        self.assertEqual(self.animal.statusAdocao, "Adotado")
        self.assertEqual(self.animal.dataSaida, data_adocao)

    def test_listar_tratamentos(self):
        """Teste para listar os tratamentos do animal."""
        tratamento1 = Tratamento(2, "Vermifugação", ["Vermífugo A"])
        tratamento2 = Tratamento(3, "Castração", ["Antibiotica A"])
        
        self.animal.adicionar_tratamento(tratamento1)
        self.animal.adicionar_tratamento(tratamento2)

        tratamentos_listados = self.animal.listar_tratamentos()
        self.assertEqual(tratamentos_listados, ["Vermifugação", "Castração"])

if __name__ == '__main__':
    unittest.main()
