class Veiculo:
    def __init__(self, marca, qtdRodas, modelo, velocidade=0):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade

    def imprimirInformacoes(self):
        print("\n--------------------")
        print(f"Marca: {self.marca}")
        print(f"Quantidade de Rodas: {self.qtdRodas}")
        print(f"Modelo: {self.modelo}")
        print(f"Velocidade: {self.velocidade} km/h")

    def acelerar(self, valor):
        self.velocidade += valor

    def frear(self, valor):
        if self.velocidade - valor >= 0:
            self.velocidade -= valor
        else:
            self.velocidade = 0