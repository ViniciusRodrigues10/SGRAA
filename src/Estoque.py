class Estoque:
    def __init__(self, id: int, item: str, quantidade: int):
        self.id = id
        self.item = item
        self.quantidade = quantidade

    def atualizar_quantidade(self, nova_quantidade: int):
        self.quantidade = nova_quantidade

    def registrar_consumo(self, quantidade_consumida: int):
        if self.quantidade >= quantidade_consumida:
            self.quantidade -= quantidade_consumida
        else:
            raise ValueError("Quantidade insuficiente em estoque.")