from datetime import date
from typing import List
from src.Animal import Animal

class Resgate:
    def __init__(self, id: int, data: date, localidade: str, animaisResgatados: List[Animal]):
        self.id = id
        self.data = data
        self.localidade = localidade
        self.animaisResgatados = animaisResgatados

    def adicionar_animal_resgatado(self, animal: Animal):
        self.animaisResgatados.append(animal)