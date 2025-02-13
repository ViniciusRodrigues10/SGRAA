class Pretendente:
    def __init__(self, id: int, nome: str, contato: str):
        self.id = id
        self.nome = nome
        self.contato = contato

    def atualizar_contato(self, novo_contato: str):
        self.contato = novo_contato