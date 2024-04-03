from Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self,marca,ano,cat,qtdPortas):
        super().__init__(marca,ano,cat)
        self.qtdPortas = qtdPortas

    def __str__(self):
        return super().__str__() +"\nPortas: "+ str(self.qtdPortas)

    def imprimir(self):
        print("---Carro---")
        super().imprimir()

        # print(self)