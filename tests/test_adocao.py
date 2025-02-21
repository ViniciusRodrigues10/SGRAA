import unittest
from datetime import date
from src.Adocao import Adocao

class TestAdocao(unittest.TestCase):
    def setUp(self):
        """Configuração inicial para cada teste."""
        self.adocao = Adocao(
            id=1,
            idAnimal=10,
            idPretendente=20,
            data=date(2024, 2, 14),
            termoResponsabilidade="Assinado"
        )

    def test_criacao_adocao(self):
        """Teste para verificar se os atributos da adoção são atribuídos corretamente."""
        self.assertEqual(self.adocao.id, 1)
        self.assertEqual(self.adocao.idAnimal, 10)
        self.assertEqual(self.adocao.idPretendente, 20)
        self.assertEqual(self.adocao.data, date(2024, 2, 14))
        self.assertEqual(self.adocao.termoResponsabilidade, "Assinado")

    def test_gerar_termo(self):
        """Teste para verificar se o termo de responsabilidade é gerado corretamente."""
        termo_esperado = "Termo de Responsabilidade assinado em 2024-02-14 por Pretendente ID 20 para Animal ID 10."
        self.assertEqual(self.adocao.gerar_termo(), termo_esperado)

if __name__ == '__main__':
    unittest.main()
