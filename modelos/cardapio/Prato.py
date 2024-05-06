from modelos.cardapio.itemCardapio import itemCardapio

class Prato(itemCardapio):
    def __init__(self, nome, preco, descicao):
        super().__init__(nome, preco)
        self.descricao = descicao

    def __str__(self):
        return self._nome
