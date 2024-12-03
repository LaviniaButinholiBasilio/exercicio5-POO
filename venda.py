from transacao import Transacao

class Venda(Transacao):
    def __init__(self, data_venda, cliente, produto, qtde_vendida):
        super().__init__(data_venda, produto, qtde_vendida)
        self.cliente = cliente

    def vender(self, produto, qtde_vendida):
        if produto.verificar_estoque_insuficiente(qtde_vendida):
            print("Erro: Estoque insuficiente.")
            return False
        produto.debitar_estoque(qtde_vendida)
        valor = produto.calcular_valor_venda(qtde_vendida)
        print(f"Valor venda = {valor}")
        if produto.verificar_estoque_baixo():
            print("Estoque baixo")
        return True
