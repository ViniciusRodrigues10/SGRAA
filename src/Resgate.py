from datetime import date
from typing import List
from src.Animal import Animal

class Resgate:
    def __init__(self, id: int, data: date, localidade: str, animaisResgatados: List[Animal]):
        if not isinstance(data, date):
            raise ValueError("A data deve ser do tipo date.")
        if not localidade:
            raise ValueError("A localidade não pode estar vazia.")
        if not animaisResgatados:
            raise ValueError("A lista de animais resgatados não pode estar vazia.")

        self.id = id
        self.data = data
        self.localidade = localidade
        self.animaisResgatados = animaisResgatados

    def adicionar_animal_resgatado(self, animal: Animal):
        if not animal:
            raise ValueError("O animal não pode ser nulo.")
        if animal not in self.animaisResgatados:
            self.animaisResgatados.append(animal)
    
    def __str__(self):
        animais_str = ", ".join([f"Animal(id={animal.id}, nome={animal.nome})" for animal in self.animaisResgatados])
        return f"Resgate(id={self.id}, data={self.data}, localidade={self.localidade}, animaisResgatados=[{animais_str}])"