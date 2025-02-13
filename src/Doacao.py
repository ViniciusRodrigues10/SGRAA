from datetime import date
from typing import List

class Doacao:
    def __init__(self, id: int, idDoador: int, items: List[str], quantidade: int, data: date):
        self.id = id
        self.idDoador = idDoador
        self.items = items
        self.quantidade = quantidade
        self.data = data

    def adicionar_item(self, item: str, quantidade: int):
        self.items.append(item)
        self.quantidade += quantidade