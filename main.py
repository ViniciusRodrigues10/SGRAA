from datetime import date
from src.Tratamento import Tratamento
from src.Animal import Animal
from src.Adocao import Adocao
from src.Pretendente import Pretendente
from src.Doacao import Doacao
from src.Doador import Doador 
from src.Voluntario import Voluntario 
from src.Resgate import Resgate 
from src.Estoque import Estoque 

animal1 = Animal(1, "Rex", "Cão", "Vira-lata", 3, "Macho", "Médio", "Marrom", "Disponível", date(2023, 10, 1))
tratamento1 = Tratamento(1, "Vacinação", ["Vacina A", "Vacina B"])
animal1.adicionar_tratamento(tratamento1)

pretendente1 = Pretendente(1, "João Silva", "joao@example.com")
adocao1 = Adocao(1, 1, 1, date(2023, 10, 15), "Termo assinado")

doacao1 = Doacao(1, 1, ["Ração", "Medicamento"], 10, date(2023, 10, 5))
doador1 = Doador(1, "Maria Oliveira", "maria@example.com", "Individual")

voluntario1 = Voluntario(1, "Carlos Souza", "carlos@example.com", "Resgate")
resgate1 = Resgate(1, date(2023, 10, 3), "Rua A", [animal1])

estoque1 = Estoque(1, "Ração", 100)
estoque1.atualizar_quantidade(90)
estoque1.registrar_consumo(10)