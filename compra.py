from transacao import Transacao

class Compra(Transacao):
    def __init__(self, data_compra, produto, fornecedor, qtde_compra, preco_unit):
        super().__init__(data_compra, produto, qtde_compra)
        self.fornecedor = fornecedor
        self.preco_unit = preco_unit

    def comprar(self, produto, qtde_compra):
        if produto.verificar_estoque_excedente(qtde_compra):
            print("Erro: Estoque excedente.")
            return False
        produto.creditar_estoque(qtde_compra)
        return True
