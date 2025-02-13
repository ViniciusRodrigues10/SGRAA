class Voluntario:
    def __init__(self, id: int, nome: str, contato: str, funcao: str):
        self.id = id
        self.nome = nome
        self.contato = contato
        self.funcao = funcao

    def atualizar_funcao(self, nova_funcao: str):
        self.funcao = nova_funcao