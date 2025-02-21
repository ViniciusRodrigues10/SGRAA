from datetime import date

class Adocao:
    def __init__(self, id: int, idAnimal: int, idPretendente: int, data: date, termoResponsabilidade: str):
        if not termoResponsabilidade:
            raise ValueError("O termo de responsabilidade não pode estar vazio.")
        self.id = id
        self.idAnimal = idAnimal
        self.idPretendente = idPretendente
        self.data = data
        self.termoResponsabilidade = termoResponsabilidade

    def gerar_termo(self):
        return f"Termo de Responsabilidade assinado em {self.data} por Pretendente ID {self.idPretendente} para Animal ID {self.idAnimal}."