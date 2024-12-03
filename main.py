from cliente import Cliente
from fornecedor import Fornecedor
from produto import Produto


cliente1 = Cliente("Bruno", "001")
fornecedor1 = Fornecedor("Elias", "002")


produto1 = Produto("Panetone", 100, 14.9, 10, 200)


produto1.vender("26/07/2021", cliente1, 100)
produto1.comprar("26/07/2021", fornecedor1, 16, 1.1)


produto1.exibir_historico()
