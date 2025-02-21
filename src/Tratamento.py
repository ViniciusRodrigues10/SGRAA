from typing import List

class Tratamento:
    def __init__(self, id: int, descricao: str, medicamentos: List[str]):
        if not medicamentos or medicamentos == [None]:
            raise ValueError("A lista de medicamentos não pode estar vazia.")
        self.id = id
        self.descricao = descricao
        self.medicamentos = medicamentos

    def adicionar_medicamento(self, medicamento: str):
        self.medicamentos.append(medicamento)

    def remover_medicamento(self, medicamento: str):
        if medicamento in self.medicamentos:
            self.medicamentos.remove(medicamento)

    def __str__(self):
        return f"Tratamento: {self.descricao}, Medicamentos: {self.medicamentos}"
