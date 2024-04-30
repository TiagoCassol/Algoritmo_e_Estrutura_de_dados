from abc import ABC, abstractmethod

class Categoria:
    def __init__(self, _id, nome):
        self.id = _id
        self.nome = nome

class Produto(ABC):
    def __init__(self, modelo, cor, preco, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria
    
    def getInformacoes(self):
        return {
            'modelo': self.modelo,
            'cor': self.cor,
            'preco': self.preco,
            'categoria': self.categoria.nome
        }
    
    @abstractmethod
    def cadastrar(self):
        pass


