from Categoria import *


class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria, potenciaDaFonte):
        super().__init__(modelo, cor, preco, categoria)
        self._potenciaDaFonte = potenciaDaFonte


    def getPotenciaDaFonte(self):
        return self._potenciaDaFonte
    
    def setPotenciaDaFonte(self, potencia):
        self._potenciaDaFonte = potencia

    def getInformacoes(self):
        informacoes = super().getInformacoes()
        informacoes['Potencia Da Fonte: '] = self._potenciaDaFonte
        return informacoes
    
    
    def cadastrar(self):
        print("Desktop cadastrado com sucesso!")
