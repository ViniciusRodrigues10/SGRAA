# import unittest
# from datetime import date
# from src.Adocao import Adocao

# class TestAdocao(unittest.TestCase):
#     def setUp(self):
#         """Configuração inicial para cada teste."""
#         self.adocao = Adocao(
#             id=1,
#             idAnimal=10,
#             idPretendente=20,
#             data=date(2024, 2, 14),
#             termoResponsabilidade="Assinado"
#         )

#     def test_criacao_adocao(self):
#         """Teste para verificar se os atributos da adoção são atribuídos corretamente."""
#         self.assertEqual(self.adocao.id, 1)
#         self.assertEqual(self.adocao.idAnimal, 10)
#         self.assertEqual(self.adocao.idPretendente, 20)
#         self.assertEqual(self.adocao.data, date(2024, 2, 14))
#         self.assertEqual(self.adocao.termoResponsabilidade, "Assinado")

#     def test_gerar_termo(self):
#         """Teste para verificar se o termo de responsabilidade é gerado corretamente."""
#         termo_esperado = "Termo de Responsabilidade assinado em 2024-02-14 por Pretendente ID 20 para Animal ID 10."
#         self.assertEqual(self.adocao.gerar_termo(), termo_esperado)

# if __name__ == '__main__':
#     unittest.main()

import unittest
from datetime import date
from src.Adocao import Adocao
from src.Animal import Animal
from src.Pretendente import Pretendente

class TestAdocao(unittest.TestCase):
    def setUp(self):
        self.animal = Animal(1, "Rex", "Cão", "Vira-lata", 3, "Macho", "Médio", "Marrom", "Disponível", date(2023, 10, 1))
        self.pretendente = Pretendente(1, "João Silva", "joao@example.com")

    def test_adotar_animal_disponivel(self):
        adocao = Adocao(1, self.animal.id, self.pretendente.id, date(2023, 10, 15), "Termo assinado")
        self.animal.marcar_como_adotado(adocao.data)
        self.assertEqual(self.animal.statusAdocao, "Adotado")

    def test_gerar_termo_de_responsabilidade(self):
        adocao = Adocao(2, self.animal.id, self.pretendente.id, date(2023, 10, 15), "Termo assinado")
        self.assertEqual(adocao.gerar_termo(), "Termo de Responsabilidade assinado em 2023-10-15 por Pretendente ID 1 para Animal ID 1.")

    def test_verificar_status_animal_adotado(self):
        adocao = Adocao(3, self.animal.id, self.pretendente.id, date(2023, 10, 15), "Termo assinado")
        self.animal.marcar_como_adotado(adocao.data)
        self.assertEqual(self.animal.statusAdocao, "Adotado")

    def test_verificar_data_saida_animal(self):
        adocao = Adocao(4, self.animal.id, self.pretendente.id, date(2023, 10, 15), "Termo assinado")
        self.animal.marcar_como_adotado(adocao.data)
        self.assertEqual(self.animal.dataSaida, date(2023, 10, 15))

    # def test_tentar_adotar_animal_ja_adotado(self):
    #     with self.assertRaises(ValueError):
    #         Adocao(1, self.animal.id, self.pretendente.id, date(2023, 10, 20), "Termo assinado")

    def test_tentar_adotar_animal_sem_termo(self):
        with self.assertRaises(ValueError):
            Adocao(2, self.animal.id, self.pretendente.id, date(2023, 10, 20), "")

    # def test_verificar_mensagem_erro_ao_adotar_animal_ja_adotado(self):
    #     with self.assertRaises(ValueError) as context:
    #         Adocao(3, self.animal.id, self.pretendente.id, date(2023, 10, 20), "Termo assinado")
    #     self.assertTrue("Animal já adotado" in str(context.exception))

    # def test_garantir_animal_continua_adotado(self):
    #     self.assertEqual(self.animal.statusAdocao, "Adotado")