from Veiculo import Veiculo

class Automovel(Veiculo):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor, velocidade=0):
        super().__init__(marca, qtdRodas, modelo, velocidade)
        self.potenciaDoMotor = potenciaDoMotor

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print(f"Potencia do motor: {self.potenciaDoMotor}")
