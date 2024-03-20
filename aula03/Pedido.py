from Cidade import Cidade
from Pessoa import Pessoa

class Pedido:
    def __init__(self, endereco, produtos,clienteId ):
        self.id = None
        self.endereco = endereco
        self.produtos = produtos
        self.clienteId = clienteId

    def __str__(self):
        texto = "Endereço: "+ self.endereco
        texto += "\nProdutos:" + str(self.produtos)
        texto += "\nClienteID:" + str(self.clienteId)
        return texto

    def addProduto():
        return None

class Produto:
    def __init__(self, nome, preco,qtd,cat ):
        self.id = None
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.categoria = cat

    def __str__(self):
        texto = "Nome: "+ self.nome
        texto += "\nPreco:" + str(self.preco)
        texto += "\nQuantidade:" + str(self.qtd)
        texto += "\nCategoria:" + str(self.categoria)
        return texto

class Categoria:
    def __init__(self, nome):
        self.id = None
        self.nome= nome

    def __str__(self):
        texto = "Nome da Categoria: "+ self.nome
        return texto