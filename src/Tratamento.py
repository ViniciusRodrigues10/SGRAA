from typing import List

class Tratamento:
    def __init__(self, id: int, descricao: str, medicamentos: List[str]):
        self.id = id
        self.descricao = descricao
        self.medicamentos = medicamentos

    def adicionar_medicamento(self, medicamento: str):
        self.medicamentos.append(medicamento)

    def remover_medicamento(self, medicamento: str):
        if medicamento in self.medicamentos:
            self.medicamentos.remove(medicamento)