from Veiculo import Veiculo

class Bicicleta(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, numMarchas, bagageiro, velocidade=0):
        super().__init__(marca, qtdRodas, modelo, velocidade)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print(f"Número de Marchas: {self.numMarchas}")
        print(f"Bagageiro: {'Sim' if self.bagageiro else 'Não'}")