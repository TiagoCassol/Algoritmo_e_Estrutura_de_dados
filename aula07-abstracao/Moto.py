from Veiculo import Veiculo
 
class Moto(Veiculo):
    def __init__(self, modelo, ano, cilindradas):
        super().__init__(modelo, ano)
        self.cilindradas = cilindradas

    def ligar(self, chave):
        if chave == "1234":
            print("Moto ligada")
        else:
            print("não foi possivel ligar a moto")
    
    def imprimir(self):
        print("Motocicleta")
        super().imprimir()
        print("quantidades de cilindradas: ",self.cilindradas)