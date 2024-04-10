
from Automovel import Automovel

class Carro(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor,qtdPortas, velocidade=0):
        super().__init__(marca, qtdRodas, modelo,potenciaDoMotor, velocidade)
        self.qtdPortas = qtdPortas

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print(f"Quantidade de portas {self.qtdPortas}")