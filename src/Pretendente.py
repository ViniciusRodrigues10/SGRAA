class Pretendente:
    def __init__(self, id: int, nome: str, contato: str):
        if not nome:
            raise ValueError("O nome não pode estar vazio.")
        if not contato:
            raise ValueError("O contato não pode estar vazio.")

        self.id = id
        self.nome = nome
        self.contato = contato

    def atualizar_contato(self, novo_contato: str):
        if not novo_contato:
            raise ValueError("O contato não pode estar vazio.")
        self.contato = novo_contato
    
    def __str__(self):
        return f"Pretendente(id={self.id}, nome={self.nome}, contato={self.contato})"