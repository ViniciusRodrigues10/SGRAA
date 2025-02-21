from datetime import date
from typing import List

class Doacao:
    def __init__(self, id: int, idDoador: int, items: List[str], quantidade: int, data: date):
        if not items:
            raise ValueError("A lista de itens não pode estar vazia.")
        if quantidade <= 0:
            raise ValueError("A quantidade não pode ser negativa ou zero.")
        if not isinstance(data, date):
            raise ValueError("A data deve ser do tipo date.")

        self.id = id
        self.idDoador = idDoador
        self.items = items
        self.quantidade = quantidade
        self.data = data

    def adicionar_item(self, item: str, quantidade: int):
        if quantidade <= 0:
            raise ValueError("A quantidade não pode ser negativa ou zero.")
        if item not in self.items:
            self.items.append(item)
        self.quantidade += quantidade

    def __str__(self):
        return f"Doacao(id={self.id}, idDoador={self.idDoador}, items={self.items}, quantidade={self.quantidade}, data={self.data})"