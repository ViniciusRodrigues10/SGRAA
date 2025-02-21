class Doador:
    def __init__(self, id: int, nome: str, contato: str, tipo: str):
        if not nome:
            raise ValueError("O nome não pode estar vazio.")
        if not contato:
            raise ValueError("O contato não pode estar vazio.")
        if tipo not in ["Individual", "Instituição"]:
            raise ValueError("O tipo deve ser 'Individual' ou 'Instituição'.")

        self.id = id
        self.nome = nome
        self.contato = contato
        self.tipo = tipo

    def atualizar_contato(self, novo_contato: str):
        if not novo_contato:
            raise ValueError("O contato não pode estar vazio.")
        self.contato = novo_contato
    
    def __str__(self):
        return f"Doador(id={self.id}, nome={self.nome}, contato={self.contato}, tipo={self.tipo})"