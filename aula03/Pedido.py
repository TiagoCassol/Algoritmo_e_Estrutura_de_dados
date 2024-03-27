from Cidade import Cidade
from Pessoa import Pessoa

class Pedido:
    def __init__(self, endereco, clienteId):
        self.id = None
        self.endereco = endereco
        self.produtos = [] 
        self.clienteId = clienteId

    def __str__(self):
        texto = "Endereço: " + self.endereco
        texto += "\nProdutos:"
        for produto in self.produtos:
            texto += str(produto)
        texto += "\n" + str(self.clienteId)
        return texto

    def addProduto(self, produto):
        self.produtos.append(produto)


class Produto:
    def __init__(self, nome, preco, qtd, cat):
        self.id = None
        self.nome = nome
        self.preco = preco
        self.qtd = qtd
        self.categoria = cat

    def __str__(self):
        texto = "\n--------------" 
        texto += "\nNome: " + self.nome
        texto += "\nPreco:" + str(self.preco)
        texto += "\nQuantidade:" + str(self.qtd)
        texto += "\n:" + str(self.categoria)
        texto += "\n--------------" 
        return texto


class Categoria:
    def __init__(self, nome):
        self.id = None
        self.nome = nome

    def __str__(self):
        texto = "Nome da Categoria: " + self.nome
        return texto


