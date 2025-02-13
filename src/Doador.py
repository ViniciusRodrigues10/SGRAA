class Doador:
    def __init__(self, id: int, nome: str, contato: str, tipo: str):
        self.id = id
        self.nome = nome
        self.contato = contato
        self.tipo = tipo

    def atualizar_contato(self, novo_contato: str):
        self.contato = novo_contato