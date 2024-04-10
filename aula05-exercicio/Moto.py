
from Automovel import Automovel

class Moto(Automovel):
    def __init__(self, marca, qtdRodas, modelo, potenciaDoMotor,partidaEletrica, velocidade=0):
        super().__init__(marca, qtdRodas, modelo,potenciaDoMotor, velocidade)
        self.partidaEletrica = partidaEletrica

    def imprimirInformacoes(self):
        super().imprimirInformacoes()
        print(f"Partida Eletrica: {self.partidaEletrica}")