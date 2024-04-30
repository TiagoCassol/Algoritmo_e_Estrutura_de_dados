from Categoria import *


# A classe Notebook possui o atributo/propriedade fortemente privado tempoDeBateria. Esta classe reimplementa o método getInformacoes() herdado de Produto. Construa 
# getters e setters para os atributos que não forem públicos. Todas as classes devem ter um método construtor.


class Notebook(Produto):
    def __init__(self, modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__(modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria


    def getTempoDeBateria(self):
        return self.__tempoDeBateria
    
    def setTempoDeBateria(self, tempoDeBateria):
        self.__tempoDeBateria = tempoDeBateria

    def getInformacoes(self):
        informacoes = super().getInformacoes()
        informacoes['Tempo De Bateria: '] = self.__tempoDeBateria
        return informacoes
    
    
    def cadastrar(self):
        print("Notebook cadastrado com sucesso!")
