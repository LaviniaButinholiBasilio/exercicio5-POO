from venda import Venda
from compra import Compra

class Produto:
    def __init__(self, nome, qtde_estoque, preco_unit, estoque_minimo, estoque_maximo):
        self.nome = nome
        self.qtde_estoque = qtde_estoque
        self.preco_unit = preco_unit
        self.estoque_minimo = estoque_minimo
        self.estoque_maximo = estoque_maximo
        self.historico = []

    def debitar_estoque(self, quantidade):
        self.qtde_estoque -= quantidade

    def creditar_estoque(self, quantidade):
        self.qtde_estoque += quantidade

    def verificar_estoque_baixo(self):
        return self.qtde_estoque < self.estoque_minimo

    def verificar_estoque_insuficiente(self, quantidade):
        return quantidade > self.qtde_estoque

    def verificar_estoque_excedente(self, quantidade):
        return (self.qtde_estoque + quantidade) > self.estoque_maximo

    def calcular_valor_venda(self, quantidade):
        return quantidade * self.preco_unit

    def vender(self, data_venda, cliente, qtde_vendida):
        venda = Venda(data_venda, cliente, self, qtde_vendida)
        if venda.vender(self, qtde_vendida):
            self.registrar_historico(f"Venda do produto {self.nome}")

    def comprar(self, data_compra, fornecedor, qtde_compra, preco_unit):
        compra = Compra(data_compra, self, fornecedor, qtde_compra, preco_unit)
        if compra.comprar(self, qtde_compra):
            self.registrar_historico(f"Compra do produto {self.nome}")

    def registrar_historico(self, transacao):
        self.historico.append(transacao)

    def exibir_historico(self):
        for registro in self.historico:
            print(registro)
