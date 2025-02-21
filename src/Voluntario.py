class Voluntario:
    def __init__(self, id: int, nome: str, contato: str, funcao: str):
        if not nome:
            raise ValueError("O nome não pode estar vazio.")
        if not contato:
            raise ValueError("O contato não pode estar vazio.")
        if not funcao:
            raise ValueError("A função não pode estar vazia.")

        self.id = id
        self.nome = nome
        self.contato = contato
        self.funcao = funcao

    def atualizar_funcao(self, nova_funcao: str):
        if not nova_funcao:
            raise ValueError("A função não pode estar vazia.")
        self.funcao = nova_funcao
    
    def __str__(self):
        return f"Voluntario(id={self.id}, nome={self.nome}, contato={self.contato}, funcao={self.funcao})"