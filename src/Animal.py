from datetime import date
from src.Tratamento import Tratamento

class Animal:
    def __init__(self, id: int, nome: str, especie: str, raca: str, idade: int, sexo: str, porte: str, cor: str, statusAdocao: str, dataChegada: date, dataSaida: date = None):
        self.id = id
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = idade
        self.sexo = sexo
        self.porte = porte
        self.cor = cor
        self.statusAdocao = statusAdocao
        self.dataChegada = dataChegada
        self.dataSaida = dataSaida
        self.tratamentos = []

    def adicionar_tratamento(self, tratamento: Tratamento):
        self.tratamentos.append(tratamento)

    def marcar_como_adotado(self, dataSaida: date):
        self.statusAdocao = "Adotado"
        self.dataSaida = dataSaida

    def listar_tratamentos(self):
        return [tratamento.descricao for tratamento in self.tratamentos]